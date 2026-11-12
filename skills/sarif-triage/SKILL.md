---
name: sarif-triage
description: >
  Use when triaging and managing security-scanner results at scale (SARIF) —
  normalizing findings from multiple tools, deduplicating, prioritizing, and
  suppressing false positives with an audit trail. Covers findings management.
type: knowledge
domain: appsec/sast-dast
maturity: canonical
tools: [sarif]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Scanner Findings Triage (SARIF)

Turn a flood of multi-tool scanner output into a managed, prioritized backlog —
normalize via SARIF, deduplicate across tools, prioritize by real risk, and suppress
false positives with justification and an audit trail — so developers see signal,
not noise.

## When to use
When multiple SAST/DAST/SCA tools produce overlapping, noisy findings.

## Procedure (gated phases)
1. **Normalize** — ingest results as SARIF; unify severity/location across tools.
2. **Deduplicate** — collapse the same issue reported by multiple tools / multiple
   times.
3. **Prioritize** — by exploitability, reachability, and asset exposure (not raw
   severity).
4. **Suppress with audit** — mark confirmed false positives with justification;
   track accepted risks; prevent re-alerting.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each finding has a disposition
(confirmed/FP/accepted) with justification and an audit trail.

## Quality bar / pitfalls
- Un-triaged scanner dumps → developer distrust.
- Suppressing without justification/audit → hidden real issues.

## Deployment
- Central findings store; CI gates on confirmed high-priority; trend metrics.

## References
- `_shared/` rules (evidence).
