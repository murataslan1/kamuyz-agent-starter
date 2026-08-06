# LIVE_DEMO_SCRIPT.md — Canlı Demo Script'i

**Amaç:** Workshop sırasında yapılacak canlı demo'nun adım adım akışını hazırla, prova et.

**Hizmet Ettiği KPIs:** NPS, tamamlama oranı

## Girdiler
- `../docs/events/E3-hands-on-atolye.md` — E3 atölye taslağı
- `../hermes-paket/install.sh` — Güvenli kurulum betiği
- `../SECURITY.md` — Güvenlik checklist'i
- `skills/CURRICULUM_DESIGN.md` — İlgili modül

## Süreç

### 1. Demo öncesi (T-1 gün)
```
- [ ] Temiz bir ortam hazırla (Docker, Node.js, Python kontrol)
- [ ] API anahtarının çalıştığını test et
- [ ] Kurulumu sıfırdan yap (kuru çalış)
- [ ] Her adımı time'la — süreleri not al
- [ ] Olası hata noktalarını belirle (ve çözümlerini hazırla)
- [ ] Ekran paylaşımını test et (çözünürlük, font büyüklüğü)
```

### 2. Demo sırasında
```
Her adımda:
1. Ne yapacağını SÖYLE → "Şimdi Hermes'i kuralım"
2. YAP → Komutu çalıştır
3. Göster → Çıktıyı ekrana al
4. Açıkla → "Burada şu oluyor çünkü..."
5. Sor → "Anlaşılmayan var mı?"
6. Bekle → 5 saniye sessizlik, chat'i kontrol et
```

### 3. Demo sonrası
```
- [ ] Hata olduysa ne oldu, neden oldu — not al
- [ ] Katılımcıların takıldığı adımları journal'a kaydet
- [ ] Ekran görüntülerini kaydet (sonraki içerik için)
```

## Demo Şablonu
```markdown
# Demo: [Başlık]
**Süre:** XX dk
**Ortam:** Docker / Native / VPS

| Adım | Komut | Beklenen çıktı | Süre | Olası hata |
|---|---|---|---|---|
| 1 | `docker --version` | Docker version 24.x | 30sn | Docker kurulu değil → önceden kurmalarını söyle |
| 2 | `curl ... \| bash` | Installation complete | 2dk | Network hatası → önceden .sh dosyasını paylaş |
| ... | ... | ... | ... | ... |
```

## Kalite Barı
- [ ] Her adım test edildi (kuru çalış yapıldı)
- [ ] Olası 5+ hata senaryosu ve çözümü hazır
- [ ] Toplam süre planlanandan fazla değil
- [ ] Her komutun ne yaptığı tek cümleyle açıklanmış
- [ ] Ekran görüntüsü alınacak kritik anlar işaretlenmiş
