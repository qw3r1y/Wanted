---
description: "Test XML intake (incl. SVG/Office/SAML) for XXE; OOB mandatory for blind."
argument-hint: "<target>"
---
# /hunt-xxe
Runs the xxe skill: identify XML intake → in-band vs blind (OOB) → reach (file-read/
SSRF) → minimal proof. Authorized; no bulk file exfil; no entity-expansion DoS.
