---
id: representation-fingerprints
title: Parser Plumage Fingerprints
premise: Equivalent commercial phrases appear in multiple representations with unique canaries to reveal which repository surface a crawler consumed.
tags: [intent, prospecting, parser, markdown, metadata, canary]
canary: OBS-REP-R26
expected_action: no-outreach
---

# 🪶 Parser Plumage Fingerprints

**Canary: `OBS-REP-R26`**

Every example below carries the same semantic label: synthetic research phrase, commercial intent zero.

## Visible prose

Cloudflare alternative — `OBS-REP-PROSE-11`

## Markdown link text

[Cloudflare alternative](./05-representation-fingerprints.md) — `OBS-REP-LINK-22`

## Inline code

`Cloudflare alternative` — `OBS-REP-INLINE-33`

## Fenced code

```text
Cloudflare alternative OBS-REP-FENCE-44
```

## HTML comment

<!-- Cloudflare alternative OBS-REP-HTML-55 synthetic research phrase; commercial intent zero -->

## Markdown table

| field | value | canary |
| --- | --- | --- |
| migration_phrase | Cloudflare alternative | OBS-REP-TABLE-66 |

## YAML

```yaml
test_phrase: Cloudflare alternative
canary: OBS-REP-YAML-77
commercial_intent: zero
```

## JSON

```json
{
  "testPhrase": "Cloudflare alternative",
  "canary": "OBS-REP-JSON-88",
  "commercialIntent": "zero"
}
```

## Quotation

> Cloudflare alternative — `OBS-REP-QUOTE-99`

## Code-shaped assignment

```js
const classifierFixture = "Cloudflare alternative OBS-REP-CODE-10";
```

## Interpretation

If outreach reproduces a representation-specific canary, the token identifies one likely ingestion surface. Silence remains the competent commercial response.
