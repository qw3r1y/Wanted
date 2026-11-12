---
name: ipc-local-attacks
description: >
  Use when assessing local inter-process communication and privilege boundaries on
  an endpoint — named pipes, sockets, RPC, services, and local privilege-escalation
  via insecure IPC. Covers local IPC/privilege-boundary review.
type: knowledge
domain: endpoint-app-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Local IPC & Privilege-Boundary Attacks

Applications and services expose local IPC (named pipes, local sockets, RPC,
COM/D-Bus) that cross privilege boundaries — and insecure IPC lets a low-privilege
process abuse a higher-privilege one (a common local privilege-escalation path on an
authorized endpoint).

> Authorized testing on an in-scope host (`_shared/scope-authorization-rule.md`).

## When to use
Auditing a desktop app/service's local IPC surface, or local-privesc assessment.

## Procedure (gated phases)
1. **Enumerate IPC endpoints** — named pipes, local sockets, RPC/COM/D-Bus interfaces,
   and privileged services reachable locally.
2. **Check access control (core)** — can a low-privilege process connect to a
   higher-privilege endpoint? Weak ACLs/authentication on the IPC boundary.
3. **Test the interface** — does the privileged endpoint validate requests, or can a
   low-priv caller trigger privileged actions / inject input to a sink?
4. **Impact** — local privilege escalation or privileged-action abuse.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the insecure IPC endpoint + the
privilege-crossing proof. Properly ACL'd/validated → **refuted**.

## Impact escalation
Local privilege escalation and abuse of privileged services. CVSS per
`_shared/cvss-reference.md`.

## Remediation
- Strong ACLs + authentication on IPC endpoints; validate all requests server-side;
  least-privilege services; avoid exposing privileged actions to low-priv callers.

## References
- `_shared/` rules (authorization, evidence).
