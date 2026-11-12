---
name: semgrep-rule-authoring
description: >
  Use when writing custom Semgrep rules to detect code-level security issues —
  pattern/dataflow rules, taint tracking, and FP control for a codebase/framework.
  Covers rule design, testing and tuning for CI integration.
type: knowledge
domain: appsec/sast-dast
maturity: canonical
tools: [semgrep]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Semgrep Rule Authoring

Write custom Semgrep rules that catch a specific vulnerability pattern or insecure
API usage in your codebase with high precision — using syntactic patterns and taint
(source→sink) analysis, with deliberate false-positive handling — so they can gate
CI without noise.

## When to use
To codify a security standard, catch a recurring bug class, or detect a
framework-specific anti-pattern.

## Procedure (gated phases)
1. **Define the pattern** — the exact insecure construct (API misuse, missing
   validation, dangerous sink) and its safe counterpart.
2. **Write the rule** — syntactic pattern or taint mode (sources/sinks/sanitizers);
   scope to language/framework.
3. **Handle FPs** — add `pattern-not`/sanitizer awareness; test against safe code.
4. **Test** — a fixtures set of vulnerable + safe samples; measure precision.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = flags vulnerable fixtures, passes
safe ones, acceptable FP rate. Record test results.

## Quality bar / pitfalls
- Over-broad patterns → CI noise/fatigue; prefer taint for injection classes.
- Missing sanitizer awareness → false positives.

## Deployment
- Integrate into CI as a gate (ci-cd-devsecops); version rules; tune with feedback.

## References
- `_shared/` rules (evidence).
