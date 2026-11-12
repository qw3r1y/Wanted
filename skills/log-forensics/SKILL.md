---
name: log-forensics
description: >
  Use when reconstructing an incident from logs — Windows event logs, auth logs,
  web/proxy/DNS logs, and application logs — correlating across sources to trace
  attacker actions. Covers log-based analysis and Sigma-to-hunt pivoting.
type: knowledge
domain: defensive/dfir
maturity: canonical
tools: [chainsaw, hayabusa]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Log Forensics

Reconstruct attacker activity from logs when host images aren't available or to
corroborate them — authentication, process/event logs, web/proxy/DNS, and app logs
— correlated across sources into a coherent account of what happened.

## When to use
During IR, especially for lateral movement, authentication abuse, and
network-visible activity.

## Procedure (gated phases)
1. **Identify relevant logs** — the sources that would record the suspected
   activity (auth for logon abuse, DNS/proxy for C2, event logs for execution).
2. **Apply detections/queries** — run Sigma/analytics (e.g., Chainsaw/Hayabusa on
   EVTX) to surface suspicious events fast.
3. **Correlate** — pivot across sources (a logon + a process + a connection) to
   build the sequence; anchor to timeline-analysis.
4. **Conclude with evidence** — the attacker action narrative with log citations.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each conclusion cites the log events;
account for log tampering/gaps.

## Impact / output
Reconstructed activity + IOCs from logs; feeds timeline, scoping, detections.

## Pitfalls
- Log gaps/tampering/retention — note limitations; corroborate.
- Timezone normalization across sources.

## Remediation / IR linkage
- Improve logging coverage/retention; convert findings to detections.

## References
- `_shared/` rules (untrusted input, evidence).
