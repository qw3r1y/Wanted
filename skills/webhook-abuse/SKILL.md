---
name: webhook-abuse
description: >
  Use when testing an authorized target's webhook features — outbound webhooks
  (SSRF via user-set URL), inbound webhooks (missing/forgeable signature
  verification), and replay. Covers configuration analysis, proof and remediation.
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl, oob-listener]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Webhook Abuse (authorized testing)

Webhooks have two attack directions: **outbound** (a user-configurable callback
URL the server fetches → SSRF) and **inbound** (the server accepts events from a
third party → missing/forgeable signature lets an attacker forge events). Test
both; the proof is an SSRF callback or an accepted forged/replayed event.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
Integrations with "notify this URL" settings, and endpoints that receive events
from providers (payment/CI/VCS webhooks).

## Prerequisites
- Authorization + scope; OOB listener. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Outbound (SSRF)** — set the webhook URL to your unique OOB host; confirm the
   server calls it; test internal/metadata targets per offensive/web/ssrf.
2. **Inbound (signature, core gate)** — determine whether inbound events are
   authenticated (HMAC signature/secret). Test: no signature required, signature
   not actually verified, wrong/empty signature accepted, or secret predictable.
3. **Replay** — resend a captured valid event; confirm whether it is reprocessed
   (no nonce/timestamp binding).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, direction (outbound SSRF
/ inbound forgery / replay), and the proof (OOB callback / accepted forged event).
Verified signatures + replay protection → **refuted** inbound.

## Impact escalation
SSRF → internal/metadata access (outbound); forged events → financial/state
manipulation (e.g., fake "payment succeeded"); replay. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Signature verified correctly and secret strong → inbound **refuted**.
- Outbound to your host proves SSRF exists, not necessarily internal reach.

## Remediation
- Outbound: allow-list destinations, block internal/metadata, validate final URL
  after redirects (see ssrf remediation).
- Inbound: verify HMAC signatures with a strong secret on every event; bind
  timestamp/nonce to prevent replay; idempotent processing.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
