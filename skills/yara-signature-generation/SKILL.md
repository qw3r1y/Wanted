---
name: yara-signature-generation
description: >
  Use when turning malware analysis into detection — deriving robust YARA
  signatures (and hunting rules) from a sample/family's durable features. Bridges
  malware-re to detection-engineering with family-level, FP-controlled rules.
type: knowledge
domain: malware-re
maturity: canonical
tools: [yara]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# YARA Signature Generation (from analysis)

Convert what you learned analyzing a sample into durable detection: pick features
that identify the **family** (not one build), write FP-controlled YARA conditions,
and validate — so detection scales across variants. Complements
detection-engineering/yara-rule-authoring with an RE-driven feature focus.

## When to use
After static/dynamic analysis, to operationalize the family into scalable detection.

## Procedure (gated phases)
1. **Select durable features** — code constants, unique strings, structural traits,
   and decoded config markers that generalize across the family (avoid build-
   specific/volatile data).
2. **Write conditions** — combine features with structure (N-of-M, PE fields,
   entropy) for coverage + precision.
3. **Validate** — test against family samples (TP) and a large benign corpus (FP);
   tune.
4. **Document & ship** — metadata (family/ref), then deploy (file/memory/feed
   scanning).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = catches family variants with
minimal FP; record TP/FP results.

## Impact / output
Scalable family detection from analysis (feeds detection-engineering, hunting).

## Pitfalls
- Over-fitting one sample (misses variants) vs over-broad strings (FPs).
- Volatile features (paths/timestamps) = brittle rules.

## Governance
- Version signatures; review against new variants; retire stale ones.

## References
- `_shared/` rules (evidence).
