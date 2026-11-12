---
name: css-injection
description: >
  Use when testing an authorized web target for CSS injection — attacker-
  controlled CSS (or style context) enabling data exfiltration via attribute
  selectors, UI redressing, or clickjacking assists, even under strict script
  CSP. Covers detection, exfil-technique assessment and remediation.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, browser]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# CSS Injection (authorized testing)

Find places where input is injected into a style context (inline `style`, a
`<style>` block, or an attacker-controllable stylesheet) and assess impact — CSS
can exfiltrate secrets (e.g., hidden token values) via attribute-selector +
resource-loading tricks, and assist UI redressing, often **even when script XSS
is blocked by CSP**.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
Rich-text/themes, user-controllable style attributes, markdown that allows style,
and reflected input landing inside `style`/`<style>`. Especially relevant on
targets with strict script CSP but lax style handling.

## Prerequisites
- Authorization + scope; OOB/resource listener to observe CSS-driven requests.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Confirm style-context injection (first gate)** — input reaches a style
   context unescaped (not HTML-encoded). Pure HTML-encoding → **refuted**.
2. **Assess technique reach** — can you use attribute selectors + background/font
   resource loads to leak the presence/value of a sensitive attribute (e.g., a
   CSRF token) to your host? Can you overlay/hide elements (redressing)?
3. **Controlled proof** — leak a **benign** marker attribute to your OOB host, or
   demonstrate an overlay — enough to prove the class without stealing real
   secrets.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the style sink, the
technique, and the OOB/visual proof. Encoded reflection → **refuted**.

## Impact escalation
Secret/token exfiltration (CSP-resistant), UI redressing/clickjacking assist, and
content spoofing. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Style value properly encoded/sanitized → **refuted**.
- Injection with no sensitive attribute to leak and no overlay impact →
  informational.

## Remediation
- Do not reflect untrusted input into style contexts; sanitize/strip `style` and
  `<style>` from user content; use a CSS allow-list in rich text.
- Strong CSP (restrict `style-src`, `img-src`, `font-src`) limits exfil channels;
  avoid putting secrets in DOM attributes.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
