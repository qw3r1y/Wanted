---
name: exposure-risk-scoring
description: >
  Use when prioritizing the external attack surface by risk — scoring each exposed
  asset/service by sensitivity, vulnerability, and exploitability so remediation
  focuses on what matters. Covers EASM risk prioritization and reporting.
type: knowledge
domain: easm
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Exposure Risk Scoring (EASM)

A big asset inventory isn't actionable without prioritization. Score each exposed
asset/service by what it is (sensitivity), what's wrong with it (vulnerabilities/
misconfig), and how reachable/exploitable it is — so teams fix the riskiest exposures
first instead of drowning in a flat list.

## When to use
To turn the EASM inventory into a prioritized remediation program.

## Procedure (gated phases)
1. **Characterize each exposure** — service type, sensitivity (admin/login/API vs
   marketing), and whether it should be internet-facing at all.
2. **Add vulnerability/misconfig signal** — known CVEs, weak TLS, exposed panels,
   default creds, takeover risk.
3. **Score** — combine asset sensitivity × exposure × exploitability into a priority;
   flag "should-not-be-exposed" assets highly.
4. **Report & route** — a ranked remediation list to owners; track closure.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each score is explainable; prioritization is
validated against real risk.

## Impact / output
A prioritized external-exposure remediation program (not a flat asset dump).

## Pitfalls
- Flat inventories / CVE-count-only scoring — weight by sensitivity + exploitability.
- Ignoring "shouldn't be exposed" assets (shadow admin panels) — rank them high.

## Linkage
- Consumes continuous-discovery + takeover-detection; feeds vulnerability-management
  + reporting.

## References
- `_shared/` rules (evidence).
