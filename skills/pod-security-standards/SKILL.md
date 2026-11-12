---
name: pod-security-standards
description: >
  Use when enforcing Kubernetes Pod Security — applying Pod Security Standards/
  admission to block privileged/host-access pods and enforce secure defaults.
  Covers workload-security policy.
type: knowledge
domain: cloud-infra/container-k8s
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Pod Security Standards / Admission

Enforce secure workload defaults cluster-wide so a compromised or misconfigured pod
can't trivially reach the node/cluster — block privileged containers, host
namespaces/mounts, and dangerous capabilities via Pod Security Standards (or an
admission policy like OPA/Kyverno).

## When to use
When securing a cluster's workload baseline.

## Procedure (gated phases)
1. **Choose the baseline** — map namespaces to PSS levels (privileged/baseline/
   restricted); aim for `restricted` where feasible.
2. **Enforce via admission** — PSS admission or policy engine (OPA/Kyverno) to
   **reject** non-compliant pods (not just warn).
3. **Restrict dangerous specs** — privileged, hostPID/Network/IPC, hostPath mounts,
   added capabilities, root user, writable root FS.
4. **Roll out safely** — audit → warn → enforce; fix workloads incrementally.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = non-compliant pods are rejected;
verify with test manifests.

## Quality bar / pitfalls
- Warn-only mode (no enforcement) — enforce for real protection.
- Over-broad exemptions that reintroduce risk.

## Linkage
- Pairs with k8s-rbac-audit, container-escape-analysis, dockerfile-hardening,
  admission (OPA).

## References
- `_shared/` rules (evidence).
