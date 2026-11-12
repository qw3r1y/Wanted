---
name: cors-misconfiguration
description: >
  Use when testing an authorized web target for CORS misconfiguration — overly
  permissive cross-origin resource sharing that lets an attacker origin read
  authenticated responses. Covers reflection/null-origin/subdomain analysis,
  credentialed-read proof and remediation.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# CORS Misconfiguration (authorized testing)

Find endpoints whose CORS policy reflects or over-trusts the request origin
**with credentials**, letting a malicious site read authenticated responses. The
proof is a cross-origin, credentialed read of sensitive data from an attacker
origin.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Use a test
> account for the credentialed-read PoC.

## When to use
APIs returning user/account data, token/config endpoints, and any authenticated
JSON endpoint that sets `Access-Control-Allow-Origin` dynamically.

## Prerequisites
- Authorization + scope; test account; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Inspect ACAO behaviour** — send varying `Origin` headers; observe
   `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials`.
2. **Misconfig classification (first gate)**:
   | Observation | Risk |
   |---|---|
   | ACAO reflects arbitrary Origin + ACAC: true | Critical: credentialed cross-origin read |
   | ACAO: null + ACAC: true | Exploitable via sandboxed null-origin |
   | Trust of `*.target` incl. attacker-controlled subdomain | Exploitable |
   | ACAO: * (no credentials) | Low: only non-credentialed data |
3. **Credentialed-read PoC** — from an attacker origin, with the test victim's
   session, confirm the sensitive response is readable cross-origin.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the reflected/trusted
origin, ACAC value, and the cross-origin read proof. `ACAO: *` without
credentials and no sensitive data → **low/refuted**.

## Impact escalation
Theft of authenticated data/tokens, account info exposure, and CSRF-like reads.
CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- `ACAO: *` **cannot** be combined with credentials by browsers → not a
  credentialed-read bug.
- Reflected origin without `Allow-Credentials` and only public data → low.
- Preflight allowed ≠ actual data readable; prove the read.

## Remediation
- **Allow-list** exact trusted origins; never reflect arbitrary `Origin`; do not
  combine `*` with credentials; reject `null` origin for credentialed endpoints.
- Scope CORS narrowly per-endpoint; avoid broad `*.domain` trust that includes
  user-controlled subdomains.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
