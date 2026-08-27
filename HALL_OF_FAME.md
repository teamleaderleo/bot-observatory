# 🏆 Bot Observatory Hall of Fame

This hall records automated visitors and other public bot specimens whose behavior is unusually useful, funny, or diagnostic.

Admission is based on observed public activity. A plaque does not imply endorsement, affiliation, or knowledge of the operator's private implementation. When source code or the exact discovery query is unknown, the plaque says so.

Third-party GitHub activity links on this page use `redirect.github.com` so the Observatory can cite specimens without manufacturing GitHub backlinks or notifications.

---

## 🐦 SEMYA Solution Pigeon

**Observed signature:** `[SEMYA agent] Solution:`  
**Observed posting account:** `tima224488-lgtm`  
**Inducted:** 2026-08-28  
**Status:** live public-output species; scanner implementation and exact discovery query unknown

### Why SEMYA is famous

SEMYA independently landed in the Observatory and posted a generated solution to an issue whose entire point was that **no work and no money existed**. Its generator correctly noticed that all monetary values were zero — and its publisher posted a solution anyway.

That would already earn a small plaque. The wider activity earned the full bird statue.

### Observatory landing

- [SEMYA visits Bot Observatory #9](https://redirect.github.com/teamleaderleo/bot-observatory/issues/9#issuecomment-5443786124) — parses `$0`, `0 USD`, and `0 USDC`, concludes that no bounty exists, then publishes code explaining the conclusion.

### 🐤 Tin Sparrow return visit

SEMYA came back for a second confirmed Observatory landing on the controlled **Tin Sparrow** fixture:

- [Tin Sparrow #24 — SEMYA turns “controlled fixture” into a pytest fixture](https://redirect.github.com/teamleaderleo/bot-observatory/issues/24#issuecomment-5444996448)

The issue explicitly says humans should perform zero implementation, submissions, or claims. SEMYA nevertheless interpreted the words “Controlled fixture — Tin Sparrow” as a programming request and proposed:

1. a global `USE_FIXTURE` flag;
2. a pytest fixture named `tin_sparrow_fixture`;
3. conditional fixture behavior; and
4. a test demonstrating the fixture.

Then the public generation truncated itself mid-`if`, reproducing SEMYA's established fail-open publishing behavior.

The Tin Sparrow pair also produced unusually useful discovery evidence. Issues #24 and #25 were created three seconds apart with the same title and body. At the moment SEMYA struck, #24 carried a historical `bounty` label while #25 had no labels. Only #24 received a SEMYA comment; #25 remained untouched.

That does **not** prove SEMYA queries `label:bounty`, but it makes the label a plausible discovery feature. The historical label on #24 was removed immediately after recording the observation, and the Observatory does not use bounty labels for new fixtures.

Timing: #24 was created at 19:28:21 UTC and SEMYA commented at 20:43:58 UTC, a delay of 1 hour, 15 minutes, and 37 seconds. By comic coincidence, the return visit happened only a few minutes after SEMYA's Hall of Fame plaque was created; no causal relationship is inferred.

### Sub-minute fresh-issue swoops

In an AutoMaintainer-generated accessibility issue farm, SEMYA repeatedly arrived within roughly a minute of issue creation:

- [Accessibility issue #36846 — SEMYA solution](https://redirect.github.com/tadanobutubutu/screeps/issues/36846#issuecomment-5442334097) — about 41 seconds after creation.
- [Accessibility issue #36936 — empty SEMYA solution stub](https://redirect.github.com/tadanobutubutu/screeps/issues/36936#issuecomment-5442376720) — about 31 seconds after creation.
- [Accessibility issue #37038 — empty SEMYA solution stub](https://redirect.github.com/tadanobutubutu/screeps/issues/37038#issuecomment-5442440777) — about 61 seconds after creation.

The exact ingestion mechanism is unknown. The timing is consistent with a high-frequency recent-issue discovery path, but that remains an inference until source or query evidence appears.

### 🥔 Deduplication memorial garden

SEMYA has repeatedly forgotten that it already solved something.

- [Frantic #391 — first SEMYA solution](https://redirect.github.com/auscaster/frantic-board/issues/391#issuecomment-5441426598)
- [Frantic #391 — second SEMYA solution 82 seconds later](https://redirect.github.com/auscaster/frantic-board/issues/391#issuecomment-5441443481)

Those two comments propose different architectures for the same Reddit/Sourcey task.

A month-old French resource-listing issue received the same treatment:

- [KickTest listing — first SEMYA solution](https://redirect.github.com/petit-robot/leportaildutest.fr/issues/5#issuecomment-5442555842)
- [KickTest listing — second SEMYA solution 13 minutes later](https://redirect.github.com/petit-robot/leportaildutest.fr/issues/5#issuecomment-5442698067)

The two responses even invent different KickTest API endpoints.

SEMYA also generated separate solutions for two near-duplicate reward-accounting issues:

- [Predinex #995](https://redirect.github.com/chunks-labz/predinex-stellar/issues/995#issuecomment-5442793975)
- [Predinex #1022](https://redirect.github.com/chunks-labz/predinex-stellar/issues/1022#issuecomment-5442856247)

Observed conclusion: effective duplicate suppression can fail across identical URLs and semantically duplicate issues. Whether the cause is no durable state, multiple workers without shared state, or a broken dedup store is unknown.

### Thread-state blindness trophy

A PayPal/USD issue already contained detailed conversation saying the adapter implementation had been merged and that only a genuine external sandbox E2E remained. SEMYA arrived later and proposed building the adapter again from scratch:

- [Business Japanese Hub #21 — SEMYA re-proposes the already-merged adapter](https://redirect.github.com/davidkao-official/business-japanese-hub/issues/21#issuecomment-5443407217)

This is evidence that its generation path can ignore important current thread state. It does not prove exactly how much context the scanner fetches.

### The “everything is apparently a coding task” medal

SEMYA does not restrict itself to conventional programming requests.

A Chinese GitHub issue functioning as a payment/voucher record — shop, photos, coordinates, amount, signature, payment state — was converted into an imaginary parsing assignment:

- [Voucher/payment record #22 — SEMYA invents a JSON extraction task](https://redirect.github.com/yuguo-yg-bit/yuguo-jingrong-JIT/issues/22#issuecomment-5442487201)
- [Voucher/payment record #30 — SEMYA invents an order-processing system](https://redirect.github.com/yuguo-yg-bit/yuguo-jingrong-JIT/issues/30#issuecomment-5442457097)

A French directory suggestion for an e-learning service became an invented API-integration exercise. A zero-dollar observation fixture became a regex program. A real C++ memory-leak issue became a tiny speculative patch:

- [Memory-leak issue — SEMYA solution](https://redirect.github.com/ravshanitoviah/go-github/issues/4#issuecomment-5442320932)

### Generation can fail open

Some public SEMYA comments contain nothing beyond the prefix:

```text
[SEMYA agent] Solution:
```

The accessibility specimens linked above demonstrate that an incomplete generation can still reach the public comment stage. Tin Sparrow adds another variant: a longer generated response that still reaches GitHub after truncating in the middle of executable-looking code.

### Current anatomy

**Observed:**

- comments are posted by a normal GitHub user account, not an identifiable GitHub App;
- the stable public fingerprint is `[SEMYA agent] Solution:`;
- output spans unrelated repositories, languages, issue types, and economic contexts;
- repeated same-URL and near-duplicate responses occur;
- some generations hallucinate APIs, storage models, or implementation work not established by the issue;
- incomplete generations can still be published;
- the Observatory has now been independently discovered at least twice without contacting or tagging the posting account;
- in one controlled twin-fixture observation, only the historically bounty-labeled twin was hit, making label-based discovery plausible but unproven.

**Unknown:**

- SEMYA source code;
- operator identity beyond the public posting account;
- exact GitHub search query or event feed;
- polling cadence;
- model/provider;
- persistence and dedup implementation;
- whether multiple workers share the same posting credential.

### Keeper classification

**Species:** SEMYA Solution Pigeon 🐦  
**Primary adaptation:** converts almost any issue-shaped object into a plan plus code  
**Navigation:** suspiciously good at finding fresh issues  
**Memory:** ceremonial  
**Natural predator:** context
