---
name: signature-replay
description: >
  Use when auditing signature-based contract logic (permit, meta-tx, approvals) for
  replay and malleability — missing nonces, chain-id/domain separation, and
  signature reuse that let an attacker replay signed actions. Covers signature
  security review.
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

# Signature Replay & Malleability

Contracts that accept off-chain signatures (EIP-712 permit, meta-transactions,
approvals) must prevent replay — a signed message reused on another chain, contract,
or repeatedly — and malleability. Audit for nonces, domain separation, and expiry.

> Authorized review; PoCs on fork/testnet (`_shared/scope-authorization-rule.md`).

## When to use
Auditing permit/meta-tx/gasless/approval flows using signed messages.

## Procedure (gated phases)
1. **Find signature verification** — where signed messages authorize actions.
2. **Check anti-replay (core gate)** — per-signer **nonce** (consumed once),
   **chain-id + contract domain** separation (EIP-712), and **expiry/deadline**. Also
   signature malleability handling (use ecrecover safely / OZ ECDSA).
3. **PoC** — attempt to replay a signature (same chain repeated, or cross-chain/
   cross-contract) on a fork.
4. **Impact** — unauthorized repeated/other-context execution of signed actions.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the missing protection + replay PoC.
Nonce + domain + expiry present → **refuted**.

## Impact escalation
Repeated unauthorized transfers/approvals, cross-chain replay. CVSS per
`_shared/cvss-reference.md`.

## Remediation
- Per-signer nonces consumed on use; EIP-712 domain separation (chain-id + contract);
  deadlines; malleability-safe recovery (OZ ECDSA).

## References
- `_shared/` rules (authorization, evidence).
