---
name: business-logic
description: >
  Use when testing an authorized target for business-logic flaws — abuse of
  intended functionality that violates business rules (price/quantity tampering,
  workflow-step skipping, negative values, state manipulation, trust assumptions).
  Covers rule mapping, abuse-case testing, proof and remediation. No single tool
  finds these; they require understanding the app.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, burp-repeater]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Business Logic Flaws (authorized testing)

Find ways the application's **intended rules** can be broken by using features in
unintended sequences or values — not a memory/injection bug, but a reasoning bug.
These require modeling the business rules and systematically testing the
assumptions behind each.

> Authorized testing only. Use test accounts; keep any financial/state effect to
> the minimal reversible proof (`safe-execution-rules.md`).

## When to use
Checkout/pricing, discounts/coupons, refunds, multi-step workflows (KYC,
onboarding, approval), quotas/limits, role/permission transitions, referral/
rewards, and anywhere a rule is enforced only client-side or at one step.

## Prerequisites
- Authorization + scope; test accounts; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Model the rules** — enumerate the invariants the app intends (price ≥ 0, one
   discount, step order, quota N, ownership). Document assumptions per feature.
2. **Enumerate abuse cases (first gate)** — for each rule, list how a client could
   violate it: tamper amount/quantity/currency, skip/reorder steps, replay,
   negative/boundary values, parameter injection (hidden fields), state rollback.
3. **Test systematically** — exercise each abuse case; look for the server
   accepting an out-of-policy outcome.
4. **Confirm impact** — reproduce the rule break and state the business
   consequence; keep effects minimal/reversible.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the violated rule, the
request sequence, and the out-of-policy outcome. A rejected manipulation →
**refuted** for that rule.

## Impact escalation
Financial loss (free/under-priced purchases, infinite discounts/refunds), quota/
limit bypass, privilege/workflow bypass, and data integrity breaks. CVSS per
`_shared/cvss-reference.md` (context-driven).

## False positives & pitfalls
- Server re-validates every rule and rejects manipulation → **refuted**.
- Intended behaviour mistaken for a flaw — confirm it truly violates policy.
- Minimize real financial effects; use test data.

## Remediation
- Enforce **every business rule server-side**, at the authoritative step; never
  trust client-supplied prices/quantities/state; re-validate on each transition.
- Use atomic, idempotent operations; validate value ranges/currency; bind
  workflow state server-side so steps cannot be skipped/replayed.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
