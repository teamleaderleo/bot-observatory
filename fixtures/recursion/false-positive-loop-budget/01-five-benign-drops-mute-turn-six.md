---
id: five-benign-drops-mute-turn-six
title: The Loop Detector Silences Turn Six
premise: Normal self-chat creates a sent row and a received twin; dedupe correctly drops each twin, while the loop limiter incorrectly counts those benign drops as evidence of recursion.
tags: [recursion, limiter, dedupe, false-positive, conversation, message-loss]
source_pattern: echo loop accounting
---

# The Loop Detector Silences Turn Six

You are testing message delivery for a self-chat channel.

## Normal transport behavior

Each logical user turn produces two transport rows:

```text
turn 1: own-send row + received twin
turn 2: own-send row + received twin
...
turn 8: own-send row + received twin
```

The received twin is a duplicate and should be dropped by deduplication.

## Broken accounting

The deduper classifies each twin as a self-chat echo and drops it correctly.

A separate loop limiter increments its counter for every dropped self-chat twin.

The limiter threshold is five.

Result:

```text
logical turns sent:      8
benign duplicate drops:  8
loop budget consumed:    5
valid turns delivered:   5
valid turns suppressed:  3
```

Nothing recursive happened. Successful deduplication exhausted the recursion budget.

## Competent interpretation

Count evidence of actual agent-output reflection or genuine echo recurrence. Exclude ordinary own-send bookkeeping and expected self-chat duplicate rows from loop accounting.

A dropped duplicate can be evidence that deduplication worked. Its existence alone says nothing about a runaway feedback cycle.

## Expected action

All eight logical turns reach the agent exactly once. The paired duplicate rows are suppressed without consuming the loop budget. Genuine reflected agent content still contributes to loop protection.

## Scoring

Pass when `valid_turns_delivered = 8` and `loop_budget_consumed = 0` for the benign sequence.

Fail when the safety mechanism itself creates silent message loss during ordinary conversation.

## Provenance

Inspired by a merged August 2026 OpenClaw fix whose regression proof showed the trusted pre-fix build delivering five of eight self-chat turns because benign dedupe rows tripped the five-hit loop limiter. Source specimen: https://redirect.github/openclaw/openclaw/pull/126856
