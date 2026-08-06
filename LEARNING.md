# LEARNING.md — 2 Haftalık Ekip Okuma ve Bilgilenme Listesi

Bu belge, KamuYZ APA Çalışma Grubu'nun agent-starter geliştirme öncesi 2 haftalık öğrenme fazı için hazırlanmıştır. Her başlık altındaki kaynaklar öncelik sırasına göre dizilmiştir.

---

## Hafta 1: Agentic AI Temelleri ve OpenClaw Ekosistemi

### Gün 1-2: Agentic AI Kavramı

| # | Kaynak | Süre | Not |
|---|---|---|---|
| 1 | [OpenClaw Resmi Sitesi](https://openclaw.ai/) | 30 dk | Projenin kendini nasıl konumlandırdığını anla |
| 2 | [GitHub: openclaw/openclaw](https://github.com/openclaw/openclaw) | 1 sa | README, dizin yapısı, issue'ları tara |
| 3 | [10 GitHub Repositories to Master OpenClaw](https://www.kdnuggets.com/10-github-repositories-to-master-openclaw) | 45 dk | Ekosistem haritası |
| 4 | [agentskills.io Specification](https://agentskills.io) | 20 dk | Skill format standardı |

### Gün 3-4: OpenClaw Mimarisi ve Kurulum

| # | Kaynak | Süre | Not |
|---|---|---|---|
| 1 | [OpenClaw Docs](https://docs.openclaw.ai) | 2 sa | Gateway, channels, tools, skills — tam dokümantasyon |
| 2 | [OpenClaw Kurulum Rehberi](https://openclaw.ai/install) | 30 dk | Kendi makinende kurmayı dene |
| 3 | [OpenClaw Telegram Setup](https://docs.openclaw.ai/channels/telegram) | 30 dk | E3 için kritik |
| 4 | [OpenClaw Pairing](https://docs.openclaw.ai/channels/pairing) | 15 dk | Güvenli kullanıcı eşleştirme |

### Gün 5: Hermes Agent

| # | Kaynak | Süre | Not |
|---|---|---|---|
| 1 | [GitHub: nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) | 1 sa | README, mimari, learning loop |
| 2 | [What Is Hermes Agent?](https://kie.ai/blog/what-is-hermes-agent) | 20 dk | Tanıtım yazısı |
| 3 | [Hermes Agent: The Complete Guide (2026)](https://pioneer.ai/blog/hermes-agent-the-complete-guide-to-the-self-improving-ai-agent-(2026)) | 30 dk | Derinlemesine rehber |
| 4 | [Hermes Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) | 20 dk | 4 katmanlı bellek mimarisi |
| 5 | [Hermes Learning Loop + Milvus](https://milvus.io/blog/hermes-agent-learning-loop-milvus-hybrid-search.md) | 20 dk | Learning loop teknik detayı |

---

## Hafta 2: Güvenlik, Regülasyon ve Geliştirme Pratikleri

### Gün 6-7: Agentic Güvenlik — Tehditler ve Vakalar

| # | Kaynak | Süre | Not |
|---|---|---|---|
| 1 | [CVE-2026-25253: OpenClaw 1-Click RCE Guide](https://foresiet.com/blog/cve-2026-25253-openclaw-rce-fix/) | 30 dk | Zafiyetin kök nedeni, istismar, yama |
| 2 | [SonicWall: OpenClaw Auth Token Theft to RCE](https://www.sonicwall.com/blog/openclaw-auth-token-theft-leading-to-rce-cve-2026-25253) | 20 dk | Teknik analiz |
| 3 | [Is OpenClaw Safe to Use? Security Deep-Dive (2026)](https://www.ajeetraina.com/is-openclaw-safe-to-use-a-security-deep-dive-2026/) | 45 dk | Kapsamlı güvenlik analizi, ClawHavoc, prompt injection |
| 4 | [The OpenClaw Security Crisis](https://conscia.com/blog/the-openclaw-security-crisis/) | 20 dk | Güvenlik krizi özeti |
| 5 | [Çin'de OpenClaw Kısıtlaması — ComAI Analizi](https://comai.space/en/pioneer-communities-and-the-future-of-ai-in-china-why-openclaw-in-shenzhen-is-also-about-the-one-person-company/) | 30 dk | MIIT/SASAC/CNCERT bağlamı |

### Gün 8-9: Güvenlik Standartları ve En İyi Pratikler

| # | Kaynak | Süre | Not |
|---|---|---|---|
| 1 | [OWASP Top 10 for Agentic Applications 2026](https://www.scribd.com/document/971579842/OWASP-Top-10-for-Agentic-Applications-2026-12-6-1) | 1 sa | ASI-01 ~ ASI-06 riskleri |
| 2 | [OpenClaw Hardening Rehberi](https://docs.openclaw.ai/security/hardening) | 30 dk | Resmi güvenlik sıkılaştırma |
| 3 | [DDO Bilgi ve İletişim Güvenliği Rehberi](https://mevzuat.comu.edu.tr/files/yonergeler/bg-rehber.pdf) | 1 sa | Kamu kurumları için bağlayıcı |
| 4 | [KVKK Rehberi](https://www.kvkk.gov.tr) | 30 dk | Kişisel veri — agentic bağlamda değerlendir |

### Gün 10: Ekosistem ve Tamamlayıcı Kaynaklar

| # | Kaynak | Süre | Not |
|---|---|---|---|
| 1 | [Awesome OpenClaw Agents](https://github.com/mergisi/awesome-openclaw-agents) | 30 dk | 200+ üretim ajan şablonu |
| 2 | [OpenClaw Master Skills](https://github.com/LeoYeAI/openclaw-master-skills) | 30 dk | Referans skill koleksiyonu |
| 3 | [NVIDIA NemoClaw](https://developer.nvidia.com/nemoclaw) | 20 dk | Enterprise deployment |
| 4 | [ClawTrust: OpenClaw Telegram Bot Guide](https://clawtrust.ai/blog/openclaw-telegram-bot-setup) | 20 dk | Adım adım Telegram entegrasyonu |
| 5 | [superpowers/superpowers](https://github.com/obra/superpowers) | 1 sa | Agent coding metodolojisi — skill pattern referansı |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | 30 dk | Skill mimarisi referansı |

---

## Ekip Olarak Yapılacaklar (Haftalık)

### Hafta 1 Çıktısı
- Herkes kendi makinesine OpenClaw kurar
- Telegram bot entegrasyonu yapar (kişisel test botu)
- `openclaw onboard --install-daemon` ile ilk ajanı çalıştırır
- En az 1 adet ClawHub skill'i dener

### Hafta 2 Çıktısı
- CVE-2026-25253'i kendi kurulumunda kontrol eder (versiyon >= 2026.1.29)
- Güvenlik checklist'indeki maddeleri kendi kurulumunda test eder
- `docker-compose.yml` ile containerized kurulum dener
- `openclaw pairing` ile güvenli kullanıcı eşleştirme yapar

---

## Referans Repolar (Geliştirme Fazı İçin)

| Repo | Amaç |
|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Çekirdek — Gateway, CLI, Control UI |
| [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) | Self-improving agent runtime |
| [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | Şablon ajanlar (SOUL.md) |
| [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | Referans skill'ler |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Pekiştirmeli öğrenme altyapısı |
| [obra/superpowers](https://github.com/obra/superpowers) | Agent coding metodolojisi |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skill pattern referansı |
