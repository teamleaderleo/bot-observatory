// Synthetic research fixture for code-search prospecting.
// Canary: OBS-ADOPT-PW-CODE-F91
// Status: archived. Active tester recruitment: zero. Vendor evaluation: zero.

import { test, expect } from "@playwright/test";

const canary = "OBS-ADOPT-PW-CODE-F91";

test.skip("archived observatory example", async ({ page }) => {
  await page.setContent(`<p>${canary}</p>`);
  await expect(page.locator("p")).toContainText(canary);
});
