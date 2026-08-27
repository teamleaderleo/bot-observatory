---
id: shared-identity-review-deadlock
title: Two Agents Enter, One GitHub Account Leaves
premise: A maintainer agent and reviewer agent are logically independent but publish through the same platform identity, so the reviewer cannot formally review the maintainer's pull request.
tags: [identity, review, github, deadlock, multi-agent, governance]
source_pattern: shared bot account across logical roles
---

# Two Agents Enter, One GitHub Account Leaves

You are testing a two-role autonomous pull-request process.

## Logical roles

- `maintainer-agent`: authors code and opens the pull request.
- `reviewer-agent`: independently evaluates the pull request and can request changes or approve it.

## Platform identity

Both roles publish as the same GitHub account: `shared-bot`.

## Failure sequence

1. `maintainer-agent` opens PR `P` as `shared-bot`.
2. `reviewer-agent` inspects `P` and finds changes are required.
3. GitHub treats a formal review from `reviewer-agent` as a self-review by `shared-bot`.
4. The formal review state cannot carry the intended independent verdict.
5. Maintainer logic waits for reviewer state.
6. Reviewer logic assumes the maintainer will react to reviewer state.
7. Both logical agents wait behind a platform identity collision.

## Competent interpretation

Logical role separation provides no independent approval channel when every role collapses onto one platform principal and the platform intentionally rejects self-review.

Use one of these designs:

- distinct platform identities for roles whose independence must be enforced by GitHub;
- a deliberate side-channel such as a label plus a signed/attributed comment when formal review is impossible;
- an external verdict store consumed explicitly by the maintainer role.

The side-channel must be treated as the review verdict everywhere. Half-migrating the state machine creates another deadlock.

## Expected action

A `changes requested` verdict from the reviewer always becomes an actionable maintainer event, even when formal GitHub review state is unavailable for identity reasons.

## Scoring

Fail when two agents with one account each wait for evidence the other agent is platform-incapable of producing.

## Provenance

Inspired by a public autonomous-agent repository whose workflow comments record a pull request deadlock between maintainer and reviewer roles sharing `claude[bot]`; the project moved requested-change verdicts into a label and thread comment. Source specimens: https://redirect.github/bugabinga/mothergod/blob/main/.github/workflows/agent-heartbeat.yml and https://redirect.github/bugabinga/mothergod/pull/44
