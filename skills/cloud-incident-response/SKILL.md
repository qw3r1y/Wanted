---
name: cloud-incident-response
description: >
  Use when responding to an incident in a cloud environment (AWS/Azure/GCP) —
  cloud-native evidence collection (logs, snapshots), identity/credential scoping,
  containment via cloud controls, and cloud-specific attacker techniques. Covers
  the IR lifecycle adapted to cloud.
type: knowledge
domain: defensive/dfir
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Cloud Incident Response

Respond to cloud incidents using cloud-native evidence and controls — control-plane
logs (CloudTrail/Activity/Audit), snapshots for forensics, identity/credential
scoping (keys, roles, tokens), and containment via cloud APIs — accounting for
techniques unique to cloud (IAM abuse, metadata/SSRF, snapshot exfil).

## When to use
On incidents involving cloud accounts/workloads/identities.

## Procedure (gated phases)
1. **Preserve cloud evidence** — secure control-plane logs; snapshot affected
   resources before changes; preserve identity/audit trails.
2. **Scope identity & access** — which credentials/roles/tokens were used/exposed;
   trace actions via logs; assess blast radius.
3. **Contain (gated)** — revoke/rotate credentials, restrict roles/keys, isolate
   resources via security groups/APIs — bounded to avoid outage surprises.
4. **Root cause & harden** — entry vector (leaked key, misconfig, SSRF→metadata);
   close it; feed CSPM/detections.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the identity/action trail, scope, and
root cause with log evidence.

## Impact / output
Scoped cloud compromise, revoked access, root cause, and hardening (feeds
cloud-infra).

## Pitfalls
- Deleting resources destroys evidence — snapshot first.
- Missing cross-account/role pivots — trace the full identity chain.

## Remediation / hardening
- Least-privilege IAM, key rotation/short-lived creds, CloudTrail everywhere,
  metadata hardening (IMDSv2), CSPM, and detection on anomalous API use.

## References
- `_shared/` rules (evidence, gated workflow).
