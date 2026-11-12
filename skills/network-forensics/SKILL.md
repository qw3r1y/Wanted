---
name: network-forensics
description: >
  Use when analyzing network evidence during IR — PCAP and flow analysis to
  identify C2, exfiltration, lateral movement, and protocol abuse. Covers packet/
  flow analysis and extracting network IOCs.
type: knowledge
domain: defensive/dfir
maturity: canonical
tools: [wireshark, zeek]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Network Forensics

Analyze packet captures and flow data to see the network side of an incident —
command-and-control channels, data exfiltration, lateral movement, and protocol
abuse — extracting network IOCs and corroborating host findings.

## When to use
During IR when PCAP/flow/Zeek data is available, especially for C2/exfil/lateral
questions.

## Procedure (gated phases)
1. **Scope the capture** — the relevant hosts/time window; parse with flow tooling
   (Zeek) for an overview, PCAP for detail.
2. **Find C2/exfil signals** — beaconing periodicity, anomalous destinations/
   volumes, suspicious TLS/DNS patterns, and large outbound transfers.
3. **Reconstruct sessions** — extract transferred files/credentials where present;
   follow conversations.
4. **Extract IOCs** — domains/IPs/JA3/certs/patterns for blocking + hunting.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Cite packets/flows for each conclusion;
distinguish benign anomalies from malicious.

## Impact / output
Confirmed C2/exfil/lateral evidence + network IOCs (feeds hunting, detections,
scoping).

## Pitfalls
- Encrypted traffic limits visibility — use metadata (JA3/SNI/volume/timing).
- Capture gaps/sampling — note limitations.

## Remediation / IR linkage
- Block IOCs; add network detections (beaconing/exfil); improve egress controls.

## References
- `_shared/` rules (untrusted input, evidence).
