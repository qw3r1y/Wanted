---
name: intel-reporting
description: >
  Use when writing threat-intelligence reports/briefs — structuring findings for
  the audience (exec vs technical), with clear assessments, confidence, and
  actionable recommendations. Covers intel writing and dissemination.
type: knowledge
domain: defensive/cti
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Threat Intelligence Reporting

Communicate intelligence so it drives action: structured for the audience,
leading with the assessment and "so what", with confidence levels, evidence, and
concrete recommendations — not a raw dump of indicators.

## When to use
To disseminate findings from analysis/incidents to leadership, SOC, or stakeholders.

## Procedure (gated phases)
1. **Audience & purpose** — exec (impact/decision) vs technical (TTPs/IOCs/
   detections); tailor accordingly.
2. **Lead with the assessment** — key judgment + confidence + "so what"; then
   supporting evidence.
3. **Make it actionable** — specific recommendations (detections, blocks, hunts,
   hardening) tied to the findings.
4. **Package IOCs/TTPs** — structured (STIX where useful) for machine consumption.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Assessments carry confidence; separate fact
from judgment.

## Impact / output
Intel that leads to decisions and defensive action.

## Pitfalls
- IOC dumps without assessment/recommendations — lead with meaning.
- No confidence levels; mixing fact and assessment.

## Governance
- Consistent report templates; feedback on usefulness; track recommendations to
  closure.

## References
- `_shared/` rules (evidence).
