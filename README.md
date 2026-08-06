# kamuyz-agent-starter

**Türkçe dokümante, güvenlik-öncelikli OpenClaw / Hermes başlangıç şablonu.**

KamuYZ APA Çalışma Grubu tarafından hazırlanan bu repo, kamu ve özel sektörde agentic AI sistemlerini güvenli şekilde kurmak isteyen ekipler için referans başlangıç noktasıdır.

## Amaç

- OpenClaw ve Hermes'i güvenli varsayılanlarla, üretime hazır şekilde kurmak
- Kurumların "bu nedir, güvenli mi, ne zaman kullanmalıyım" sorularına cevap vermek
- E3 Hands-on Atölyesi'nde canlı kurulum yapılabilir seviyede dokümantasyon sağlamak

## Hızlı Başlangıç

```bash
# OpenClaw kurulumu
curl -fsSL https://openclaw.ai/install.sh | bash

# İlk yapılandırma
openclaw onboard --install-daemon

# Gateway durumu
openclaw gateway status
```

Güvenli üretim kurulumu için [docs/docker-compose.yml](docs/docker-compose.yml) ve [SECURITY.md](SECURITY.md) dosyalarına bakın.

## İçindekiler

```
kamuyz-agent-starter/
├── README.md                   # Bu dosya
├── CONTEXT.md                  # Proje terimleri sözlüğü
├── GLOSSARY.md                 # TR-EN terimler sözlüğü
├── LEARNING.md                 # 2 haftalık ekip öğrenme planı
├── SECURITY.md                 # Üretim öncesi güvenlik checklist'i
├── docker-compose.yml          # Güvenli Docker kurulumu
├── skills/                     # Agent skill'leri
│   └── engineering/            # Mühendislik skill'leri
├── docs/
│   ├── adr/                    # Mimari karar kayıtları
│   ├── research/               # Araştırma raporları
│   ├── events/                  # Etkinlik içerik taslakları
│   └── sprint-plan.md          # Sprint görev planı
└── config/                     # Örnek yapılandırma dosyaları
    └── telegram-pairing.json5  # Telegram + pairing örneği
```

## Kimler İçin?

- Kamu BT personeli
- Agentic AI'yi kurum içinde denemek isteyen ekipler
- Güvenlik-öncelikli deployment yapmak isteyen herkes

## KamuKod ile İş Bölümü

| KamuKod | kamuyz-agent-starter (biz) |
|---|---|
| "Nasıl kurulur?" | "Bu nedir, güvenli mi, ne zaman kullanmalı?" |
| 4 haftalık uygulamalı kurs | Kamuya açık etkinlikler + kalıcı çıktılar |
| Üyelik bazlı | Açık erişim |

## Etkinlikler

| # | Etkinlik | Format |
|---|---|---|
| E1 | OpenClaw nedir, ne yapar? Hermes ve agentic dalga | Webinar, 90 dk |
| E2 | Otonom sistemlerin gerçeği: güvenlik ve zorluklar | Webinar/Panel, 90 dk |
| E3 | Hands-on atölye — canlı kurulum | Online atölye, 2-3 saat |

## Lisans

MIT
