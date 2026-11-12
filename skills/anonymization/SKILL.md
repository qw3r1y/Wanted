---
name: anonymization
description: >
  Use when anonymizing/pseudonymizing data for analytics, sharing, or testing —
  choosing techniques (masking, tokenization, k-anonymity, differential privacy) and
  avoiding re-identification. Covers privacy-preserving data transformation.
type: knowledge
domain: data-privacy
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Anonymization & Pseudonymization

Transform personal data so it can be used (analytics, sharing, test environments)
with reduced privacy risk — choosing the right technique for the use case and,
critically, avoiding re-identification, which naive anonymization often fails to
prevent.

## When to use
When sharing/analyzing data or populating non-production environments with
production-derived data.

## Procedure (gated phases)
1. **Define the goal & model** — use case, who sees the data, and the
   re-identification threat (linkage with other data).
2. **Choose technique** — masking/redaction, tokenization/pseudonymization
   (reversible with a key), k-anonymity/generalization, or differential privacy —
   matched to utility vs privacy needs.
3. **Assess re-identification risk (core)** — quasi-identifiers that enable linkage;
   test that the result resists re-identification for the threat model.
4. **Govern** — control any re-identification keys; document the method.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = data meets utility needs and resists
re-identification for the stated threat model.

## Quality bar / pitfalls
- "Anonymized" data that is re-identifiable via quasi-identifiers/linkage.
- Pseudonymization treated as anonymization (it's reversible) — handle keys.

## Linkage
- Consumes data-classification; supports test-data, analytics, gdpr-kvkk.

## References
- `_shared/` rules (evidence).
