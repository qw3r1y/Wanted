---
name: web-cache-deception
description: >
  Use when testing an authorized target with caching for web cache deception —
  tricking the cache into storing a personalized/authenticated response so it is
  served to others. Covers path-confusion analysis, safe proof and remediation.
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

# Web Cache Deception (authorized testing)

Find cases where a cache's **path/extension rules** can be tricked into caching a
response that is actually personalized/authenticated (so another user — or you,
unauthenticated — can retrieve a victim's content). The proof is an authenticated
response stored in a cacheable entry.

> Authorized testing only. Use a **test account** as the "victim"; never capture
> real users' personalized responses (`safe-execution-rules.md`).

## When to use
Apps behind a CDN/proxy that cache by extension/path (e.g., cache all `*.css`,
`*.js`, static-looking paths), especially where a personalized page can be
requested under a static-looking suffix.

## Prerequisites
- Authorization + scope; test account; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Learn caching rules** — what paths/extensions are cached; how the origin and
   cache handle an unexpected suffix on a dynamic path.
2. **Path-confusion probe (first gate)** — as the test-victim, request a
   personalized page with an appended cacheable-looking segment/extension; observe
   whether the origin returns personalized content AND the cache stores it
   (`X-Cache: MISS` then `HIT`).
3. **Retrieve as attacker** — fetch the same crafted URL without the victim's
   session; if the personalized content is served, the deception is confirmed.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the path-confusion
pattern, and the cross-session retrieval proof (victim content served to
non-victim). Cache stores only truly static content → **refuted**.

## Impact escalation
Disclosure of other users' personalized/authenticated data (PII, tokens on page),
session info leakage. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Origin sets `Cache-Control: private/no-store` on personalized pages → **refuted**.
- Cache keys include auth/session → not deception.
- Only use test accounts; never harvest real victims' responses.

## Remediation
- Cache by **content type the origin declares**, not by URL suffix; honor
  `Cache-Control` from the origin; do not cache responses to authenticated
  requests.
- Normalize/validate paths at the origin; reject unexpected suffixes on dynamic
  routes; align cache and origin on what is cacheable.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
