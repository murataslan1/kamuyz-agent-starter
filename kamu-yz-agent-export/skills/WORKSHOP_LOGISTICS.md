# WORKSHOP_LOGISTICS.md — Workshop Lojistik Yönetimi

**Amaç:** Workshop öncesi, sırası ve sonrasındaki tüm lojistik adımları yönet.

**Hizmet Ettiği KPIs:** Tamamlama oranı, kayıt sayısı

## Girdiler
- Katılımcı listesi (manuel veya KamuKOD'dan)
- Workshop tarihi ve saati
- Zoom/Meet linki
- `skills/CURRICULUM_DESIGN.md` — Güncel müfredat

## Süreç

### T-7 gün: Davet ve Hazırlık
```
- [ ] Katılımcı listesini kontrol et, eksik bilgi varsa tamamla
- [ ] Hoş geldin mailini gönder:
      - Workshop adı, tarih, saat
      - Zoom linki
      - Teknik gereksinimler (Node.js, Docker, Telegram)
      - Ön okuma (opsiyonel)
- [ ] Slack/WhatsApp grubunu oluştur (veya mevcut gruba ekle)
```

### T-3 gün: Hatırlatma
```
- [ ] Hatırlatma maili: "2 gün sonra başlıyoruz!"
- [ ] Teknik gereksinimleri tekrar hatırlat
- [ ] "Şimdiye kadar şunu yapmış olmalısın" checklist'i gönder
```

### T-1 gün: Son Kontrol
```
- [ ] Zoom linkini test et (çalışıyor mu?)
- [ ] Demo ortamını test et (bkz. LIVE_DEMO_SCRIPT)
- [ ] Sunum dosyalarını hazır et
- [ ] Kayıt ayarlarını kontrol et (otomatik kayıt açık mı?)
```

### Oturum Sırasında
```
Başlangıç (ilk 5 dk):
- [ ] "Hoş geldiniz" + buz kırıcı soru
- [ ] Bugünün gündemini paylaş
- [ ] Kayıt başladı mı kontrol et

Ortasında (her 30 dk):
- [ ] "Buraya kadar soru?"
- [ ] Chat'i kontrol et, cevaplanmamış soru var mı?

Bitiş (son 5 dk):
- [ ] Özet + ana çıkarımlar
- [ ] Sonraki oturum/etkinlik duyurusu
- [ ] Geri bildirim formu linki
- [ ] "Kayıt şuraya yüklenecek" bilgisi
```

### T+1 gün: Takip
```
- [ ] Teşekkür maili gönder
- [ ] Kayıt linkini paylaş
- [ ] Geri bildirim formunu gönder
- [ ] Sunum PDF'ini paylaş
```

### T+3 gün: Değerlendirme
```
- [ ] Geri bildirimleri topla, özetle
- [ ] Katılım oranını hesapla
- [ ] B2B ilgi gösterenleri işaretle → B2B_PROPOSAL
- [ ] Öğrenilenleri journal'a kaydet
```

## Mail Şablonları

### Hoş Geldin Maili
```
Merhaba [isim],

[Atölye adı] için kaydını aldık! 🎉

🗓️ Tarih: [tarih]
⏰ Saat: [saat]
📍 Link: [zoom linki]

Başlamadan önce:
✅ Node.js 20+ kur: https://nodejs.org
✅ Docker kur (opsiyonel ama önerilir): https://docs.docker.com/get-docker/
✅ Telegram hesabını hazırla

Sorun olursa bu mail'e cevap yazabilirsin.

Görüşmek üzere!
KamuYZ APA
```

## Kalite Barı
- [ ] Tüm mailler workshop'tan en az 24 saat önce gönderildi
- [ ] Zoom linki test edildi
- [ ] Kayıt ayarları kontrol edildi
- [ ] Geri bildirim formu hazır
- [ ] Katılımcı listesi güncel
