---
name: email-authentication
description: >
  Use when configuring/auditing email authentication — SPF, DKIM, and DMARC — to
  prevent domain spoofing and improve deliverability. Covers email-auth setup and
  enforcement (pairs with email-security domain).
type: knowledge
domain: data-privacy
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Email Authentication (SPF/DKIM/DMARC)

Prevent attackers from spoofing your domain in phishing by correctly configuring and
**enforcing** SPF, DKIM, and DMARC. Many domains publish these but leave DMARC in
monitor-only (`p=none`), providing no actual protection.

## When to use
When securing a domain against spoofing / improving email trust.

## Procedure (gated phases)
1. **SPF** — publish an accurate SPF record listing authorized senders; avoid overly
   permissive (`+all`) or too many lookups.
2. **DKIM** — sign outbound mail with DKIM; rotate keys; ensure all legitimate
   senders sign.
3. **DMARC (core)** — publish DMARC; move from `p=none` (monitor) to **enforcement**
   (`quarantine`/`reject`) after verifying legitimate mail passes; collect reports.
4. **Audit** — verify alignment and that enforcement is actually on.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = SPF+DKIM aligned and DMARC at
enforcement; spoofing of the domain is rejected.

## Quality bar / pitfalls
- DMARC stuck at `p=none` (no protection) — the most common gap.
- Breaking legitimate mail by enforcing before verifying alignment — use reports
  first.

## Linkage
- Feeds email-security (bec-defense, phishing-infra); reduces brand-impersonation.

## References
- `_shared/` rules (evidence).
