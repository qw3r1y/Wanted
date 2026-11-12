# Ortak Referans: Raporlama Şablonu

> Bulgu raporlayan skill'ler bu yapıyı izler (bkz. reporting-docs/*).

## Bulgu kaydı (finding)
```
Başlık: <kısa, ne/nerede>
Severity: <Critical/High/Medium/Low/Info> (CVSS: <vektör>)   # bkz. cvss-reference.md
Durum (verdict): confirmed | inconclusive | refuted           # bkz. evidence-confidence-rule.md
Varlık/Endpoint: <hedef>
Açıklama: <zafiyet sınıfı + kök neden>
Tekrar adımları:
  1. ...
  2. ...
Kanıt: <OUTPUT_DIR/... screenshot/HAR/OOB log yolu>
Etki: <somut güvenlik sonucu: principal/resource/outcome>
Remediation: <spesifik, aksiyon alınabilir düzeltme>
```

## Rapor yapısı
1. **Executive Summary** — risk, iş etkisi, öncelikler (jargonsuz) — reporting-docs/executive-summary-writing
2. **Scope & Methodology** — ne test edildi/edilmedi, yetki, sınırlar
3. **Findings** — yukarıdaki kayıt formatında, severity sırası
4. **Remediation Roadmap** — gruplanmış, köken-odaklı, önceliklendirilmiş
5. **Appendix** — kanıt, araç çıktıları

## İlkeler
- Kanıtsız iddia raporlanmaz; her severity gerekçeli.
- Test edilmeyen/doğrulanmayan kısımlar ve artık risk açıkça belirtilir.
- OUTPUT_DIR altındaki kanıtlara atıf; hassas veri maskelenir.
