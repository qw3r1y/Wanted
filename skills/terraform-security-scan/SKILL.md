---
name: terraform-security-scan
description: >
  Use when scanning Terraform (and other IaC) for security misconfigurations before
  deploy — insecure resource settings, exposed access, and policy violations — to
  shift cloud security left. Covers IaC scanning and gating.
type: knowledge
domain: cloud-infra/iac
maturity: canonical
tools: [checkov, tfsec]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Terraform / IaC Security Scanning

Catch cloud misconfigurations in the IaC before they're deployed — public storage,
open security groups, missing encryption/logging, over-broad IAM — so the cloud is
secure by construction rather than fixed after exposure.

## When to use
In CI on IaC changes and pre-deploy.

## Procedure (gated phases)
1. **Scan IaC** — Terraform/CloudFormation/etc. against security policies (Checkov/
   tfsec) for misconfigurations.
2. **Prioritize** — real exposure (public/unencrypted/over-broad IAM) over stylistic
   checks; account for module context.
3. **Gate** — fail CI on high-severity real misconfigurations; allow justified
   exceptions with audit.
4. **Remediate** — fix in code; prevent recurrence via policy (opa-rego/checkov-
   policy).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings with exposure + priority; gate on
real risk.

## Quality bar / pitfalls
- Noise from stylistic checks → fatigue; prioritize exposure.
- Scanning only some IaC — cover all cloud-defining code.

## Deployment
- CI gate; custom policies (checkov-policy/opa-rego); drift detection post-deploy.

## References
- `_shared/` rules (evidence).
