---
name: bec-defense
description: >
  Use when defending against Business Email Compromise — the technical + process
  controls against invoice fraud, CEO fraud, and vendor impersonation that bypass
  malware detection. Covers BEC-specific defenses.
type: knowledge
domain: email-security
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Business Email Compromise (BEC) Defense

BEC is pure social engineering — no malware — so it evades technical filters and
causes huge financial loss (wire/invoice fraud, CEO impersonation, vendor account
changes). Defend with layered email authentication, lookalike-domain and anomaly
detection, and — critically — **process controls** for financial actions.

## When to use
To reduce BEC/invoice-fraud risk (a top financial-loss threat).

## Procedure (gated phases)
1. **Email authentication** — DMARC enforcement (stops exact-domain spoofing);
   detect lookalike/cousin domains and display-name impersonation.
2. **Detection** — flag external mail impersonating executives/vendors, unusual
   financial requests, and reply-to mismatches; auto-banner external mail.
3. **Process controls (core)** — out-of-band verification for payment/bank-detail
   changes; dual approval for wires; no payment changes on email alone.
4. **Awareness** — train finance/execs on BEC patterns (social-engineering).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = technical + process controls make a
single spoofed email insufficient to cause payment.

## Quality bar / pitfalls
- Relying on technical filters alone — BEC has no malware; process controls are key.
- No out-of-band verification for payment changes (the core failure).

## Linkage
- Builds on dmarc-enforcement + phishing-detection + awareness-training.

## References
- `_shared/` rules (evidence).
