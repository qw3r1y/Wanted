---
name: database-security-audit
description: >
  Use when auditing database security — access control, encryption (at rest/in
  transit), configuration hardening, auditing, and exposure — to protect the data
  store itself. Covers DB security assessment.
type: knowledge
domain: data-privacy
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Database Security Audit

Databases hold the crown jewels. Audit the data store's own security — who can
access it and at what privilege, encryption at rest/in transit, hardened
configuration, auditing/logging, and network exposure — beyond the application's SQL
injection surface.

> Authorized, read-only audit (`_shared/scope-authorization-rule.md`).

## When to use
Auditing databases holding sensitive data.

## Procedure (gated phases)
1. **Access control** — accounts/roles and least-privilege; no shared/over-privileged
   app accounts; strong auth; no default credentials.
2. **Encryption** — at rest (TDE/disk) and in transit (TLS); key management.
3. **Configuration hardening** — secure defaults, disabled dangerous features,
   patched version.
4. **Exposure & auditing** — network exposure (should not be internet-reachable);
   audit logging of sensitive access.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings with exposure + priority.

## Impact / output
Prioritized DB risk findings + hardening.

## Pitfalls
- Internet-exposed databases; default/weak credentials — high priority.
- Over-privileged app DB accounts (amplify SQLi impact).

## Remediation
- Least-privilege accounts, strong auth, encryption at rest + TLS, hardened config,
  no internet exposure, audit logging, backups + patching.

## References
- `_shared/` rules (authorization, evidence).
