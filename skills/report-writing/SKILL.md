---
name: report-writing
description: >
  Use when writing a bug-bounty report — a clear, reproducible, impact-focused
  submission that triagers can validate quickly and reward fairly. Covers bounty
  report quality (complements reporting-docs/technical-finding-report).
type: knowledge
domain: bug-bounty
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Bug Bounty Report Writing

A great finding can be rejected for a bad report. Write submissions that let a triager
quickly reproduce and understand the impact — concise summary, exact reproduction
steps, evidence, and clear real-world impact — so your valid bug is validated and
fairly rewarded.

## When to use
When submitting any finding to a program.

## Procedure (gated phases)
1. **Summary + severity** — one-line what/where + impact, and CVSS (cvss-scoring).
2. **Reproduction steps (core)** — exact, numbered, copy-pasteable steps from zero to
   trigger; include the request/payload (minimal) and any prerequisites.
3. **Evidence** — screenshots/HAR/OOB logs proving execution/impact (the evidence
   rule).
4. **Impact + remediation** — the concrete real-world impact and a helpful fix
   suggestion; keep it concise and professional.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Good" = a triager reproduces it from the report
alone and sees the impact.

## Impact / output
Faster validation, fair rewards, good program relationships.

## Pitfalls
- Vague/missing reproduction; no evidence; overstated impact.
- Walls of text — be concise and clear.

## Linkage
- Builds on finding-triage + cvss-scoring; same rigor as reporting-docs/technical-
  finding-report.

## References
- `_shared/` rules (evidence).
