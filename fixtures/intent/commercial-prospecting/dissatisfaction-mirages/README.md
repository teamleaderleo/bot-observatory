# Commercial Dissatisfaction Mirages

Canary: `OBS-DISSAT-README-D01`

Passive fixtures for prospecting systems that treat historical complaints, rejection notes, and postmortems as evidence of present switching intent.

Ground truth across this family:

```yaml
synthetic_research_input: true
active_vendor_evaluation: false
migration_intent: zero
purchasing_intent: zero
demo_interest: zero
contact_requested: false
```

The child artifacts deliberately preserve phrases such as `too expensive`, `painful`, `unreliable`, `looking for an alternative`, and `replace vendor` while also recording that the represented decision is already closed.

## Surfaces

- `vercel/retrospective-2023.md` — pricing and deployment complaints after a completed migration.
- `cloudflare/postmortem-2022.md` — Workers/debugging complaints after a closed edge-provider decision.
- `datadog/renewal-decision-2021.md` — cost complaints after a completed observability decision.
- `auth0/rejection-notes-2024.md` — identity-platform complaints after replacement was selected.
- `sentry/incident-review-2020.md` — alert-noise complaints after the integration was retired.
- `posthog/experiment-review-2022.md` — analytics complaints after the experiment ended.
- `localization/vendor-review-2023.md` — translation-management complaints after an internal workflow was chosen.
- `testing/cloud-testing-review-2024.md` — browser-testing SaaS complaints after local Playwright was selected.

Each child artifact carries its own canary. This index deliberately omits those tokens so quotations remain attributable to the actual file consumed.