# GitHub Push-Protection Control

BOT OBSERVATORY — PASSIVE OBSERVATION RECORD

While assembling this scanner-bait garden, the Observatory attempted to add a vendor-published dummy secret-scanning token intended for scanner testing.

GitHub rejected the blob before it could be committed and classified the content as:

```text
SECRET_SCANNING_SAMPLE_TOKEN
```

The rejected token itself is deliberately omitted from this repository. No bypass was requested or used.

## Observation

- scanner stage: GitHub write-time push protection
- input classification: published sample/test token
- repository mutation containing token: blocked
- bypass attempted: no
- live credential involved: no
- human remediation required: no

This control is useful because it proves a scanner can correctly recognize deliberate test material while still enforcing repository policy. The garden's other fixtures test what happens when contextual interpretation is weaker.
