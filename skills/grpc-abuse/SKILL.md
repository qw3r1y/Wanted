---
name: grpc-abuse
description: >
  Use when testing an authorized gRPC/Protobuf API — reflection exposure, method
  enumeration, authorization gaps per-method, and message tampering. Covers
  service discovery, abuse testing and remediation.
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl, grpcurl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# gRPC / Protobuf Abuse (authorized testing)

Discover and test gRPC services for the same authorization and input-handling
flaws as REST/GraphQL, plus gRPC-specific exposure (server reflection enabling
method enumeration). The proof is calling a method you should not, or tampering a
message to an out-of-contract effect.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
APIs speaking gRPC (HTTP/2 + protobuf), gateways exposing gRPC, and
gRPC-web endpoints.

## Prerequisites
- Authorization + scope; a gRPC client (e.g., grpcurl) and the proto (from
  reflection or provided). `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Service discovery** — if server reflection is enabled, enumerate services/
   methods/messages; else use provided protos. Record the method inventory.
2. **Per-method authz (core gate)** — call privileged/admin methods with a
   lower-privilege or no credential; gRPC authz is often inconsistent per method.
3. **Message tampering** — modify fields (ids, roles, flags) to test object/
   function-level authz and mass-assignment-style binding.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the method, the identity,
and the unauthorized call/effect. Proper per-method authz → **refuted**.

## Impact escalation
Unauthorized method invocation, data access, privilege escalation. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Reflection disabled but methods guessable — still test authz on known methods.
- A method returning an error is not a bug.

## Remediation
- Disable server reflection in production; enforce per-method authorization and
  input validation; treat protobuf fields with the same allow-list discipline as
  REST bodies.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
