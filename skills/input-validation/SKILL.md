---
name: input-validation
description: >
  Use when designing/reviewing input validation and output encoding — allow-list
  validation, canonicalization, and context-aware encoding to prevent injection
  classes at the source. Covers the patterns that neutralize whole bug families.
type: knowledge
domain: appsec/secure-coding
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Input Validation & Output Encoding

Apply the patterns that neutralize entire injection families at the source:
allow-list validation at trust boundaries, canonicalization before validation, and
**context-aware output encoding** at every sink. The right pattern prevents XSS/
SQLi/command-injection by construction.

## When to use
Designing/reviewing any code that accepts untrusted input or renders/executes data.

## Procedure (gated phases)
1. **Validate at the boundary** — allow-list (type/format/range) over deny-list;
   reject rather than sanitize where possible; canonicalize before checks.
2. **Encode at the sink (context-aware)** — HTML/attribute/JS/URL/SQL-parameter/
   shell-arg encoding matched to the sink (not one-size-fits-all).
3. **Prefer safe APIs** — parameterized queries, safe templating, process-arg
   arrays — so encoding isn't hand-rolled.
4. **Verify** — review that every untrusted→sink path is covered.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Correct" = every sink uses context-appropriate
encoding/safe API; demonstrated on representative paths.

## Quality bar / pitfalls
- Single global "sanitizer" for all contexts → gaps (e.g., HTML-encoding in a JS
  context).
- Deny-list validation (bypassable) — prefer allow-list.

## Linkage
- Underpins web/* injection remediation; enforce via semgrep rules + review.

## References
- `_shared/` rules (evidence).
