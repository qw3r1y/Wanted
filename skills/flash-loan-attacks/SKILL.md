---
name: flash-loan-attacks
description: >
  Use when assessing a DeFi protocol's exposure to flash-loan-enabled attacks —
  where uncollateralized in-tx capital amplifies oracle manipulation, governance,
  or economic logic flaws. Covers flash-loan threat analysis.
type: knowledge
domain: blockchain-web3/smart-contract
maturity: canonical
tools: [foundry]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Flash-Loan Attack Analysis

Flash loans give an attacker enormous uncollateralized capital for one transaction —
turning otherwise-minor economic/oracle/governance flaws into protocol-draining
exploits. Assess whether any protocol logic can be abused at flash-loan scale.

> Authorized review; PoCs on fork/testnet (`_shared/scope-authorization-rule.md`).

## When to use
Auditing DeFi protocols with price-dependent logic, governance, or economic
invariants.

## Procedure (gated phases)
1. **Find amplifiable logic** — anything whose outcome depends on balances/prices/
   votes that huge in-tx capital could swing (oracle, collateral, governance,
   reward math).
2. **Model the attack (core)** — borrow → manipulate (price/vote/state) → extract →
   repay, all atomically.
3. **PoC** — implement the flash-loan attack on a fork; quantify profit/damage.
4. **Impact** — fund drain, insolvency, governance capture.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the amplified flaw + PoC. Logic robust
to flash-scale capital → **refuted**.

## Impact escalation
Protocol drain/insolvency, governance takeover. Critical. CVSS per
`_shared/cvss-reference.md`.

## Remediation
- Don't rely on manipulable spot prices (robust oracles); make economic invariants
  flash-resistant; snapshot/delay governance voting power; design for atomic-capital
  adversaries.

## References
- `_shared/` rules (authorization, evidence).
