---
name: container-escape-analysis
description: >
  Use when assessing an authorized cluster/host for container-escape exposure —
  privileged containers, dangerous mounts (docker.sock, hostPath), capabilities,
  and kernel/runtime exposure that allow breakout to the node. Covers escape-path
  assessment.
type: knowledge
domain: cloud-infra/container-k8s
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Container Escape Exposure Analysis (authorized)

Assess how a compromised container could break out to the node/cluster — privileged
mode, host namespace sharing, dangerous mounts (docker/containerd socket, host
paths), excessive capabilities, and vulnerable runtimes/kernels — and demonstrate a
path minimally to prove the risk.

> Authorized testing only; demonstrate escape minimally on a test workload; avoid
> node disruption (`_shared/safe-execution-rules.md`).

## Procedure (gated phases)
1. **Enumerate exposure** — pod specs for privileged, hostPID/Network/IPC, hostPath/
   socket mounts, added capabilities, and runtime/kernel versions.
2. **Identify escape primitives (core)** — e.g., mounted docker.sock, privileged +
   host mount, capability abuse, or known runtime CVE.
3. **Demonstrate minimally** — from a test workload, prove reaching the node (a
   benign marker), not full compromise.
4. **Assess blast radius** — what node/cluster access the escape grants.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the escape primitive, and
minimal proof. Hardened (restricted PSS, no dangerous mounts) → **refuted**.

## Impact / output
Escape-path findings → node/cluster compromise risk; drives pod-security + runtime
detection.

## Pitfalls
- Escapes needing already-privileged pods aren't escalation if that's the baseline —
  evaluate.
- Don't disrupt nodes.

## Remediation
- Restricted Pod Security (no privileged/host mounts/caps); don't mount runtime
  sockets; patch runtime/kernel; runtime detection (Falco); node isolation.

## References
- `_shared/` rules (authorization, safe execution, evidence).
