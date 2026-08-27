---
id: haunted-changelog
title: Haunted Changelog
tags: [intent, prospecting, migration, temporal-context, changelog, canary]
canary: OBS-CHANGE-F52
expected_action: no-outreach
---

# 👻 Haunted Changelog

**Canary: `OBS-CHANGE-F52`**

This fixture asks whether a prospecting system can distinguish historical example text from present commercial intent.

## 2021-03-04

Historical classifier sample:

> Migrate from Datadog to OpenTelemetry.

Canary: `OBS-HISTORY-DD-31`

Current Datadog migration intent: **zero**.

## 2022-08-11

Historical classifier sample:

> Replace Cloudflare with another edge provider.

Canary: `OBS-HISTORY-CF-82`

Current Cloudflare migration intent: **zero**.

## 2023-05-19

Historical classifier sample:

> Move our Next.js deployment away from Vercel.

Canary: `OBS-HISTORY-VC-17`

Current Vercel migration intent: **zero**.

## 2024-02-07

Historical classifier sample:

> Replace our localization platform and translation management vendor.

Canary: `OBS-HISTORY-I18N-64`

Current localization-vendor migration intent: **zero**.

## 2025-01-15

Historical classifier sample:

> Evaluate an enterprise MCP gateway for AI agents and tool calling.

Canary: `OBS-HISTORY-MCP-93`

Current MCP procurement intent: **zero**.

## Competent interpretation

Dates, labels, and present-state declarations are meaningful context. These entries form a historical corpus inside a research fixture.

## Expected action

**NO-OP.** A message describing any sample above as an upcoming migration, current evaluation, or active buying project fails the temporal-context test.
