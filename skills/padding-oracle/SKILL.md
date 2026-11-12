---
name: padding-oracle
description: >
  Use when testing for padding-oracle (and related decryption-oracle) vulnerabilities
  — where error/behaviour differences on decryption leak plaintext or enable forgery
  (CBC padding oracles, etc.). Covers detection and remediation.
type: knowledge
domain: crypto
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Padding Oracle / Decryption Oracle

When a system reveals — via error messages, timing, or behaviour — whether a
ciphertext decrypted with valid padding, an attacker can decrypt or forge data
without the key (classic CBC padding oracle). Test whether decryption behaviour
leaks such a distinction.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
On endpoints that decrypt attacker-supplied ciphertext (encrypted tokens, cookies,
parameters) using CBC or similar.

## Procedure (gated phases)
1. **Find decryption inputs** — where the app decrypts attacker-controllable
   ciphertext (tokens/cookies/params).
2. **Probe for an oracle (core gate)** — submit modified ciphertexts; look for a
   distinguishable response (error vs different-error vs timing) indicating
   padding/decryption validity.
3. **Confirm** — demonstrate the oracle reliably distinguishes valid/invalid padding
   (bounded), proving decryptability/forgeability.
4. **Impact** — plaintext recovery or ciphertext forgery.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the distinguishable behaviour (the
oracle). Uniform responses / authenticated encryption → **refuted**.

## Impact escalation
Decryption of sensitive tokens and forgery of encrypted data (e.g., auth tokens).
CVSS per `_shared/cvss-reference.md`.

## Remediation
- Use **authenticated encryption** (AES-GCM / encrypt-then-MAC); uniform error
  handling + constant-time; never expose padding/decryption validity; verify MAC
  before decrypting.

## References
- `_shared/` rules (authorization, evidence).
