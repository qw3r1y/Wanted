---
name: federation-sso-security
description: >
  Use when securing federation/SSO (SAML, OIDC, OAuth) at the identity layer —
  trust configuration, token/assertion validation, and the attacks against federated
  identity (golden SAML, token theft, IdP compromise). Covers SSO/federation
  hardening.
type: knowledge
domain: identity-iam
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Federation / SSO Security

SSO centralizes authentication — and risk: a compromised IdP or forged assertion can
unlock everything. Secure the federation trust configuration, token/assertion
validation, and signing-key protection, and understand the attacks (golden SAML,
token theft, IdP compromise) to defend against them.

## When to use
Securing SAML/OIDC/OAuth federation and the IdP.

## Procedure (gated phases)
1. **Trust configuration** — exact entity/audience/redirect validation; correct
   signing-cert trust; no overly broad trust.
2. **Token/assertion validation** — enforce signature, audience, expiry, and
   anti-replay at relying parties (ties to api/oauth-oidc + auth-identity/saml).
3. **Signing-key protection (core)** — protect IdP token-signing keys (golden-SAML/
   token-forgery risk); HSM, rotation, and tight access.
4. **IdP hardening & monitoring** — MFA + conditional access on the IdP; monitor for
   anomalous federation (new trusts, unusual token issuance).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Secure" = strict validation, protected
signing keys, hardened monitored IdP.

## Quality bar / pitfalls
- Exposed/weakly-protected token-signing keys (golden SAML).
- Lax audience/redirect validation enabling token misuse.

## Linkage
- Pairs with auth-identity/saml-attacks + api/oauth-oidc-abuse (offensive view);
  IdP is a top target.

## References
- `_shared/` rules (evidence).
