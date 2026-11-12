---
name: retest-verification
description: >
  Use when retesting remediated findings and documenting the verification — confirming
  fixes work, catching incomplete remediation, and producing a defensible retest
  report. Covers remediation retesting and reporting.
type: knowledge
domain: reporting-docs
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Retest & Verification Report

After remediation, retest to confirm each finding is actually fixed — re-running the
original test, catching incomplete/regressed fixes, and documenting the verified
status — so "fixed" is evidence-based and the organization has a defensible record of
closure.

## When to use
After the client/team reports findings remediated.

## Procedure (gated phases)
1. **Re-run original tests** — reproduce each finding's test; confirm the condition is
   resolved (not just version/status changed) — tie to patch-verification.
2. **Check for incomplete fixes** — partial remediation, fixes that address the
   instance but not the class, or regressions.
3. **Document status** — per finding: fixed / partially-fixed / not-fixed, with
   evidence.
4. **Report** — an updated risk posture reflecting verified remediation.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each "fixed" status is backed by a retest with
evidence.

## Quality bar / pitfalls
- Accepting "fixed" without retesting; missing incomplete fixes.
- Not checking for the same class elsewhere (variant analysis).

## Linkage
- Closes the loop from remediation-roadmap; feeds metrics + grc evidence.

## References
- `_shared/` rules (evidence).
