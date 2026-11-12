---
name: tls-config-audit
description: >
  Use when auditing TLS configuration in depth — protocol/cipher selection, key
  exchange, certificate/chain, and hardening (HSTS, OCSP) — for servers and internal
  services. Deeper config focus complementing network/tls-attacks.
type: knowledge
domain: crypto
maturity: canonical
tools: [testssl, sslscan]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# TLS Configuration Audit

Audit TLS configuration for confidentiality/integrity gaps — deprecated protocols,
weak cipher suites/key exchange, certificate/chain issues, and missing hardening —
across external and **internal** services (internal TLS is often neglected).

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
Auditing any TLS endpoint, especially internal/service-to-service.

## Procedure (gated phases)
1. **Protocol & cipher** — supported protocols (deprecate <TLS1.2) and cipher
   suites/key exchange (forward secrecy, no weak/export/NULL).
2. **Certificate & chain** — validity, trust chain, key strength, signature algo,
   hostname, and expiry monitoring.
3. **Hardening** — HSTS, OCSP stapling, session handling; mutual TLS where expected.
4. **Internal services** — apply the same scrutiny internally (often weaker).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings per issue; TLS1.2+/strong/valid →
**refuted** for those.

## Quality bar / pitfalls
- Auditing only edge, missing internal/service TLS.
- Legacy support that is intentional — note context.

## Remediation
- TLS1.2+ (prefer 1.3), strong forward-secret ciphers, valid strong certs, HSTS,
  OCSP stapling; mTLS for services; monitor expiry.

## References
- `_shared/` rules (authorization, evidence).
