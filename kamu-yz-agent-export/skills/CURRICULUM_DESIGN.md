# CURRICULUM_DESIGN.md — Müfredat Tasarımı

**Amaç:** OpenClaw ve Hermes eğitim müfredatını tasarla, güncelle, iyileştir.

**Hizmet Ettiği KPIs:** NPS, tamamlama oranı

## Girdiler
- `../docs/research/*.md` — Güncel araştırma raporları
- `../docs/events/*.md` — Mevcut etkinlik taslakları
- `../CONTEXT.md` — Proje terimleri
- `knowledge/MEMORY.md` — Geçmiş workshop'lardan öğrenilenler
- `journal/` — Workshop sinyalleri

## Süreç

### 1. Seviye belirleme
| Seviye | Hedef kitle | İçerik derinliği | Süre |
|---|---|---|---|
| L1 — Tanı | Sıfır teknik bilgi | Kavramsal, metaforlu, demosuz | 90 dk |
| L2 — Dene | Temel komut satırı | Kurulum + ilk görev | 3 saat |
| L3 — Uygula | Yazılımcı | Derin mimari + kodlama | 8 saat |
| L4 — Uzmanlaş | DevOps/SysAdmin | Production deployment + güvenlik | 3 gün |

### 2. Modül yapısı
Her modül şu formatta olmalı:
```
# Modül: [Başlık]
## Neden? (5 dk) — Bu konuyu neden öğrenmelisin?
## Nedir? (15 dk) — Kavramsal anlatım + metafor
## Nasıl? (30 dk) — Canlı demo
## Birlikte yapalım (20 dk) — Katılımcı kendi yapar
## Kontrol (10 dk) — Mini quiz veya kontrol listesi
```

### 3. Güncelleme tetikleyicileri
- Yeni OpenClaw/Hermes sürümü çıkınca → ilgili modülü güncelle
- Yeni CVE/güvenlik olayı → E2 içeriğine ekle
- Grok/Gemini'den yeni araştırma gelince → araştırma referanslarını güncelle
- Öğrenci geri bildiriminde "burası anlaşılmadı" denilen yerleri düzelt

## Çıktı Formatı
```markdown
# Atölye [Seviye] — [Başlık]
**Tarih:** YYYY-AA-GG
**Sürüm:** vX.Y
**Son güncelleme nedeni:** [değişiklik açıklaması]

## Modül 1: [Başlık]
...

## Modül N: [Başlık]
...
```

## Kalite Barı
- [ ] Her modülde "Neden?" bölümü var
- [ ] Teknik terimlerin Türkçe açıklaması var
- [ ] En az 2 metafor/analoji kullanılmış
- [ ] Canlı demo adımları eksiksiz, test edildi
- [ ] Kontrol soruları öğrenme hedefini ölçüyor
- [ ] Toplam süre planlanan süreyi aşmıyor
