---
name: http-request-smuggling
description: >
  Use when testing an authorized target behind a proxy/CDN chain for HTTP request
  smuggling — desync between front-end and back-end parsing of request boundaries
  (CL.TE / TE.CL / TE.TE / H2 downgrade). Covers safe differential detection,
  impact assessment and remediation. High blast-radius — test with extreme care.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, http-toolkit]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# HTTP Request Smuggling (authorized testing)

Find a parsing **desync** between a front-end (proxy/CDN/LB) and back-end over how
a request's length/boundaries are interpreted, letting one request's bytes be
treated as the start of another. Impact can hit *other users*, so detection must
be careful and non-disruptive.

> Authorized testing only, with heightened caution: smuggling can affect other
> users and cache integrity. Prefer **timing-based differential** detection; stop
> at the first sign of cross-user impact and report (`safe-execution-rules.md`).

## When to use
Targets behind a proxy/CDN/load-balancer chain (most production web apps).
Especially where HTTP/1.1 is spoken to the back-end, or HTTP/2 is downgraded.

## Prerequisites
- Authorization + **explicit approval for desync testing**; scope recorded.
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Map the chain** — identify front-end/back-end servers and HTTP versions;
   note how each handles `Content-Length` vs `Transfer-Encoding`.
2. **Safe differential detection (first gate)** — use **timing-based** probes that
   reveal a CL/TE discrepancy by delaying only *your own* connection (no payload
   that would poison another user's request). A reproducible self-timing delta is
   the signal.
3. **Classify** — CL.TE / TE.CL / TE.TE / H2-downgrade, based on which end honors
   which header.
4. **Impact assessment (bounded)** — reason about and, only with explicit
   approval and on a test surface, minimally demonstrate consequence (e.g., your
   own subsequent request affected) without touching other users.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, desync class, the timing
differential proof, and the server chain. Never claim based on theory; require a
reproducible differential confined to your own traffic.

## Impact escalation
Request routing/credential capture, cache poisoning, security-control bypass
(auth/WAF), and response queue poisoning. Describe impact; do **not** execute
cross-user exploitation on production. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Normal latency/keep-alive behaviour mistaken for desync → require repeatable,
  attributable differential.
- Any technique that would poison another user's request is **out of bounds**
  without explicit, isolated test authorization.

## Remediation
- Use HTTP/2 end-to-end or normalize/close ambiguous messages; **reject** requests
  with both `Content-Length` and `Transfer-Encoding`.
- Ensure front-end and back-end agree on parsing; disable back-end connection
  reuse where ambiguity exists; keep proxy/CDN software patched.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
