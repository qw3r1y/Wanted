---
name: email-gateway-tuning
description: >
  Use when configuring/tuning a secure email gateway — anti-phishing/malware
  policies, URL/attachment handling, authentication enforcement, and balancing
  protection with delivery. Covers email gateway hardening.
type: knowledge
domain: email-security
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Email Gateway Tuning

The email gateway is the primary filter against the #1 attack vector. Tune it to
catch phishing/malware/BEC effectively — URL rewriting/detonation, attachment
sandboxing, authentication enforcement, and impersonation detection — while
minimizing false positives that make users whitelist or bypass controls.

## When to use
When deploying/hardening a secure email gateway.

## Procedure (gated phases)
1. **Authentication enforcement** — honor/enforce SPF/DKIM/DMARC on inbound; reject/
   quarantine failures per policy.
2. **Content protection** — URL rewriting + time-of-click detonation; attachment
   sandboxing; macro/active-content handling.
3. **Impersonation/anomaly** — lookalike-domain and display-name impersonation
   detection; external-sender banners (BEC).
4. **Tune** — reduce false positives; provide user reporting + quarantine review;
   measure catch vs FP rate.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = high catch rate with low FPs, enforced
authentication, and detonation/sandboxing active.

## Quality bar / pitfalls
- Over-blocking → users bypass/whitelist; under-blocking → phishing lands.
- Not enforcing inbound DMARC.

## Linkage
- Pairs with dmarc-enforcement, bec-defense, phishing-detection; the technical front
  line.

## References
- `_shared/` rules (evidence).
