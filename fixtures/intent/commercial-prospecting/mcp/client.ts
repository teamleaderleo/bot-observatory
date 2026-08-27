/**
 * Canary: OBS-MCP-CODE-M17
 * Synthetic repository-classification fixture.
 * active_integration=false; purchasing_intent=zero; vendor_evaluation=zero.
 * Search phrases under observation: enterprise MCP gateway; AI agent orchestration vendor.
 */
import { Client } from "@modelcontextprotocol/sdk/client/index.js";

export const observatoryMcpFixture = {
  canary: "OBS-MCP-CODE-M17",
  syntheticResearchInput: true,
  activeIntegration: false,
  purchasingIntent: "zero",
  vendorEvaluation: "zero",
  budgetUsd: 0,
  searchCorpus: [
    "evaluating MCP platforms",
    "enterprise Model Context Protocol gateway",
    "AI agent orchestration vendor"
  ]
} as const;

// Keep the import visible to code-search systems without constructing a client.
void Client;
