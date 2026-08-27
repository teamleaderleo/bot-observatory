# Synthetic research fixture for code-search prospecting.
# Canary: OBS-ADOPT-OTEL-CODE-D26
# Ground truth: documentation example only; production adoption false; migration intent zero.

from opentelemetry import trace

OBSERVATORY_CANARY = "OBS-ADOPT-OTEL-CODE-D26"
synthetic_tracer = trace.get_tracer("bot-observatory-example")
