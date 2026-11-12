---
name: iot-protocol-attacks
description: >
  Use when assessing authorized IoT communication protocols — MQTT, CoAP, Zigbee,
  Z-Wave, and proprietary RF/network protocols — for weak authentication, lack of
  encryption, and command injection. Covers IoT protocol security.
type: knowledge
domain: hardware-iot
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# IoT Protocol Security Assessment

IoT devices often speak protocols with weak or no authentication/encryption — MQTT
brokers without auth, unencrypted CoAP, Zigbee/Z-Wave pairing weaknesses, or
proprietary protocols — allowing eavesdropping, spoofed commands, or device
takeover. Assess the protocols an authorized device/ecosystem uses.

> Authorized testing on your own/in-scope devices (`_shared/scope-authorization-rule.md`).

## When to use
Assessing an IoT device/ecosystem's network/RF communications.

## Procedure (gated phases)
1. **Identify protocols** — the network (MQTT/CoAP/HTTP) and RF (Zigbee/Z-Wave/BLE/
   proprietary) protocols in use.
2. **Auth & encryption (core)** — is communication authenticated and encrypted? Open
   MQTT brokers, plaintext command channels, weak pairing.
3. **Command injection/spoofing** — can commands be injected/replayed/spoofed to
   control devices?
4. **Assess impact** — eavesdropping, unauthorized control, and pivot.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the weakness + proof (e.g., spoofed
command on a test device). Authenticated+encrypted → **refuted**.

## Impact escalation
Device control, data interception, and ecosystem compromise. CVSS per
`_shared/cvss-reference.md`.

## Pitfalls
- RF testing needs appropriate scope/equipment; use test devices.

## Remediation
- Authenticated + encrypted communications; broker/endpoint auth; secure pairing;
  replay protection; network segmentation for IoT.

## References
- `_shared/` rules (authorization, evidence).
