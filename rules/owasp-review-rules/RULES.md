---
name: owasp-review-rules
type: rule
description: >
  Review rules mapping code review to the OWASP Top 10 — prompts the assistant to
  check each category when reviewing web/API code.
references: [_shared/owasp-mappings.md, skills/appsec/secure-coding/secure-code-review]
license: MIT
version: 1.0.0
---

# OWASP Review Rules (assistant)

When reviewing web/API code, check each OWASP category:
- **Broken Access Control** — authz on every object + function (IDOR/BOLA/BFLA)? default-deny?
- **Crypto Failures** — strong algorithms, authenticated encryption, no weak hashing?
- **Injection** — parameterized queries, context-aware encoding, no command/template
  injection?
- **Insecure Design** — threat-modeled? abuse cases handled?
- **Misconfiguration** — secure defaults, no debug in prod, least-privilege?
- **Vulnerable Components** — patched, reachable-vuln checked?
- **Auth Failures** — MFA, rate-limit, secure session, strong reset?
- **Integrity Failures** — no untrusted deserialization; signed artifacts?
- **Logging Failures** — security events logged, no secrets in logs?
- **SSRF** — outbound URLs allow-listed; internal/metadata blocked?
Flag missing authorization first — it's the #1 real bug.
