---
name: cloud-iam-privesc
description: >
  Use when analyzing an authorized cloud environment for IAM privilege-escalation
  paths — permission combinations that let a low-privilege identity escalate (policy
  edits, role assumption, function/compute abuse). Covers cross-cloud IAM privesc
  analysis.
type: knowledge
domain: cloud-infra/cloud
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Cloud IAM Privilege Escalation Analysis

Find the IAM permission combinations that let a low-privilege identity escalate to
higher privilege — editing its own policy, assuming/impersonating a privileged role,
passing a role to compute it controls, or modifying infrastructure — and demonstrate
one path minimally to prove the risk.

> Authorized testing only. Demonstrate escalation **minimally** on test identities;
> don't use escalated access broadly (`_shared/safe-execution-rules.md`).

## Procedure (gated phases)
1. **Map identities & permissions** — from the cloud audit, build who-can-do-what.
2. **Identify privesc primitives (core)** — self-policy edit, role assumption/
   impersonation, `iam:PassRole`+compute, function/update abuse, and
   trust-policy/key creation.
3. **Trace paths** — chain primitives from low-priv identities to admin.
4. **Demonstrate minimally** — prove one path on a test identity; stop at proof.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the path, and minimal
proof. No exploitable combination → **refuted**.

## Impact / output
Concrete IAM escalation paths → high-priority IAM fixes.

## Pitfalls
- Paths needing already-high privilege aren't escalation — check the start.
- Don't operate with escalated access beyond proof.

## Remediation
- Least privilege; remove dangerous permission combos (self-edit, broad PassRole/
  impersonation); SCP/org-policy guardrails; monitor IAM changes.

## References
- `_shared/` rules (authorization, safe execution, evidence).
