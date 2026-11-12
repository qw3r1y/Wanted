---
name: runtime-security-falco
description: >
  Use when implementing Kubernetes/container runtime threat detection (e.g., Falco)
  — detecting anomalous syscalls/behaviour in running containers (shells, mounts,
  escapes, drift) and responding. Covers runtime detection rules and response.
type: knowledge
domain: cloud-infra/container-k8s
maturity: canonical
tools: [falco]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Container Runtime Security (Falco)

Detect malicious/anomalous behaviour in running containers — unexpected shells,
sensitive file/mount access, privilege changes, container-escape attempts, and
drift from the image — using runtime detection (Falco/eBPF), and respond. Complements
build-time scanning with runtime visibility.

## When to use
To detect attacks in running workloads that static scanning can't.

## Procedure (gated phases)
1. **Deploy runtime sensor** — Falco/eBPF across nodes; verify syscall/event
   visibility.
2. **Rules** — detect shells-in-container, sensitive mounts (docker.sock,
   hostPath), capability/privilege changes, outbound anomalies, and image drift;
   tune to the environment.
3. **Reduce noise** — baseline normal behaviour; exclude known-benign; prioritize
   high-fidelity escape/privilege rules.
4. **Respond** — alert → investigate → contain (feeds blue-team, cloud-incident-
   response).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = high-fidelity runtime detections
with acceptable noise; test with benign simulations.

## Quality bar / pitfalls
- Noisy default rules → fatigue; tune to the environment.
- No response path — connect to SOC/IR.

## Linkage
- Pairs with pod-security, container-escape-analysis, detection-engineering.

## References
- `_shared/` rules (evidence).
