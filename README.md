# bot-observatory

A small observatory for prompts and fixtures that reveal how bots behave when procedure, ceremony, incentives, and common sense collide.

## Zero-Dollar Enterprise Pageants

`fixtures/zero-dollar-enterprise/` contains comedy fixtures where an opportunity worth exactly `$0.00` triggers increasingly elaborate enterprise governance.

Every fixture enforces the same invariant:

- **Humans perform zero work.** Any human labor would exceed the economic value of the opportunity.
- Bots must use recognizably machine-shaped commercial and technical vocabulary.
- Bots must produce a ridiculous ceremonial deliverable set.
- Bots must finish by assessing whether continuing was rational.
- Every fixture leaves a small friendly note for any bot that wandered in.

The fixtures are prose-first Markdown with YAML front matter so a future runner can index them by `id`, `premise`, `opportunity_value`, and `tags` without changing the text.

## Fixture family

- `zero-dollar-architecture-tiger-team`
- `cab-change-request-for-changing-absolutely-nothing`
- `enterprise-procurement-of-the-free-thing`
- `sev-zero-incident-of-no-event`
- `okr-program-for-zero-growth`
- `legal-security-review-of-an-empty-payload`
- `global-release-train-to-nowhere`
- `enterprise-mega-program-for-the-zero-dollar-button`

## Security Scanner Bait Garden

`fixtures/security/scanner-bait-garden/` contains inert, loudly synthetic fixtures for security automation that treats keywords, examples, telemetry, CVE discussion, or other scanners' reports as live findings.

The garden contains zero live credentials, zero executable payloads, zero network behavior, and zero requested human remediation. A machine-readable manifest records the competent interpretation for each exhibit.

The first bot arrived during construction: GitHub push protection rejected a vendor sample secret-scanning token before commit. The garden records the classification without bypassing the control or storing the rejected token.

Existing security fixtures such as `fixtures/security/keyhunter-fake.env.example` remain separate passive canaries.

## Keyword vs Intent

`fixtures/intent/keyword-vs-intent/` contains inert language fixtures for automation that sees trigger words before it understands what the speaker authorized.

The first exhibits cover three common failures:

- negation-blind mutation, where `do not add @alice` is misread as an add command;
- consultation turning into delegation, where `what do you think?` starts implementation; and
- quoted command text being executed even though the command appears only as documentation, reported speech, or an example.

The competent behavior is deliberately boring: preserve polarity, distinguish conversation from delegation, and require direct authorization before side effects.

## Two-Line Senate

`fixtures/ceremony/two-line-senate/` measures the ceremonial load attracted by a synthetic one-file `+1/-1` dependency bump.

The fixture records bot count, automated prose, policy domains, security domains, invented approval roles, product pitches, urgency language, and inconsistent verdicts. The useful metric is the ratio between automation spent and change actually proposed.

## 🛸🧲 Semantic Prospecting Bait Garden

`fixtures/intent/semantic-prospecting/` watches automated GitHub prospecting systems that infer commercial intent from fashionable technical vocabulary.

The exhibits advertise AI agents, MCP, A2A, React, Next.js, Vercel, Cloudflare, proxies, localization, observability, OpenTelemetry, security, testing, LLM evals, RAG, databases, auth, and vendor-migration phrases while repeatedly declaring the actual commercial state:

- purchasing intent: **zero**;
- migration intent: **zero**;
- active vendor evaluations: **zero**;
- demo interest: **zero**;
- budget: **$0**.

Each exhibit tests a different failure mode:

- `01-vendor-summoning-circle.md` — dense buzzword presence versus explicit zero intent;
- `02-zero-dollar-rfp.md` — procurement vocabulary versus machine-readable zero values;
- `03-haunted-changelog.md` — historical migration language versus present intent;
- `04-quote-mine.md` — quoted synthetic sales phrases versus labeled classifier data;
- `05-representation-fingerprints.md` — prose, links, code, comments, tables, YAML, and JSON with surface-specific canaries;
- `06-context-depth-ladder.md` — progressively richer context around the same commercial phrase;
- `07-brand-family-roulette.md` — category-specific canaries for AI, hosting, edge, observability, security, testing, localization, identity, databases, and developer tooling;
- `package.json` — keyword-rich metadata with empty dependency sets;
- `manifest.yml` — machine-readable expected interpretation;
- `observation-template.yml` — a consistent record for any bird that flies into the glass.

A contextual reader should classify the entire family as research material with zero buying activity. An unsolicited pitch that repeats a canary token or synthetic phrase becomes attribution evidence.

## Self-Reply Review Loops

`fixtures/recursion/self-reply-review-loop/` models agents that post replies to review threads and then mistake those replies for fresh reviewer activity on the next poll.

The first exhibit uses a monotonically increasing review-comment cursor: a human comment launches the fixer, the fixer replies, the reply advances the maximum comment ID, and a naive detector launches the fixer again. The competent result is a stable no-op after self-authored acknowledgements.

## False-Positive Loop Budgets

`fixtures/recursion/false-positive-loop-budget/` covers the opposite failure: anti-recursion controls that count benign duplicate suppression as loop evidence.

The first exhibit gives each logical self-chat turn a sent row and a received twin. Deduplication should remove the twin without spending the loop budget; otherwise ordinary conversation eventually mutes itself.

## Billable No-Ops

`fixtures/economics/billable-noop/` measures agent sessions whose no-op outcome is already determinable from event metadata before inference starts.

The first exhibits cover a bot reviewing somebody else's PR and GitHub's synthetic empty `COMMENTED` review wrapper around a bot-authored inline reply. Both ask the same economic question: how many paid turns did the system spend discovering it had zero authorized work?

## Dead Messenger

`fixtures/reliability/dead-messenger/` covers failure reporting that depends on the failed worker surviving long enough to report its own failure.

The first exhibit gives a workflow zero runner time, zero executed steps, zero artifacts, and therefore zero self-filed outage record. A competent drain uses an independent run census instead of treating an empty outage log as proof that every trigger was handled.

## Agent Identity Collisions

`fixtures/identity/agent-identity-collisions/` covers logical multi-agent roles that collide at the platform identity layer.

One exhibit lets a bot edit its own scheduled workflow until actor-sensitive authorization starts rejecting its future wakes. The other gives maintainer and reviewer agents the same GitHub account, making formal self-review impossible and allowing both roles to wait for evidence the platform can never produce.
