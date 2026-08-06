# kamuyz-agent-starter

> Yapay zeka ajanlarını anla, kur, güvenli kullan. Adım adım, Türkçe.

Bu repo bir **öğrenme kaynağıdır**. OpenClaw ve Hermes gibi açık kaynak yapay zeka ajanlarının ne olduğunu, nasıl çalıştığını, güvenli olup olmadığını, gerçek kullanıcıların neler yaşadığını ve kendi ajanını nasıl kuracağını öğrenmek için ihtiyacın olan her şey burada.

---

## Bu repodan ne öğreneceksin?

| Soru | Cevabı nerede? |
|---|---|
| "Bu ajan olayı nedir, ne işe yarar?" | [Araştırma raporları](docs/research/) — Grok ve Gemini derin analizleri |
| "Gerçek kullanıcılar ne diyor?" | [Toplu deneyim raporu](docs/research/2026-08-06-grok-toplu-deneyim-sonucu.md) — X, Reddit, YouTube, Medium |
| "Nasıl kurarım?" | [E3 atölyesi](docs/events/E3-hands-on-atolye.md) — adım adım canlı kurulum |
| "Güvenli mi?" | [SECURITY.md](SECURITY.md) — 24 maddelik kontrol listesi |
| "Bu terimler ne demek?" | [GLOSSARY.md](GLOSSARY.md) — 80+ İngilizce-Türkçe terim |
| "Nereden başlamalıyım?" | [LEARNING.md](LEARNING.md) — 2 haftalık öğrenme planı |
| "Proje takvimi ne?" | [Sprint planı](docs/sprint-plan.md) — 6 sprint, 12 hafta |

---

## Öğrenme yolculuğu

```
1. ARAŞTIRMA          2. ANLAMA             3. KURMA              4. GÜVENCE
docs/research/  →     CONTEXT.md      →     E3 atölyesi    →     SECURITY.md
                       GLOSSARY.md           docker-compose       24 madde kontrol
                       LEARNING.md
```

**5 dakikada kurmak isteyenler için:**

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
openclaw gateway status
```

Ama asıl değer, kurmadan **önce** anlamakta. Yukarıdaki sırayla git.

---

## İçindekiler

```
kamuyz-agent-starter/
├── LEARNING.md                              ← Başlangıç noktası: 2 haftalık plan
├── CONTEXT.md                               ← 25 temel terimin tanımı
├── GLOSSARY.md                              ← TR-EN 80+ terim sözlüğü
├── SECURITY.md                              ← 24 maddelik güvenlik kontrolü
├── docker-compose.yml                       ← Güvenli Docker kurulumu
├── config/                                  ← Örnek yapılandırmalar
├── skills/                                  ← Agent yetenek (skill) setleri
├── docs/
│   ├── research/                            ← 4 kapsamlı araştırma raporu
│   │   ├── grok-ekosistem-taramasi          ← OpenClaw/Hermes teknik ekosistem
│   │   ├── gemini-derin-inceleme            ← Güvenlik, regülasyon, KVKK/DDO
│   │   └── grok-toplu-deneyim-sonucu        ← X/Reddit/YT/Medium gerçek deneyimler
│   ├── adr/                                 ← Mimari karar kayıtları
│   ├── events/                              ← E1, E2, E3 etkinlik içerikleri
│   └── sprint-plan.md                       ← Görev takvimi
```

---

## Hedef kitle

- **Hiç bilmeyen:** `docs/research/` ile başla, temel kavramları öğren
- **Merak eden:** `LEARNING.md`'deki 2 haftalık planı takip et
- **Kurmak isteyen:** `E3 atölyesi` + `docker-compose.yml` ile adım adım kur
- **Güvenlik odaklı:** `SECURITY.md`'deki 24 maddeyi kontrol et
- **Karar verici:** Araştırma raporlarını oku, riskleri ve fırsatları değerlendir

---

## Neden öğrenmelisin?

ChatGPT sana "ne yapman gerektiğini" söyler.  
OpenClaw ve Hermes ise **senin yerine yapar.**

Dosya okur, e-posta gönderir, araştırma yapar, takvimi yönetir, Telegram'dan komut alır. 7/24 çalışır.

Ama gücü kadar riski de var. O yüzden bu repo **önce anlamayı, sonra kurmayı** öğretir.

---

## Etkinlikler (herkese açık)

| # | Ne öğreneceksin? | Süre |
|---|---|---|
| E1 | Yapay zeka ajanı nedir, ne işe yarar? | 90 dk |
| E2 | Hangi güvenlik riskleri var? Gerçek vakalar | 90 dk |
| E3 | Canlı kurulum — kendi ajanını sıfırdan yap | 2-3 saat |

---

## KamuKod ile bağlantı

KamuKod: **"Nasıl kurulur?"** (4 haftalık uygulamalı kurs)  
Bu repo: **"Nedir, güvenli mi, ne zaman kullanılır?"** (açık erişim, ücretsiz)

İkisi birlikte tam öğrenme paketi.

---

## Lisans

MIT — öğren, kullan, paylaş, geliştir.
