# Ortak Referans: MITRE ATT&CK

> Defensive/offensive skill'leri için ortak ATT&CK dili.

## Taktikler (Enterprise, sıra)
Reconnaissance · Resource Development · Initial Access · Execution · Persistence ·
Privilege Escalation · Defense Evasion · Credential Access · Discovery · Lateral
Movement · Collection · Command and Control · Exfiltration · Impact

## Kullanım ilkesi
- **Davranışı** (technique) eşle, araç/IOC'yi değil (bkz. cti/mitre-attack-mapping).
- Belirsiz davranışı over-mapping yapma; düşük güvenli eşlemeyi işaretle.
- Her detection/hunt bir technique'e bağlanır (detection-coverage-mapping).

## Offensive ↔ ATT&CK (örnek)
- recon-osint → Reconnaissance/Resource Dev · post-exploitation/privesc → Privilege Escalation
- active-directory/* → Credential Access + Lateral Movement · c2-redteam → C2/Defense Evasion
- social-engineering/phishing → Initial Access

## Defensive kullanım
- detection-coverage-mapping: tespitleri technique'lere eşle, boşluk bul.
- adversary-emulation: tehdit profilinin TTP'lerini ATT&CK ile planla, detect/prevent/
  respond skorla.
- threat-hunting/mitre-attack-coverage: hunt önceliğini relevance × coverage ile belirle.

## MITRE D3FEND
Savunma karşı-önlemlerini eşlemek için D3FEND kullanılabilir (detection/hardening/
isolation/deception) — defensive skill'lerde remediation eşlemesi.
