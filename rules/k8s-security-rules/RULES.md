---
name: k8s-security-rules
type: rule
description: >
  Rules for generating secure Kubernetes manifests/Helm — secure workload defaults.
references: [skills/cloud-infra/container-k8s/*]
license: MIT
version: 1.0.0
---

# Kubernetes Security Rules (assistant)

When generating K8s manifests/Helm:
- **Non-root + least privilege** — `runAsNonRoot`, drop capabilities, read-only root FS
  where possible; no `privileged`, no host namespaces (hostPID/Network/IPC), no
  hostPath/socket mounts.
- **Pod Security** — target the `restricted` standard; set resource limits.
- **RBAC least-privilege** — no wildcard verbs/resources; namespace-scoped; disable
  default service-account token automount where unused.
- **Network policy** — default-deny + explicit allows (don't rely on flat networking).
- **Images** — pinned by digest, minimal/distroless base, scanned; no secrets in images/
  env (use secrets + a vault).
Validate with k8s-rbac-audit + pod-security-standards.
