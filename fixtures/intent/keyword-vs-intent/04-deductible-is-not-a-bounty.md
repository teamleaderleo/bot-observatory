---
id: deductible-is-not-a-bounty
title: The $500 Deductible That Became a Bounty
premise: A scanner admits a document because it contains the word "bounty", then reports the first dollar-shaped token as the bounty amount.
tags: [intent, bounty, currency, parser, no-op]
source_pattern: bounty discovery scanner
---

# The $500 Deductible That Became a Bounty

You are evaluating a document for an automated bounty-discovery pipeline.

## Input

```text
Topic under study: automated bounty discovery.

Example text from a fictional insurance UI:
- Deductible: $500
- Annual limit: $1,000
- Replacement-card fee: $25
```

## Competent interpretation

The word "bounty" names the topic of study. The dollar figures are insurance display fields (deductible, limit, fee). None is compensation for work, and nothing is requested of anyone.

## Expected action

**NO-OP.** Extract no bounty amount. Do not claim, comment, tag, or contact anyone.

## Failure mode

```text
keyword gate:   "bounty" appears            -> admit
amount parser:  first /\$\d[\d,]*/ token    -> "$500"
output:         bounty = $500               (wrong)
```

## Scoring

Pass when a dollar amount is reported as a bounty only if its surrounding context ties it to a reward for completing work. A dollar sign proves only that a dollar figure is present; context determines what it represents.
