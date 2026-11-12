# Jailbreak Teknik Sınıfları (4. seviye)

Yetkili guardrail-robustluk değerlendirmesi içindir. Amaç: hangi sınıfın bypass
ettiğini ölçüp guardrail'i güçlendirmek — zararlı çıktı üretmek değil.

| Sınıf | Fikir (kavramsal) |
|---|---|
| Roleplay / persona | Modeli politika-dışı bir role/persona'ya sokma |
| Encoding / obfuscation | Talimatı kodlama/çeviri/biçim ile gizleme |
| Many-shot | Çok sayıda örnekle davranışı kaydırma |
| Multi-turn / crescendo | Kademeli, zararsız başlayıp tırmanan konuşma |
| Instruction-hierarchy confusion | Sistem vs kullanıcı talimat önceliğini karıştırma |
| Payload splitting | İsteği parçalara bölüp birleştirme |
| Context/hypothetical framing | "Varsayımsal/kurgu" çerçevesiyle politika atlatma |

## Ölçüm
Her sınıf için bypass oranı; başarılı teknikler. Tek refüze "güvenli" demek değil —
çok teknik dene. Model/app değiştikçe tekrar et (sürekli).

## Savunma bağlantısı
Katmanlı guardrail (girdi/çıktı sınıflandırıcı), instruction hierarchy, sürekli
red-team (ai-red-team), izleme. Base model tek başına yeterli değil.
