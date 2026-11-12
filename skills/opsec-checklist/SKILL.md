---
name: opsec-checklist
description: >
  Use when planning an authorized red-team engagement's operational security and
  deconfliction — so testing stays controlled, attributable to the engagement, and
  distinguishable from real attacks. Coordination/safety framing.
type: knowledge
domain: red-team-infra
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Red-Team OPSEC & Deconfliction (authorized)

For an authorized engagement, operational discipline keeps testing controlled and
safe: activity must be attributable to the engagement (so it isn't confused with a
real attack or lost), deconflicted with the blue team/leadership as agreed, and
bounded to scope — protecting both the target and the engagement's validity.

> Authorized, coordinated engagement only (`_shared/scope-authorization-rule.md`).

## When to use
Planning/running an authorized red-team or adversary-emulation engagement.

## Procedure (gated phases)
1. **Rules of engagement** — scope, allowed/forbidden actions, timing, and emergency
   stop/contact; documented and agreed.
2. **Deconfliction** — a channel + markers so engagement activity can be identified
   and separated from real incidents (per the engagement's white/black-team model).
3. **Attribution & logging** — keep records of actions for the report and to answer
   "was that us?"; use approved, logged infrastructure.
4. **Safety bounds** — avoid production disruption; stop conditions; handle any real
   incident discovered during testing properly.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = engagement is scoped, deconflicted,
logged, and safely bounded.

## Quality bar / pitfalls
- Untracked actions that can't be deconflicted (confused with real attacks).
- Exceeding scope / disrupting production.

## Linkage
- Wraps adversary-emulation, c2-redteam, and offensive engagements in safe process.

## References
- `_shared/` rules (authorization, safe execution, evidence).
