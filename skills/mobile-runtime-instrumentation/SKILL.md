---
name: mobile-runtime-instrumentation
description: >
  Use when dynamically testing an authorized mobile app with runtime
  instrumentation (Frida/Objection) — bypassing client-side controls (root/
  jailbreak/pinning detection), hooking methods, and observing data at runtime, to
  reach and test the real logic/backend. Covers method hooking and control-bypass
  assessment.
type: knowledge
domain: offensive/mobile
maturity: canonical
tools: [frida, objection]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Mobile Runtime Instrumentation (authorized)

Use dynamic instrumentation to see and manipulate an app's behaviour at runtime —
primarily to **bypass client-side-only controls** (so you can test the server/
logic that really matters) and to observe sensitive data handling. The point is
to demonstrate that client-side checks are not a security boundary.

> Authorized testing only, on a test device/build you control
> (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope; a test device with instrumentation; the app installed.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Attach & map** — instrument the app; enumerate classes/methods of interest
   (auth, crypto, storage, network).
2. **Control-bypass (core)** — hook and neutralize client-side-only controls
   (root/jailbreak detection, cert pinning) to reach the backend — demonstrating
   they are bypassable (not a server boundary).
3. **Observe & manipulate** — hook methods to observe sensitive data and tamper
   inputs/return values; confirm whether the server re-validates.
4. **Pivot to backend** — with pinning bypassed, test the API with the mobile
   client's traffic (feeds api/* skills).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the bypassed control, and
the runtime proof. If server re-validates everything, client bypass is **low** by
itself.

## Impact escalation
Client-control bypass enabling backend testing; exposure of runtime secrets; logic
tampering where the server trusts the client. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Bypassing a client check is only impactful if the **server** doesn't enforce the
  same rule — always verify server-side.
- Use only test devices/accounts.

## Remediation
- Never trust client-side controls as a security boundary; enforce auth/limits/
  validation server-side; pinning/anti-tamper are defense-in-depth only.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
