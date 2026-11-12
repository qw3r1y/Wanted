---
name: pii-discovery
description: >
  Use when discovering and mapping personal/sensitive data across an environment —
  databases, files, logs, and services — to know what PII exists and where, as the
  basis for privacy and data-protection controls. Covers data discovery.
type: knowledge
domain: data-privacy
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# PII / Sensitive Data Discovery

You can't protect what you don't know you have. Discover and map where personal and
sensitive data lives — databases, object storage, files, logs, backups, and
third-party services — with classification, as the foundation for DLP, access
control, retention, and regulatory compliance.

> Authorized discovery within scope (`_shared/scope-authorization-rule.md`).

## When to use
At the start of a privacy/data-protection program and continuously as data spreads.

## Procedure (gated phases)
1. **Scope data stores** — databases, storage, file shares, logs, backups, SaaS.
2. **Scan & match** — identify PII/sensitive data via patterns + context (names,
   IDs, financial/health data); include unstructured + logs (often overlooked).
3. **Classify & map** — tag by sensitivity; record where each category lives and
   flows (data map).
4. **Flag exposure** — sensitive data in logs, unencrypted stores, or over-broad
   access.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a data map (what/where/
sensitivity) + exposure findings.

## Impact / output
The foundation for DLP, access control, retention, and compliance (gdpr-kvkk).

## Pitfalls
- Structured-only scanning (missing logs/files/backups).
- Pattern matching without context → FPs; validate.

## Remediation / linkage
- Feeds data-classification, dlp-policy, retention, and access review.

## References
- `_shared/` rules (authorization, evidence).
