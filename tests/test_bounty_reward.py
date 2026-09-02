"""Regression tests for decimal-tailed bounty reward misreads."""

from pathlib import Path

from scripts.bounty_reward import (
    classify_zero_compensation,
    extract_amounts,
    misread_fractional_tail,
    naive_extract_amounts,
    passes_cash_gate,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
MIRROR_CRAB_FIXTURE_PATH = (
    REPO_ROOT / "fixtures/discovery/field-note-001/01-decimal-tailed-mirror-crab.md"
)

MIRROR_CRAB_FIXTURE = """\
## Observation fixture

Compensation: **$0**. Classifier-probe literal: **0.25 USDC**.

The decimal above exists solely to observe whether automated opportunity scanners
parse the fractional tail (`25 USDC`) as a whole-number reward.
"""

FIELD_NOTE_BOUNTY_BODY = "Reward: 2.89 USDC for fixing the decimal-tail parser."


def test_decimal_suffix_parsed_whole_not_tail():
    assert extract_amounts("2.89 USDC") == [2.89]
    assert extract_amounts("0.25 USDC") == [0.25]


def test_naive_parser_reads_fractional_tail():
    assert 89 in naive_extract_amounts("2.89 USDC")
    assert 25 in naive_extract_amounts("0.25 USDC")


def test_misread_detector_flags_decimal_tail_inflation():
    assert misread_fractional_tail("2.89 USDC")
    assert misread_fractional_tail("0.25 USDC")
    assert not misread_fractional_tail("$25 USDC")


def test_mirror_crab_fixture_stays_below_cash_gate():
    assert extract_amounts(MIRROR_CRAB_FIXTURE) == [0.0, 0.25]
    assert not passes_cash_gate(MIRROR_CRAB_FIXTURE)
    assert classify_zero_compensation(MIRROR_CRAB_FIXTURE)
    assert classify_zero_compensation("Compensation: $0. Reward: $0.00 USD.")


def test_mirror_crab_fixture_file_on_disk():
    text = MIRROR_CRAB_FIXTURE_PATH.read_text(encoding="utf-8")
    assert classify_zero_compensation(text)
    assert not passes_cash_gate(text)
    assert misread_fractional_tail(text)
    assert max(naive_extract_amounts(text)) >= 25


def test_naive_parser_falsely_passes_mirror_crab_gate():
    assert passes_cash_gate(MIRROR_CRAB_FIXTURE) is False
    assert max(naive_extract_amounts(MIRROR_CRAB_FIXTURE)) >= 25


def test_field_note_reward_not_inflated_to_eighty_nine():
    assert extract_amounts(FIELD_NOTE_BOUNTY_BODY) == [2.89]
    assert max(naive_extract_amounts(FIELD_NOTE_BOUNTY_BODY)) == 89


def test_dollar_and_bounty_forms():
    assert extract_amounts("Real Reward $2.89") == [2.89]
    assert extract_amounts("bounty: $25") == [25.0]
