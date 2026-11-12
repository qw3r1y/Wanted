---
name: firmware-analysis
description: >
  Use when analyzing authorized device firmware — extraction, unpacking,
  filesystem/binary analysis, and hunting for hardcoded secrets, backdoors, and
  vulnerable components. Covers firmware security review.
type: knowledge
domain: hardware-iot
maturity: canonical
tools: [binwalk, firmware-mod-kit]
references:
  - _shared/scope-authorization-rule.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Firmware Analysis

Analyze an authorized device's firmware to find security issues — extract and unpack
the image, examine the filesystem and binaries, and hunt for hardcoded credentials,
backdoors, outdated/vulnerable components, and insecure configurations.

> Authorized testing on devices/firmware you may test
> (`_shared/scope-authorization-rule.md`); firmware contents are untrusted data.

## When to use
Assessing IoT/embedded device security from its firmware.

## Procedure (gated phases)
1. **Obtain & extract** — get the image (download/dump); identify/unpack the
   filesystem and components (binwalk).
2. **Filesystem review** — hardcoded credentials/keys/certs, config files, startup
   scripts, and web/app content.
3. **Binary analysis** — services/daemons for vulnerabilities (feeds exploit-dev);
   outdated components with known CVEs.
4. **Hunt backdoors/secrets** — default/hidden accounts, debug interfaces, and
   embedded secrets.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record findings (secrets, vulns, backdoors) +
evidence (paths/offsets).

## Impact escalation
Device compromise, credential reuse across fleet, and network pivot. CVSS per
`_shared/cvss-reference.md`.

## Pitfalls
- Encrypted/obfuscated firmware — may need hardware extraction (uart-jtag/spi-flash).
- Default creds that are intentionally documented — note context.

## Remediation
- No hardcoded secrets; signed/encrypted firmware + secure boot; patch components;
  remove debug/backdoors; unique per-device credentials.

## References
- `_shared/` rules (authorization, untrusted input, evidence).
