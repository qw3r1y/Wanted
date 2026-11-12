---
name: thick-client-audit
description: >
  Use when auditing a desktop/thick-client application — local data storage,
  client-side trust, API communication, binary protections, and privilege handling —
  for security issues. Covers thick-client assessment.
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

# Thick-Client Application Audit

Desktop apps often trust the client, store secrets locally, and talk to backends in
ways users can intercept/modify. Audit a thick client for insecure local storage,
client-side trust (logic/authz that the server should enforce), weak API
communication, and binary/privilege issues.

> Authorized review (`_shared/scope-authorization-rule.md`).

## When to use
Auditing a native/desktop client application.

## Procedure (gated phases)
1. **Local storage** — sensitive data/secrets/config stored on disk; encryption; and
   recoverable credentials.
2. **Client-side trust (core)** — logic/authorization/validation done only on the
   client (bypassable); the server must enforce security, not the client.
3. **API communication** — intercept the client↔server traffic (proxy); test the API
   with the api/* skills (the real attack surface); TLS/cert validation.
4. **Binary & privilege** — protections, DLL/injection risks, and whether the app
   runs/with-privilege unsafely.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record findings (storage, client-trust, API,
binary) + impact.

## Impact escalation
Local data/secret theft, server-side abuse via client-trust bypass, and privilege
issues. CVSS per `_shared/cvss-reference.md`.

## Remediation
- Enforce security server-side (never trust the client); encrypt local sensitive data;
  no hardcoded secrets; validate TLS; harden the binary + least privilege.

## References
- `_shared/` rules (authorization, evidence).
