---
name: weak-randomness
description: >
  Use when assessing an application's randomness for security use — predictable
  tokens/IDs/keys from non-CSPRNG or low-entropy sources that enable prediction/
  brute-force. Covers randomness-quality review.
type: knowledge
domain: crypto
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Weak Randomness

Security tokens, session IDs, password-reset tokens, keys, and nonces must be
unpredictable. Using a non-cryptographic RNG (e.g., `Math.random`, `rand()`),
seeding with time, or low entropy lets an attacker predict or brute-force them.
Assess where randomness matters and whether it's cryptographically secure.

## When to use
Auditing generation of tokens/IDs/keys/nonces/salts.

## Procedure (gated phases)
1. **Find security-relevant randomness** — session/reset/CSRF tokens, IDs used for
   access, keys, nonces, salts.
2. **Assess the source (core)** — is a CSPRNG used? Non-crypto RNGs, predictable
   seeds (time/PID), or insufficient length are weaknesses.
3. **Predictability test** — where feasible, assess whether tokens are predictable/
   enumerable (sequential, time-based, low entropy).
4. **Impact** — token/ID prediction → account/resource access.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the weak source + impact. CSPRNG +
sufficient length → **refuted**.

## Impact escalation
Session hijacking, reset-token prediction, key compromise. CVSS per
`_shared/cvss-reference.md`.

## Remediation
- Use a CSPRNG for all security values; sufficient length (≥128 bits); never seed
  with predictable values; language-appropriate secure-random APIs.

## References
- `_shared/` rules (evidence).
