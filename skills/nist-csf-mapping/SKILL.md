---
name: nist-csf-mapping
description: >
  Use when assessing a security program against the NIST Cybersecurity Framework —
  mapping capabilities to the functions (Govern/Identify/Protect/Detect/Respond/
  Recover), scoring maturity, and prioritizing gaps. Covers CSF-based program
  assessment.
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# NIST CSF Program Assessment

The NIST CSF gives a common language to assess and communicate a security program's
maturity across its functions (Govern, Identify, Protect, Detect, Respond, Recover).
Map your capabilities to the categories, score maturity, and prioritize the gaps —
a flexible, business-aligned way to steer the program.

## When to use
To assess overall program maturity and build a prioritized improvement plan.

## Procedure (gated phases)
1. **Assess current state** — map existing capabilities to CSF functions/categories;
   score maturity per category honestly.
2. **Define target state** — risk-appropriate target maturity per category (not all
   need to be max).
3. **Gap & prioritize** — the biggest current-vs-target gaps weighted by risk.
4. **Roadmap** — initiatives to close gaps; track maturity over time.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a maturity scorecard + prioritized
roadmap; scores backed by evidence.

## Quality bar / pitfalls
- Inflated self-scores — assess honestly with evidence.
- Targeting max maturity everywhere vs risk-appropriate targets.

## Linkage
- Rolls up detection-coverage, IR, VM, identity, etc.; feeds leadership metrics +
  roadmap.

## References
- `_shared/` rules (evidence).
