# KamuYZ Agent Export — Referans Dökümanlar

Bu dizin, KamuYZ Workshop Agent'ın ihtiyaç duyduğu alan bilgisini içerir. Skill'ler tarafından ihtiyaç anında yüklenir.

## İçindekiler

| Dosya | İçerik |
|---|---|
| `openclaw-hermes-knowledge.md` | Agentic AI temel bilgileri, Hermes vs OpenClaw |
| `workshop-platforms.md` | Kullanılan platformlar ve araçlar |
| `b2b-pricing-guide.md` | B2B fiyatlandırma ve paket rehberi |
| `turkish-ai-ecosystem.md` | Türkiye AI ekosistemi ve regülasyonları |

---

## Bu repo neyi çözüyor?

Bu repo (`kamuyz-agent-starter`) şu sorunları çözmek için var:

### Sorun 1: "Hermes'i duydum ama ne olduğunu anlamadım"
→ **Çözüm:** [Araştırma raporları](../docs/research/), [GLOSSARY.md](../GLOSSARY.md), [CONTEXT.md](../CONTEXT.md)

### Sorun 2: "Kurmak istiyorum ama güvenli mi bilmiyorum"
→ **Çözüm:** [hermes-paket/](../hermes-paket/) — tek komutla güvenli kurulum, [SECURITY.md](../SECURITY.md) — 24 maddelik kontrol

### Sorun 3: "Kurdum ama nasıl kullanacağımı bilmiyorum"
→ **Çözüm:** [LEARNING.md](../LEARNING.md) — 2 haftalık plan, [E3 atölyesi](../docs/events/E3-hands-on-atolye.md) — canlı kurulum

### Sorun 4: "Kurumumda kullanmak istiyorum, karar vericiyi nasıl ikna ederim?"
→ **Çözüm:** [B2B-paket.md](../docs/B2B-paket.md) — hazır teklif şablonları, güvenlik değerlendirme raporu

### Sorun 5: "OpenClaw mu Hermes mi?"
→ **Çözüm:** Karşılaştırma tabloları araştırma raporlarında ve [README.md](../README.md)'de

### Sorun 6: "Güncel mi, gerçek kullanıcılar ne diyor?"
→ **Çözüm:** [Toplu deneyim raporu](../docs/research/2026-08-06-grok-toplu-deneyim-sonucu.md) — X, Reddit, YouTube, Medium'dan derlenmiş, Mayıs-Ağustos 2026

---

## Workshop'ta bu repo nasıl anlatılır?

### E1 (Tanıtım) — "Bu repo ne işe yarar?"
```
1. README'yi aç, ana sayfayı göster
2. "Şu sorulara cevap veriyor" diyerek tabloyu göster
3. Araştırma raporlarından bir alıntı oku
4. "Hepsi Türkçe, hepsi açık kaynak" vurgusu
```

### E2 (Güvenlik) — "Güvenlik nasıl sağlanıyor?"
```
1. SECURITY.md'yi aç, 24 maddeyi göster
2. hermes-paket/install.sh'ın güvenlik varsayılanlarını göster
3. docker-compose.yml'daki izolasyon ayarlarını açıkla
```

### E3 (Hands-on) — "Hadi kuralım"
```
1. hermes-paket/install.sh'ı çalıştır
2. Her adımda hangi dosyanın ne işe yaradığını açıkla
3. Katılımcılar kendi kurulumlarını yaparken repo'dan referans göster
```
