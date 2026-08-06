# Grok Araştırma Sonucu — OpenClaw & Hermes Ekosistem Taraması

**Tarih:** Ağustos 2026
**Kaynak:** Grok (xAI) araştırma taraması
**Amaç:** E1, E2, E3 etkinlikleri ve kamuyz-agent-starter reposu için kaynak oluşturmak

> Bu dosya, Grok araştırma prompt'una verilen yanıtın orijinalidir.
> Tam prompt için: `grok-research-prompt.md`

## İçindekiler

### Bölüm 1: OpenClaw — Nedir, Nasıl Çalışır?

- **Mimari:** TypeScript/Node.js, MIT lisans, 385K yıldız, 81K çatal
- **Katmanlar:** Gateway (kontrol düzlemi), Agent Runtime (LLM çağrıları), Connectors (WhatsApp, Telegram, Discord, Slack, Signal, iMessage, 50+)
- **Core kavramlar:** Agent, Tool (MCP), Task (Heartbeat), Memory (Markdown/YAML), Provider (model-agnostic), Skills (ClawHub 10.000+)
- **Yerel model desteği:** Ollama, vLLM
- **Güvenlik modeli:** Sandbox (opsiyonel), VirusTotal skill tarama, MCP trust tier, SOUL.md koruması, HITL onay
- **Sistem gereksinimleri:** Node.js 20+, Docker/K8s destekli

### Bölüm 2: Hermes — Learning Loop Farkı

- **Konum:** Nous Research, MIT lisans, OpenClaw'dan bağımsız ayrı proje
- **`hermes claw migrate`:** Persona, bellek ve skill taşıma desteği
- **Closed learning loop:** Görev → episodic memory → SKILL.md (agentskills.io) → kullandıkça iyileştir
- **4 katmanlı bellek:** Prompt Memory (MEMORY.md + USER.md), Skills, Session Archive (FTS5), User Model (Honcho)
- **Kullanım alanı:** Tekrarlayan iş akışları, uzun süreli asistanlık, research pipeline

### Bölüm 3: Agentic AI Ekosistem Manzarası 2026

- **OpenClaw:** En büyük community, çok kanallı gateway, skill ekosistemi
- **Hermes Agent:** Self-improving skill'ler, uzun vadeli öğrenme
- **CrewAI:** Role-based multi-agent, Fortune 500 benimseme
- **LangGraph:** State-machine tabanlı, production-grade güvenilirlik
- **Agno:** Hafif, hızlı, düşük overhead
- **Diğer:** AutoGPT, Microsoft Agent Framework/AutoGen, OpenAI Agents SDK, Google ADK
- **Trendler:** Multi-agent, MCP standartlaşması, self-improving, heartbeat, skill marketplace, local-first + serverless hibrit

### Bölüm 4: Güvenlik — Zafiyetler, Saldırılar, Riskler

- **CVE-2026-25253:** `gatewayUrl` → WebSocket → token exfiltration → 1-click RCE, CVSS 8.8
- **ClawHub zararlıları:** %12-17 zararlı skill, 341 ClawHavoc AMOS bilgi hırsızı
- **Çin kısıtlaması (Mart 2026):** MIIT/SASAC/CNCERT, "lethal trifecta" gerekçesiyle yasak
- **Prompt injection:** Doğrudan (jailbreaking) ve dolaylı (e-posta/web/PDF)
- **Data exfiltration vektörleri:** Tool çağrıları, mesajlaşma kanalları, zararlı skill'ler
- **Credential yönetimi:** Environment variable, least privilege, sandbox, audit, rotasyon
- **Standartlar:** OWASP LLM Top 10, NIST AI RMF, ISO/IEC 42001, EU AI Act

### Bölüm 5: Regülasyon ve Kurumsal Değerlendirme

- **EU AI Act:** Transparency (Madde 50, Ağustos 2026), high-risk sınıflandırma
- **ABD:** NIST AI RMF (gönüllü), AI AGENT Act taslağı 2026
- **Singapur:** Bankacılık spesifik agentic kurallar
- **Kurumsal değerlendirme çerçevesi (12 soru):** İş süreci uygunluğu, HITL, veri yerleşikliği, supply-chain, audit, credential, sandbox, model bağımsızlığı, maliyet, regülasyon, incident response, şeffaflık
