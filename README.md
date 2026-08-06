# kamuyz-agent-starter

> Kendi yapay zeka asistanını kur. Güvenli. Ücretsiz. Türkçe.

Bu rehber, **OpenClaw** ve **Hermes** adlı açık kaynak yapay zeka ajanlarını kendi bilgisayarına kurmanı ve Telegram gibi uygulamalar üzerinden kullanmanı sağlar. Tüm adımlar güvenlik öncelikli olarak hazırlanmıştır — kurduğun sistem dışarıya kapalı, verilerin sana ait olur.

---

## Nedir bu?

Günlük hayatta ChatGPT'ye soru sorup cevap alıyorsun. **Yapay zeka ajanı (agent)** bundan bir adım ötesi:

- Sadece cevap vermez, **senin için iş yapar**
- Dosyalarını okuyabilir, yazı yazabilir, e-posta gönderebilir
- Telegram, WhatsApp gibi her gün kullandığın uygulamalardan komut alabilir
- 7/24 arka planda çalışır, sen sormasan da görevleri takip eder

Bu repo, böyle bir sistemi **güvenli şekilde** kurmak için ihtiyacın olan her şeyi içerir.

---

## Nasıl kurarım? (5 dakika)

```bash
# 1. OpenClaw'u bilgisayarına kur
curl -fsSL https://openclaw.ai/install.sh | bash

# 2. İlk kurulum sihirbazını başlat (sana sorular soracak)
openclaw onboard --install-daemon

# 3. Çalıştığını kontrol et
openclaw gateway status
```

Hepsi bu. Artık ajanın arka planda çalışıyor. Telegram'a bağlamak için [detaylı kurulum rehberine](docs/events/E3-hands-on-atolye.md) bak.

---

## Ne işe yarar?

| Sen ne dersin | Ajan ne yapar |
|---|---|
| "Bugünkü toplantılarımı özetle" | Takvimini okur, özet çıkarır, Telegram'dan sana gönderir |
| "Bu 10 PDF'i tara, önemli yerleri işaretle" | Dosyaları okur, kritik bölümleri bulur |
| "Her sabah 8'de hava durumunu söyle" | Her gün aynı saatte otomatik çalışır |
| "Sunucu loglarını kontrol et, hata varsa bildir" | Sistem loglarını tarar, sorun bulursa uyarır |

---

## Güvenli mi?

Bu repoyu diğerlerinden ayıran en önemli şey: **önce güvenlik**.

Bir yapay zeka ajanına dosyalarını okuma, komut çalıştırma yetkisi veriyorsun. Bu yanlış yapılandırılırsa veri sızıntısına yol açabilir. O yüzden:

- Kurulum **varsayılan olarak güvenli** ayarlarla gelir
- Sistem dışarıya kapalı, sadece senin bilgisayarında çalışır
- 24 maddelik güvenlik kontrol listesi ([SECURITY.md](SECURITY.md))
- Telegram'da kimlerin ajana erişebileceğini sen belirlersin (onay koduyla)

---

## Bu repoda neler var?

| Dosya | İçindeki |
|---|---|
| [LEARNING.md](LEARNING.md) | Ekibin 2 haftada öğreneceği her şey (okuma listesi) |
| [SECURITY.md](SECURITY.md) | Sistemi canlıya almadan önce kontrol edilecek 24 madde |
| [CONTEXT.md](CONTEXT.md) | Projede kullanılan terimlerin tanımları |
| [GLOSSARY.md](GLOSSARY.md) | İngilizce-Türkçe terimler sözlüğü |
| [docker-compose.yml](docker-compose.yml) | Docker ile güvenli kurulum dosyası |
| [config/](config/) | Örnek yapılandırma dosyaları |
| [docs/sprint-plan.md](docs/sprint-plan.md) | İş takvimi ve görev dağılımı |
| [docs/events/](docs/events/) | 3 etkinliğin içerik taslakları |
| [docs/research/](docs/research/) | Yapay zeka ajanları hakkında derin araştırma raporları |

---

## Kimler kullanabilir?

- Kamu kurumlarında çalışan BT personeli
- Şirketinde yapay zeka ajanı denemek isteyen ekipler
- Kendi asistanını kurmak isteyen yazılımcılar
- "Bu ajan olayı nedir?" diye merak eden herkes

Teknik bilgi şart değil. Komut satırına yazı yazmayı biliyorsan yeter.

---

## Etkinlikler

KamuYZ APA Çalışma Grubu olarak 3 açık etkinlik düzenliyoruz. Herkes katılabilir.

| Sıra | Konu | Süre |
|---|---|---|
| E1 | Yapay zeka ajanı nedir? Ne işe yarar? | 90 dk webinar |
| E2 | Güvenlik riskleri ve gerçek dünyadan örnekler | 90 dk panel |
| E3 | Canlı kurulum atölyesi (bu repoyu kullanarak) | 2-3 saat |

---

## KamuKod ile bağlantı

KamuKod kursu sana **"nasıl kurulur"** sorusunun cevabını uygulamalı olarak öğretir.  
Biz burada **"bu nedir, güvenli mi, ne zaman kullanılır"** sorularına cevap veriyoruz.  
İkisi birbirini tamamlar, çakışmaz.

---

## Katkı

Repo'ya katkıda bulunmak ister misin? Issue açabilir, PR gönderebilirsin. Başlamak için [CONTEXT.md](CONTEXT.md)'i oku.

---

## Lisans

MIT — istediğin gibi kullan, değiştir, paylaş.
