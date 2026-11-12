---
name: web-cache-poisoning
description: >
  Use when testing an authorized target with caching (CDN/reverse proxy) for web
  cache poisoning — unkeyed input that influences a cached response served to
  other users. Covers cache-key analysis, unkeyed-input discovery, safe proof and
  remediation. Shares caution with request-smuggling: can affect other users.
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

# Web Cache Poisoning (authorized testing)

Find input that is **unkeyed** (not part of the cache key) but still influences
the response, so a poisoned response gets cached and served to other users. Test
carefully on non-shared cache entries; avoid poisoning production pages real users
hit.

> Authorized testing only, with caution for shared impact. Prefer a unique,
> self-scoped cache key (your own path/param) for the PoC; stop if real users
> could be served poisoned content (`safe-execution-rules.md`).

## When to use
Any CDN/reverse-proxy-cached app. Candidates: responses that reflect headers
(`X-Forwarded-Host`, `X-Forwarded-Scheme`, `X-Host`), unkeyed query params, or
other inputs influencing links/scripts/redirects in a cacheable response.

## Prerequisites
- Authorization + scope; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Understand the cache** — identify cache headers (`Cache-Control`, `Age`,
   `X-Cache`), what is cached, and the apparent cache key.
2. **Find unkeyed inputs (first gate)** — vary candidate headers/params on a
   **unique self-scoped URL**; detect which influence the response but are not in
   the key (response changes yet same cache key).
3. **Reflect to a sink** — determine whether the unkeyed input reaches an
   exploitable sink (script/link/redirect/header).
4. **Controlled proof** — demonstrate caching of your influence on a URL only you
   request (unique cache-buster), proving the mechanism without poisoning shared
   pages.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the unkeyed input, the
sink, and `X-Cache: HIT` proof on your self-scoped entry. Keyed input (varies the
key) → not poisoning.

## Impact escalation
Stored-XSS-at-scale via cache, cache-served redirects/defacement, DoS (cache
flooding), and credential/script injection to many users. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Input that changes the cache key → served only to you → not poisoning.
- `Cache-Control: no-store`/private responses → not cacheable.
- Never poison real production cache entries that serve other users.

## Remediation
- Include all response-influencing inputs in the **cache key**, or strip/normalize
  them before caching; do not cache responses that vary on untrusted headers.
- Disable caching for personalized/sensitive responses; constrain which headers
  are honored; keep CDN config explicit.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
