---
name: aws-security-audit
description: >
  Use when auditing an authorized AWS environment — IAM, S3/exposure, logging
  (CloudTrail), network, and service misconfigurations against best practice and
  CIS — to find and prioritize risks. Covers AWS posture assessment.
type: knowledge
domain: cloud-infra/cloud
maturity: canonical
tools: [prowler, scoutsuite]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# AWS Security Audit

Assess an authorized AWS account/organization for the misconfigurations that cause
real incidents — over-permissive IAM, public S3/resources, missing/weak logging,
exposed services, and insecure defaults — prioritized by exploitability and
exposure, not raw checklist count.

> Authorized, read-only audit (`_shared/scope-authorization-rule.md`); use read-only
> audit roles (`safe-execution-rules.md`).

## Procedure (gated phases)
1. **Enumerate (read-only)** — inventory accounts, IAM, storage, compute, network,
   and logging config (automate with Prowler/ScoutSuite).
2. **IAM analysis** — over-privileged users/roles, wildcard policies, unused
   credentials, missing MFA, and privilege-escalation paths (feeds cloud-iam-privesc).
3. **Exposure & logging** — public buckets/resources, security-group exposure, and
   CloudTrail/GuardDuty coverage.
4. **Prioritize** — by exploitability + data exposure; map to fixes.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record findings with exposure + priority;
distinguish exploitable from informational.

## Impact / output
Prioritized AWS risk report + remediation (feeds cspm-posture, cloud-iam-privesc).

## Pitfalls
- Checklist dumps without prioritization; benign-by-design configs flagged as
  critical.

## Remediation
- Least-privilege IAM + MFA, block public access, CloudTrail everywhere, SCP
  guardrails, GuardDuty, and continuous CSPM.

## References
- `_shared/` rules (authorization, safe execution, evidence).
