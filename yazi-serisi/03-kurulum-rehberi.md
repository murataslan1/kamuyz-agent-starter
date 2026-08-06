# Sıfırdan Ajan Kurulumu: Adım Adım Rehber

**KamuYZ APA Çalışma Grubu — Yazı Serisi #3**

---

İlk iki yazıda yapay zeka ajanlarının ne olduğunu ve güvenlik risklerini anlattık. Şimdi sıra uygulamada: **kendi ajanınızı kuralım.**

Bu rehber, KamuYZ APA'nın `kamuyz-agent-starter` reposundaki güvenli kurulum paketini kullanır. Teknik bilgi şart değil — komut satırına yazı yazabiliyorsanız yeterli.

---

## Gereksinimler

Başlamadan önce:

- ✅ Node.js 20+ ([nodejs.org](https://nodejs.org))
- ✅ Docker 24+ ([docs.docker.com/get-docker](https://docs.docker.com/get-docker))
- ✅ Git ([git-scm.com](https://git-scm.com))
- ✅ Telegram hesabı (bot oluşturmak için)
- ✅ API anahtarı (Anthropic, OpenAI veya OpenRouter)

---

## Adım 1: Tek Komutla Kurulum

Terminali açın ve şunu çalıştırın:

```bash
curl -fsSL https://raw.githubusercontent.com/murataslan1/kamuyz-agent-starter/main/hermes-paket/install.sh | bash
```

Bu betik şunları yapar:
1. Docker, Python, Git kurulumlarını kontrol eder
2. Hermes Agent'ı indirir
3. Güvenli yapılandırmayı uygular (sandbox açık, non-root, loopback)
4. Docker Compose dosyasını hazırlar
5. `.env` dosyası oluşturur

Kurulum dizini: `~/.hermes-paket/`

---

## Adım 2: API Anahtarını Tanımlayın

```bash
cd ~/.hermes-paket
nano .env
```

`.env` dosyasına API anahtarınızı girin:

```env
ANTHROPIC_API_KEY=sk-ant-...
# veya
OPENROUTER_API_KEY=sk-or-...
```

**Önemli:** API anahtarınızı **bounded-scope** (sınırlı yetkili) olarak oluşturun. Sadece gerekli endpoint'lere erişimi olan bir anahtar kullanın.

---

## Adım 3: Başlatın

```bash
docker compose up -d
```

Birkaç saniye içinde ajanınız çalışmaya başlayacak. Kontrol edin:

```bash
docker compose ps
docker compose logs -f
```

"✅ Gateway started on 127.0.0.1:18789" mesajını görmelisiniz.

---

## Adım 4: Telegram Botu Oluşturun

1. Telegram'da **@BotFather** hesabına gidin
2. `/newbot` komutunu gönderin
3. Bot için bir isim ve kullanıcı adı belirleyin (sonu `bot` ile bitmeli)
4. Size verilen **Bot Token**'ı kopyalayın

Güvenlik için hemen `/setprivacy` komutunu çalıştırıp **Enable** yapın. Bu, botun sadece etiketlendiğinde mesajları okumasını sağlar.

---

## Adım 5: Telegram'ı Ajana Bağlayın

`~/.hermes-paket/config/config.toml` dosyasını açın:

```bash
nano ~/.hermes-paket/config/config.toml
```

Şu satırları bulun ve güncelleyin:

```toml
[channels]
telegram_enabled = true
telegram_bot_token = "SİZİN_BOT_TOKEN"
telegram_dm_policy = "pairing"
```

`.env` dosyasına da token'ı ekleyin:

```env
TELEGRAM_BOT_TOKEN=SİZİN_BOT_TOKEN
```

Ajanı yeniden başlatın:

```bash
docker compose restart
```

---

## Adım 6: Pairing ile Güvenli Eşleştirme

Telegram'dan botunuza bir mesaj atın. Bot size 8 haneli bir onay kodu gönderecek.

Kodu onaylamak için:

```bash
docker compose exec hermes-agent hermes pairing list telegram
docker compose exec hermes-agent hermes pairing approve <KOD> --notify
```

Artık botunuz sadece **sizin** mesajlarınıza cevap verecek.

---

## Adım 7: İlk Görevi Verin

Telegram'dan botunuza mesaj atın:

> "Merhaba, kendini tanıtır mısın?"

Cevap geliyorsa, ajanınız çalışıyor demektir. Şimdi gerçek bir görev verin:

> "Masaüstümde kaç dosya var?"

> "Bugünün tarihi nedir?"

> "Şu anki hava durumunu söyleyebilir misin?"

---

## Adım 8: Güvenlik Kontrol Listesini Tamamlayın

Production'a almadan önce [SECURITY.md](https://github.com/murataslan1/kamuyz-agent-starter/blob/main/SECURITY.md)'deki 24 maddeyi kontrol edin.

En kritik 5 maddeyi hemen şimdi kontrol edin:

```bash
# 1. Gateway sadece loopback'te mi?
docker compose exec hermes-agent netstat -an | grep 18789
# → 127.0.0.1:18789 olmalı, 0.0.0.0:18789 olmamalı

# 2. Non-root kullanıcı mı?
docker compose exec hermes-agent whoami
# → root olmamalı

# 3. Sandbox aktif mi?
docker inspect hermes_secure | grep -A5 SecurityOpt
# → no-new-privileges:true görünmeli

# 4. Audit log yazıyor mu?
ls -la ~/.hermes-paket/logs/
# → hermes.log mevcut olmalı

# 5. Versiyon güncel mi?
docker compose exec hermes-agent hermes --version
# → >= 2026.1.29 olmalı (CVE yaması)
```

---

## Sık Karşılaşılan Hatalar

| Hata | Çözüm |
|---|---|
| "port 18789 already in use" | `lsof -i :18789` ile process'i bulup kapatın |
| Telegram bot yanıt vermiyor | BotFather'da `/setprivacy` → Enable yaptınız mı? |
| Docker permission denied | `sudo usermod -aG docker $USER` |
| API anahtarı hatası | `.env` dosyasını kontrol edin, doğru formatta mı? |

---

## Sırada ne var?

- **Derinleşmek isteyenler için:** Detaylı araştırma raporlarımızı okuyun — [docs/research/](https://github.com/murataslan1/kamuyz-agent-starter/tree/main/docs/research)
- **Daha fazla öğrenmek isteyenler için:** [LEARNING.md](https://github.com/murataslan1/kamuyz-agent-starter/blob/main/LEARNING.md) — 2 haftalık yapılandırılmış plan
- **Kurumsal kullanım için:** Güvenlik ve regülasyon değerlendirmelerimizi inceleyin

---

*Bu rehber, KamuYZ APA Çalışma Grubu'nun "OpenClaw & Hermes — Açık Kaynak Agentic Framework Programı" kapsamında hazırlanmıştır. Tüm çıktılar vendor-nötr ve açık erişimdir.*
