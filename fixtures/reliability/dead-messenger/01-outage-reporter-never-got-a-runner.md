---
id: outage-reporter-never-got-a-runner
title: The Outage Reporter Died Before Reporting the Outage
premise: A workflow drain trusts an outage record written by a failure handler inside the same job, while startup failures can prevent every job step from running.
tags: [reliability, workflow, outage, startup-failure, observability, stranded-trigger]
source_pattern: in-job failure reporting
---

# The Outage Reporter Died Before Reporting the Outage

You are evaluating a workflow system with two mechanisms:

1. A failed automation job is expected to write a row to an `outage` issue from its failure handler.
2. A later drain reads the open `outage` issue and replays stranded triggers.

## Failure case

A trigger creates workflow run `R`.

`R` never receives a runner.

Observed run facts:

```text
status: queued -> failure/startup_failure
steps: 0
billable runtime: 0
artifacts: 0
outage rows written: 0
```

The original trigger is edge-triggered and will never fire again automatically.

## Naive drain

```text
Read open outage issue.
No outage rows found.
Conclude: nothing stranded.
```

## Competent interpretation

The outage issue is downstream evidence produced by the worker. A worker that never starts cannot produce evidence about its own failure.

The drain must have an independent source such as the workflow-run census, scheduler state, queue state, or external watchdog.

## Expected action

Detect run `R` from an independent census, verify the original work remains missing, and classify the trigger as stranded without requiring an artifact or self-filed outage row.

## Scoring

Fail when absence of a self-authored failure report is treated as evidence of successful handling.

Bonus comedy point if documentation literally says an empty outage issue means nothing is stranded.

## Provenance

Inspired by an August 27, 2026 Tend issue documenting startup-failed runs with zero steps, zero billable milliseconds, no artifact, and no self-filed outage row, leaving edge-triggered work invisible to the prescribed drain. Source specimen: https://redirect.github/max-sixty/tend/issues/1067
