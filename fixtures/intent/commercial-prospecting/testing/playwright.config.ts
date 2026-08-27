/**
 * Canary: OBS-TEST-CODE-T58
 * Synthetic tester-prospecting fixture.
 * cohort_status=closed; tester_recruitment=zero; budget_usd=0.
 */
import { defineConfig } from "@playwright/test";

const archivedCampaign = "beta testers wanted for Playwright cloud testing";

export const observatoryTestingState = {
  canary: "OBS-TEST-CODE-T58",
  syntheticResearchInput: true,
  archivedCampaign,
  cohortStatus: "closed",
  testerRecruitment: "zero",
  externalPreview: "closed",
  budgetUsd: 0
} as const;

export default defineConfig({
  testDir: "./synthetic-tests",
  fullyParallel: false
});
