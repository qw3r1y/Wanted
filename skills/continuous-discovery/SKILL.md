---
name: continuous-discovery
description: >
  Use when operating EASM continuously — re-running attribution/discovery on a
  cadence, detecting new/changed/removed assets, and alerting on changes to the
  external attack surface. Covers the monitoring loop of EASM.
type: knowledge
domain: easm
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Continuous Discovery & Monitoring (EASM)

The attack surface changes constantly — new subdomains, spun-up cloud assets,
expired certs, shadow IT. Run attribution/discovery continuously, diff against the
known inventory, and alert on new/changed/removed assets so exposures are caught in
hours, not at the next pentest.

## When to use
As the ongoing operation of an EASM program.

## Procedure (gated phases)
1. **Schedule discovery** — re-run attribution + discovery on a cadence (and on
   triggers like new certificates).
2. **Diff the inventory** — detect **new** assets (shadow IT, new deployments),
   **changed** assets (new services/exposure), and **removed** assets.
3. **Enrich & score** — run new assets through confidence-scoring + FP-rejection
   before alerting.
4. **Alert & route** — notify owners of net-new exposures and significant changes;
   feed exposure scoring + remediation.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = inventory changes are detected and
alerted with low false-positive noise.

## Impact / output
Timely detection of new exposures and shadow IT across the external surface.

## Pitfalls
- Alerting on unscored/raw discoveries → noise; score first.
- Only detecting additions (missing removals/changes).

## Linkage
- Orchestrates asset-attribution/scoring/FP-rejection; feeds takeover-detection +
  exposure scoring.

## References
- `_shared/` rules (evidence).
