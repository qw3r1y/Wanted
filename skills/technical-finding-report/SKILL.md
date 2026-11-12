---
name: technical-finding-report
description: >
  Use when documenting a technical security finding — clear description, evidence,
  reproduction steps, impact, severity, and remediation — so engineers can
  understand, reproduce, and fix it. Covers finding write-up quality.
type: knowledge
domain: reporting-docs
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Technical Finding Report

A finding is only as useful as its write-up. Document each so an engineer can
understand it, reproduce it, grasp the impact, and fix it — with evidence, clear
reproduction steps, severity, and concrete remediation — turning a discovery into a
closed issue.

## When to use
For each finding in a pentest/audit/review report.

## Procedure (gated phases)
1. **Describe clearly** — what the issue is, where (asset/endpoint/code), and the
   vulnerability class.
2. **Evidence + reproduction** — concrete evidence (request/response, screenshot, PoC)
   and step-by-step reproduction (the evidence rule).
3. **Impact + severity** — the real consequence and a justified severity/CVSS (tie to
   business impact).
4. **Remediation** — specific, actionable fix guidance (not "fix the XSS" but how).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Good" = an engineer can reproduce and fix it
from the write-up alone; severity is justified.

## Quality bar / pitfalls
- Vague findings without reproduction/evidence (can't be acted on).
- Severity not justified; no concrete remediation.

## Linkage
- Rolls up into executive-summary + remediation-roadmap; uses evidence from the
  offensive/* skills.

## References
- `_shared/` rules (evidence).
