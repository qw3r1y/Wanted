---
name: mitm-poisoning
description: >
  Use when, in an authorized internal test with explicit approval, assessing
  exposure to on-path and name-resolution poisoning attacks (ARP/LLMNR/NBT-NS/
  mDNS/DHCP) that enable interception or credential capture. Disruptive — strictly
  scoped and coordinated; defensive remediation emphasis.
type: knowledge
domain: offensive/network
maturity: canonical
tools: [responder]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# On-Path / Name-Resolution Poisoning Exposure (authorized)

Assess whether a network is exposed to on-path interception and name-resolution
poisoning (ARP spoofing, LLMNR/NBT-NS/mDNS poisoning, rogue DHCP) that can capture
authentication or traffic. These techniques are **disruptive and detectable**, so
they run only with explicit approval and tight bounds; the value is proving the
exposure to drive mitigation.

> Authorized testing only, with **explicit approval for active poisoning** and a
> defined window. Keep it bounded; stop on signs of disruption
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope + explicit poisoning approval; a network position.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Baseline (first gate)** — check whether mitigations are present (no LLMNR/
   NBT-NS, DHCP snooping, dynamic ARP inspection, 802.1X). If enforced → exposure
   is low; often you can conclude without active poisoning.
2. **Bounded poisoning** — within the window, enable name-resolution poisoning and
   observe whether authentication/traffic is captured — minimal.
3. **Assess capture** — what could be captured (e.g., NetNTLM hashes) and its
   relay/crack potential (feeds active-directory/ntlm-relay-coercion).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the exposure, and minimal
capture proof. Mitigations enforced → **refuted**.

## Impact escalation
Credential capture → relay/crack → lateral movement; traffic interception. CVSS
per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Segmented/802.1X networks resist this → **refuted**.
- Disruptive/detectable — only in approved windows.

## Remediation
- Disable LLMNR/NBT-NS/mDNS; enable DHCP snooping + dynamic ARP inspection; 802.1X;
  SMB signing + LDAP channel binding; network segmentation; monitor poisoning.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
