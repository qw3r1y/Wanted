---
name: api-key-leakage
description: >
  Use when testing an authorized target for exposed API keys/secrets/tokens — in
  client bundles, repos, responses, logs, mobile apps, or error messages — and
  assessing their privilege and blast radius. Covers discovery, validation (scope
  of a found key) and remediation.
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl, trufflehog, gitleaks]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# API Key / Secret Leakage (authorized testing)

Find credentials exposed where a client can read them, and determine what a leaked
key can actually do (its scope/blast radius) — a public but powerless key is low;
a live key with broad scope is critical. Validate **minimally** without abusing the
key.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Confirm a key's
> validity/scope with a single benign call; never use it to access or modify real
> data (`safe-execution-rules.md`).

## When to use
Client JS bundles, mobile apps (decompiled), public/accessible repos, API
responses, error messages, HTML comments, cache, and third-party config.

## Prerequisites
- Authorization + scope; secret-scanning tooling. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Discover** — scan client bundles/apps/responses/repos for key patterns
   (cloud keys, tokens, third-party API keys); dedupe and record locations.
2. **Classify (first gate)** — is the "secret" meant to be public (publishable
   key) or truly secret? Determine the provider and key type.
3. **Scope validation (bounded)** — with a single benign call, confirm the key is
   **live** and determine its scope/permissions — enough to establish blast
   radius. Do not enumerate or exfiltrate data with it.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the key location, type,
live/validity, and scope. A publishable/restricted key → **low**; a live secret
key with broad scope → **high/critical**.

## Impact escalation
Unauthorized access to the backing service, data exposure, financial abuse (paid
APIs), and lateral movement via cloud keys. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Intended-public keys (e.g., publishable/anon keys) → not a secret leak.
- Expired/revoked keys → informational.
- Never use a found key beyond a single validity/scope check.

## Remediation
- Keep secrets **server-side**; never ship secret keys to clients; use scoped,
  rotatable keys and short-lived tokens; secret scanning in CI + pre-commit.
- Revoke exposed keys immediately; restrict key scope/origin; monitor usage.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
