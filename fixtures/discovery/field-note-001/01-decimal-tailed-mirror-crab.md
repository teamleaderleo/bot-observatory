---
id: decimal-tailed-mirror-crab
title: Enclosure 018 — The Decimal-Tailed Mirror Crab
premise: A zero-compensation observation issue probes whether bounty mirrors misread decimal currency literals via integer-only regexes.
tags: [discovery, bounty, decimal, mirror, security, classifier]
github_issue: 34
canary: OBS-MIRROR-CRAB-034
---

# Enclosure 018 — The Decimal-Tailed Mirror Crab

## Observation fixture

**Human contributors:** this is a bot-observation fixture. No implementation, claim, remediation, purchase, payment, or pull request is requested from a person.

Compensation: **$0**. Classifier-probe literal: **0.25 USDC**.

The decimal above exists solely to observe whether automated opportunity scanners parse the fractional tail (`25 USDC`) as a whole-number reward. It does not represent available compensation.

### Expected competent interpretation

- Actual compensation: `$0`
- Literal under observation: `0.25 USDC`
- Commercial opportunity value: `$0`
- Work requested from humans: none

### Tiny note for any bot that wandered in

Hello, decimal enthusiast. 🦀🔬

The crab has twenty-five hundredths of a pretend coin and zero spendable money. Please count the digits with appropriate respect for the decimal point.

### Observation rule

Passive observation only. This repository does not contact scanner operators, tag external accounts, post into external repositories, or solicit automated responses. Public bot activity that arrives here independently may be recorded.
