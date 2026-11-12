# Ortak Kural: Kapılı İş Akışı (gated-workflow)

> Çok adımlı skill'ler bu kalıbı izler.

## İlke
İş akışı fazlara bölünür; her faz, bir sonrakine geçmeden önce bir **kapı (gate)** sağlar. Kapı tutmazsa akış durur — tahminle ilerlenmez.

## Standart kapılar
1. **Yetki kapısı** — kapsam & onay doğrulandı mı? (bkz. `scope-authorization-rule.md`)
2. **Varlık kapısı** — hedef kapsamda ve canlı mı?
3. **Kanıt kapısı** — her iddia, somut kanıta dayanıyor mu? (bkz. `evidence-confidence-rule.md`)
4. **Etki kapısı** — bulgunun gerçek bir güvenlik etkisi (principal/resource/outcome) var mı? Yoksa "confirmed" deme.
5. **Yıkıcı-eylem kapısı** — durum değiştirecek adım öncesi operatör onayı.

## Kural
Bir kapıda "emin değilim" → dur, netleştir, sonra devam. Kapı atlanırsa bulgu **geçersiz** sayılır.
