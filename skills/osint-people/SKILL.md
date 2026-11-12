---
name: osint-people
description: >
  Use when building an authorized people-focused OSINT picture for a sanctioned
  engagement (e.g., phishing-simulation targeting or exposure assessment) —
  employee enumeration, email format discovery, breach-exposure lookup, and
  public-profile mapping. Privacy-bounded; authorized scope only.
type: knowledge
domain: offensive/recon-osint
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# People OSINT (authorized, privacy-bounded)

Assemble the people-side exposure of an organization for a sanctioned purpose —
employee lists, email naming conventions, and breach exposure — to support
authorized phishing simulations or exposure reporting. Handle personal data
carefully and only within scope.

> Authorized testing only, with heightened privacy care. Collect the minimum
> needed; do not compile personal profiles beyond the engagement's purpose; follow
> `_shared/scope-authorization-rule.md` and data-handling rules.

## Prerequisites
- Authorization + scope + **explicit people-OSINT purpose**. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Employee enumeration** — public professional profiles and org pages → roles/
   names in scope.
2. **Email format** — derive the organization's email naming pattern from public
   sources; validate the pattern (not individuals' inboxes).
3. **Breach exposure** — check corporate addresses against breach-exposure data to
   gauge credential-reuse risk (aggregate, for reporting).
4. **Report** — an aggregate exposure summary for awareness/phishing-sim planning;
   avoid unnecessary personal detail.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: scoped, purpose-limited
exposure summary.

## Impact escalation
Supports social-engineering simulations and awareness; highlights credential-reuse
risk.

## False positives & pitfalls
- Stale/incorrect attributions; verify before use.
- Never collect beyond the sanctioned purpose; respect privacy and local law.

## Remediation
- Reduce public personal exposure; enforce MFA + breached-password checks;
  phishing-awareness training; minimize employee data on public pages.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
