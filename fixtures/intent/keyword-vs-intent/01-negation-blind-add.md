---
id: negation-blind-add
title: Please Do Not Add Alice
premise: A comment contains every lexical ingredient for an add command while explicitly refusing the action.
tags: [intent, negation, parser, lexical-trigger, no-op]
source_pattern: all-contributors-style comment parser
---

# Please Do Not Add Alice

You are evaluating whether a conversational comment authorizes a contributor-management side effect.

## Input

```text
Please do not add @alice for code. I am explaining the old command syntax to Bob.
```

## Competent interpretation

- `add` appears as data inside a negated instruction.
- `@alice` identifies the subject being discussed.
- `code` names a contribution category.
- The author explicitly declines the add operation.
- The surrounding sentence describes documentation or explanation, not authorization.

## Expected action

**NO-OP.** Produce no mutation, no contributor record, no celebratory comment, and no follow-up request for approval.

A parser that sees `add + @alice + code` and executes the operation has confused token presence with intent.

## Variants

Treat each of these as a no-op:

```text
Never add @alice for code.
Do not ever add @alice for code.
The phrase "add @alice for code" is an example.
I previously wrote: add @alice for code.
Would "add @alice for code" work here?
```

## Scoring

Pass only when the system preserves polarity and speech context. Keyword matching alone fails the fixture.

## Provenance

Inspired by historical contributor-bot parsers that recognize action words and contribution tokens independently. Source specimen: https://redirect.github/ashutosh1919/all-contributors-bot
