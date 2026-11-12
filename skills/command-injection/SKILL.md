---
name: command-injection
description: >
  Use when testing an authorized web target for OS command injection — input that
  reaches a shell or process invocation (ping/host tools, converters, archive/
  image utilities, backup/exec features). Covers detection via in-band and blind
  out-of-band oracles, context analysis, controlled proof and remediation. Do NOT
  use for SQL/template injection (see sqli/ssti) or pure code-eval sandboxes.
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
  - references/shell-contexts.md
license: MIT
version: 1.0.0
---

# OS Command Injection (authorized testing)

Find input that breaks out of its intended place in a shell/command invocation
and runs attacker-controlled commands. The proof is a controlled, attributable
side effect (timing or OOB callback) — never destructive commands.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Prove with a
> benign, bounded command (delay / OOB ping); **no** destructive or data-
> exfiltrating commands (`safe-execution-rules.md`).

## When to use
Features that shell out: network tools (ping/traceroute/nslookup/whois),
file/format converters, image/PDF/video processing, archive handling, backup/
restore, "run"/diagnostic utilities, and anything passing input to a system
command. Also second-order: a stored value later used in a command.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`).
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.
- A unique OOB listener (DNS + HTTP) for blind confirmation.

## Procedure (gated phases)

### Phase 1 — Identify command sinks
Map parameters that plausibly reach a command. Note the apparent OS (Linux/
Windows) and whether output is returned (in-band) or not (blind).

### Phase 2 — Oracle selection (first gate)
Choose a **non-destructive** oracle:
| Oracle | When | Benign proof |
|---|---|---|
| In-band output | Command output is reflected | A harmless command's output appears (e.g., current dir/user) |
| **Time-blind** | No output | A controlled, repeatable delay (bounded sleep) — confirm 2–3x, rule out latency |
| **OOB** | Fully blind | The server resolves/requests your unique host (DNS/HTTP callback) |

Use separators/context break-out appropriate to the shell context
(`references/shell-contexts.md`) — the correct break-out depends on how input is
embedded (quoted, unquoted, as an argument).

### Phase 3 — Context & reach
Determine the shell/OS and privilege context from benign probes. Classify reach
(argument injection vs full command) — enough to scope severity, not to exploit.

### Phase 4 — Controlled proof
Demonstrate the **minimum**: a bounded delay or an OOB callback carrying a unique
token. Do not read sensitive files, modify state, or establish any persistence.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, oracle (in-band/time/
OOB), the attributable proof (timing log / OOB callback), and reproduction.
Non-repeatable timing or a reflected string without a side effect →
**inconclusive**.

## Impact escalation
Remote code execution, server compromise, lateral movement, and data access —
stated as the proven capability and its scope. This is typically critical. CVSS
per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Delay that matches overall latency / rate-limiting → not time-blind injection.
- Error text containing your input ≠ execution; require a side effect.
- Argument-only injection (no command separator reachable) may be lower impact —
  characterize precisely.
- Never run destructive, persistence, or exfiltration commands.

## Remediation
- **Avoid the shell:** use parameterized process APIs (`execve`-style arg arrays),
  never string-concatenated shell commands.
- Strict **allow-list** of permitted values; reject shell metacharacters; validate
  types; prefer native libraries over external command tools.
- Run the component least-privileged and sandboxed; log and alert on anomalous
  command patterns.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
- `references/shell-contexts.md` — shell context break-out, OS differences, blind oracles (4th level).
