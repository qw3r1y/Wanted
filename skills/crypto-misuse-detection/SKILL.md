---
name: crypto-misuse-detection
description: >
  Use when detecting cryptographic misuse in an application — weak algorithms, bad
  modes, poor key/IV handling, and insecure randomness — across code and config.
  Umbrella crypto-misuse assessment (pairs with secure-coding/crypto-usage-review).
type: knowledge
domain: crypto
maturity: canonical
tools: [semgrep]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Cryptographic Misuse Detection

Systematically find the crypto mistakes that break confidentiality/integrity even
with "strong" primitives — weak/deprecated algorithms, insecure modes (ECB),
static/reused IVs, unauthenticated encryption, weak KDFs for passwords, and
non-CSPRNG randomness — across code and configuration.

## When to use
Auditing an application's use of cryptography at scale.

## Procedure (gated phases)
1. **Inventory crypto usage** — algorithms, modes, key management, randomness, and
   where each is used.
2. **Detect misuse** — weak/broken algorithms (MD5/SHA1 for security, DES/RC4), ECB,
   static/reused IV/nonce, unauthenticated encryption, fast/unsalted password
   hashing, non-CSPRNG, hardcoded keys.
3. **Assess impact** — what each misuse exposes (confidentiality/integrity/auth).
4. **Prioritize & fix** — toward authenticated encryption + strong KDFs + vetted
   libraries.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each finding cites the misuse + impact + fix.

## Quality bar / pitfalls
- Flagging algorithm names without context (e.g., MD5 for non-security checksums is
  fine) — assess usage.
- Missing config-level crypto (TLS, at-rest) — include it.

## Linkage
- Pairs with secure-coding/crypto-usage-review; feeds padding-oracle/weak-randomness/
  tls-config.

## References
- `_shared/` rules (evidence).
