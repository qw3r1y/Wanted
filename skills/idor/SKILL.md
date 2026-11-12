---
name: idor
description: >
  Use when testing an authorized web/API target for IDOR / broken object-level
  authorization — any request that references an object by id, hash, or path and
  may serve another user's data. Covers reference discovery, horizontal/vertical
  access testing, predictable/indirect identifiers, chained and API IDOR, impact
  and remediation. Do NOT use for missing-function-level authz only (that is
  BFLA — related but distinct).
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, burp-repeater]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
  - references/reference-patterns.md
license: MIT
version: 1.0.0
---

# IDOR — Insecure Direct Object Reference (authorized testing)

Find requests that fetch or act on an object by a reference the server trusts
without checking **who is asking**. The proof is accessing *another principal's*
object with *your* session — minimally, with explicit two-identity comparison.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Access the
> **least** data needed to prove the break; never bulk-enumerate real users'
> records (`safe-execution-rules.md`).

## When to use
Any request carrying an object reference: numeric ids, UUID/GUIDs, slugs, hashes,
filenames, path segments, or references nested in JSON/GraphQL. **High-value
surfaces:** account/profile/order/invoice/document endpoints, "export/download"
features, team/tenant-scoped resources, admin-object endpoints, and API routes
like `/api/users/{id}` or `/api/orders/{id}`.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`).
- **Two controlled identities** (low-priv A, and B/high-priv) — the core of a
  clean IDOR proof. A single identity gives weaker evidence.
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)

### Phase 1 — Reference discovery
Catalogue every object reference the app uses and its format: sequential int,
UUID, hash, composite, or path. Note which are in the URL, body, headers, or
GraphQL variables. Predictable/sequential references and "hidden" client-side
references (not shown in UI but accepted by the API) are prime candidates.

### Phase 2 — Two-identity differential (core gate)
With identity A, capture a request for A's object. **Replay the same request
substituting B's reference while keeping A's session.** Compare:
- A's session returns **B's data / performs action on B's object** → IDOR.
- Returns 403/404/empty for B's object → authorization enforced (**refuted** for
  that endpoint).
Do the inverse (B→A) and test both **read** and **write/state-changing** variants
(the latter only with per-action approval).

### Phase 3 — Reference-type nuances
- **Sequential ids:** test id±1, boundaries, and other users' ranges (bounded).
- **UUID/GUID:** not automatically safe — check for leakage (in other responses,
  emails, logs), predictable/v1 time-based UUIDs, or indirect lookup that accepts
  a guessed value.
- **Indirect refs (hash/encoded):** decode/derive; many are reversible or
  enumerable; test whether the server maps them per-user or globally.
- **Chained IDOR:** one object's response leaks another's reference → pivot.
- **API/GraphQL IDOR:** object-level authz often missing on API routes even when
  the UI enforces it; test batched queries and nested object access.

### Phase 4 — Vertical vs horizontal
- **Horizontal:** access a same-privilege peer's object (A reads B).
- **Vertical:** access a higher-privilege object/action (user reaches admin
  object) — higher severity.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the two-identity proof
(request/response pair for A-session-reading-B), reference type, read vs write,
and horizontal/vertical. A guessable id alone is **inconclusive** until a
cross-identity access is shown.

## Impact escalation
Unauthorized read of other users' PII/financial/medical data, account takeover
(password/email change on another id), cross-tenant data exposure, and
admin-object manipulation. Severity scales with data sensitivity and write
capability. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Accessing **your own** object with a different reference form → not IDOR.
- 403/404 for other ids → authorization working; do not report.
- Rate-limited/soft responses can mimic access — confirm the body actually
  contains B's data.
- Keep enumeration minimal and bounded; never harvest real users' records at scale.

## Remediation
- Enforce **object-level authorization on every request**, server-side: check
  that the authenticated principal owns/may access the referenced object — do not
  trust client-supplied references.
- Prefer **indirect, per-session reference maps** or scoped queries
  (`WHERE owner_id = current_user`) over exposing global ids.
- Centralize authorization (policy/middleware) so API and UI share the same
  checks; add authz tests to CI. UUIDs are not an access-control substitute.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
- `references/reference-patterns.md` — id formats, enumeration bounds, chained/API variants (4th level).
