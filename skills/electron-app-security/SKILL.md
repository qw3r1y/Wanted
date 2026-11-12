---
name: electron-app-security
description: >
  Use when auditing an Electron (or similar webview-based) desktop app — nodeIntegration/
  contextIsolation settings, remote content, IPC exposure, and the web-to-native
  bridge that can turn XSS into RCE. Covers Electron security review.
type: knowledge
domain: endpoint-app-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Electron App Security

Electron apps combine web and native: a web vulnerability (XSS) can become **remote
code execution** on the user's machine if the app's security settings are weak. Audit
the Electron security configuration, remote-content handling, and IPC bridge.

> Authorized review (`_shared/scope-authorization-rule.md`).

## When to use
Auditing an Electron/webview-based desktop app you build or vet.

## Procedure (gated phases)
1. **Security settings (core)** — `contextIsolation` on, `nodeIntegration` off,
   `sandbox` on, and safe `webPreferences`; disabling these lets XSS reach Node → RCE.
2. **Remote content** — does the app load untrusted/remote content into privileged
   windows? Restrict navigation; validate.
3. **IPC bridge** — the exposed `preload`/IPC API should be minimal and validated;
   the renderer must not get arbitrary native capability.
4. **XSS→RCE path** — assess whether an XSS in the renderer could reach native code
   given the settings.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record misconfigurations + the XSS→RCE exposure.

## Impact escalation
Renderer XSS → native RCE on the user's machine. Critical. CVSS per
`_shared/cvss-reference.md`.

## Remediation
- `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`; minimal
  validated preload/IPC; restrict navigation + remote content; CSP; keep Electron
  patched.

## References
- `_shared/` rules (authorization, evidence).
