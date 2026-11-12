---
name: jwt-attacks
description: >
  Use when an authorized API uses JWTs for auth and you need to test token
  integrity — alg:none, algorithm confusion (RS256→HS256), weak-secret cracking,
  key confusion/injection (jwk/kid/jku), and claim tampering. Covers verification
  analysis, controlled proof and remediation.
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl, jwt-tooling, hashcat]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# JWT Attacks (authorized testing)

Test whether a JWT's signature/claims can be forged or tampered so the server
accepts an attacker-controlled identity. The proof is the server honoring a token
you forged or modified without the legitimate signing key.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Use test
> accounts; forge only to prove acceptance, not to access real data.

## When to use
Any API issuing/accepting JWTs (bearer tokens, cookies). Inspect the header
(`alg`, `kid`, `jwk`, `jku`) and claims first.

## Prerequisites
- Authorization + scope; a valid test-user JWT to analyze.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Decode & analyze** — read header/claims; note `alg`, key hints, expiry,
   privilege claims (`role`, `sub`, `admin`).
2. **Integrity tests (core gate)** — check whether the server validates the
   signature at all, and which attacks it resists:
   | Attack | Idea | Confirmed when |
   |---|---|---|
   | `alg:none` | Strip signature | Server accepts unsigned token |
   | RS256→HS256 confusion | Sign with public key as HMAC secret | Forged token accepted |
   | Weak secret | Offline-crack HS* secret (own token) | Secret recovered → forge |
   | `kid`/`jku`/`jwk` injection | Point to attacker key/path | Server trusts attacker key |
3. **Forge & tamper** — with a confirmed weakness, mint a token elevating a **test**
   identity and confirm acceptance (a protected endpoint responds as the forged
   role).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the specific weakness,
the forged token, and the server's acceptance proof. A tampered token rejected →
**refuted** for that attack.

## Impact escalation
Authentication bypass, privilege escalation, and full account impersonation. CVSS
per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Server rejects `alg:none`/tampered sig → that attack **refuted**.
- Crack attempts only on your own token's secret; keep bounded.

## Remediation
- Pin the expected algorithm server-side (never accept `none` or client-chosen
  alg); use strong, rotated secrets/keys; validate `kid`/`jku`/`jwk` against a
  trusted set (no remote key fetch from untrusted input).
- Short expiries + revocation; validate all security-relevant claims.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
