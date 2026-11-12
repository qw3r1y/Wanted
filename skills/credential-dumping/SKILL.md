---
name: credential-dumping
description: >
  Use when, in an authorized engagement, assessing host-level credential exposure —
  where credentials/secrets live on a compromised host (memory, files, browsers,
  config, tokens) and how protected they are — to demonstrate blast radius.
  Exposure-assessment + detection + remediation focus.
type: knowledge
domain: offensive/post-exploitation
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Host Credential Exposure Assessment (authorized)

On an authorized compromised host, assess what credentials/secrets are exposed and
how well protected — process memory, config files, browser stores, cloud/SSH keys,
and cached tokens — to demonstrate the blast radius a foothold grants and drive
hardening. Framed around exposure and detection, not mass harvesting.

> Authorized testing only. Demonstrate exposure **minimally** (prove a secret is
> reachable); do not harvest/reuse real credentials at scale
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope + explicit approval for credential-exposure testing; a
  foothold. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Locate stores** — enumerate where credentials/secrets could reside (config/
   env, SSH/cloud keys, browser stores, app secrets, cached tokens, process
   memory) and the OS protections present (Credential Guard, keychain, DPAPI).
2. **Assess protection (core)** — determine which are accessible from the current
   privilege and how protected.
3. **Minimal demonstration** — prove a single reachable secret/credential exists
   (capability), without bulk extraction or reuse.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the exposure, and minimal
proof. Protected stores (Cred Guard/keychain/encrypted) → **refuted**.

## Impact escalation
Lateral movement and privilege escalation via reused/exposed credentials. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Encrypted/protected stores inaccessible at current privilege → lower impact.
- Never reuse real credentials beyond minimal proof.

## Remediation
- Credential Guard / OS secret protection; no plaintext secrets on disk/env; secret
  managers; short-lived tokens; EDR detection of credential access; least privilege.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
