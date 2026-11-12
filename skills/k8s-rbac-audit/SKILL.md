---
name: k8s-rbac-audit
description: >
  Use when auditing Kubernetes RBAC — over-permissive roles/bindings, dangerous
  permissions, and privilege-escalation paths (to cluster-admin) — in an authorized
  cluster. Covers RBAC risk analysis and least-privilege.
type: knowledge
domain: cloud-infra/container-k8s
maturity: canonical
tools: [kubectl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Kubernetes RBAC Audit

Audit an authorized cluster's RBAC for the permission combinations that let a
workload/user escalate toward cluster-admin — wildcard verbs/resources, secret
access, `exec`/`pods/exec`, impersonation, or the ability to modify RBAC itself —
and drive least-privilege.

> Authorized, read-only audit (`_shared/scope-authorization-rule.md`).

## Procedure (gated phases)
1. **Enumerate** — Roles/ClusterRoles and their bindings; subjects (users, groups,
   service accounts).
2. **Flag dangerous permissions (core)** — wildcards, secret read, create/patch on
   pods/workloads, `exec`, impersonate, escalate/bind, and RBAC self-modification.
3. **Trace privesc paths** — from workload/service-account to cluster-admin.
4. **Recommend least-privilege** — scope roles to namespaces + minimal verbs/
   resources.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record dangerous permissions + escalation
paths with evidence.

## Impact / output
RBAC risk findings + least-privilege recommendations.

## Pitfalls
- Default/over-broad service-account tokens; `cluster-admin` sprawl.
- Workload SAs with secret/exec access.

## Remediation
- Namespace-scoped least-privilege roles; disable default SA token automount;
  restrict exec/impersonate; review RBAC changes.

## References
- `_shared/` rules (authorization, evidence).
