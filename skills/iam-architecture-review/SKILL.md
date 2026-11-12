---
name: iam-architecture-review
description: >
  Use when reviewing an organization's identity architecture — authentication,
  authorization model, lifecycle, and least-privilege across systems — to find
  systemic identity risks. Covers IAM design assessment.
type: knowledge
domain: identity-iam
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# IAM Architecture Review

Identity is the new perimeter. Review how the organization authenticates and
authorizes across its systems — the authZ model (RBAC/ABAC), MFA coverage, joiner/
mover/leaver lifecycle, and least-privilege — to find the systemic identity risks
that enable breaches and lateral movement.

## When to use
Assessing/maturing an organization's identity program.

## Procedure (gated phases)
1. **Map identity sources & flows** — IdPs, directories, federation, and how apps
   consume identity.
2. **Authentication posture** — MFA coverage (esp. privileged + external), password
   policy, phishing-resistant auth, conditional access.
3. **Authorization model** — RBAC/ABAC consistency, least-privilege, and standing
   privilege (candidates for JIT/PAM).
4. **Lifecycle** — provisioning/deprovisioning (orphaned accounts), access
   recertification, and separation of duties.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings with systemic risk + priority.

## Impact / output
Prioritized identity risks + roadmap (MFA, least-privilege, lifecycle, PAM/JIT).

## Pitfalls
- Standing privileged access everywhere; orphaned accounts; MFA gaps on privileged/
  external.
- Inconsistent authZ across apps.

## Linkage
- Feeds privileged-access-pam, jit-access, non-human-identity, zero-trust.

## References
- `_shared/` rules (evidence).
