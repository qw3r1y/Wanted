---
name: program-scope-analysis
description: >
  Use when analyzing a bug-bounty program before hunting — parsing scope/out-of-scope,
  rules, reward structure, and known-issue lists to focus effort legally and
  profitably. Covers program selection and scope discipline.
type: knowledge
domain: bug-bounty
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Bug Bounty Program & Scope Analysis

Before hunting, understand the program: what's **in scope** (and strictly what's
out), the rules of engagement, reward structure, and known/accepted issues — so your
effort is legal, within bounds, and aimed where the program pays. Scope discipline is
both ethical and efficient.

> Test strictly within the program's scope and rules (`_shared/scope-authorization-rule.md`).

## When to use
When selecting a program and before testing any asset.

## Procedure (gated phases)
1. **Parse scope (core gate)** — exact in-scope assets/domains/apps and
   **out-of-scope** (never touch); wildcard interpretation; test-account rules.
2. **Rules of engagement** — allowed techniques, rate limits, forbidden actions (no
   DoS, no social engineering, no data exfiltration), and safe-harbor terms.
3. **Reward & focus** — what pays well, severity bands, and known-issue/duplicate
   lists (avoid wasting effort).
4. **Plan** — prioritize high-value in-scope surfaces.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the scope boundaries used; never test
out-of-scope assets.

## Impact / output
A focused, compliant hunting plan.

## Pitfalls
- Testing out-of-scope assets (legal risk; the critical mistake).
- Chasing low-reward/known issues.

## Linkage
- Gates all offensive/* testing in a bounty context; feeds recon-workflow.

## References
- `_shared/` rules (authorization, evidence).
