---
name: reentrancy
description: >
  Use when auditing a smart contract for reentrancy — external calls made before
  state updates that allow recursive re-entry to drain funds or corrupt state
  (single-function, cross-function, read-only, cross-contract). Covers detection
  and remediation.
type: knowledge
domain: blockchain-web3/smart-contract
maturity: canonical
tools: [foundry, slither]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Reentrancy

The classic fund-drain bug: a contract makes an external call before updating its
state, letting the callee re-enter and act on stale state (withdraw repeatedly,
etc.). Covers single-function, cross-function, cross-contract, and read-only
reentrancy.

> Authorized review; PoCs on fork/testnet (`_shared/scope-authorization-rule.md`).

## When to use
Auditing any contract that makes external calls (token transfers, ETH sends,
callbacks) around state changes.

## Procedure (gated phases)
1. **Find external-call points** — ETH sends, token transfers (esp. ERC777/ERC721
   hooks), and arbitrary external calls.
2. **Check ordering (core gate)** — is state updated **after** the external call?
   (checks-effects-interactions violated). Also check cross-function and read-only
   (view functions reading mid-update state) reentrancy.
3. **PoC** — write an attacker contract that re-enters; prove drain/corruption on a
   fork.
4. **Assess impact** — funds drained / invariant broken.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the vulnerable call-ordering + PoC.
Proper ordering/guards → **refuted**.

## Impact escalation
Fund theft, state corruption, protocol insolvency. Critical. CVSS/impact per
`_shared/cvss-reference.md`.

## Remediation
- **Checks-Effects-Interactions**: update state before external calls; reentrancy
  guards (nonReentrant); be wary of ERC777/callback tokens; consider read-only
  reentrancy in view-dependent logic.

## References
- `_shared/` rules (authorization, evidence).
