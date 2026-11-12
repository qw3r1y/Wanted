---
name: sigma-rule-authoring
description: >
  Use when writing or improving Sigma detection rules — translating a technique or
  threat behaviour into a portable, high-fidelity Sigma rule with good logic,
  false-positive handling, and ATT&CK mapping. Covers rule design, testing and
  tuning. For SIEM-native queries see siem-detection-queries.
type: knowledge
domain: defensive/detection-engineering
maturity: canonical
tools: [sigma, sigmac]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - references/sigma-structure.md
license: MIT
version: 1.0.0
---

# Sigma Rule Authoring

Turn a specific attacker behaviour into a portable, maintainable Sigma rule that
detects it with high fidelity — precise selection logic, deliberate false-positive
handling, correct log source, and ATT&CK mapping — so it can be converted to any
SIEM backend.

## When to use
When creating/improving detections for a technique (from threat-hunting, purple-
team gaps, CTI, or incident findings).

## Procedure (gated phases)
1. **Define the behaviour** — the exact observable(s) that indicate the technique
   (process, command-line, registry, network, file) and the log source that
   carries them.
2. **Write selection logic** — precise `selection`/`filter` conditions; prefer
   behaviour over brittle string IOCs; avoid over-broad matches.
3. **False-positive handling** — enumerate benign triggers and exclude them;
   document known FPs in the rule.
4. **Map & tag** — ATT&CK technique id, severity, and metadata (`references/sigma-structure.md`).
5. **Test** — against known-malicious and known-benign data; measure FP rate before
   deploying.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. A rule is "done" when it detects the
behaviour on test data with an acceptable, documented FP rate. Record detection +
FP test results.

## Quality bar / pitfalls
- Over-broad rules (alert fatigue) or IOC-only rules (brittle) — prefer robust
  behavioural logic.
- Wrong/absent log source makes the rule silently useless — verify telemetry
  exists.

## Deployment notes
- Convert to the target SIEM; stage in audit/test mode; tune thresholds; version
  the rule; feed detection-coverage-mapping.

## References
- `_shared/` rules; `references/sigma-structure.md` — Sigma field/structure reference.
