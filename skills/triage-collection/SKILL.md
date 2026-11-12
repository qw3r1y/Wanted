---
name: triage-collection
description: >
  Use when rapidly collecting forensic triage data from hosts during IR — the
  key artifacts needed for fast analysis without full disk imaging, preserving
  evidence integrity at scale. Covers collection scope, tooling and chain of
  custody.
type: knowledge
domain: defensive/dfir
maturity: canonical
tools: [kape, velociraptor]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Forensic Triage Collection

Collect the high-value forensic artifacts from one or many hosts quickly — enough
to triage and scope an incident without waiting for full disk images — while
preserving integrity and chain of custody. Speed and scale matter in live
incidents.

## When to use
Early in IR, especially across many hosts, to rapidly determine scope.

## Procedure (gated phases)
1. **Define the collection set** — the artifacts that answer the triage questions
   (execution, persistence, logs, memory where needed), scoped to the incident.
2. **Collect at scale** — use remote/forensic collection (KAPE/Velociraptor-style)
   across target hosts; minimize footprint on evidence.
3. **Preserve integrity** — hashing + chain of custody; store centrally.
4. **Prioritize analysis** — triage collected data to find compromised hosts for
   deeper analysis (disk/memory forensics).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = required artifacts collected with
integrity, enabling triage. Record collection manifest + hashes.

## Impact / output
Rapid scope of affected hosts; inputs for deeper forensics.

## Pitfalls
- Collecting too little (missing key artifacts) or altering evidence — define the
  set and minimize footprint.
- No integrity/chain of custody → evidence disputes.

## Remediation / IR linkage
- Feeds disk/memory/timeline analysis and containment decisions.

## References
- `_shared/` rules (evidence).
