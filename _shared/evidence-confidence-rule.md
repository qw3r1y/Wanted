# Ortak Kural: Kanıt & Güven (evidence-confidence)

> Bulgu üreten her skill bu şemayı kullanır.

## Verdict (zorunlu)
Her bulgu üç durumdan biriyle işaretlenir:
- **confirmed** — somut, tekrarlanabilir kanıt var (yürütme/OOB geri-dönüş/veri erişimi).
- **inconclusive** — sinyal var ama kesin kanıt yok; ek doğrulama gerek.
- **refuted** — test edildi, güvenli çıktı (ör. doğru encode/escape, framework savunması).

## Kanıt tipleri (güç sırası)
1. Out-of-band geri-dönüş (DNS/HTTP callback) — blind/stored için altın standart.
2. Tarayıcıda/çalışma-zamanında gözlemlenen yürütme.
3. Yetkisiz veri/kaynağa erişim kanıtı (ekran/response).
4. Ham yansıma/hata (yalnız **sinyal**, tek başına kanıt değil).

## Presence ≠ Exploitation
Girdinin yanıtta görünmesi (presence) açık değildir. Sink/bağlam ve gerçek etki doğrulanmadan **confirmed** verilmez. Modern framework savunmaları (auto-escape, CSP, parametreli sorgu) çoğu "görünür ama sömürülemez" durumu üretir.

## Kayıt
Her bulgu: `verdict` + `severity` (CVSS, bkz. `cvss-reference.md`) + `evidence_path` (OUTPUT_DIR altında) + tekrar-adımları. Kanıtsız iddia raporlanmaz.
