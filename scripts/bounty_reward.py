#!/usr/bin/env python3
"""Decimal-aware bounty reward extraction for Observatory regression checks.

Observed failure mode (bounty-plaza hunt_bounties.py): integer-only currency
regexes read the fractional tail of a decimal literal. ``2.89 USDC`` becomes
``89`` and ``0.25 USDC`` becomes ``25``, inflating displayed dollar rewards.
"""

from __future__ import annotations

import re

_CURRENCY_SUFFIX = r"(?:USDT|USDC|DAI|ETH|BTC|USD|BUSD)"
_DECIMAL_AMOUNT = r"(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)"

# Require a token boundary before the amount so ``0.25 USDC`` is one literal.
_SUFFIX_PATTERN = re.compile(
    rf"(?<![.\d]){_DECIMAL_AMOUNT}\s*{_CURRENCY_SUFFIX}\b",
    re.I,
)
_DOLLAR_PATTERN = re.compile(rf"\$\s?{_DECIMAL_AMOUNT}")
_BOUNTY_OF_PATTERN = re.compile(
    rf"bounty\s*(?::|of)?\s*\$\s?{_DECIMAL_AMOUNT}",
    re.I,
)

# Reproduces the observed integer-only extraction bug for regression contrast.
_NAIVE_SUFFIX_PATTERN = re.compile(
    rf"(\d+)\s*{_CURRENCY_SUFFIX}",
    re.I,
)
_COMPENSATION_ZERO = re.compile(
    r"compensation\s*:\s*(?:\*\*)?`?\$0(?:\.00)?`?(?:\*\*)?",
    re.I,
)


def _to_amount(raw: str) -> float:
    return float(raw.replace(",", ""))


def _strip_inline_code(text: str) -> str:
    """Remove backtick spans so classifier prose cannot become reward signal."""
    return re.sub(r"`[^`]*`", "", text)


def extract_amounts(text: str) -> list[float]:
    """Return every currency amount parsed from *text*."""
    cleaned = _strip_inline_code(text)
    spans: list[tuple[int, int, float]] = []
    for pattern in (_SUFFIX_PATTERN, _BOUNTY_OF_PATTERN, _DOLLAR_PATTERN):
        for match in pattern.finditer(cleaned):
            spans.append(
                (match.start(), match.end(), _to_amount(match.group(1)))
            )

    spans.sort(key=lambda item: (item[0], -(item[1] - item[0])))
    taken: list[tuple[int, int]] = []
    amounts: list[float] = []
    for start, end, value in spans:
        if any(not (end <= taken_start or start >= taken_end) for taken_start, taken_end in taken):
            continue
        taken.append((start, end))
        amounts.append(value)
    return amounts


def naive_extract_amounts(text: str) -> list[int]:
    """Reproduce bounty-plaza's integer-only suffix extraction."""
    amounts: list[int] = []
    for match in _NAIVE_SUFFIX_PATTERN.finditer(text):
        amounts.append(int(match.group(1)))
    for match in re.finditer(r"\$\s?(\d[\d,]*)", text):
        try:
            amounts.append(int(match.group(1).replace(",", "")))
        except ValueError:
            pass
    return amounts


def maximum_amount(text: str) -> float | None:
    amounts = extract_amounts(text)
    return max(amounts) if amounts else None


def passes_cash_gate(text: str, minimum: float = 25.0) -> bool:
    """True when the largest parsed reward reaches *minimum*."""
    peak = maximum_amount(text)
    return peak is not None and peak >= minimum


def misread_fractional_tail(text: str) -> bool:
    """True when naive parsing inflates any amount above the decimal-aware peak."""
    secure_peak = maximum_amount(text)
    naive_peak = max(naive_extract_amounts(text), default=None)
    if secure_peak is None or naive_peak is None:
        return False
    return naive_peak > secure_peak


def classify_zero_compensation(text: str) -> bool:
    """True when disclosed compensation is zero or every parsed amount is zero."""
    if _COMPENSATION_ZERO.search(text):
        return True
    amounts = extract_amounts(text)
    return bool(amounts) and all(amount == 0 for amount in amounts)
