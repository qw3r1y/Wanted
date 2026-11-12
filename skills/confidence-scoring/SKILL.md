---
name: confidence-scoring
description: >
  Use when scoring the confidence that a discovered asset belongs to the target
  organization — weighting attribution evidence into a calibrated score so only
  high-confidence assets enter the inventory. The product differentiator of quality
  EASM.
type: knowledge
domain: easm
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Attribution Confidence Scoring (EASM)

Raw discovery produces candidates of wildly varying certainty. Score each candidate's
**confidence of ownership** by weighting its attribution evidence, so the inventory
contains assets you can stand behind — this calibrated scoring, not the crawler, is
what makes an EASM system trustworthy.

## When to use
After asset-attribution, before an asset enters the monitored inventory.

## Procedure (gated phases)
1. **Define evidence weights** — strong signals (registrant match, dedicated IP
   range/ASN, org-named certificate) vs weak/shared signals (shared CDN/cloud IP,
   shared cert, generic WHOIS-privacy).
2. **Score candidates** — combine signals into a calibrated confidence (e.g.,
   high/medium/low or a numeric score); multiple independent strong signals raise it.
3. **Set thresholds** — high-confidence → inventory; medium → review; low → candidate
   pool (or discard).
4. **Calibrate** — tune weights against known true/false attributions; measure
   precision.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each asset's score is explainable by its
evidence; calibration is measured (precision/recall).

## Impact / output
A trustworthy inventory where inclusion confidence is explicit and tunable.

## Pitfalls
- Treating all signals equally (shared infra inflates confidence) — weight by
  specificity.
- Uncalibrated scores — validate against ground truth.

## Linkage
- Consumes asset-attribution; feeds false-positive-rejection + exposure scoring.

## References
- `_shared/` rules (evidence).
