---
name: finding-triage
description: >
  Use when triaging a candidate bug before reporting — verifying it's real,
  exploitable, in-scope, and not a duplicate/known-issue, and assessing severity — to
  submit only valid, impactful reports. Covers pre-submission discipline.
type: knowledge
domain: bug-bounty
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Finding Triage (pre-submission)

Before submitting, gate the finding: is it a **real, exploitable** security issue
(not reflection/theory), in scope, demonstrably impactful, and not a known-issue/
duplicate? This discipline — the same presence≠exploitation rigor as the offensive
skills — protects your signal and the program's time.

> In-scope only (`_shared/scope-authorization-rule.md`).

## When to use
On every candidate finding, before writing a report.

## Procedure (gated phases)
1. **Reality gate** — reproduce it; confirm actual exploitation (execution/OOB/data
   access), not just a signal (evidence-confidence rule).
2. **Impact gate** — a concrete security impact (affected principal/resource/outcome);
   self-XSS, missing headers alone, best-practice nits → usually not valid/rewarded.
3. **Scope & dedup** — in-scope asset, not a listed known-issue; search for likely
   duplicates.
4. **Severity** — assess CVSS/impact (cvss-scoring) to set expectations.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Only `confirmed`, impactful, in-scope,
non-duplicate findings proceed to reporting.

## Impact / output
High-quality submissions; preserved reputation/signal.

## Pitfalls
- Submitting reflections/theory/low-impact (noise → lower program trust).
- Out-of-scope or duplicate submissions.

## Linkage
- Applies the offensive skills' verification discipline; feeds report-writing + CVSS.

## References
- `_shared/` rules (authorization, evidence, gated workflow).
