---
name: redirector-detection
description: >
  Use when, from a defensive perspective, understanding and detecting red-team/
  attacker redirector and domain-fronting infrastructure — so defenders can spot C2
  that hides behind legitimate-looking fronts. Detection-focused.
type: knowledge
domain: red-team-infra
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Redirector / Fronting Detection (defensive)

Attackers hide C2 behind redirectors and domain-fronting/CDN tricks to look like
legitimate traffic. This skill is defensive: understand how such infrastructure works
so you can **detect** it — spotting the traffic and DNS/TLS patterns that distinguish
fronted C2 from normal use.

## When to use
When building detections for C2 that hides behind legitimate-looking infrastructure
(coordinated with red-team findings).

## Procedure (gated phases)
1. **Understand the technique** — redirectors (traffic relayed through innocuous
   hosts) and fronting (SNI/Host mismatch via shared CDNs) that mask the real C2.
2. **Detection signals (core)** — SNI vs Host header mismatches, anomalous CDN usage,
   JA3/TLS fingerprints, beaconing patterns through "legit" domains, and DNS anomalies.
3. **Build detections** — turn signals into analytics (detection-engineering);
   egress/CDN monitoring.
4. **Validate** — against red-team/purple-team traffic to confirm coverage.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = detections that flag fronted/relayed
C2 with acceptable FPs; validated via purple-team.

## Impact / output
Detection coverage for evasive C2 infrastructure.

## Pitfalls
- Legitimate CDN/fronting-like traffic → FPs; combine signals (beaconing + mismatch).

## Linkage
- Defensive counterpart to offensive c2-redteam/c2-opsec; feeds detection-engineering.

## References
- `_shared/` rules (evidence).
