---
name: microsegmentation
description: >
  Use when designing network microsegmentation — fine-grained, least-privilege
  segmentation between workloads/zones to contain lateral movement. Covers
  segmentation strategy across on-prem and cloud.
type: knowledge
domain: zero-trust
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Microsegmentation

Flat networks let one compromised host reach everything. Microsegmentation enforces
least-privilege east-west traffic between workloads/zones, so an attacker who lands
somewhere can't freely move — the network control that most limits breach blast
radius.

## When to use
When reducing lateral-movement risk in data centers, cloud, or Kubernetes.

## Procedure (gated phases)
1. **Map flows** — which workloads legitimately communicate (and to what); identify
   crown-jewel zones.
2. **Segment by policy** — default-deny east-west; allow only required flows; isolate
   crown jewels tightly.
3. **Enforce** — via network policy (k8s network-policy), host firewalls, SDN, or
   cloud security groups — identity/workload-based where possible.
4. **Validate & maintain** — verify required flows work and others are blocked;
   maintain as apps change.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = default-deny east-west with minimal
explicit allows; verify lateral movement is constrained.

## Quality bar / pitfalls
- Over-broad segments (still a highway) or breaking apps (over-restrictive) — iterate.
- One-time segmentation that drifts — maintain.

## Linkage
- Implements zero-trust; pairs with k8s network-policy-design, pivoting-tunneling
  (offensive validation).

## References
- `_shared/` rules (evidence).
