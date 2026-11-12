---
name: rest-abuse
description: >
  Use when testing an authorized REST API for method/verb and parameter abuse —
  unexpected HTTP methods, verb tunneling, parameter pollution, content-type
  confusion, and mismatched validation between endpoints. Covers systematic
  method/param testing and remediation.
type: knowledge
domain: offensive/api
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

# REST Method & Parameter Abuse (authorized testing)

Probe the gaps that appear when REST endpoints handle methods, content types, and
parameters inconsistently — a GET-protected resource writable via PUT, verb
tunneling, HTTP parameter pollution, or JSON-vs-form parsing differences that
bypass validation. The proof is behaviour that the intended contract should not
allow.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
After api-recon, on endpoints with state-changing capability, strict-looking
validation, or multiple accepted content types.

## Prerequisites
- Authorization + scope; test account. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Method matrix** — for each endpoint try all methods (incl. OPTIONS, PATCH,
   verb-override headers); note where authz/validation differs by method.
2. **Content-type confusion** — resend as JSON vs form vs XML; observe parsing/
   validation differences (a filter applied to one type but not another).
3. **Parameter pollution** — duplicate params, array vs scalar, nested keys; watch
   for last-wins/first-wins differences bypassing checks.
4. **Confirm the deviation** — show a request that achieves an out-of-contract
   outcome (auth/validation bypass, unexpected write).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the method/type/param
trick, and the deviant outcome. Consistent handling across methods/types →
**refuted**.

## Impact escalation
Authorization/validation bypass, unexpected state change, and injection reaching
a differently-parsed sink. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Uniform validation/authz across methods and content types → **refuted**.
- A 405/415 is correct behaviour, not a bug.

## Remediation
- Enforce authorization and validation **uniformly** across all methods and
  content types; disable unused methods/verb-override; canonicalize parameters;
  one parsing path with a strict schema.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
