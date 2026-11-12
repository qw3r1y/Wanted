---
name: mobile-storage-api
description: >
  Use when testing an authorized mobile app's data storage and backend API —
  insecure local storage, data in transit, and the mobile-backed API surface
  (often weaker authz than the web). Ties mobile findings to api/* testing. Covers
  storage/transit review and API surface pivot.
type: knowledge
domain: offensive/mobile
maturity: canonical
tools: [curl, mobsf]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Mobile Storage & Backend API (authorized)

Review how a mobile app stores data and talks to its backend, and test the
mobile-facing API — which frequently has weaker object/function authorization than
the web because developers assume the app is the only client. The proof is
insecure data at rest/in transit or an API authz flaw.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope; app + ability to proxy its traffic (pinning bypass via
  mobile-runtime-instrumentation if needed). `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Storage at rest** — sensitive data in local DBs/prefs/files/keychain; encryption
   posture.
2. **Data in transit** — TLS use, pinning, and whether sensitive data is sent/
   logged insecurely.
3. **API surface (core)** — capture the app's API calls; test them with api/*
   skills (BOLA/BFLA/mass-assignment/jwt), as mobile APIs often under-enforce
   authz.
4. **Confirm** — insecure storage/transit or an API authz flaw, with evidence.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the issue (storage/
transit/API), and proof. Encrypted storage + enforced API authz → **refuted**.

## Impact escalation
Local data theft, interception, and backend compromise via weak mobile-API authz.
CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- App-private encrypted storage → lower impact.
- Mobile API = same backend as web; test authz regardless of client.

## Remediation
- Encrypt sensitive data at rest; enforce TLS + pinning; **enforce the same
  server-side authz** for mobile APIs as web; never assume the app is the only
  client.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
