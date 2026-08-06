# Açık Kaynak Agentic AI Framework'leri: Kurumsal Değerlendirme ve Güvenlik Kılavuzu

**KamuYZ APA Çalışma Grubu — Ağustos 2026**
**Türkçe · Açık Erişim · Vendor-Nötr**

---

## Yönetici Özeti

Bu whitepaper, açık kaynak agentic AI framework'lerinin (özellikle OpenClaw ve Hermes Agent) kurumsal kullanıma uygunluğunu değerlendirmektedir. Mayıs-Ağustos 2026 dönemini kapsayan araştırmamız, 30+ kaynaktan derlenmiş olup; teknik mimari, güvenlik riskleri, regülasyon uyumu ve kurumsal benimseme kriterlerini vendor-nötr bir çerçevede sunmaktadır.

**Ana bulgular:**
- Agentic AI, tekrarlayan kurumsal iş süreçlerinde %70-90 arası zaman tasarrufu sağlayabilir
- Önde gelen iki açık kaynak framework (OpenClaw ve Hermes Agent) farklı felsefelere sahiptir: OpenClaw çok kanallı iletişim geçidi, Hermes kendi kendine öğrenen otonom ajan
- Güvenlik, kurumsal benimsemenin önündeki en büyük engeldir — CVE-2026-25253 ve ClawHub tedarik zinciri saldırıları bu riski somutlaştırmıştır
- Yerel (on-premise) çalıştırma, sandbox izolasyonu ve human-in-the-loop onay mekanizmaları ile riskler yönetilebilir

---

## 1. Giriş

### 1.1 Agentic AI Nedir?

Geleneksel chatbot'lar (ChatGPT vb.) kullanıcıdan girdi alır ve yanıt üretir. Agentic AI sistemleri ise:

- **Planlama:** Karmaşık hedefleri alt görevlere böler
- **Araç kullanımı:** Dosya sistemi, API'ler, veritabanları ile etkileşime girer
- **Hafıza:** Oturumlar arası bilgi taşır, öğrendiğini biriktirir
- **Çok adımlı muhakeme:** Her aksiyon sonrası durumu değerlendirir, gerektiğinde planı günceller

### 1.2 KamuKod ile İş Bölümü

| KamuKod (ücretli kurs) | KamuYZ APA (açık erişim) |
|---|---|
| "Nasıl kurulur?" | "Bu nedir, güvenli mi, ne zaman kullanmalı?" |
| 4 haftalık uygulamalı eğitim | Araştırma, whitepaper, açık etkinlikler |
| Üyelik bazlı | Herkese açık, ücretsiz |

---

## 2. Ekosistem Manzarası (2026)

### 2.1 Öne Çıkan Açık Kaynak Framework'ler

| Framework | Yıldız | Dil | Felsefe | Güvenlik Profili |
|---|---|---|---|---|
| OpenClaw | 385K+ | TypeScript | Gateway-first (çok kanallı) | CVE-2026-25253, ClawHub riskleri |
| Hermes Agent | 140K+ | Python | Agent-first (öğrenme odaklı) | Sıfır bildirilen CVE |
| CrewAI | — | Python | Multi-agent "crew" | Kurumsal benimseme yüksek |
| LangGraph | — | Python | State-machine tabanlı | Production-grade güvenilirlik |

### 2.2 OpenClaw — Detaylı İnceleme

**Mimari:** Gateway (kontrol düzlemi) + Agent Runtime + Connectors (50+ platform)
**Lisans:** MIT
**Kurucu:** Peter Steinberger (PSPDFKit)
**Öne çıkan özellik:** Telegram, WhatsApp, Slack, Discord dahil 50+ platforma bağlanabilen iletişim geçidi
**Zayıf yönler:** ClawHub marketplace güvenliği (820+ zararlı eklenti), CVE geçmişi, yüksek kurulum süresi (~4 saat)

### 2.3 Hermes Agent — Detaylı İnceleme

**Mimari:** Kapalı devre öğrenme döngüsü + 4 katmanlı hafıza
**Lisans:** MIT
**Geliştirici:** Nous Research
**Öne çıkan özellik:** Kendi kendine skill üretimi (SKILL.md), hafıza katmanları (L1-L4), 25 dakika kurulum süresi
**Zayıf yönler:** Daha az kanal desteği, daha küçük hazır eklenti ekosistemi

---

## 3. Güvenlik Analizi

### 3.1 Tehdit Vektörleri

| Risk | Açıklama | Şiddet | Önlem |
|---|---|---|---|
| Prompt Injection | Veri-talimat ayrımı yapılamaması | Kritik | Girdi sanitasyonu, HITL |
| Token Sızıntısı (CVE-2026-25253) | URL üzerinden auth token çalınması | Kritik | Origin doğrulama, allowedOrigins |
| Tedarik Zinciri (ClawHub) | Zararlı eklentiler (%12 oran) | Yüksek | Özel skill registry, kod incelemesi |
| Hafıza Zehirlenmesi | Uzun süreli belleğe zararlı girdi | Orta | Periyodik bellek sanitasyonu |
| Yetki Aşımı | Ajanın gereksiz yüksek yetkileri | Yüksek | Least privilege, sandbox |

### 3.2 Vaka İncelemesi: CVE-2026-25253

**Keşif:** Ocak 2026, DepthFirst (Mav Levin)
**CVSS:** 8.8 (Yüksek)
**Etkilenen:** OpenClaw < 2026.1.29
**Mekanizma:** `applySettingsFromUrl()` → `gatewayUrl` parametresi → doğrulamasız WebSocket → token sızıntısı → RCE
**Yama:** v2026.1.29 — Origin doğrulaması, allowedOrigins kısıtlaması

### 3.3 Vaka İncelemesi: Çin Kısıtlaması (Mart 2026)

MIIT, SASAC, CNCERT, MSS ve PBoC eşzamanlı olarak kamu kurumlarında OpenClaw kullanımını kısıtladı. Gerekçeler: ClawHub zararlıları, veri sınır-aşımı, kontrolsüz konuşlandırma. Regüle sektörler için önemli bir uyarı niteliğinde.

---

## 4. Kurumsal Değerlendirme Çerçevesi

### 4.1 Benimseme Öncesi Sorulması Gereken Sorular

1. Hangi iş süreçleri otonomiye uygundur? (risk sınıflandırması)
2. Human-in-the-loop nerelerde zorunludur?
3. Veri nerede kalır? (on-premise / cloud, KVKK/GDPR)
4. Eklenti ve araç tedarik zinciri güvenliği nasıl sağlanır?
5. Audit trail ve açıklanabilirlik var mıdır?
6. Credential yönetimi ve least privilege uygulanıyor mu?
7. Sandbox / runtime izolasyonu yeterli midir?
8. Model provider bağımlılığı ve fallback planı nedir?
9. Incident response ve kill-switch mekanizması var mıdır?
10. Regülasyon (EU AI Act, KVKK, DDO BİGR) uyumu nasıl sağlanır?

### 4.2 Vendor-Nötr Teknik Gereksinimler

| Alan | Gereksinim |
|---|---|
| Güvenlik | Yerel çalışma, sandbox izolasyonu, HITL, audit logging |
| Denetlenebilirlik | Detaylı log, SIEM entegrasyonu, immutable audit trail |
| Yetkilendirme | RBAC, AD/LDAP/OAuth2 entegrasyonu |
| Model Bağımsızlığı | Multi-provider destek, model değiştirebilme |
| Hafıza Yönetimi | Bellek zehirlenmesine karşı koruma, silinebilir hafıza |

### 4.3 Regülasyon Uyumu

| Regülasyon | Kapsam | Gereklilik |
|---|---|---|
| KVKK (6698) | Türkiye | Yurt dışı veri aktarım kısıtlamaları (Madde 9) |
| DDO BİGR | Türkiye (kamu) | Veri izolasyonu, sunucu sıkılaştırma, SOME entegrasyonu |
| EU AI Act | AB | Yüksek riskli sistem sınıflandırması, şeffaflık, insan gözetimi |
| ISO 42001 | Uluslararası | AI yönetim sistemi standardı |
| OWASP Agentic Top 10 | Uluslararası | Agentic-spesifik güvenlik riskleri (ASI-01 ~ ASI-06) |

---

## 5. Stratejik Öneriler

### Kamu Kurumları İçin

1. **İhtiyaç analizi yapın:** Çok kanallı vatandaş etkileşimi → OpenClaw. Veri analizi, kod inceleme, kurumsal hafıza → Hermes.
2. **İzole ortamda başlayın:** Docker konteynerlerinde, kısıtlı yetkilerle, non-root kullanıcı ile.
3. **Harici eklenti yüklemeyin:** Sadece kod incelemesinden geçmiş, kurum içi onaylı eklentiler.
4. **DDO BİGR ve KVKK uyumunu bağımsız denetimle doğrulayın.**

### Özel Sektör İçin

1. **Pilot use-case ile başlayın:** Tek bir tekrarlayan süreci seçin, ölçün, sonucu değerlendirin.
2. **ROI hesaplayın:** Harcanan insan-saat × saatlik maliyet üzerinden tasarrufu ölçün.
3. **Hibrit mimari değerlendirin:** OpenClaw (iletişim geçidi) + Hermes (arka plan beyni).

---

## 6. Sonuç

Agentic AI teknolojileri, pasif yanıt üreteçlerinden otonom iş gücüne geçişi temsil etmektedir. OpenClaw'un orkestrasyon kabiliyetleri ve Hermes'in öğrenme döngüsü, kamu ve özel sektörde operasyonel verimlilik artışı sağlama potansiyeline sahiptir.

Ancak CVE-2026-25253, ClawHub zararlı yazılım kampanyaları ve regülatif kısıtlamalar; yeterli güvenlik ve yönetişim mekanizmaları kurulmadan dağıtılan otonom sistemlerin ciddi riskler taşıdığını göstermektedir.

**Önerimiz:** Farkında olarak, güvenlik öncelikli, vendor-nötr bir yaklaşımla başlayın. Açık kaynak araçları kendi altyapınızda, kendi kontrolünüzde kullanın.

---

## Kaynaklar ve İleri Okuma

- [GitHub: kamuyz-agent-starter](https://github.com/murataslan1/kamuyz-agent-starter)
- [Grok Ekosistem Taraması](../research/2026-08-06-grok-ekosistem-taramasi.md)
- [Gemini Derin İnceleme](../research/2026-08-06-gemini-derin-inceleme.md)
- [Grok Toplu Deneyim Raporu](../research/2026-08-06-grok-toplu-deneyim-sonucu.md)
- [Güvenlik Kontrol Listesi](../SECURITY.md)
- [OpenClaw Resmi Site](https://openclaw.ai)
- [Hermes Agent Dokümantasyon](https://hermes-agent.nousresearch.com)
- [CVE-2026-25253 Detay](https://nvd.nist.gov/vuln/detail/CVE-2026-25253)
- [OWASP Agentic Top 10](https://owasp.org)

---

*Bu whitepaper, KamuYZ APA Çalışma Grubu tarafından hazırlanmıştır. Tüm içerik vendor-nötr ve açık erişimdir. Ağustos 2026 itibarıyla günceldir.*
