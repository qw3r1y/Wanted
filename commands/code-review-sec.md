---
description: "Security-review code — manual review + SAST, focused on trust boundaries and authz."
argument-hint: "<path-or-diff>"
---
# /code-review-sec
Runs code-auditor: secure-code-review (trust boundaries, authz, injection sinks, crypto,
logic) + SAST (semgrep/codeql) + variant analysis. Findings with exploit scenario + fix.
