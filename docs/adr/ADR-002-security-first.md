# ADR-002: Güvenlik-öncelikli varsayılanlar

**Tarih:** 2026-08-06
**Durum:** Kabul edildi
**Karar veren:** KamuYZ APA Çalışma Grubu

## Bağlam

Araştırma sonuçları (Grok + Gemini Deep Research), agentic AI sistemlerinde güvenliğin en kritik başarısızlık noktası olduğunu gösterdi:

- **CVE-2026-25253:** URL'den gelen `gatewayUrl` parametresine otomatik WebSocket bağlantısı → token sızıntısı → RCE (CVSS 8.8)
- **ClawHavoc:** ClawHub'da 820+ zararlı skill, 341'i AMOS bilgi hırsızı
- **Lethal Trifecta:** Güvenilmeyen girdi + yüksek yetki + kalıcı hafıza = güvenlik imkansız
- **Çin 2026:** MIIT/SASAC/CNCERT kamu kurumlarında kullanımı yasakladı

Bu repo, "kur ve unut" yaklaşımına karşı güvenlik-öncelikli bir duruş sergilemelidir.

## Karar

Repo, güvenlik-öncelikli varsayılanları zorunlu kılar:

1. **docker-compose.yml** varsayılan olarak:
   - Non-root kullanıcı (`user: "1000:1000"`)
   - Sadece loopback binding (`127.0.0.1:18789`)
   - `no-new-privileges:true` + `cap_drop: ALL`
   - `allowedOrigins` kısıtlaması

2. **config/** örnekleri:
   - `dmPolicy: "pairing"` varsayılan
   - `requireMention: true` grup sohbetlerinde
   - Sandbox `mode: "isolated"`

3. **SECURITY.md** zorunlu kontrol listesi (24 madde)

4. **LEARNING.md** okuma listesinde güvenlik 2. haftanın ana konusu

## Sonuçlar

- E3 atölyesinde güvenlik checklist'i canlı uygulanır
- E2 panelinde bu kararların gerekçeleri anlatılır
- Whitepaper'da vendor-nötr güvenlik gereksinimleri bu temelden türer
- Kurumlar "güvenlik checklist'ini geçtim" diyerek kullanıma başlayabilir
