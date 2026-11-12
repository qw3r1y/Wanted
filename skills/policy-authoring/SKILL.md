---
name: policy-authoring
description: >
  Use when writing security policies and standards — clear, enforceable, risk-aligned
  documents that people actually follow, with the right policy/standard/procedure
  hierarchy. Covers security policy development.
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Security Policy Authoring

Policies set the rules security is built on — but only if they're clear, enforceable,
and followed. Write them at the right level (policy = what/why, standard = specific
requirements, procedure = how), aligned to risk, and practical enough that people
comply rather than route around.

## When to use
When establishing/updating the security policy framework.

## Procedure (gated phases)
1. **Structure** — policy (principles/intent) → standards (specific, measurable
   requirements) → procedures (step-by-step); don't cram all into one.
2. **Write clearly & enforceably** — unambiguous, testable requirements; avoid vague
   "should be secure"; align to real risk + frameworks.
3. **Make it practical** — feasible to follow; exceptions process; owner + review
   cycle.
4. **Socialize & enforce** — communicate, train, and tie to controls/consequences;
   measure compliance.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Good" = clear, enforceable, risk-aligned,
owned, and actually followed.

## Quality bar / pitfalls
- Vague/aspirational policies no one can comply with or enforce.
- Copy-paste templates not aligned to the org's risk/reality.

## Linkage
- Consumes risk-assessment; supports iso27001/soc2; enforced via technical controls +
  rules/.

## References
- `_shared/` rules (evidence).
