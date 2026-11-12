# Sigma Kural Yapısı — Referans (4. seviye)

Sigma = platform-bağımsız tespit kuralı formatı; backend'e (Splunk/Elastic/Sentinel)
çevrilir.

## Temel alanlar
| Alan | Amaç |
|---|---|
| `title` | Kısa, net davranış adı |
| `id` | Benzersiz UUID |
| `status` | experimental / test / stable |
| `logsource` | `category`/`product`/`service` — hangi telemetri |
| `detection` | `selection*` + `filter*` + `condition` |
| `falsepositives` | Bilinen benign tetikleyiciler |
| `level` | low/medium/high/critical |
| `tags` | ATT&CK (`attack.tXXXX`), vb. |

## condition kalıpları
- `selection and not filter` (benign hariç tut)
- `selection1 or selection2`
- `all of selection_*` / `1 of selection_*`
- sayısal: `| count() by Field > N` (korelasyon/eşik)

## Kalite kuralları
- Davranış > kırılgan IOC string'i.
- Doğru `logsource` (telemetri yoksa kural sessizce ölü).
- FP'leri `falsepositives`'te belgele; over-broad seçimden kaçın.
- ATT&CK tag'i + severity zorunlu (coverage mapping için).

## Test
Known-malicious (TP) + known-benign (FP) veriye karşı; FP oranını deploy öncesi ölç;
audit modda stage'le.
