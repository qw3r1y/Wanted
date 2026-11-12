---
name: patch-verification
description: >
  Use when verifying that remediations actually fixed the vulnerability — confirming
  patches applied, the vulnerable condition is gone, and no regression — closing the
  loop on remediation. Covers remediation validation.
type: knowledge
domain: vulnerability-management
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Patch / Remediation Verification

"Marked as fixed" isn't fixed. Verify that remediations truly closed the
vulnerability — the patch applied everywhere, the vulnerable condition is actually
gone (not just version-bumped with a backport confusion), and nothing regressed —
before closing the finding.

## When to use
After any remediation, before closing a vulnerability.

## Procedure (gated phases)
1. **Confirm application** — the patch/config change is deployed to **all** affected
   assets (partial rollout is a common gap).
2. **Verify the condition is gone (core)** — re-test the actual vulnerable condition
   (re-run the check/PoC non-destructively), not just the version string (backports
   confound version checks).
3. **Regression check** — the fix didn't break functionality or introduce new issues.
4. **Close with evidence** — record verification; reopen if any asset still affected.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Closed" requires evidence the condition is
resolved on all assets, not a status flag.

## Quality bar / pitfalls
- Closing on version/ticket status without re-testing the condition.
- Partial deployment leaving some assets vulnerable.

## Linkage
- Closes the loop from prioritization/KEV; feeds metrics (reporting).

## References
- `_shared/` rules (evidence).
