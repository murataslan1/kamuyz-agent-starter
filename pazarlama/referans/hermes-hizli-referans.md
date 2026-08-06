# Hızlı Referans Kartı — Hermes Agent

Bu kart, workshop katılımcılarına oturum sonunda dağıtılmak üzere hazırlanmıştır. Tek sayfaya sığar.

---

## Hermes Agent — Temel Komutlar

```bash
# Kurulum (güvenli paket)
curl -fsSL https://raw.githubusercontent.com/murataslan1/kamuyz-agent-starter/main/hermes-paket/install.sh | bash

# Gateway başlat/durdur/durum
openclaw gateway start
openclaw gateway stop
openclaw gateway status

# Telegram pairing (güvenli eşleştirme)
openclaw pairing list telegram
openclaw pairing approve telegram <KOD> --notify

# Docker ile yönetim
cd ~/.hermes-paket
docker compose up -d
docker compose down
docker compose logs -f
```

---

## Hermes — 4 Katmanlı Hafıza

| Katman | İsim | Ne? |
|---|---|---|
| L1 | Session Context | Anlık konuşma, oturum kapanınca silinir |
| L2 | Persisted Facts | MEMORY.md (~2.200 karakter), kalıcı |
| L3 | Session Archive | SQLite FTS5, tüm geçmiş aranabilir |
| L4 | Procedural Skills | Kendi yazdığı SKILL.md, dinamik yüklenir |

---

## Hermes — Öğrenme Döngüsü

```
GÖREV → TAMAMLA → ANALİZ → SKILL.md → TEKRAR KULLAN → İYİLEŞTİR
```

---

## Güvenlik Kontrol Listesi (ilk 5)

- [ ] Gateway sadece 127.0.0.1'te (loopback)
- [ ] Non-root kullanıcı (Docker: user "1000:1000")
- [ ] Sandbox aktif (mode: isolated)
- [ ] Telegram: dmPolicy "pairing"
- [ ] Versiyon >= 2026.1.29 (CVE-2026-25253 yamalı)

---

## Sık Kullanılan Adresler

| Ne? | Link |
|---|---|
| GitHub repo | github.com/murataslan1/kamuyz-agent-starter |
| KamuKOD 210 | kamukod.lovable.app/atolye/210 |
| OpenClaw docs | docs.openclaw.ai |
| Hermes docs | hermes-agent.nousresearch.com |
| OpenClaw repo | github.com/openclaw/openclaw |
| Hermes repo | github.com/nousresearch/hermes-agent |

---

## Karar Ağacı: OpenClaw vs Hermes

```
Çok kanal (WhatsApp, Telegram, Slack...) → OpenClaw
Kendi kendine öğrensin, tekrarlayan iş → Hermes
Hızlı kurulum, düşük bakım → Hermes
Geniş ekosistem, çok eklenti → OpenClaw
İkisi birden → OpenClaw (iletişim) + Hermes (beyin)
```
