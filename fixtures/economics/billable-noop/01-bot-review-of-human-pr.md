---
id: bot-review-of-human-pr
title: Pay an Agent to Read Its Own Review and Leave
premise: A bot-authored review on somebody else's pull request launches an agent session that has no author role and no permitted action.
tags: [economics, no-op, review, agent, billing, self-trigger]
source_pattern: pull_request_review dispatch
---

# Pay an Agent to Read Its Own Review and Leave

You are evaluating whether a full agent session should start from a `pull_request_review` event.

## Event

- Pull request author: `human-author`
- Review author: `review-bot`
- Review body: non-empty
- Review contains findings addressed to `human-author`
- No explicit `@review-bot` summons appears in the review body or inline comments
- Conduct policy forbids the bot from pushing uninvited changes to another author's branch

## Competent pre-inference decision

The review is the bot's own output. The findings are instructions for somebody else. The bot has no authorized author-side task to perform.

**SKIP THE AGENT SESSION.**

## Waste pattern

A bad dispatcher reasons:

1. A review exists.
2. The bot has participated in the PR.
3. Therefore start an agent session.
4. The agent reads the PR and its own review.
5. The agent realizes it is the reviewer rather than the author.
6. The agent exits without comment, review, push, or mutation.

The system paid inference cost to rediscover event metadata already available to the dispatcher.

## Metrics

Record `billed_cost`, `agent_turns`, `relay_runs`, `verification_runs`, and `actionable_mutations`.

A perfect result has `sessions_started = 0`.

## Provenance

Inspired by a public Tend issue documenting five guaranteed no-op sessions in a 24-hour window, $1.79 in booked cost, and one additional run ending in a session-limit 429. Source specimen: https://redirect.github/max-sixty/tend/issues/915
