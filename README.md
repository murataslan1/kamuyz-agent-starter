# kamuyz-agent-starter — Hermes Agent Öğrenme Rehberi

> Bu repo, Hermes Agent'ı anlamak için yazıldı. Sonuna kadar oku — Hermes'in ne olduğunu, neden farklı olduğunu, nasıl çalıştığını tam olarak kavrayacaksın.

---

## Hermes Agent nedir?

Hermes Agent, **Nous Research** tarafından geliştirilen, MIT lisanslı, **kendi kendine öğrenen** bir yapay zeka ajanıdır.

Diğer tüm ajanlardan (OpenClaw dahil) farkı şu: Hermes zamanla **sana özel yetenekler geliştirir**. Sen öğretmezsin, o kendi deneyimlerinden öğrenir.

Basitçe:

| Sistem | Mantığı |
|---|---|
| ChatGPT | Soru sorarsın, cevap verir |
| OpenClaw | Görev verirsin, yapar (ama her seferinde sıfırdan) |
| **Hermes Agent** | Görev verirsin, yapar, **nasıl yaptığını kaydeder**, bir dahaki sefere daha iyi yapar |

---

## Hermes'i diğerlerinden ayıran şey: Kapalı Devre Öğrenme Döngüsü

Hermes'in kalbi **Closed Learning Loop** (Kapalı Devre Öğrenme Döngüsü) denen mekanizmadır. Şöyle çalışır:

```
GÖREV → TAMAMLA → ANALİZ ET → SKILL OLUŞTUR → BİR DAHAKİ SEFERE KULLAN → İYİLEŞTİR
```

1. **Görevi tamamlar:** Karmaşık, çok adımlı bir işi bitirir (örneğin "şu 10 PDF'i tara, önemli yerleri işaretle, özet çıkar")
2. **Analiz eder:** Hangi araçları kullandı, hangi adımlar işe yaradı, nerede hata yaptı — hepsini yapılandırılmış şekilde episodic memory'e kaydeder
3. **Skill oluşturur:** Başarılı iş akışını `SKILL.md` adında yeniden kullanılabilir bir yetenek dosyasına dönüştürür (agentskills.io standardında)
4. **Bir dahaki sefere kullanır:** Aynı tür görev geldiğinde, kendi yazdığı skill'i yükler, sıfırdan düşünmez
5. **Kullandıkça iyileştirir:** Skill çalışırken karşılaştığı uç durumları ve performans sorunlarını tespit edip skill'i günceller

Bu, Hermes'in **zamanla sana özel bir uzman** haline gelmesi demek. Ne kadar kullanırsan, o kadar iyi olur.

---

## Hafızası nasıl çalışır? (4 katman)

Hermes, "her şeyi tek bir yere yazıp unutmak" yerine 4 katmanlı bir hafıza kullanır:

| Katman | Ne saklar? | Ne kadar? | Ne zaman silinir? |
|---|---|---|---|
| **L1 — Session Context** | O anki konuşma, aktif görev | Sınırsız | Oturum kapanınca |
| **L2 — Persisted Facts** | Kritik bilgiler: ortam, kararlar, tercihlerin | ~2.200 karakter (MEMORY.md) + ~1.375 (USER.md) | Sen silene kadar kalır |
| **L3 — Session Archive** | Tüm geçmiş oturumlar | Sınırsız | SQLite FTS5'te kalır, tam metin aramayla bulunur |
| **L4 — Procedural Skills** | Kendi yazdığı SKILL.md yetenekleri | Sınırsız | İhtiyaç anında dinamik yüklenir |

Bu mimari sayesinde:
- Oturum kapansa da **seni unutmaz** (L2)
- Haftalar önceki bir konuşmayı **bulup hatırlayabilir** (L3)
- Öğrendiği her şeyi **yeniden kullanılabilir becerilere dönüştürür** (L4)

---

## Hermes vs OpenClaw: Temel fark

Her ikisi de açık kaynak, her ikisi de MIT lisanslı. Ama felsefeleri tamamen farklı:

| | OpenClaw | Hermes Agent |
|---|---|---|
| **Felsefe** | Gateway-first: "Her yere bağlan" | Agent-first: "Kendini geliştir" |
| **Dil** | TypeScript / Node.js | Python (%88) + TypeScript |
| **Skill'ler** | İnsan yazar, ClawHub'dan indirirsin (13.000+ hazır) | **Ajan kendi yazar**, deneyimlerinden üretir |
| **Hafıza** | Dosya tabanlı (AGENTS.md, SOUL.md, MEMORY.md) | 4 katmanlı (FTS5, SessionDB, Honcho/mem0) |
| **Kanal** | 50+ mesajlaşma platformu | Terminal, CLI, Docker, SSH |
| **Kurulum** | ~4 saat (kullanıcı deneyimi) | ~25 dakika (kullanıcı deneyimi) |
| **Güvenlik** | CVE-2026-25253 yaşadı, ClawHub riskleri var | Henüz sıfır bildirilen CVE |

**Kim ne zaman tercih edilmeli:**
- WhatsApp/Telegram/Slack gibi onlarca kanala bağlanacak, hazır eklentilerle hızlıca çalışacak bir asistan → OpenClaw
- Zamanla seni öğrenecek, kendi kendine yetenek geliştirecek, kodlama ve araştırmada uzmanlaşacak bir çalışma arkadaşı → Hermes

Birçok ileri düzey kullanıcı ikisini birlikte kullanıyor: **OpenClaw dış dünyayla iletişimi yöneten kapı, Hermes arkadaki beyin.**

---

## Gerçek kullanıcılar Hermes hakkında ne diyor?

Mayıs-Ağustos 2026 arası X, Reddit, YouTube ve Medium'dan derlenen deneyimler:

> *"Hermes'e geçince aynı iş akışı ilk denemede sorunsuz çalıştı, bir hafta boyunca müdahalesiz devam etti."* — Reddit kullanıcısı, Haziran 2026

> *"OpenClaw'da 7 agent'lı Mission Control kurmuştum, tool onay süreçlerinde sürekli hata alıyordum. Hermes'te bu sorun yok."* — Medium, "I Tested Hermes Agent for a Week"

> *"Hermes kurulum ~25 dakika, bakım daha az, ama self-generated skill'ler bazen fazla yaratıcı kalıyor."* — 30 günlük dört platform karşılaştırma testi

> *"OpenClaw'u sildim, Hermes'e geçtim — akşam 7'de bilgisayar kapatıyorum."* — Türkçe YouTube videosu

> *"Hermes'in kendi becerilerini kendisinin yazma yeteneği sayesinde kodlama görevlerinde ciddi zaman kazandım."* — r/LocalLLaMA, 342 upvote

> *"Hermes = zamanla sizi daha iyi öğrenen, kendi yöntemlerini geliştiren asistan."* — Softtech Medium (Türkçe)

---

## Nasıl öğrenmeye başlarsın?

Bu repoda Hermes'i anlamak için ihtiyacın olan her şey sırayla dizildi:

```
1. TEMELLER              2. DERİNLEŞ            3. KUR                  4. GÜVENLİ KULLAN
docs/research/     →     LEARNING.md      →     docker-compose    →     SECURITY.md
(Araştırma raporları)    (2 haftalık plan)       E3 atölyesi              (24 kontrol)
```

| Adım | Dosya | Ne öğreneceksin? | Süre |
|---|---|---|---|
| 1 | [Gemini Derin İnceleme](docs/research/2026-08-06-gemini-derin-inceleme.md) | Hermes'in mimarisi, learning loop, 4 katmanlı hafıza | 30 dk |
| 2 | [Grok Ekosistem Taraması](docs/research/2026-08-06-grok-ekosistem-taramasi.md) | Hermes vs OpenClaw, ekosistem, güvenlik | 20 dk |
| 3 | [Grok Toplu Deneyim](docs/research/2026-08-06-grok-toplu-deneyim-sonucu.md) | Gerçek kullanıcılar ne yaşamış? X/Reddit/YT/Medium | 25 dk |
| 4 | [CONTEXT.md](CONTEXT.md) | 25 temel terim: Learning Loop, Skill, Memory, HITL... | 15 dk |
| 5 | [GLOSSARY.md](GLOSSARY.md) | 80+ İngilizce-Türkçe teknik terim | Referans |
| 6 | [LEARNING.md](LEARNING.md) | 2 haftalık yapılandırılmış öğrenme planı | Takip et |
| 7 | [E3 Atölyesi](docs/events/E3-hands-on-atolye.md) | Sıfırdan Hermes kurulumu + Telegram bağlantısı | 2-3 saat |
| 8 | [SECURITY.md](SECURITY.md) | 24 maddelik güvenlik kontrol listesi | Uygula |
| 9 | [Sprint Planı](docs/sprint-plan.md) | Proje takvimi ve görev dağılımı | Takip et |

---

## Hedef kitle

Bu repo **teknik bilgi şartı olmadan** Hermes'i anlamak isteyen herkes için:

- Kamu BT personeli — "Kuruma alabilir miyiz?" sorusuna cevap
- Teknik olmayan karar vericiler — Risk/fırsat değerlendirmesi
- Yazılımcılar — Derinlemesine mimari ve kurulum
- Öğrenciler — Agentic AI'ye giriş
- Merak eden herkes — "Bu ajan olayı ne?" sorusunun tam cevabı

---

## Neden Hermes?

Çünkü yapay zekanın geleceği **sadece cevap vermek değil, öğrenmek.**

ChatGPT bir kütüphane gibidir — gider sorarsın, cevap alırsın.  
OpenClaw bir asistan gibidir — görev verirsin, yapar.  
**Hermes bir çırak gibidir — birlikte çalıştıkça ustalaşır, sana özel hale gelir.**

Her kullandığında biraz daha iyi olur. İşte bu yüzden farklı.

---

## KamuKOD ile Tamamlayıcı Zincir

KamuKOD ve KamuYZ birbirini besleyen iki kanaldır. Birlikte tam öğrenme paketi oluşturur:

```
KamuKOD 210 (ücretli kurs)          KamuYZ E1-E2-E3 (ücretsiz)
"Nasıl kurulur, nasıl işletilir?"    "Nedir, güvenli mi, ne zaman?"
4 oturum · 8 saat · Zoom             3 etkinlik · açık erişim · YouTube
       │                                      │
       └──────────── birbirine yönlendirir ─────────┘
                              │
                    KamuKOD 220 (kurumsal)
                    "Enterprise Agentic Design"
                    1 gün · yüz yüze · B2B
```

| Ne istiyorsun? | Nereden başla? |
|---|---|
| "Ne olduğunu anlamak istiyorum" | KamuYZ E1 (ücretsiz webinar) |
| "Kendi ajanımı kurmak istiyorum" | KamuKOD 210 (ücretli kurs) |
| "Kurumuma entegre etmek istiyorum" | [B2B Paketler](docs/B2B-paket.md) |
| "Güvenlik denetimi yapmak istiyorum" | [SECURITY.md](SECURITY.md) |
| "ISO 42001 uyumlu işletim prosedürleri" | [B2B Paket 3](docs/B2B-paket.md) |

🔗 **KamuKOD:** [kamukod.lovable.app](https://kamukod.lovable.app) — Atölye 210: OpenClaw-Hermes

---

## Güvenli Hermes Paketi (Tek Komutla)

```bash
curl -fsSL https://raw.githubusercontent.com/murataslan1/kamuyz-agent-starter/main/hermes-paket/install.sh | bash
```

Güvenlik varsayılanları açık, Docker izolasyonlu, non-root, sandbox aktif. Detaylar: [hermes-paket/](hermes-paket/)

---

## Etkinlikler

| # | Ne öğreneceksin? | Süre |
|---|---|---|
| E1 | Yapay zeka ajanı nedir, Hermes neyi farklı yapar? | 90 dk |
| E2 | Agentic sistemlerde güvenlik riskleri | 90 dk |
| E3 | Hermes canlı kurulum atölyesi | 2-3 saat |

---

## Lisans

MIT — öğren, kullan, paylaş, geliştir.
