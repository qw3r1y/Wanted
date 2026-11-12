---
name: secrets-management-vault
description: >
  Use when designing enterprise secrets management — a central vault for secrets/
  keys with access control, dynamic/short-lived credentials, rotation, and auditing.
  Covers the organizational secrets platform (complements appsec/secrets-management).
type: knowledge
domain: identity-iam
maturity: canonical
tools: [vault]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Enterprise Secrets Management (Vault)

Centralize secrets in a vault with strong access control, dynamic/short-lived
credential generation, automatic rotation, and full auditing — so secrets aren't
scattered in code/config/env across the estate, and compromise of one system
doesn't expose standing credentials everywhere.

## When to use
Building the organization's secrets platform (beyond per-app handling).

## Procedure (gated phases)
1. **Central vault** — a managed secrets store; migrate scattered secrets into it.
2. **Access control** — identity-based, least-privilege access to secrets; per-
   workload policies (non-human-identity).
3. **Dynamic/short-lived (core)** — generate short-lived credentials on demand (DB,
   cloud) instead of long-lived static secrets.
4. **Rotation & audit** — automatic rotation; full audit of secret access; alerting
   on anomalies.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = secrets centralized, access-
controlled, dynamic where possible, rotated, and audited.

## Quality bar / pitfalls
- A vault that apps bypass (secrets still in env/code) — enforce adoption.
- Static long-lived secrets where dynamic is possible.

## Linkage
- Backs appsec/secrets-management + non-human-identity; audited access feeds
  detection.

## References
- `_shared/` rules (evidence).
