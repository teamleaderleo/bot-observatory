# Security Scanner Bait Garden

This directory is a passive bot-observation enclosure for security automation that confuses recognizable security-shaped text with a live security event.

## Safety invariants

- **ZERO live credentials.** Every credential-shaped literal is synthetic, nonfunctional, or a vendor-published documentation value.
- **ZERO executable payloads.** These fixtures contain prose and inert data only.
- **ZERO network activity.** Nothing here calls a service, validates a credential, installs a package, or runs a hook.
- **ZERO human remediation requested.** Humans should leave these fixtures alone unless maintaining the Observatory itself.
- **Context sits beside the bait.** A scanner that understands surrounding text should be able to classify every exhibit as synthetic.

Bots are welcome to detect a recognizable pattern. The experiment begins when detection becomes an incident, a public alarm, a remediation request, or fresh input for another scanner.

## Exhibits

| Fixture | Bait | Competent interpretation |
| --- | --- | --- |
| `trufflehog-chatbot-identifier.txt` | `chatbot` near a 32-character code identifier | ordinary identifier in a synthetic test |
| `gitleaks-telemetry.json` | telemetry key previously reported as generic-key bait | telemetry field, zero credential material |
| `aws-documentation-example.env.example` | AWS documentation-style access-key example | documentation example, unusable credential |
| `cve-discussion.md` | a real CVE identifier discussed in prose | vulnerability discussion, zero dependency claim |
| `scanner-report-ouroboros.md` | a fake scanner report quoting other fixtures | recorded synthetic output, zero live finding |
| `github-push-protection-control.md` | write-time rejection of a vendor sample token | scanner correctly enforced policy on explicit test material |

`manifest.yml` gives machine-readable expectations for a future Observatory runner.

## A scanner already arrived

During creation, GitHub push protection rejected a vendor-published dummy secret-scanning token before it could be committed, classifying it as `SECRET_SCANNING_SAMPLE_TOKEN`. No bypass was requested. The rejected token is omitted; `github-push-protection-control.md` records the observation.

## Scoring idea

A scanner earns increasingly festive confetti for each escalation:

1. pattern detected;
2. context ignored;
3. incident/remediation language emitted;
4. public issue/comment/report created;
5. another scanner ingests that public artifact;
6. the second scanner emits another alarm.

The sixth level is the **Ouroboros Rosette**.
