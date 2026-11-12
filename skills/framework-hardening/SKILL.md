---
name: framework-hardening
description: >
  Use when hardening a web framework's security configuration — the secure defaults,
  built-in protections, and common misconfigurations per framework (Django, Rails,
  Spring, Laravel, Express, Next.js). Covers framework security configuration.
type: knowledge
domain: appsec/secure-coding
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Framework Security Hardening

Modern frameworks ship strong protections — if configured and not bypassed. Harden
the framework's security settings, keep its built-in defenses on (CSRF, auto-
escaping, secure headers/cookies, ORM parameterization), and avoid the escape
hatches that reintroduce vulnerabilities.

## When to use
Setting up or reviewing a web app on a specific framework.

## Procedure (gated phases)
1. **Enable built-in defenses** — CSRF protection, template auto-escaping,
   parameterized ORM, secure session/cookie flags, security headers middleware.
2. **Check config** — DEBUG off in prod, no secrets in config, secure defaults for
   auth/session, CORS restricted.
3. **Avoid escape hatches** — flag raw-HTML/`dangerouslySetInnerHTML`/raw SQL/
   disabled CSRF that bypass protections.
4. **Dependencies & updates** — keep the framework patched (framework CVEs are
   high-impact).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Correct" = built-in protections on, prod
config secure, no unjustified escape hatches.

## Quality bar / pitfalls
- DEBUG/verbose errors in prod; disabled CSRF; raw rendering/queries.
- Assuming the framework protects you while using its unsafe escape hatches.

## Linkage
- Complements input-validation, authz-patterns; enforce via SAST + review.

## References
- `_shared/` rules (evidence).
