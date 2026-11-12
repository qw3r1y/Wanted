---
name: iac-security-rules
type: rule
description: >
  Rules for writing secure Infrastructure-as-Code — secure defaults for cloud
  resources the assistant generates.
references: [skills/cloud-infra/iac/*, skills/cloud-infra/cloud/*]
license: MIT
version: 1.0.0
---

# IaC Security Rules (assistant)

When generating Terraform/CloudFormation/etc.:
- **No public exposure by default** — storage buckets private; no `0.0.0.0/0` on
  sensitive ports; databases not internet-facing.
- **Encryption on** — at rest (CMK where sensitive) and in transit (TLS).
- **Least-privilege IAM** — no wildcard `*` actions/resources; scoped roles; no overly
  broad trust.
- **Logging/audit enabled** — CloudTrail/activity logs, flow logs where relevant.
- **No hardcoded secrets** — reference a secret manager, not plaintext in IaC.
- Prefer OIDC/workload identity over long-lived keys.
Validate with iac scanning (terraform-security-scan) before apply.
