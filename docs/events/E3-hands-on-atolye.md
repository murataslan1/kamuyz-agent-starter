# E3 — Hands-on Atölye: Canlı Kurulum

**Format:** Online atölye, 2-3 saat, sınırlı kontenjan
**Teknik önkoşul:** Node.js 20+, Docker (opsiyonel), Telegram hesabı
**Hedef:** Her katılımcı kendi OpenClaw ajanını kurar, Telegram'a bağlar, güvenlik checklist'ini uygular

---

## Atölye Öncesi Katılımcı Hazırlığı

Katılımcılara 3 gün öncesinden gönderilecek:

```
Merhaba,

E3 Hands-on Atölye'ye hazırlık için lütfen aşağıdakileri tamamlayın:

1. Node.js 20+ kurun: https://nodejs.org
2. Telegram hesabınızı hazırlayın
3. (Opsiyonel) Docker kurun: https://docs.docker.com/get-docker/
4. kamuyz-agent-starter reposunu klonlayın:
   git clone https://github.com/kamuyz/kamuyz-agent-starter
5. LEARNING.md'deki Hafta 1 okumalarını gözden geçirin

Atölye günü görüşmek üzere!
```

---

## Akış (150-180 dk)

### Bölüm 1: Kurulum (45 dk)

**1a. OpenClaw Native Kurulum (20 dk)**

```bash
# Adım 1: Kurulum betiği
curl -fsSL https://openclaw.ai/install.sh | bash

# Adım 2: İlk yapılandırma
openclaw onboard --install-daemon

# Adım 3: Sihirbazı takip et
# - LLM provider seçimi (Claude, GPT, Grok, Ollama)
# - API anahtarı girme
# - Temel tercihler

# Adım 4: Doğrulama
openclaw gateway status
openclaw dashboard
```

**1b. Telegram Bot Oluşturma (15 dk)**

```
1. Telegram'da @BotFather'a /newbot komutu gönder
2. Bot adı ve kullanıcı adı belirle
3. Bot Token'ı kopyala
4. /setprivacy → Enable (sadece etiketlenince okusun)
```

**1c. Telegram'ı OpenClaw'a Bağlama (10 dk)**

```bash
# config/default.json5 dosyasına ekle:
# channels.telegram.enabled = true
# channels.telegram.botToken = "SENİN_TOKEN"
# channels.telegram.dmPolicy = "pairing"

# Gateway'i yeniden başlat
openclaw gateway restart
```

---

### Bölüm 2: Güvenlik Sıkılaştırma (30 dk)

**2a. Temel Güvenlik Kontrolleri (15 dk)**

SECURITY.md checklist'i üzerinden teker teker kontrol:

| # | Kontrol | Komut/Ayar |
|---|---|---|
| 1 | Gateway portu kontrolü | `netstat -an | grep 18789` → sadece 127.0.0.1 |
| 2 | Versiyon kontrolü | `openclaw --version` → >= 2026.1.29 |
| 3 | allowedOrigins | Config'e ekle |
| 4 | dmPolicy pairing | Config'te "pairing" olarak ayarla |
| 5 | Non-root kullanıcı | `whoami` → root değil |

**2b. Pairing ile Güvenli Eşleştirme (15 dk)**

```bash
# Katılımcı kendi Telegram botuna mesaj atar
# Sistem yöneticisi (katılımcının kendisi):
openclaw pairing list telegram

# Çıktı: KULLANICI_ADI — EŞLEŞTİRME_KODU
openclaw pairing approve telegram <KOD> --notify
```

---

### Bölüm 3: Docker ile Üretim Kurulumu (30 dk)

**3a. docker-compose.yml İncelemesi (10 dk)**

- Non-root user, no-new-privileges, cap_drop
- Loopback binding
- Volume yapılandırması (config:ro, workspace:rw)
- Environment değişkenleri

**3b. Docker ile Başlatma (20 dk)**

```bash
# .env dosyası oluştur
cat > .env << EOF
ANTHROPIC_API_KEY=sk-ant-...
TELEGRAM_BOT_TOKEN=...
EOF

# Başlat
docker compose up -d

# Durum kontrolü
docker compose ps
docker compose logs -f
```

---

### Bölüm 4: İlk Görev ve Skill Denemesi (30 dk)

**4a. İlk Görev (15 dk)**

Telegram'dan ajana mesaj at:
- "Merhaba, kendini tanıtır mısın?"
- "Bugünün tarihi nedir?"
- "Masaüstümdeki dosyaları listeler misin?"
- "Şu anki hava durumunu söyleyebilir misin?"

**4b. Skill Yükleme (15 dk)**

```bash
# Bir ClawHub skill'i yükle (kontrollü ortamda)
openclaw skill install <skill-adi>

# Ajanın yeni skill ile çalıştığını test et
```

---

### Bölüm 5: Güvenlik Checklist'i Tamamlama (15 dk)

Her katılımcı kendi kurulumunda SECURITY.md'deki 24 maddeyi kontrol eder:

- [ ] Gateway portu kapalı
- [ ] CVE yaması uygulandı
- [ ] Origin doğrulaması aktif
- [ ] Pairing modu açık
- [ ] Non-root çalışıyor
- [ ] API anahtarları bounded-scope
- [ ] Sandbox aktif
- [ ] ClawHub kapalı
- [ ] Loglama aktif
- [ ] ... (24 madde)

---

### Bölüm 6: Soru-Cevap ve Sonraki Adımlar (15 dk)

- Karşılaşılan sorunlar ve çözümler
- "Bundan sonra ne yapabilirim?"
- KamuKod kursuna yönlendirme
- Topluluk kanalları (WhatsApp, Discord)
- Geri bildirim formu

---

## Atölye Sonrası

- Katılımcılara SECURITY.md checklist'inin PDF'i gönderilir
- Atölye kaydı (teknik bölüm) YouTube'a yüklenir
- Atölye retrospektifi blog yazısı olarak yayınlanır
- Repo'ya katkı için CONTRIBUTING.md yönlendirmesi yapılır

---

## Acil Durum ve Sık Karşılaşılan Hatalar

| Hata | Çözüm |
|---|---|
| "port 18789 already in use" | `lsof -i :18789` ile process bul ve kapat |
| "gateway connection refused" | `openclaw gateway restart` |
| Telegram bot yanıt vermiyor | BotFather'da /setprivacy → Enable kontrol et |
| "npm: command not found" | Node.js 20+ kur |
| Docker permission denied | `sudo usermod -aG docker $USER` |
