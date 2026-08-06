# CONTEXT.md — KamuYZ Agent Starter

Bu belge, projenin kullandığı terimleri ve bu terimlere yüklenen anlamları tanımlar. Her yeni terim, hakkında karar verildiği anda buraya eklenir. Uygulama detayı veya spek içermez; saf sözlüktür.

---

## Agent (Ajan)

Kendi başına hedef belirleyebilen, alt görevlere bölebilen, dış araçları (tools) çalıştırabilen ve oturumlar arası hafıza taşıyan otonom yazılım varlığı. Chatbot'tan farkı: pasif yanıt değil, proaktif aksiyon alır.

## Agentic AI

LLM'lerin planlama, araç kullanımı, hafıza yönetimi ve çok adımlı muhakeme yetenekleriyle donatılarak otonom karar alıcıya dönüştüğü yapay zeka paradigması.

## Agentic Framework

Bir agent oluşturmak ve çalıştırmak için gereken altyapıyı sağlayan yazılım çatısı. Gateway, tool orchestration, memory management, channel connectors gibi katmanları içerir.

## OpenClaw

Peter Steinberger tarafından başlatılan, MIT lisanslı, self-hosted, çok kanallı (WhatsApp, Telegram, Discord, Slack, vb.) kişisel AI agent framework'ü. Gateway-first mimari. GitHub: 385K+ yıldız. Kasım 2025'te Clawdbot adıyla başladı.

## Hermes Agent

Nous Research tarafından geliştirilen, MIT lisanslı, self-improving (kendi kendini iyileştiren) agent runtime'ı. Temel farkı: kapalı devre öğrenme döngüsü (closed learning loop) — başarılı görevlerden otomatik skill üretir ve biriktirir.

## Gateway

OpenClaw mimarisinde merkezi kontrol düzlemi. Oturum yönetimi, mesaj yönlendirme, tool execution ve kanal orkestrasyonunu sağlar. Yerelde 127.0.0.1:18789 üzerinde çalışır.

## Skill (Yetenek)

Ajana öğretilen, tekrar kullanılabilir prosedürel bilgi. Markdown + YAML formatında tanımlanır. agentskills.io standardına uygundur. İki kaynaktan gelir: (1) insan tarafından yazılır, (2) Hermes'te ajan kendi deneyiminden otomatik üretir.

## MCP (Model Context Protocol)

LLM'lerin dış araçlarla (API'ler, veritabanları, dosya sistemleri) güvenli iletişim kurmasını sağlayan açık standart protokol. Agent ekosisteminde tool eklemenin standart yolu.

## ClawHub

OpenClaw'un topluluk tabanlı skill marketplace'i. 10.000+ skill barındırır. Güvenlik riski: denetimsiz skill'ler zararlı kod içerebilir (ClawHavoc olayı).

## Heartbeat

Ajanın arka planda sürekli çalışmasını sağlayan mekanizma. Belirli aralıklarla görev listesini kontrol eder, proaktif aksiyon alır. Long-running agent davranışının temeli.

## Learning Loop (Öğrenme Döngüsü)

Hermes'in temel inovasyonu: (1) karmaşık görevi tamamla, (2) episodic memory'ye kaydet, (3) başarılı iş akışını SKILL.md olarak çıkar, (4) skill'i kullanım sırasında iyileştir. Diğer framework'lerden farkı: skill'ler insan tarafından değil, ajan tarafından deneyimden üretilir.

## Prompt Injection

LLM tabanlı sistemlerde veri (data) ile talimatın (instruction) birbirinden ayrılamamasından kaynaklanan güvenlik zafiyeti. İki türü: (1) Doğrudan (direct) — kullanıcı girdisiyle sistem prompt'unu geçersiz kılma, (2) Dolaylı (indirect) — dış kaynaktan (e-posta, web sayfası, PDF) okunan içeriğin ajan tarafından komut olarak algılanması.

## Lethal Trifecta (Ölümcül Üçlü)

Agentic sistemlerde güvenliği imkansız kılan üç unsurun kesişimi: (1) güvenilmeyen girdilere erişim, (2) yüksek yetkili araç kullanımı (shell, dosya sistemi), (3) kalıcı hafıza yapısı. Bu üçü aynı anda varsa sistem güvenli kabul edilemez.

## CVE-2026-25253

OpenClaw 2026.1.29 öncesi sürümlerde, URL'deki `gatewayUrl` parametresine otomatik WebSocket bağlantısı kurup auth token'ı sızdıran zafiyet. CVSS 8.8. One-click RCE'ye yol açar. Yamalandı.

## Human-In-The-Loop (HITL)

Kritik aksiyonlarda (veri silme, finansal işlem, dışarı e-posta) ajanın otonom hareket etmesini engelleyip insan onayı isteyen güvenlik mekanizması.

## Least Privilege (En Az Yetki)

Ajana yalnızca görevi için gerekli minimum yetkilerin verilmesi ilkesi. İşletim sistemi (non-root kullanıcı), ağ (sadece yetkili endpoint'ler), API (bounded-scope anahtarlar) katmanlarında uygulanır.

## Sandbox

Ajanın çalışma zamanı ortamının sistemin geri kalanından izole edilmesi. Docker/AppArmor/seccomp profilleriyle sağlanır. Shell komutlarının isolated modda çalıştırılması.

## Private Skill Registry (Özel Yetenek Deposu)

Kurumların, ClawHub gibi halka açık pazarlar yerine kendi kod incelemesinden geçmiş onaylı skill'leri barındırdığı dahili depo. Tedarik zinciri riskini azaltır.

## kamuyz-agent-starter

Bu repo. Türkçe dokümante, güvenlik-öncelikli, OpenClaw ve Hermes için başlangıç template'i. Hedef: E3 atölyesinde canlı kurulum yapılabilir seviyede, üretime hazır yapılandırma.

## KamuKod

Üyelik bazlı 4 haftalık uygulamalı kurs. "Nasıl kurulur" sorusunu cevaplar. KamuYZ APA ile iş bölümü: KamuKod kurulumu, biz "nedir, güvenli mi, ne zaman kullanılmalı" sorularını cevaplarız.

## DDO BİGR

T.C. Cumhurbaşkanlığı Dijital Dönüşüm Ofisi Bilgi ve İletişim Güvenliği Rehberi. Kamu kurumları için bağlayıcı güvenlik standardı. Agentic sistemlerin kurum içinde çalıştırılmasında uyulması gereken referans çerçeve.
