---
name: host-header-injection
description: >
  Use when testing an authorized web target for Host / forwarded-header injection
  — the app trusts Host/X-Forwarded-Host to build links, reset URLs, or cache
  keys, enabling password-reset poisoning, cache poisoning, SSRF-ish routing or
  auth bypass. Covers detection, impact and remediation.
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

# Host Header Injection (authorized testing)

Find places where the server trusts the `Host` (or `X-Forwarded-Host`/`X-Host`)
header to construct absolute URLs, links, or cache keys, and prove it influences
a security-relevant output — most impactfully **password-reset link poisoning**
and web cache poisoning.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Use a test
> account for reset-poisoning proofs.

## When to use
Password-reset/email flows, absolute link generation, redirects, cache behaviour,
and routing/virtual-host handling.

## Prerequisites
- Authorization + scope; test account + a mailbox you control; OOB host.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Probe header trust (first gate)** — vary `Host`/`X-Forwarded-Host` and
   observe whether generated links/redirects/responses reflect your value.
2. **Classify the sink** — password-reset link, absolute URL in email/response,
   cache key (link to web-cache-poisoning), or routing/auth.
3. **Reset-poisoning proof** — on a **test account**, trigger a password reset
   with an attacker Host; confirm the reset link in the received email points to
   your host (token would be sent to attacker). Do not use on real users.
4. **Other sinks** — demonstrate cache/redirect/routing influence minimally.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the trusted header, the
sink, and the poisoned-output proof (e.g., reset email link to attacker host on a
test account). Reflected Host not used in any sink → **informational**.

## Impact escalation
Account takeover via reset-link/token theft, cache poisoning, open-redirect-like
routing, and authentication/routing bypass. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- App uses a fixed canonical hostname for links → **refuted**.
- Host reflected in a non-security output → informational.
- Reset-poisoning tests only on accounts/mailboxes you control.

## Remediation
- Use a **configured canonical host** for all generated links/URLs; never build
  security-relevant URLs from the incoming Host header.
- Validate Host against an allow-list at the edge; do not trust
  `X-Forwarded-Host` unless from a trusted proxy; include Host in cache keys only
  when safe.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
