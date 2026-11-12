---
name: secret-scanning-in-pipeline
description: >
  Use when preventing secret leaks via CI/CD — pre-commit + pipeline secret scanning
  that blocks secrets before they land and catches them in history, with rotation
  workflow. Covers pipeline secret-leak prevention.
type: knowledge
domain: ci-cd-devsecops
maturity: canonical
tools: [gitleaks, trufflehog]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Pipeline Secret-Leak Prevention

Stop secrets before they reach the repo and catch those that already did: run secret
scanning at pre-commit (block locally) and in the pipeline (block PRs), scan history,
and wire in rotation — because once a secret hits a remote repo, it must be treated
as compromised.

## When to use
As a standard pipeline + developer control against credential leaks.

## Procedure (gated phases)
1. **Pre-commit** — local hooks that block committing secrets (fast feedback, stops
   leaks at source).
2. **Pipeline gate (core)** — scan PRs/commits; block merges containing secrets;
   scan full history periodically.
3. **Validate & rotate** — on a hit, determine if live (api/api-key-leakage); if a
   secret reached the remote, rotate it (it's compromised) + purge history.
4. **Reduce false positives** — allow-list test/example values; tune.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = secrets are blocked pre-merge and
leaked ones trigger rotation.

## Quality bar / pitfalls
- Scanning only current tree (missing history).
- Treating a blocked-but-already-pushed secret as "handled" without rotating.

## Linkage
- Operationalizes appsec/secret-scanning; feeds secrets-management adoption.

## References
- `_shared/` rules (evidence).
