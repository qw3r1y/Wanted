---
name: crypto-usage-review
description: >
  Use when reviewing cryptography usage in code — algorithm choice, key management,
  randomness, modes/IVs, password hashing, and common misuse — to ensure crypto is
  used correctly. Covers crypto-misuse review (not designing primitives).
type: knowledge
domain: appsec/secure-coding
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Cryptography Usage Review

Most crypto failures are **misuse**, not broken primitives. Review how code uses
crypto — algorithm/mode choice, key management, randomness source, IV/nonce
handling, password hashing, and authentication of ciphertext — against known
pitfalls, and steer toward vetted libraries/defaults.

## When to use
When reviewing code handling secrets, encryption, hashing, signing, or tokens.

## Procedure (gated phases)
1. **Inventory crypto usage** — where encryption/hashing/signing/randomness happens
   and which libraries/algorithms.
2. **Check against misuse patterns** — weak/broken algorithms, ECB mode, static/
   reused IVs, non-CSPRNG randomness, unsalted/fast password hashing, unauthenticated
   encryption, hardcoded keys.
3. **Key management** — generation, storage, rotation, and scope.
4. **Recommend** — vetted library defaults (authenticated encryption, strong KDFs)
   over hand-rolled crypto.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each finding cites the misuse + correct
pattern.

## Quality bar / pitfalls
- Hand-rolled crypto; "custom" encryption — flag strongly.
- Confidentiality without integrity (unauthenticated encryption).

## Linkage
- Feeds crypto/ domain for deeper issues (padding-oracle, weak-random); enforce via
  rules.

## References
- `_shared/` rules (evidence).
