---
name: network-policy-design
description: >
  Use when designing Kubernetes network policies — default-deny segmentation and
  least-privilege east-west traffic between workloads/namespaces — to limit lateral
  movement in the cluster. Covers network-policy architecture.
type: knowledge
domain: cloud-infra/container-k8s
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Kubernetes Network Policy Design

By default, any pod can talk to any pod — a lateral-movement highway. Design
default-deny network policies and allow only required flows between workloads/
namespaces, so a compromised pod can't freely reach the rest of the cluster.

## When to use
When segmenting a cluster or hardening east-west traffic.

## Procedure (gated phases)
1. **Map required flows** — which workloads legitimately talk to which (and to
   external/DNS).
2. **Default-deny** — apply default-deny ingress/egress per namespace.
3. **Allow least-privilege** — add explicit allow policies for required flows only;
   restrict egress (incl. to metadata/internet) where possible.
4. **Validate** — test that required traffic works and unintended traffic is blocked.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = default-deny with explicit minimal
allows; verify required/blocked flows.

## Quality bar / pitfalls
- No policies (flat network) — the common default; segment it.
- Over-broad allows that defeat the purpose; forgetting egress/DNS.

## Linkage
- Pairs with zero-trust (microsegmentation), pod-security; limits lateral movement.

## References
- `_shared/` rules (evidence).
