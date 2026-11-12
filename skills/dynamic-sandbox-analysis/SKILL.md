---
name: dynamic-sandbox-analysis
description: >
  Use when analyzing malware behaviour by detonating it in an isolated sandbox —
  observing file/registry/process/network activity to characterize behaviour and
  extract runtime IOCs. Controlled, isolated execution only.
type: knowledge
domain: malware-re
maturity: canonical
tools: [cuckoo]
references:
  - _shared/untrusted-input-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Dynamic Sandbox Analysis

Observe what a sample *does* by running it in an isolated, instrumented sandbox —
process/file/registry changes, network/C2 traffic, injection, and persistence — to
characterize behaviour and extract runtime IOCs that static analysis may miss.

> Detonation happens ONLY in a properly isolated sandbox/VM with controlled
> networking; never on a production or networked host
> (`_shared/safe-execution-rules.md`).

## When to use
To quickly characterize behaviour, or to complement static analysis (especially for
packed samples).

## Procedure (gated phases)
1. **Prepare isolation** — a sandbox with monitoring + controlled/simulated network
   (to safely observe C2 without real harm).
2. **Detonate & observe** — run the sample; capture process/file/registry/network/
   API behaviour and persistence.
3. **Handle evasion** — note sandbox-evasion/anti-analysis; adjust environment
   (timing, artifacts) if the sample detects the sandbox.
4. **Extract IOCs** — C2 domains/IPs, dropped files/hashes, mutexes, registry keys,
   for hunting/detection.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record observed behaviour + runtime IOCs;
note evasion limits.

## Impact / output
Behavioural profile + runtime IOCs (feeds hunting, detection, CTI).

## Pitfalls
- Sandbox evasion (sample behaves benignly) — use realistic environments.
- Real network egress — always control/simulate networking.

## Remediation / linkage
- Feed IOCs/behaviour to detection-engineering and threat-hunting.

## References
- `_shared/` rules (untrusted input, safe execution, evidence).
