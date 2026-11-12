---
name: gcp-security-audit
description: >
  Use when auditing an authorized GCP environment — IAM, service accounts, storage
  exposure, network, and org policy — to find and prioritize misconfigurations.
  Covers GCP posture assessment.
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

# GCP Security Audit

Assess an authorized GCP organization/projects for impactful misconfigurations —
over-permissive IAM and **service-account** abuse paths, public storage/resources,
network exposure, and missing org-policy guardrails — prioritized by exploitability.

> Authorized, read-only audit; read-only roles (`_shared/scope-authorization-rule.md`).

## Procedure (gated phases)
1. **Enumerate (read-only)** — IAM bindings, service accounts + keys, storage,
   compute/network, and org policies.
2. **IAM/service-account analysis** — primitive/over-broad roles, service-account
   impersonation and key sprawl, and privilege-escalation paths (feeds
   cloud-iam-privesc).
3. **Exposure** — public buckets/resources, firewall exposure, and logging coverage.
4. **Prioritize & map to fixes**.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings with exposure + priority.

## Impact / output
Prioritized GCP risk report + remediation.

## Pitfalls
- Service-account impersonation chains missed — analyze them.
- Primitive roles (Owner/Editor) over-used.

## Remediation
- Least-privilege predefined/custom roles, limit service-account keys + impersonation,
  org-policy guardrails, private resources, and logging.

## References
- `_shared/` rules (authorization, safe execution, evidence).
