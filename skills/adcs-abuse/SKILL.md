---
name: adcs-abuse
description: >
  Use when testing an authorized AD Certificate Services deployment for the ESC
  misconfiguration classes — vulnerable templates/enrollment leading to privilege
  escalation via certificate issuance. Focused on identifying misconfigurations
  and the remediation that closes them.
type: knowledge
domain: offensive/active-directory
maturity: canonical
tools: [certipy]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
  - references/esc-classes.md
license: MIT
version: 1.0.0
---

# AD CS (ADCS) Abuse — ESC Classes (authorized)

Audit an authorized AD Certificate Services deployment for the known escalation
classes (ESC1–ESC8+) — misconfigured templates/enrollment that let a low-priv user
obtain a certificate authenticating as a privileged principal. The proof is
obtaining a certificate that escalates, on a test principal, bounded.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Demonstrate the
> escalation minimally; do not use issued certs beyond proving the path.

## Prerequisites
- Authorization + scope; a domain context; ADCS reachable (from ad-recon).
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate CAs & templates** — find published templates, their enrollment
   rights, and settings (EKU, SAN handling, manager approval).
2. **Classify ESC exposure (core gate)** — map findings to ESC classes (template
   misconfig, SAN abuse, enrollment-agent, HTTP enrollment relay, CA ACL, etc.) —
   see `references/esc-classes.md`.
3. **Demonstrate (bounded)** — for one confirmed class, request a certificate that
   authenticates as a **test** privileged principal; stop at proof of issuance.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the ESC class, the
misconfigured template/setting, and the issuance proof. Hardened templates →
**refuted**.

## Impact escalation
Domain privilege escalation / persistence via certificate-based authentication
(often to Domain Admin). Critical. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Manager-approval/hardened templates and EPA/HTTPS enrollment → **refuted**.
- Don't reuse issued certs beyond the minimal proof.

## Remediation
- Harden templates (no enrollee-supplied SAN, restricted EKUs, approval); restrict
  enrollment rights; enforce HTTPS/EPA on web enrollment; monitor certificate
  issuance; audit CA ACLs.

## References
- `_shared/` rules; `references/esc-classes.md` — ESC1–ESC8+ summary (4th level).
