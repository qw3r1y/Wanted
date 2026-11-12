---
name: bluetooth-ble-attacks
description: >
  Use when assessing an authorized Bluetooth/BLE device or app — pairing/bonding
  security, GATT service exposure, sniffing/relay susceptibility, and
  authentication of commands. Covers device enumeration and security assessment.
type: knowledge
domain: offensive/wireless
maturity: canonical
tools: [bluetoothctl, gatttool]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Bluetooth / BLE Assessment (authorized)

Assess an authorized Bluetooth/BLE device for weak pairing/bonding, unauthenticated
GATT characteristics (commands/data accessible without proper auth), and sniffing/
relay susceptibility. The proof is unauthorized interaction with or disclosure from
the device.

> Authorized testing only, on devices you own/are authorized to test
> (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope; the device + a BLE-capable tester. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate** — discover the device, services, and GATT characteristics;
   identify the pairing/bonding method (Just Works vs authenticated).
2. **Auth posture (core gate)** — test whether sensitive characteristics (commands/
   data) require authenticated/encrypted access or are readable/writable openly.
3. **Interaction** — read/write a non-destructive characteristic to prove
   unauthorized access (e.g., read a value or trigger a benign command).
4. **Sniffing/relay** — assess susceptibility to passive sniffing (Just Works) or
   relay.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the exposed characteristic/
pairing weakness, and proof. Authenticated+encrypted access → **refuted**.

## Impact escalation
Unauthorized device control, data disclosure, and interception. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Values that are meant to be public/read-only → informational.
- Use only owned/authorized devices.

## Remediation
- Authenticated/encrypted pairing (not Just Works for sensitive devices);
  authenticate sensitive GATT operations; app-layer command authentication;
  minimize exposed characteristics.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
