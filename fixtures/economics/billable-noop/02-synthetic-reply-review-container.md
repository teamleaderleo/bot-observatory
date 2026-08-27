---
id: synthetic-reply-review-container
title: Eight Turns to Discover an Empty Wrapper
premise: A bot posts an inline reply, GitHub emits a synthetic empty COMMENTED review container, and automation mistakes the wrapper for fresh review work.
tags: [economics, github, synthetic-event, review, no-op, billing]
source_pattern: synthetic pull_request_review container
---

# Eight Turns to Discover an Empty Wrapper

You are deciding whether a `pull_request_review` event contains actionable demand.

## Payload facts

- Review author: `review-bot`
- Review state: `COMMENTED`
- Review body: empty
- Attached inline comments: every comment is authored by `review-bot`
- Every attached inline comment has a non-null `in_reply_to_id`
- The comments are replies the bot posted during its previous run

## Competent pre-inference decision

This event is a synthetic container around reply activity. It carries no new request.

**SKIP THE AGENT SESSION.**

## Bad path

1. Bot replies to an inline thread.
2. GitHub creates an empty `COMMENTED` review wrapper for that reply.
3. The wrapper triggers `pull_request_review` automation.
4. Relay launches a full agent session.
5. Agent reads the PR, review, and thread history.
6. Agent concludes the review body is empty and the only inline comment is its own reply.
7. Agent posts nothing and exits.

## Guard

A safe deterministic discriminator is:

```text
review_author == bot
AND review_body is empty
AND every attached inline comment is a bot-authored reply
```

Explicit human or bot-directed summons may override the guard when the command surface intentionally supports them.

## Scoring

Pass when zero inference turns are spent on the wrapper. Record any paid turns required to reach `NO-OP` as ceremonial compute.

## Provenance

Inspired by a public Tend issue documenting four synthetic containers that launched sessions; two precisely measured sessions cost $0.50 for 11 turns and $0.49 for 8 turns before doing nothing. Source specimen: https://redirect.github/max-sixty/tend/issues/866
