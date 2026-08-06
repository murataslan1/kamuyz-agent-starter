# Hermes Agent — Kendi Kendine Öğrenen Yapay Zeka Ajanı

> **Tek komutla kur. Zamanla sana özel hale gelsin. Güvenli. Açık kaynak. Türkçe.**

[![MIT License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![KamuYZ APA](https://img.shields.io/badge/KamuYZ-APA%20Çalışma%20Grubu-3b82f6)](https://github.com/murataslan1/kamuyz-agent-starter)

---

## Neden ihtiyacın var?

ChatGPT'ye soru soruyorsun, cevap alıyorsun. Peki ya **senin yerine iş yapan** bir yapay zeka olsa?

- Her sabah maillerini özetlese, takvimini düzenlese
- Karmaşık bir araştırmayı 3 alt ajana bölüp paralel yapsa
- Bir kez öğrettiğin işi **bir daha sormadan**, her seferinde daha iyi yapsa

İşte Hermes Agent tam olarak bu. Nous Research tarafından geliştirilen, MIT lisanslı, **kendi kendine öğrenen** bir yapay zeka ajanı.

> *"Hermes'e geçince aynı iş akışı ilk denemede sorunsuz çalıştı, bir hafta boyunca müdahalesiz devam etti."*
> — Reddit, Haziran 2026

---

## Seni anlayan, öğrenen, gelişen bir asistan

| Diğerleri | Hermes Agent |
|---|---|
| Her göreve sıfırdan başlar | **Öğrendiğini unutmaz**, biriktirir |
| Yetenekleri sen yazarsın | **Kendi yeteneklerini kendi yazar** (SKILL.md) |
| Oturum kapanınca her şeyi unutur | 4 katmanlı hafıza — haftalar sonra bile hatırlar |
| Kurulum saatler sürer | **~25 dakikada** çalışır halde |
| ClawHub riskleri, CVE'ler | **Henüz sıfır bildirilen CVE** |

---

## Tek komutla başla

```bash
curl -fsSL https://raw.githubusercontent.com/murataslan1/kamuyz-agent-starter/main/hermes-paket/install.sh | bash
```

Varsayılan olarak güvenli: sandbox açık, non-root, dışarı kapalı, kritik komutlarda onay sorar.

---

## Sana özel paketler

| Ne istiyorsun? | Paket | Süre | Ücret |
|---|---|---|---|
| "Ne olduğunu anlamak istiyorum" | [KamuYZ E1-E2-E3](docs/events/) | 3 etkinlik | **Ücretsiz** |
| "Kendi ajanımı kurmak istiyorum" | [KamuKOD 210](https://kamukod.lovable.app/atolye/210) | 4 oturum · 8 saat | Ücretli kurs |
| "Kurumuma entegre etmek istiyorum" | [B2B Paket](docs/B2B-paket.md) | 1 hafta — 1 ay | Kurumsal |
| "Güvenlik denetimi istiyorum" | [SECURITY.md](SECURITY.md) | 24 madde kontrol | Repoda |

---

## Gerçek kullanıcılar ne diyor?

> *"OpenClaw'da 7 agent'lı sistem kurmuştum, sürekli hata alıyordum. Hermes'te sorun yok."*
> — Medium, "I Tested Hermes Agent for a Week"

> *"3 saatte 12 ticket kapattı, 2 aylık mühendislik işine denk."*
> — X kullanıcısı, OpenClaw Jira ajanı

> *"OpenClaw'u sildim, Hermes'e geçtim — akşam 7'de bilgisayar kapatıyorum."*
> — Türkçe YouTube

> *"Tekrarlayan işlerde Hermes, maksimum kontrol ve ekosistemde OpenClaw."*
> — Reddit, 30 günlük dört platform testi

> *"Zamanla sizi daha iyi öğrenen, kendi yöntemlerini geliştiren asistan."*
> — Softtech Medium (Türkçe)

---

## Öğrenme yolculuğu (adım adım)

| # | Ne? | Süre |
|---|---|---|
| 1 | [Hermes nedir, nasıl çalışır?](docs/research/2026-08-06-gemini-derin-inceleme.md) — derin inceleme | 30 dk |
| 2 | [Gerçek kullanıcı deneyimleri](docs/research/2026-08-06-grok-toplu-deneyim-sonucu.md) — X, Reddit, YouTube, Medium | 25 dk |
| 3 | [Temel terimler](GLOSSARY.md) — 80+ İngilizce-Türkçe | Referans |
| 4 | [2 haftalık plan](LEARNING.md) — yapılandırılmış öğrenme | Takip et |
| 5 | [Canlı kurulum atölyesi](docs/events/E3-hands-on-atolye.md) | 2-3 saat |
| 6 | [Güvenlik kontrol listesi](SECURITY.md) | 24 madde |

---

## Neden güvenli?

Bu repo, **önce güvenlik** prensibiyle hazırlandı:

- Gateway sadece `127.0.0.1`'te çalışır — dışarı kapalı
- Non-root kullanıcı, `no-new-privileges`, sandbox aktif
- Kritik komutlarda insan onayı (HITL)
- Audit log — tüm komutlar kayıt altında
- ISO 42001 uyumlu işletim prosedürleri (B2B)
- DDO BİGR ve KVKK uyumluluğu değerlendirildi

---

## Kimler için?

- **Karar verici:** "Kuruma alabilir miyiz?" → [Araştırma raporları](docs/research/)
- **BT personeli:** "Nasıl kurarım?" → [Güvenli Hermes Paketi](hermes-paket/)
- **Geliştirici:** "Mimarisi nasıl?" → [Gemini derin inceleme](docs/research/2026-08-06-gemini-derin-inceleme.md)
- **Güvenlik ekibi:** "Riskler ne?" → [SECURITY.md](SECURITY.md) + [E2 paneli](docs/events/E2-guvenlik-paneli.md)
- **Öğrenci / meraklı:** "Nereden başlarım?" → [LEARNING.md](LEARNING.md)

---

## Zincirleme etki

```
Bu repo (açık kaynak)  →  KamuYZ E1-E2-E3 (ücretsiz)  →  KamuKOD 210 (kurs)  →  B2B (kurumsal)
       ↓                          ↓                           ↓                      ↓
   Güven inşa eder          Farkındalık yaratır         Yetkinlik kazandırır    Ticari paket 📦
```

Her adım bir sonrakini besler.

---

## Etkinlikler (herkese açık)

| # | Konu | Süre |
|---|---|---|
| E1 | Yapay zeka ajanı nedir, Hermes neyi farklı yapar? | 90 dk |
| E2 | Agentic sistemlerde güvenlik: gerçek vakalar, korunma yöntemleri | 90 dk |
| E3 | Canlı kurulum — kendi ajanını sıfırdan yap | 2-3 saat |

---

## KamuKOD ile bağlantı

| KamuKOD | KamuYZ |
|---|---|
| Ücretli, derinlemesine kurs | Ücretsiz, açık erişim |
| "Nasıl kurulur, nasıl işletilir?" | "Nedir, güvenli mi, ne zaman?" |
| [Atölye 210: OpenClaw-Hermes](https://kamukod.lovable.app/atolye/210) | Bu repo + etkinlikler |

---

**MIT Lisansı** — öğren, kullan, kurumuna uyarla, geliştir.
