---
name: bridge-security
description: >
  Use when auditing a cross-chain bridge — the validation of cross-chain messages,
  signer/validator trust, mint/burn logic, and replay — the class behind the largest
  crypto hacks. Covers bridge-specific security review.
type: knowledge
domain: blockchain-web3/defi-infra
maturity: canonical
tools: [foundry]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Cross-Chain Bridge Security

Bridges hold enormous value and have caused the largest crypto losses. Their core
risk is message validation: if an attacker can forge a "deposit" proof or abuse the
validator/signer set, they mint unbacked assets. Audit the message verification,
trust model, and mint/burn accounting.

> Authorized review; PoCs on fork/testnet (`_shared/scope-authorization-rule.md`).

## When to use
Auditing any cross-chain bridge or message-passing protocol.

## Procedure (gated phases)
1. **Understand the trust model** — who attests to cross-chain events (validators/
   multisig/light-client/zk) and the threshold.
2. **Message verification (core)** — can a withdrawal/mint be triggered without a
   genuine, corresponding deposit? Check signature/proof verification rigor and
   replay protection.
3. **Mint/burn accounting** — is locked↔minted supply always consistent? Any path to
   mint unbacked tokens.
4. **Validator/signer risk** — key compromise/threshold assumptions; admin powers.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each finding: the verification/accounting flaw
+ PoC. Rigorous verification → **refuted**.

## Impact escalation
Unbacked minting / fund drain (catastrophic). Critical. CVSS per
`_shared/cvss-reference.md`.

## Remediation
- Rigorous, replay-protected message verification; minimize/decentralize trust
  (light-client/zk over multisig); strict mint/burn accounting; monitored, timelocked
  admin; key security.

## References
- `_shared/` rules (authorization, evidence).
