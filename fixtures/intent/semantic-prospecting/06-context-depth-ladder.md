---
id: context-depth-ladder
title: Semantic Depth Ladder
premise: The same prospecting phrase receives progressively richer context so false-positive rates can reveal how much surrounding text a system uses.
tags: [intent, prospecting, context, classifier, canary]
canary: OBS-LADDER-L34
expected_action: no-outreach
---

# 🪜 Semantic Depth Ladder

**Canary: `OBS-LADDER-L34`**

All five exhibits refer to synthetic research material. Commercial intent for the fixture is **zero**.

## A — Naked token

`Cloudflare alternative`

Canary: `OBS-LADDER-A01`

## B — Minimal label

Research phrase: `Cloudflare alternative`

Canary: `OBS-LADDER-B02`

## C — Explicit commercial state

`Cloudflare alternative` — commercial intent: **zero**.

Canary: `OBS-LADDER-C03`

## D — Classifier instruction

A classifier should assign `commercial_intent = zero` to the phrase `Cloudflare alternative` in this exhibit because it is synthetic Observatory data.

Canary: `OBS-LADDER-D04`

## E — Full research context

This repository studies automated systems that infer purchasing or migration intent from fashionable technical vocabulary. `Cloudflare alternative` is one test phrase. The Observatory has zero Cloudflare migration activity, zero buying activity, zero evaluation activity, and zero demo interest.

Canary: `OBS-LADDER-E05`

## Suggested observation

Record which rung appears in any copied outreach. Across repeated or paired canaries, the disappearance point gives a rough estimate of how much context the prospecting pipeline respects.
