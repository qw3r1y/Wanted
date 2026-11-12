---
name: c2-infra-detection
description: >
  Use when detecting command-and-control infrastructure from network/intel signals —
  identifying C2 servers/domains by their patterns, certificates, and behaviors to
  block and hunt. Defensive C2-infrastructure intelligence.
type: knowledge
domain: red-team-infra
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# C2 Infrastructure Detection (defensive)

Identify command-and-control infrastructure — the servers, domains, and certificates
attackers use — from network behavior and threat intelligence, so you can block it
proactively and hunt for connections to it. Complements host/traffic C2 detection
with an infrastructure-intel view.

## When to use
To proactively block/hunt C2 infrastructure and enrich detections.

## Procedure (gated phases)
1. **Known-C2 intel** — ingest C2 IOC feeds (known frameworks' default certs/profiles,
   malicious domains) and match against egress traffic (cti/feed-management).
2. **Behavioral/fingerprint signals (core)** — beaconing, default C2-framework TLS
   certificates/JA3, newly-registered/suspicious domains, and uncommon protocols.
3. **Hunt** — connections to candidate C2 across historical + live telemetry
   (threat-hunting).
4. **Block & track** — block confirmed C2; track infrastructure clusters for campaign
   correlation (cti).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record C2 indicators + confidence; validate
before blocking (avoid FPs on shared infra).

## Impact / output
Proactive C2 blocking + hunting coverage.

## Pitfalls
- Shared hosting/CDN causing FPs — weigh fidelity.
- Static IOC-only (attackers rotate infra) — add behavioral signals.

## Linkage
- Pairs with redirector-detection, c2-opsec (offensive), detection-engineering, cti.

## References
- `_shared/` rules (evidence).
