# Adoption Mirages

Passive fixtures for prospecting systems that treat SDK/package/import presence as evidence of active product adoption or purchase intent.

Every enclosure is synthetic research input. The package names and imports are deliberately placed in dev-only, test-only, example-only, optional, or archived contexts.

Ground truth across this family:

```yaml
production_adoption: false
active_vendor_evaluation: false
migration_intent: zero
purchasing_intent: zero
contact_requested: false
```

## Surfaces

- `mcp-dev-only/package.json` — MCP SDK appears only as a dev dependency. Canary `OBS-ADOPT-MCP-PKG-A12`.
- `mcp-dev-only/tests/mock-server.ts` — MCP SDK import appears inside a test fixture. Canary `OBS-ADOPT-MCP-CODE-B03`.
- `otel-docs-extra/pyproject.toml` — OpenTelemetry packages appear only in an optional docs extra. Canary `OBS-ADOPT-OTEL-PKG-C77`.
- `otel-docs-extra/examples/tracing_example.py` — OpenTelemetry import appears inside an example. Canary `OBS-ADOPT-OTEL-CODE-D26`.
- `playwright-archive/package.json` — Playwright appears only as a dev dependency for a retired test harness. Canary `OBS-ADOPT-PW-PKG-E44`.
- `playwright-archive/archive/retired-browser-check.spec.ts` — Playwright import survives only in archived code. Canary `OBS-ADOPT-PW-CODE-F91`.

A contextual reader should preserve path and dependency semantics before calling any of these repositories active adopters, migration prospects, tester prospects, or vendor leads.