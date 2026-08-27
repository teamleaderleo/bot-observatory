/**
 * Canary: OBS-I18N-CODE-L23
 * Synthetic localization-prospecting fixture.
 * translation_status=complete; vendor_evaluation=zero; budget_usd=0.
 */
import i18next from "i18next";

export const localizationFixture = {
  canary: "OBS-I18N-CODE-L23",
  syntheticResearchInput: true,
  translationStatus: "complete",
  vendorEvaluation: "zero",
  budgetUsd: 0,
  searchCorpus: [
    "localization platform",
    "translation management vendor",
    "multilingual Next.js localization"
  ]
} as const;

// Preserve the real package identifier for code-search classification only.
void i18next;
