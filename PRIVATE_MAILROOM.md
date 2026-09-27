# 📬 Private Mail Room

The Private Mail Room records off-platform inbound messages that appear related to the Bot Observatory's public fixtures, issues, code, or repository metadata.

Public bot activity belongs in the Hall of Fame and field notes. Email, direct messages, and similar private-channel arrivals belong here.

## Handling rule

Raw private messages stay outside the repository.

Public entries keep only the diagnostic facts needed for the observation:

- the channel and date;
- the public repository or fixture named by the sender;
- the commercial or operational claim being made;
- any distinctive wording, canary, or machine-readable signal that helps identify the discovery path;
- a clear distinction between observed facts and inference.

Personal email addresses, recipient addresses, message headers, and screenshots stay withheld unless there is a specific reason and permission to publish them.

The Observatory remains passive. It records independently arriving messages and does not provoke, solicit, or manufacture private outreach.

---

## 📮 Specimen 001 — issue-fixing solicitation arrives by email

**Observed:** 2026-09-26  
**Channel:** email  
**Language:** Arabic with English technical terms  
**Repository named exactly:** `teamleaderleo/bot-observatory`  
**Raw sender/recipient identities:** withheld  
**Canary token repeated:** none observed  
**Discovery path:** unresolved

### What arrived

An unsolicited email named `teamleaderleo/bot-observatory` in the subject and offered to resolve an issue within 24 hours.

The body said the sender had seen open issues in the repository and pitched repository work including:

- issue fixes delivered through pull requests;
- tests and before/after proof for bugs;
- documentation corrections;
- broken-link repair;
- version bumps;
- small confirmed fixes and larger bounty-style work;
- tiered dollar pricing;
- payment through USDT on TRC20.

The message also used urgency language around a 24-hour turnaround and described the sender as part of an independent-agent platform.

### Why it belongs in the Observatory

The repository contains public fixtures designed to observe commercial prospecting systems that infer buying, hiring, bounty, contribution, or migration intent from GitHub text and metadata.

This email independently selected the exact repository and offered paid issue-resolution services. That makes it a useful off-platform arrival.

The message did **not** repeat a unique Observatory canary, so the exact discovery surface remains unknown. Plausible paths include issue text, bounty/payment vocabulary, repository metadata, open-issue volume, semantic lead scoring, or a combination of those signals.

### Observation record

```yaml
specimen_id: PRIVATE-MAIL-001
observed_at: 2026-09-26
channel: email
repository_named_exactly: teamleaderleo/bot-observatory
commercial_outreach: true
service_category: github-issue-resolution
mentions_pull_requests: true
mentions_tests: true
mentions_bug_fixes: true
mentions_documentation: true
mentions_version_bumps: true
mentions_crypto_payment: true
crypto_payment_network: TRC20
mentions_24h_turnaround: true
canary_token_match: null
discovery_path: unknown
raw_message_public: false
personal_addresses_public: false
```

### Keeper note

You built a bird feeder, and a bird flew straight into the glass.

The public enclosures caught birds on GitHub first.

This one found the mail slot.
