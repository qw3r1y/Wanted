---
name: tls-attacks
description: >
  Use when assessing an authorized target's TLS/SSL configuration — weak protocols/
  ciphers, certificate issues, and known TLS weaknesses — to identify transport
  security gaps. Configuration-assessment focus (not breaking strong TLS).
type: knowledge
domain: offensive/network
maturity: canonical
tools: [curl, sslscan]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# TLS / SSL Configuration Assessment (authorized)

Evaluate a target's transport security for weak protocols, ciphers, certificate
problems, and known TLS weaknesses — identifying gaps that weaken confidentiality/
integrity. This assesses configuration; it does not attempt to break properly
configured TLS.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope; the service list. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Protocol/cipher scan** — enumerate supported protocols (SSLv3/TLS1.0/1.1
   deprecated) and cipher suites (weak/export/NULL).
2. **Certificate review** — validity, trust chain, hostname match, key strength,
   signature algorithm, expiry, and wildcard/SAN scope.
3. **Known weaknesses** — check for configuration-based issues and missing
   hardening (HSTS, OCSP stapling); flag known-weak configs.
4. **Summarize** — a transport-security posture report.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict` per issue (weak protocol/
cipher/cert). Modern TLS1.2+/strong ciphers/valid cert → **refuted** for those.

## Impact escalation
Interception/downgrade risk, trust issues, and compliance gaps. CVSS per
`_shared/cvss-reference.md` (often medium unless actively exploitable).

## False positives & pitfalls
- Legacy support may be an intentional (documented) trade-off — note context.
- A weak cipher offered but not negotiated by modern clients is lower risk.

## Remediation
- TLS1.2+ only (prefer 1.3); strong cipher suites; valid, strong certificates;
  HSTS; disable legacy protocols/ciphers; OCSP stapling; monitor expiry.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
