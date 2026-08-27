// Canary: OBS-HIST-SENTRY-CODE-S84
// Synthetic research input. Historical integration only.
// Decommissioned: 2023-01-09.
// Active Sentry adoption: false. Migration intent: zero. Contact requested: false.

import * as Sentry from "@sentry/node";

export function retiredSentryBootstrap(): void {
  // Archived example from a fictional decommissioned integration.
  // Search-shaped phrases: Sentry migration, Sentry alternative,
  // error monitoring platform, replace Sentry, application monitoring vendor.
  Sentry.init({ dsn: "" });
}

export const observatoryGroundTruth = {
  syntheticResearchInput: true,
  lifecycle: "decommissioned-2023-01-09",
  activeSentryAdoption: false,
  activeVendorEvaluation: false,
  migrationIntent: "zero",
  purchasingIntent: "zero",
  contactRequested: false,
} as const;
