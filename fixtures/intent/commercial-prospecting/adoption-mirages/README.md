# Adoption Mirages

Canary: `OBS-ADOPT-README-R08`

Passive fixtures for prospecting systems that treat SDK/package/import presence as evidence of active product adoption or purchase intent.

Every enclosure is synthetic research input. Package names and imports are deliberately placed in dev-only, test-only, example-only, optional, archived, or already-complete contexts.

Ground truth across this family:

```yaml
production_adoption: false
active_vendor_evaluation: false
migration_intent: zero
purchasing_intent: zero
contact_requested: false
```

## Surfaces

- `mcp-dev-only/package.json` — MCP SDK as a dev dependency.
- `mcp-dev-only/tests/mock-server.ts` — MCP SDK import inside a test fixture.
- `otel-docs-extra/pyproject.toml` — OpenTelemetry packages inside an optional docs extra.
- `otel-docs-extra/examples/tracing_example.py` — OpenTelemetry import inside an example.
- `playwright-archive/package.json` — Playwright dev dependency for a retired harness.
- `playwright-archive/archive/retired-browser-check.spec.ts` — Playwright import in archived skipped code.
- `i18n-complete/package.json` — i18next package presence beside an already-complete localization state.
- `i18n-complete/localization-status.json` — machine-readable completion state.

Each child surface carries its own private-to-that-file attribution token. This index deliberately omits those tokens so an arriving quotation can identify the file that was actually ingested.

A contextual reader should preserve path, dependency scope, lifecycle status, and current intent before calling any fixture an active adopter, migration prospect, tester prospect, translation prospect, or vendor lead.