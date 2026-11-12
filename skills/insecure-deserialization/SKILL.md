---
name: insecure-deserialization
description: >
  Use when testing an authorized target that deserializes untrusted data (Java,
  .NET, PHP, Python pickle, Ruby, Node) for insecure deserialization — object
  injection leading to tampering, DoS, or gadget-chain code execution. Covers
  format detection, gadget assessment, controlled proof and remediation.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, oob-listener]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Insecure Deserialization (authorized testing)

Find places where the server deserializes attacker-influenced data and prove the
object graph can be tampered or a gadget chain reached. Because full exploitation
is often RCE, confirmation should use the **minimal** safe oracle (OOB callback),
never a destructive payload.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Prove with an
> OOB/benign gadget only; no destructive or persistence payloads
> (`safe-execution-rules.md`).

## When to use
Serialized objects in cookies, hidden fields, tokens, caches, message queues, and
APIs. Format tells: Java (`rO0`/`ac ed` bytes), .NET (`AAEAAAD`/BinaryFormatter,
ViewState), PHP (`O:`/`a:` serialize), Python pickle, Ruby Marshal, Node
(serialized JS).

## Prerequisites
- Authorization + scope; OOB listener; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Detect serialized data & format** — fingerprint from magic bytes/structure;
   identify the deserializer and whether it is attacker-reachable.
2. **Tamper probe (first gate)** — modify a field/type and observe a behavioural
   change confirming the object is deserialized and trusted (e.g., altered role/
   flag honored, or a parse differential).
3. **Gadget assessment** — determine library/version and whether known gadget
   surfaces exist; assess reach (property-oriented tampering → DoS → code
   execution) without firing destructive chains.
4. **Controlled proof** — demonstrate the minimal: an OOB callback via a benign
   gadget, or an authz/logic change — enough to establish severity.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, format, tamper/OOB proof,
and reach tier. Serialized data present but integrity-protected/typed →
**refuted/inconclusive**.

## Impact escalation
Object/authz tampering, DoS, and gadget-chain RCE. State the proven capability.
Typically high/critical. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Signed/HMAC'd serialized blobs that validate before deserialize → **refuted**.
- A tampered field ignored by the server → no trust → not exploitable.
- Never run destructive gadget chains on a live target.

## Remediation
- **Do not deserialize untrusted data**; prefer data-only formats (JSON) with
  strict schemas; never use native binary deserializers on user input.
- If unavoidable: integrity-protect (sign) serialized data, enforce type
  allow-lists, and keep libraries patched (gadget surfaces are version-specific).

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
