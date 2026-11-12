# IDOR — Referans Tipleri & Varyantlar (4. seviye)

Yetkili test içindir. İki-kimlik differential çekirdek kanıttır; minimal, sınırlı
enumerasyon; gerçek kullanıcı verisini toplu çekme yok.

## Referans tipleri → test yaklaşımı
| Tip | Yaklaşım | Not |
|---|---|---|
| Sequential int | id±1, sınır değerleri, komşu aralık (sınırlı) | En klasik; öngörülebilir |
| UUID v1 (zaman-tabanlı) | Zaman/MAC öngörülebilirliği | "Random" sanılır, değildir |
| UUID v4 | Sızıntı ara (yanıt/e-posta/log) | Tahmin zor; sızıntı anahtar |
| Hash/encoded | Decode/derive; per-user mı global mı | Çoğu geri-çevrilebilir |
| Slug/filename | Path/isim enumerasyonu | Dosya indirme uçları |
| Composite | Parçalardan birini değiştir | Biri doğrulanmıyor olabilir |

## Konum
URL path (`/users/{id}`) · query · body/JSON · header · GraphQL variables ·
"gizli" API alanları (UI göstermez ama API kabul eder).

## İleri varyantlar
- **Chained IDOR:** A nesnesinin yanıtı B'nin referansını sızdırır → pivot.
- **API/GraphQL IDOR:** UI authz uygular ama API object-level authz eksik;
  batched/nested sorgularda object erişimi test et.
- **Read vs Write:** GET sızıntısı + state-changing (PUT/PATCH/DELETE) ayrı test;
  write varyantı yalnız anlık onayla.
- **Vertical:** düşük-yetki → yüksek-yetki nesne/eylem (daha yüksek önem).

## Kanıt kalıbı
`A oturumu → B referansı → B verisi döndü` request/response çifti; ters yön (B→A);
read ve (onaylıysa) write; horizontal/vertical etiketi. Tahmin edilebilir id tek
başına **inconclusive**.

## Remediation hatırlatması
Her istekte sunucu-taraflı object-level authz (`WHERE owner = current_user`),
merkezî policy/middleware, global id ifşasından kaçınma, authz testlerini CI'a ekleme.
