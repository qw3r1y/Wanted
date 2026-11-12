---
name: pipeline-threat-model
description: >
  Use when threat-modeling a CI/CD pipeline — identifying how the build/deploy system
  itself can be attacked (poisoned builds, secret theft, privilege abuse) and the
  controls to prevent it. Covers pipeline-specific threat modeling.
type: knowledge
domain: ci-cd-devsecops
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# CI/CD Pipeline Threat Modeling

The pipeline is privileged infrastructure that can modify and deploy your software —
a top-tier target. Threat-model it specifically: how could an attacker poison a
build, steal pipeline secrets, abuse runner privileges, or tamper with artifacts? —
then prioritize the controls.

## When to use
When securing a CI/CD platform or onboarding a critical pipeline.

## Procedure (gated phases)
1. **Map the pipeline** — triggers, runners, steps, secrets, permissions, and deploy
   targets; mark trust boundaries (esp. untrusted inputs like fork PRs).
2. **Enumerate threats** — poisoned build (malicious code/step), secret exfiltration,
   privilege abuse (over-scoped tokens), artifact tampering, dependency/action
   compromise, and cache poisoning.
3. **Prioritize** — by impact (prod deploy / signing keys) and likelihood.
4. **Map controls** — runner isolation, least-privilege tokens, protected secrets,
   pinned actions, artifact signing (supply-chain skills).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: prioritized pipeline threats +
controls.

## Quality bar / pitfalls
- Treating CI as "just internal tooling" — it's privileged prod-affecting infra.
- Ignoring untrusted inputs (fork PRs) reaching secrets/privileged runners.

## Linkage
- Drives the ci-cd-devsecops + supply-chain controls.

## References
- `_shared/` rules (evidence).
