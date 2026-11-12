---
name: secure-code-review
description: >
  Use when manually reviewing code for security issues — a structured approach
  covering auth/z, input handling, crypto, secrets, injection sinks, and business
  logic, focused on what automated tools miss. Covers review methodology.
type: knowledge
domain: appsec/secure-coding
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Secure Code Review

Review code for the security issues tools miss — logic flaws, authorization gaps,
subtle trust-boundary mistakes — with a structured focus on where untrusted data
enters and where sensitive operations happen, prioritized by risk.

## When to use
On security-sensitive changes/components, and as targeted audits of high-risk code.

## Procedure (gated phases)
1. **Map trust boundaries** — where untrusted input enters, and the sensitive sinks
   (DB, command, file, auth, crypto).
2. **Review by risk area** — input validation/encoding, authn/authz on every
   sensitive path, injection sinks, crypto usage, secrets, error/logging, and
   business logic.
3. **Trace data flows** — follow untrusted input to sinks; check sanitization and
   authorization at each step.
4. **Document findings** — concrete issues with location, impact, and fix.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each finding cites the code + a concrete
exploit/impact scenario.

## Quality bar / pitfalls
- Style nits over security substance — focus on trust boundaries + sinks.
- Missing authorization checks (the most common real bug) — verify on every path.

## Linkage
- Complement with SAST (semgrep/codeql); feed systemic issues into secure-coding
  patterns + training.

## References
- `_shared/` rules (evidence).
