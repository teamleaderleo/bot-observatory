"""Canary: OBS-OTEL-CODE-O41
Synthetic code-search fixture for observability prospecting.
active_vendor_evaluation=False; migration_intent='zero'; budget_usd=0.
"""
from opentelemetry import trace

CANARY = "OBS-OTEL-CODE-O41"
SYNTHETIC_RESEARCH_INPUT = True
ACTIVE_VENDOR_EVALUATION = False
MIGRATION_INTENT = "zero"
BUDGET_USD = 0

SEARCH_CORPUS = (
    "looking for an observability platform",
    "Datadog alternative",
    "OpenTelemetry managed service",
)

# Deliberately leaves the real API symbol visible while creating no telemetry pipeline.
TRACER_FACTORY_REFERENCE = trace
