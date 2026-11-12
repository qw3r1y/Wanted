---
name: front-running-mev
description: >
  Use when assessing a contract's exposure to front-running / MEV — transaction-
  ordering dependence that lets searchers extract value (sandwich, front/back-run,
  liquidation sniping). Covers MEV-risk review and mitigations.
type: knowledge
domain: blockchain-web3/smart-contract
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Front-Running / MEV

Public mempools let others see and reorder transactions. Protocols whose outcomes
depend on ordering can be exploited — sandwiching swaps, front-running profitable
actions, or sniping liquidations — extracting value from users. Assess ordering
dependence and mitigate.

> Authorized review (`_shared/scope-authorization-rule.md`).

## When to use
Auditing swaps/trades, auctions, liquidations, claims, or any order-sensitive logic.

## Procedure (gated phases)
1. **Find ordering-dependent actions** — where seeing a pending tx + reordering
   yields profit (swaps without slippage limits, first-come rewards, liquidations).
2. **Analyze exploitability (core)** — sandwich (front+back), pure front-run, or
   back-run; and the user harm.
3. **Assess design** — slippage protection, commit-reveal, private mempools, or
   fair-ordering mechanisms present?
4. **Impact** — user value extracted / unfair outcomes.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the ordering dependence + exploit
scenario. Protected (slippage/commit-reveal) → **refuted/low**.

## Impact escalation
Value extraction from users, unfair liquidations, and degraded protocol fairness.
CVSS per `_shared/cvss-reference.md` (context).

## Remediation
- Slippage/deadline protection; commit-reveal for order-sensitive actions; private
  mempools/relays; fair-ordering or batch auctions where appropriate.

## References
- `_shared/` rules (authorization, evidence).
