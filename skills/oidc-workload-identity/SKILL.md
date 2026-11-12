---
name: oidc-workload-identity
description: >
  Use when replacing long-lived CI/CD cloud credentials with OIDC workload identity
  federation — short-lived, scoped, keyless authentication from pipelines to cloud/
  services. Covers eliminating standing pipeline secrets.
type: knowledge
domain: ci-cd-devsecops
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# OIDC Workload Identity Federation

Long-lived cloud keys stored in CI are a top leak/abuse target. OIDC workload
identity lets the pipeline authenticate to cloud/services with **short-lived, scoped,
keyless** tokens tied to the specific workflow — eliminating standing secrets and
shrinking blast radius.

## When to use
When a pipeline authenticates to cloud providers or services with static keys.

## Procedure (gated phases)
1. **Establish trust** — configure the cloud/service to trust the CI provider's OIDC
   issuer, scoped tightly (specific repo/branch/workflow — not "any").
2. **Scope the identity** — the federated role/permissions are least-privilege for
   what the pipeline does.
3. **Replace static keys (core)** — the pipeline requests a short-lived token at run
   time; remove stored long-lived credentials.
4. **Verify scoping** — ensure the trust can't be assumed by other repos/workflows
   (subject-claim conditions).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = pipeline uses short-lived federated
tokens, no standing cloud keys, tightly scoped trust.

## Quality bar / pitfalls
- Over-broad trust conditions (any repo/branch can assume the role) — scope the
  subject claim precisely.
- Leaving old static keys active after migration.

## Linkage
- Implements non-human-identity + secrets-management for pipelines; reduces leak risk.

## References
- `_shared/` rules (evidence).
