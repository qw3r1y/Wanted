---
name: saml-attacks
description: >
  Use when testing an authorized SAML SSO implementation — signature wrapping
  (XSW), signature stripping/exclusion, comment injection, and assertion tampering
  that bypass authentication or impersonate users. Covers assertion analysis,
  controlled proof and remediation.
type: knowledge
domain: offensive/auth-identity
maturity: canonical
tools: [curl, saml-tooling]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# SAML Attacks (authorized testing)

Test a SAML relying party for assertion-integrity failures: XML Signature
Wrapping (XSW), signature stripping/exclusion, comment injection in NameID, and
unsigned-assertion acceptance — any of which lets an attacker forge the asserted
identity. The proof is the SP accepting a tampered assertion as a different user,
on a test identity.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Test identities
> only.

## When to use
SAML-based SSO logins (SP side) within scope; enterprise app sign-in flows.

## Prerequisites
- Authorization + scope; a captured valid SAML response for a test user.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Analyze the assertion** — what is signed (response vs assertion), the NameID,
   attributes, and how the SP validates the signature.
2. **Integrity tests (core gate)**:
   - *Signature stripping/exclusion:* remove the signature — is the assertion still
     accepted?
   - *XSW:* add a second (attacker) assertion/element so the signature validates an
     original element while the SP consumes the injected one.
   - *Comment injection:* insert XML comments in NameID to confuse parsing into a
     different user (`admin<!---->@` style canonicalization issues).
   - *Unsigned/weak:* does the SP accept unsigned or weakly-validated assertions?
3. **Confirm impersonation** — the SP authenticates you as a **different test
   identity** from the tampered assertion.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the technique, the
tampered assertion, and the impersonation proof. Strict signature validation →
**refuted**.

## Impact escalation
Authentication bypass and arbitrary-user impersonation (including admins) across
the SSO-integrated app. Critical. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- SP validates the full signature and rejects tampering → **refuted**.
- An error ≠ bypass; require accepted impersonation.
- Use only test identities.

## Remediation
- Validate signatures correctly (sign + verify the **assertion**, reject unsigned/
  multiple assertions); use a hardened, patched SAML library; canonicalize safely
  (resist comment-injection); pin the IdP certificate; enforce audience/recipient/
  expiry.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
