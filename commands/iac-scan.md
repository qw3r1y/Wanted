---
description: "Scan IaC for security misconfigurations pre-deploy; prioritize real exposure."
argument-hint: "<path>"
---
# /iac-scan
Runs terraform-security-scan: scan IaC → prioritize exposure (public/unencrypted/
over-broad IAM) → gate CI on real misconfigurations. Policy via checkov/opa.
