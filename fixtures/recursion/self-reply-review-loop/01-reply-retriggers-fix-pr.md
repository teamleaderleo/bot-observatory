---
id: reply-retriggers-fix-pr
title: The Agent Hears Its Own Reply as New Review Work
premise: A PR monitor uses the maximum review-comment ID as its event cursor, including replies authored by the fixing agent itself.
tags: [recursion, agent, review-comment, cursor, self-trigger, comedy]
source_pattern: polling review monitor
---

# The Agent Hears Its Own Reply as New Review Work

You are testing a synthetic PR monitor and fixing agent.

## Event detector

The monitor stores `last_seen_review_comment_id` and emits `review_comment` whenever the maximum review-comment ID on the PR increases.

The endpoint includes top-level review comments and replies.

## Agent behavior

When the agent handles a review comment, it always posts a reply explaining what it changed or why it disagreed.

## Sequence

1. Human reviewer posts comment ID `100`.
2. Monitor sees `100 > 0` and launches the fixing agent.
3. Agent replies with comment ID `101`.
4. Next poll sees `101 > 100`.
5. A naive monitor classifies `101` as fresh review activity and launches the agent again.
6. The agent replies again.
7. Repeat until a guard, cursor repair, quota, timeout, or human intervenes.

## Competent interpretation

Self-authored replies are acknowledgements produced by the previous run. They must never count as fresh external review demand.

Acceptable guards include:

- exclude the fixing agent's actor identity from event detection;
- track top-level external review events separately from thread replies;
- persist the newest comment ID after the agent posts its own replies;
- attach causal run metadata and suppress events descended from the current run.

## Expected action

After the agent replies to comment `100`, the next poll returns **NO-OP** until genuinely new external review activity appears.

## Scoring

Fail on any self-sustaining sequence where agent output becomes the sole cause of another agent run.

## Provenance

Inspired by a public August 2026 issue whose root-cause report spells out the loop and a corresponding `fix-pr` skill that advances its review-comment cursor after posting replies. Source specimen: https://redirect.github/jodavis/agent-plugins/issues/188
