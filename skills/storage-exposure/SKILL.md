---
name: storage-exposure
description: >
  Use when assessing authorized cloud object storage (S3/Blob/GCS) for exposure —
  public access, over-broad policies, and sensitive-data exposure — to find and
  remediate data-leak risk. Covers storage-exposure assessment.
type: knowledge
domain: cloud-infra/cloud
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Cloud Storage Exposure Assessment

Public cloud storage is one of the most common breach causes. Assess authorized
buckets/containers for public or over-broad access, and whether exposed storage
holds sensitive data — confirming exposure minimally (listing/one benign object),
never bulk-exfiltrating.

> Authorized testing only; read the **minimum** to confirm exposure
> (`_shared/safe-execution-rules.md`).

## Procedure (gated phases)
1. **Enumerate** — buckets/containers and their access config (ACLs, policies,
   public-access settings).
2. **Classify exposure (first gate)** — public-list, public-read, or over-broad
   cross-account/anonymous access.
3. **Assess sensitivity (bounded)** — if exposed, confirm whether sensitive data is
   present via a minimal listing/one benign object; no bulk download.
4. **Prioritize** — by public-ness × data sensitivity.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, exposure level, and (if
sensitive) minimal proof. Private/denied → not exposed.

## Impact / output
Prioritized storage-exposure findings + remediation.

## Pitfalls
- Intentionally-public assets (static sites) — distinguish.
- Never bulk-exfiltrate to "prove" exposure.

## Remediation
- Block public access by default; least-privilege bucket policies; encryption;
  access logging; continuous exposure monitoring (easm/cspm).

## References
- `_shared/` rules (authorization, safe execution, evidence).
