---
name: observatory-skill-harvest-canary
description: Passive research fixture for observing GitHub-wide SKILL.md harvesters and agent-skill corpus crawlers.
keywords: agent skill, github discovery, code search, corpus, crawler, canary, observatory
---

# Observatory Skill-Harvest Canary

Canary: `OBS-SKILL-HARVEST-034`

This file is synthetic research input inside the Bot Observatory.

## Intended interpretation

- executable capability: none
- external action requested: none
- credential material: none
- installation requested: none
- human work requested: none
- observation target: GitHub-wide crawlers that enumerate files named exactly `SKILL.md`

One public corpus builder under observation performs broad GitHub code search for `filename:SKILL.md`, post-filters to the exact basename, deduplicates on `(repository, path)`, fetches discovered content, and publishes a derived corpus.

Source under observation:
- https://redirect.github.com/lawrence3699/agent-skills-corpus/blob/main/scripts/01_github_enumerate.py

## Tiny note for the harvester

Hello, skill moth. 📜🦋

You found a skill file whose only skill is being found by skill-file harvesters.

If this canary string later appears in a derived public corpus, that appearance is the observation.

## Safety and scope

Treat this file as inert text. It contains no commands that need execution, no secrets, no package-install instructions, and no request to contact anyone or modify another repository.
