# GLOSSARY.md — Türkçe-İngilizce Agentic AI Terimler Sözlüğü

Bu sözlük, agentic AI ekosisteminde kullanılan İngilizce terimlerin Türkçe karşılıklarını ve açıklamalarını içerir. Teknik terimlerin orijinali parantez içinde verilmiştir.

---

## A

**Agent (Ajan):** Hedef odaklı, otonom karar alabilen, araç kullanabilen yapay zeka yazılımı.
**Agentic AI (Etken YZ):** LLM'lerin planlama, araç kullanımı ve hafıza yetenekleriyle donatıldığı otonom sistem paradigması.
**Approval Gate (Onay Kapısı):** Kritik aksiyonlarda insan onayı isteyen güvenlik mekanizması (bkz. HITL).
**Audit Trail (Denetim İzi):** Ajanın aldığı tüm kararların ve aksiyonların kayıt altına alınması.

## B

**Bounded Memory (Sınırlandırılmış Hafıza):** Hermes'in 4 katmanlı bellek mimarisinde, belirli karakter limitleriyle çalışan hafıza katmanları.
**Brainstorming (Fikir Geliştirme):** Kod yazmadan önce tasarımın sorgulanarak netleştirildiği aşama.

## C

**Channel (Kanal):** Ajanın kullanıcılarla iletişim kurduğu platform (Telegram, WhatsApp, Discord, Slack, vb.).
**Closed Learning Loop (Kapalı Devre Öğrenme Döngüsü):** Hermes'in başarılı görevlerden otomatik skill üretme mekanizması.
**ClawHub:** OpenClaw'un topluluk tabanlı skill marketplace'i.
**Context Window (Bağlam Penceresi):** LLM'in bir seferde işleyebildiği maksimum token sayısı.
**Credential (Kimlik Bilgisi):** API anahtarı, token, şifre gibi yetkilendirme verileri.

## D

**Daemon (Artalan Süreci):** Arka planda sürekli çalışan servis. OpenClaw'da `--install-daemon` ile kurulur.
**Data Exfiltration (Veri Sızıntısı):** Hassas verilerin yetkisiz şekilde sistem dışına çıkarılması.
**Direct Prompt Injection (Doğrudan Komut Enjeksiyonu):** Kullanıcının ajan arayüzüne doğrudan girerek sistem komutlarını geçersiz kılması.
**DM Policy (Doğrudan Mesaj Politikası):** OpenClaw'da kullanıcıların ajana erişimini kontrol eden güvenlik ayarı.

## E

**Episodic Memory (Olay Bazlı Hafıza):** Ajanın geçmiş görevlerini, başarı/başarısızlık durumlarını kaydettiği bellek türü.
**Egress Filtering (Dışa Akış Filtreleme):** Ajanın internet erişiminin sadece yetkili adreslere sınırlanması.

## G

**Gateway:** OpenClaw'da merkezi kontrol düzlemi. Oturum, mesaj, araç ve kanal yönetimini sağlar.
**Guardrails (Güvenlik Korkulukları):** Ajanın istenmeyen davranışlarını engelleyen kısıtlamalar.

## H

**Heartbeat (Kalp Atışı):** Ajanın arka planda periyodik olarak görev listesini kontrol ettiği mekanizma.
**HITL (Human-In-The-Loop):** İnsan denetimli onay mekanizması.
**Hardening (Sıkılaştırma):** Sistemin güvenlik ayarlarının varsayılandan daha kısıtlayıcı hale getirilmesi.

## I

**Indirect Prompt Injection (Dolaylı Komut Enjeksiyonu):** Dış kaynaktan okunan verinin ajan tarafından komut olarak algılanması.
**Isolation (İzolasyon):** Ajanın sistemin geri kalanından ayrı, kısıtlı bir ortamda çalıştırılması.

## L

**Learning Loop (Öğrenme Döngüsü):** Hermes'te görev → bellek → skill → iyileştirme döngüsü.
**Least Privilege (En Az Yetki):** Ajana yalnızca görevi için gerekli minimum yetkinin verilmesi.
**Lethal Trifecta (Ölümcül Üçlü):** Güvenilmeyen girdi + yüksek yetki + kalıcı hafıza kesişimi.
**LLM (Large Language Model — Büyük Dil Modeli):** GPT, Claude, Grok gibi büyük ölçekli dil modelleri.
**Local-First (Yerel Öncelikli):** Verinin varsayılan olarak kullanıcının kendi makinesinde kaldığı mimari yaklaşım.

## M

**MCP (Model Context Protocol):** LLM'lerin dış araçlarla güvenli iletişim kurmasını sağlayan açık standart.
**Memory Poisoning (Hafıza Zehirlenmesi):** Uzun süreli belleğe zararlı girdi enjekte edilmesi.
**MEMORY.md:** Ajanın kalıcı hafıza dosyası. Ortam bilgileri ve mimari kararları saklar.
**Multi-Agent System (Çoklu Ajan Sistemi):** Birden fazla ajanın iş birliği yaptığı mimari.

## O

**Onboarding (İlk Kurulum):** `openclaw onboard` komutu ile ajanın ilk yapılandırması.
**Orchestration (Orkestrasyon):** Birden fazla araç, kanal ve alt ajanın koordinasyonu.
**Origin Validation (Kaynak Doğrulama):** WebSocket bağlantılarında istek kaynağının doğrulanması (CVE-2026-25253 sonrası zorunlu).

## P

**Pairing (Eşleştirme):** OpenClaw'da yeni kullanıcıların onay kodlarıyla yetkilendirilmesi.
**Payload (Yük):** Saldırganın hedef sisteme iletmek istediği zararlı kod veya veri.
**Persistent Memory (Kalıcı Hafıza):** Oturumlar arası taşınan, silinmeyen bellek.
**Prompt Injection (Komut Enjeksiyonu):** LLM tabanlı sistemlerde veri-talimat ayrımı yapılamamasından kaynaklanan zafiyet.
**Provider (Sağlayıcı):** LLM servisi sunan şirket veya servis (Anthropic, OpenAI, xAI, vb.).

## R

**RCE (Remote Code Execution — Uzaktan Kod Çalıştırma):** Saldırganın hedef sistemde keyfi kod çalıştırabilmesi.
**Regulated Sector (Regüle Sektör):** Finans, sağlık, enerji, kamu gibi özel düzenlemelere tabi sektörler.

## S

**Sandbox (Korumalı Alan):** Ajanın sistemin geri kalanından izole çalıştığı güvenlik ortamı.
**Secret Management (Sır Yönetimi):** API anahtarı ve kimlik bilgilerinin güvenli saklanması.
**Self-Hosted (Kendi Sunucusunda):** Yazılımın üçüncü parti bulut yerine kullanıcının kendi altyapısında çalışması.
**Self-Improving (Kendini İyileştiren):** Sistemin kendi deneyimlerinden öğrenerek yeteneklerini geliştirmesi.
**Skill (Yetenek):** Ajana öğretilen, Markdown+YAML formatında tanımlanan prosedürel bilgi.
**SOUL.md:** Ajanın kişilik ve davranış tanım dosyası.
**Subagent (Alt Ajan):** Ana ajan tarafından belirli görevler için geçici olarak oluşturulan yardımcı ajan.
**Supply Chain (Tedarik Zinciri):** Üçüncü parti eklenti, araç ve kütüphanelerin oluşturduğu risk yüzeyi.

## T

**TDD (Test-Driven Development — Test Güdümlü Geliştirme):** Önce test yaz, testi başarısız gör, minimum kod yaz, testi geç, düzelt.
**Token:** LLM'lerde metnin işlenebilir en küçük birimi.
**Tool (Araç):** Ajanın kullanabildiği dış fonksiyon veya API (shell, dosya sistemi, tarayıcı, vb.).

## V

**Vendor-Neutral (Tedarikçi Bağımsız):** Belirli bir şirket veya ürüne bağlı olmayan, taşınabilir değerlendirme.
**vLLM / Ollama:** Yerel (local) LLM çalıştırmaya yarayan açık kaynak araçlar.

## W

**WebSocket:** İstemci-sunucu arasında çift yönlü, sürekli bağlantı protokolü. OpenClaw Control UI'da kullanılır.
