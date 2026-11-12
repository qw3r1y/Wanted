---
description: "Run authorized end-to-end reconnaissance and produce a prioritized attack-surface inventory."
argument-hint: "<target>"
---
# /recon
Confirms scope, then runs passive-recon → subdomain-enumeration → content-discovery →
port-service-scan, outputting a prioritized in-scope surface to OUTPUT_DIR.
Authorized + in-scope only.
