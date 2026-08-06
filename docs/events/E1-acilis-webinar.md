# E1 — OpenClaw Nedir, Ne Yapar? Hermes ve Agentic Dalga

**Format:** Webinar, 90 dk, YouTube kaydı
**Teknik önkoşul:** Yok
**Hedef kitle:** Kamu ve özel sektör teknik/teknik olmayan karar vericiler, yazılımcılar

---

## Akış (90 dk)

### 1. Açılış ve Tanıtım (5 dk)
- KamuYZ APA Çalışma Grubu kimdir?
- Program tanıtımı (E1-E2-E3, çıktılar)
- KamuKod ile iş bölümü

### 2. Agentic AI Nedir? (15 dk)
- Chatbot'tan otonom ajana evrim
- 4 temel fark: planlama, araç kullanımı, hafıza, çok adımlı muhakeme
- Gerçek dünya örneği: "sunucu harcamalarını analiz et, yöneticine e-posta gönder"
- Agentic AI ekosistem manzarası 2026

### 3. OpenClaw Derin Bakış (20 dk)
- Nedir? Kim geliştiriyor? Neden 385K yıldız?
- Mimari: Gateway, Agent Runtime, Channels
- Temel kavramlar: Agent, Tool, Task, Memory, Skill, Provider
- Canlı demo: OpenClaw kurulumu ve ilk komut (5 dk)
- Hangi platformlarda çalışıyor? (Telegram, WhatsApp, Discord, Slack...)
- Hangi modellerle çalışıyor? (Claude, GPT, Grok, yerel Ollama...)

### 4. Hermes ve Learning Loop (15 dk)
- Hermes nedir? OpenClaw'dan farkı
- Kapalı devre öğrenme döngüsü nasıl çalışır?
  - Görev tamamla → belleğe kaydet → SKILL.md üret → kullandıkça iyileştir
- 4 katmanlı bellek mimarisi
- OpenClaw + Hermes birlikte nasıl çalışır?

### 5. Ekosistem ve Trendler (10 dk)
- Multi-agent sistemler
- MCP (Model Context Protocol) standardı
- Self-improving agent'lar
- Skill marketplace'ler
- Türkiye'de agentic AI kimler çalışıyor?

### 6. Sırada Ne Var? (5 dk)
- E2: Güvenlik ve zorluklar (panel)
- E3: Hands-on atölye (canlı kurulum)
- kamuyz-agent-starter reposu
- KamuKod kursuna yönlendirme

### 7. Soru-Cevap (15 dk)

---

## Demo Senaryosu

1. `curl -fsSL https://openclaw.ai/install.sh | bash` ile kurulum
2. `openclaw onboard --install-daemon` ile ilk yapılandırma
3. `openclaw gateway status` ile durum kontrolü
4. Telegram bot oluşturma ve bağlama
5. İlk mesaj: "Merhaba, bugün ne yapabilirim?"
6. Ufak bir görev: "Masaüstümde kaç dosya var?"

---

## Kaynak Gösterimi

- Grok araştırması: Bölüm 1-3
- Gemini Deep Research: Bölüm 1
- openclaw.ai, clawdocs.org, GitHub: openclaw/openclaw
- Hermes: nousresearch/hermes-agent, hermes-agent.nousresearch.com
