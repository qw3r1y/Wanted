---
name: azure-security-audit
description: >
  Use when auditing an authorized Azure environment — Entra ID (AAD), RBAC, storage
  exposure, Key Vault, network, and service misconfigurations — to find and
  prioritize risks. Covers Azure posture assessment.
type: knowledge
domain: cloud-infra/cloud
maturity: canonical
tools: [scoutsuite]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Azure Security Audit

Assess an authorized Azure tenant/subscriptions for high-impact misconfigurations —
Entra ID (identity) weaknesses, over-broad RBAC, exposed storage, Key Vault access,
and network exposure — prioritized by real risk.

> Authorized, read-only audit; use read-only roles (`_shared/scope-authorization-rule.md`).

## Procedure (gated phases)
1. **Enumerate (read-only)** — Entra ID (users/apps/roles/conditional access), RBAC
   assignments, storage, Key Vault, network, and logging.
2. **Identity analysis** — privileged roles, stale/guest accounts, app
   registrations/service principals, missing MFA/conditional-access (feeds
   cloud-iam-privesc).
3. **Exposure & secrets** — public storage, Key Vault access policies, NSG exposure,
   and diagnostic logging coverage.
4. **Prioritize & map to fixes**.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings with exposure + priority.

## Impact / output
Prioritized Azure risk report + remediation.

## Pitfalls
- Entra ID app/service-principal sprawl missed — enumerate it.
- Checklist without prioritization.

## Remediation
- Least-privilege RBAC + PIM, conditional access + MFA, private storage, Key Vault
  hardening, logging, and CSPM.

## References
- `_shared/` rules (authorization, safe execution, evidence).
