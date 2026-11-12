---
name: remediation-roadmap
description: >
  Use when turning findings into a prioritized remediation plan — grouping issues,
  sequencing fixes by risk and effort, assigning owners, and addressing root causes.
  Covers remediation planning.
type: knowledge
domain: reporting-docs
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Remediation Roadmap

A list of findings isn't a plan. Turn them into a prioritized, sequenced remediation
roadmap — grouping related issues, ordering by risk and effort, assigning owners, and
fixing **root causes** (not just instances) — so the organization actually reduces
risk efficiently.

## When to use
After an assessment, to drive actual remediation.

## Procedure (gated phases)
1. **Group & find root causes** — cluster findings; identify systemic root causes
   (e.g., many authz bugs → centralize authorization) to fix once.
2. **Prioritize** — by risk (impact × likelihood) and effort; quick high-impact wins
   first, strategic fixes planned.
3. **Assign & sequence** — owners, timelines, and dependencies; immediate vs
   short/long-term.
4. **Track** — closure + verification (patch-verification); measure risk reduction.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Good" = a sequenced, owned plan addressing
root causes with tracked progress.

## Quality bar / pitfalls
- Fixing instances not root causes (issues recur).
- Flat priority / no owners → nothing gets done.

## Linkage
- Consumes technical findings; feeds vulnerability-management + metrics.

## References
- `_shared/` rules (evidence).
