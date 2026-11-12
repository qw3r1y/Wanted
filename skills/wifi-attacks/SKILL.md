---
name: wifi-attacks
description: >
  Use when assessing an authorized Wi-Fi network — WPA2/WPA3 auth posture, PMKID/
  handshake capture for offline analysis, rogue-AP/evil-twin exposure, and
  guest/segmentation review. Scope-bounded RF testing with defensive remediation.
type: knowledge
domain: offensive/wireless
maturity: canonical
tools: [aircrack-ng, hashcat]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Wi-Fi Security Assessment (authorized)

Assess an authorized wireless network's authentication strength and architecture —
passphrase strength (via offline analysis of captured handshakes/PMKID), evil-twin/
rogue-AP susceptibility, and whether guest/corporate traffic is properly segmented.
RF testing is physically scoped; coordinate and bound it.

> Authorized testing only, within the owner's physical premises/scope. No
> deauth/disruption without explicit approval (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope (SSIDs, premises, approval for active RF). `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Posture (first gate)** — identify WPA2 vs WPA3/SAE, PMF, and enterprise
   (802.1X) vs PSK; strong config reduces exposure.
2. **Handshake/PMKID capture (bounded)** — for PSK networks, capture material for
   **offline** passphrase analysis (no live cracking against the AP).
3. **Offline analysis** — bounded attempt against the captured material to prove
   weak-passphrase risk.
4. **Architecture** — evil-twin/rogue-AP exposure and guest/corporate segmentation.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the posture, and offline
proof. WPA3/SAE + PMF + strong passphrase/802.1X → **refuted** for passphrase risk.

## Impact escalation
Network access via weak passphrase, credential capture via evil-twin, and lateral
reach where guest isn't segmented. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- WPA3-SAE/PMF resist offline + deauth → **refuted**.
- Avoid deauth/disruption unless explicitly approved.

## Remediation
- WPA3-SAE + PMF (or 802.1X enterprise); strong passphrases; rogue-AP detection;
  segment guest from corporate; WIDS/WIPS.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
