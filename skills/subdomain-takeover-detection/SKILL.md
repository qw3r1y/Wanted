---
name: subdomain-takeover-detection
description: >
  Use when detecting subdomain-takeover exposure across the external surface —
  dangling DNS records pointing to unclaimed third-party services that an attacker
  could claim. Covers detection and safe confirmation.
type: knowledge
domain: easm
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Subdomain Takeover Detection (EASM)

A subdomain whose DNS points to a third-party service that no longer exists (a
dangling CNAME to an unclaimed cloud/SaaS resource) can be **claimed by an attacker**
to serve content from your domain. Detect these across the surface and confirm
safely without actually hijacking.

> Authorized; confirm takeover potential **without** claiming the resource
> (`_shared/safe-execution-rules.md`).

## When to use
Continuously across the subdomain inventory (feeds from continuous-discovery).

## Procedure (gated phases)
1. **Enumerate DNS records** — CNAMEs/aliases pointing to third-party services
   (cloud storage, SaaS, PaaS, CDNs).
2. **Detect dangling (core)** — the target service returns a "not found/unclaimed"
   fingerprint indicating the resource is free to claim.
3. **Confirm safely** — verify the takeover fingerprint **without claiming** the
   resource (claiming = taking over; don't). Note the specific service + evidence.
4. **Prioritize** — by the subdomain's trust/exposure (auth subdomains > marketing).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the dangling record + takeover
fingerprint. Active/claimed target → **refuted**.

## Impact escalation
Phishing/content from a trusted subdomain, cookie/session theft (same-site), and
brand abuse. CVSS per `_shared/cvss-reference.md`.

## Remediation
- Remove dangling DNS records promptly; decommission DNS before the backing resource;
  monitor continuously; claim/retain critical third-party resources.

## References
- `_shared/` rules (authorization, safe execution, evidence).
