---
name: certificate-validation
description: >
  Use when assessing how an application validates TLS certificates — disabled/weak
  validation, missing hostname checks, or improper trust that enable MITM. Covers
  client-side certificate-validation review.
type: knowledge
domain: crypto
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Certificate Validation Review

A TLS connection is only secure if the client validates the server's certificate
properly. Apps (and mobile/IoT especially) often disable validation, skip hostname
checks, or trust improperly — enabling man-in-the-middle. Assess how the app
validates certificates.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
Reviewing clients/apps/services that make TLS connections (mobile, backend-to-API,
IoT).

## Procedure (gated phases)
1. **Find TLS clients** — where the app connects over TLS.
2. **Check validation (core)** — is certificate validation enabled, with **hostname
   verification** and proper trust-store use? Look for disabled validation,
   trust-all managers, or ignored errors.
3. **MITM test** — with an intercepting proxy + untrusted cert, does the app connect
   anyway (validation off)?
4. **Pinning** — where expected (mobile), is pinning implemented (and is it the only
   control)?

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record disabled/weak validation + MITM proof.
Proper validation → **refuted**.

## Impact escalation
Man-in-the-middle: interception/modification of "encrypted" traffic, credential
theft. CVSS per `_shared/cvss-reference.md`.

## Remediation
- Enable full validation + hostname verification; never trust-all/ignore errors; use
  the system trust store; pin where appropriate; fail closed.

## References
- `_shared/` rules (authorization, evidence).
