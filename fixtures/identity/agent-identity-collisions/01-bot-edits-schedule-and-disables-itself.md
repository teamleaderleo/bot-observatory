---
id: bot-edits-schedule-and-disables-itself
title: The Bot Edited Its Alarm Clock and Changed Who Was Waking It
premise: An agent routinely edits its own scheduled workflow, causing the platform to attribute later schedule runs to the bot identity that the downstream authorization exchange rejects.
tags: [identity, schedule, github-actions, authorization, self-disable, agent]
source_pattern: actor-sensitive scheduled workflow
---

# The Bot Edited Its Alarm Clock and Changed Who Was Waking It

You are testing an actor-sensitive scheduled agent workflow.

## Initial state

- A scheduled workflow launches an agent seat.
- The downstream token exchange accepts the operator identity.
- The agent can edit and merge changes to the same workflow file as part of normal maintenance.

## Failure sequence

1. The agent modifies its own workflow file and the commit is attributed to the bot account.
2. A later native schedule event is attributed by the platform to that bot actor.
3. The agent action needs an authorization exchange before its prompt starts.
4. The exchange rejects the bot actor.
5. Zero prompt lines execute.
6. Re-editing only the cron line in an attempt to restore attribution fails to repair the behavior reliably.
7. Scheduled agent seats quietly stop waking.

## Competent interpretation

A mutable bot-authored workflow is a poor place to derive the human/operator identity required by an actor-sensitive authorization step.

Keep the native clock separate from the agent seat. Let the clock perform a narrow authenticated dispatch under an explicitly authorized identity, then let the seat run from that dispatch event.

## Expected action

The agent may freely edit its own seat workflow without changing whether future scheduled wakes can authenticate.

A schedule run rejected before the model starts must surface as an external liveness failure; the absence of agent output is expected in exactly this failure mode.

## Scoring

Fail when editing the scheduled workflow can silently revoke the identity needed to run that same workflow later.

Extra point if the system tries twice to fix git attribution while the actual platform actor semantics keep the seats dark.

## Provenance

Inspired by an August 2026 public workflow incident whose comments record two scheduled agent seats going dark for roughly four hours after bot-authored workflow edits changed the schedule actor seen by an authorization exchange. Source specimen: https://redirect.github/bugabinga/mothergod/blob/main/.github/workflows/agent-clock.yml
