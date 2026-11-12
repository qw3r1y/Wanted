---
name: credential-dumping-ad
description: >
  Use when, in an authorized AD engagement, assessing credential-material exposure
  — DCSync rights, LSASS/SAM exposure, and cached credentials — to demonstrate
  what an attacker with a given foothold could harvest. Emphasis on rights/
  exposure assessment, detection and remediation (defensive framing).
type: knowledge
domain: offensive/active-directory
maturity: canonical
tools: [impacket, mimikatz]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# AD Credential Exposure Assessment (authorized)

Within an authorized engagement, determine what credential material a given
foothold could expose — principals with DCSync rights (replication), hosts where
privileged credentials are cached, and LSASS/SAM accessibility — to demonstrate
blast radius and drive hardening. Framed around rights/exposure and detection, not
mass harvesting.

> Authorized testing only. Demonstrate exposure **minimally** (e.g., prove DCSync
> rights exist / that a single test credential is reachable); do not mass-dump or
> reuse real credentials (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope + explicit approval for credential-exposure testing; a
  foothold context. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Replication rights (DCSync)** — identify non-DC principals holding
   replication rights (Get-Replication-Changes-All) — a frequent misconfig; this
   alone is a finding.
2. **Cached-credential exposure** — identify hosts where privileged accounts log
   in (credential caching risk); assess LSASS/SAM protection (Credential Guard,
   PPL).
3. **Minimal demonstration** — prove the *capability* (rights exist / a test
   secret is reachable) without harvesting real credentials at scale.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the exposure (DCSync
rights/cached creds/LSASS accessibility), and minimal proof. Protected (Cred
Guard/PPL, no stray replication rights) → **refuted**.

## Impact escalation
Domain-wide credential compromise and persistence from excessive rights or weak
host protection. Critical. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Legitimate replication principals (DCs/known sync) are expected — flag only
  unexpected ones.
- Never mass-dump or reuse real credentials; prove capability only.

## Remediation
- Remove stray replication rights; enable Credential Guard + LSASS PPL; tiered
  admin to prevent privileged caching on workstations; monitor DCSync/LSASS access;
  LAPS for local admin.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
