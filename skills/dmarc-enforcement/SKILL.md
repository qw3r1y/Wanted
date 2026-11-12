---
name: dmarc-enforcement
description: >
  Use when driving DMARC to enforcement — moving a domain from monitoring (p=none)
  to quarantine/reject without breaking legitimate mail, using reports and alignment
  fixes. Covers the DMARC enforcement journey (deepens data-privacy/email-auth).
type: knowledge
domain: email-security
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# DMARC Enforcement

Publishing DMARC at `p=none` provides visibility but **no protection** — spoofing
still works. Drive the domain to enforcement (`quarantine` → `reject`) by using DMARC
reports to find and fix all legitimate senders' SPF/DKIM alignment first, so
enforcement blocks spoofing without dropping real mail.

## When to use
When a domain has DMARC at `p=none` (the common stuck state) and needs real
anti-spoofing protection.

## Procedure (gated phases)
1. **Collect reports** — ingest DMARC aggregate reports to inventory all senders
   (including shadow/third-party) using the domain.
2. **Fix alignment** — ensure every legitimate sender passes SPF and/or DKIM aligned
   to the domain (data-privacy/email-authentication).
3. **Ramp enforcement (core)** — move to `p=quarantine` (with percentage ramp), then
   `p=reject`, watching reports for legitimate-mail impact.
4. **Maintain** — monitor reports for new senders; keep alignment current.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = `p=reject` (or quarantine) with
legitimate mail passing; spoofing of the domain is rejected.

## Quality bar / pitfalls
- Enforcing before fixing alignment → dropping legitimate mail.
- Staying at `p=none` indefinitely (no protection).

## Linkage
- Builds on data-privacy/email-authentication; feeds bec-defense + brand protection.

## References
- `_shared/` rules (evidence).
