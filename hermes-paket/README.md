# Güvenli Hermes Paketi

> Tek komutla kur. Güvenli. Türkçe. Pardus gibi.

Bu paket, **Hermes Agent'ı** güvenlik öncelikli varsayılanlarla, tek komutla kuran bir başlangıç setidir. Kamu kurumları ve güvenlik hassasiyeti olan ekipler için hazırlanmıştır.

---

## Neden bu paket?

Hermes'i sıfırdan kurduğunda:
- Hafıza modülü varsayılan olarak **kapalı** gelir → öğrenemez
- Sandbox **kapalı** gelir → sistemin tamamına erişir
- Onay mekanizması **kapalı** gelir → kritik komutları sormaz
- Dış ağa **açık** gelebilir → güvenlik riski

Bu paket tüm bunları tersine çevirir: **önce güvenlik, sonra kullanım.**

---

## Tek komutla kur

```bash
curl -fsSL https://raw.githubusercontent.com/murataslan1/kamuyz-agent-starter/main/hermes-paket/install.sh | bash
```

Kurulum 6 adımda tamamlanır:
1. Gereksinim kontrolü (Docker, Python, Git)
2. Hermes Agent indirme
3. Güvenli yapılandırma uygulama
4. Docker Compose hazırlama
5. `.env` dosyası oluşturma
6. Başlatma

---

## Güvenlik varsayılanları

| Ayar | Varsayılan (normal) | Bu pakette |
|---|---|---|
| Gateway bağlantısı | `0.0.0.0` (herkese açık) | `127.0.0.1` (sadece yerel) |
| Kullanıcı | `root` | `1000:1000` (servis hesabı) |
| Sandbox | Kapalı | Açık + `isolated` mod |
| Hafıza / öğrenme | Kapalı | Açık (skill_generation = true) |
| Komut onayı | Kapalı | Açık (kritik komutlarda sorar) |
| Token bütçesi | Sınırsız | Görev başı 100.000 token limit |
| Docker yetkileri | Tam | `no-new-privileges:true` + `cap_drop: ALL` |
| Ağ | Dışa açık | `internal: true` (sadece container'lar arası) |
| Config | Yazılabilir | Salt okunur (`:ro`) |
| Audit log | Kapalı | Açık (tüm komutlar kayıt altında) |
| Telegram | Varsayılan ayarlar | `dmPolicy: pairing` (onaylı kullanıcı) |

---

## Dosya yapısı

```
~/.hermes-paket/
├── install.sh               ← Kurulum betiği
├── docker-compose.yml       ← Güvenli Docker yapılandırması
├── .env                     ← API anahtarların (sana özel)
├── config/
│   └── config.toml          ← Güvenli varsayılanlar
├── workspace/               ← Çalışma alanı
├── data/
│   ├── memory/              ← Kalıcı hafıza (L2)
│   └── skills/              ← Kendi yazdığı skill'ler (L4)
└── logs/                    ← Audit log'lar
```

---

## Kurulum sonrası

```bash
# Durum kontrolü
cd ~/.hermes-paket
docker compose ps

# Log'ları izle
docker compose logs -f

# Durdur
docker compose down

# Güncelle
docker compose pull && docker compose up -d
```

---

## Telegram bağlama (opsiyonel)

1. `config/config.toml` dosyasında `telegram_enabled = true` yap
2. `.env` dosyasına `TELEGRAM_BOT_TOKEN` ekle
3. `docker compose restart`
4. Telegram'dan bota mesaj at
5. Pairing kodunu onayla: `docker compose exec hermes-agent hermes pairing approve <KOD>`

---

## Gereksinimler

- Docker 24+
- Python 3.10+
- Git
- 4 GB RAM (önerilen)
- API anahtarı (Anthropic veya OpenRouter)

---

## Sık Sorulan Sorular

**Pardus'ta çalışır mı?**  
Evet. Docker'ın çalıştığı her yerde çalışır. Pardus, Ubuntu, Debian, macOS, Windows (WSL2).

**Verilerim nerede?**  
`~/.hermes-paket/data/` altında. Sadece senin makinede. Dışarı çıkmaz.

**Güncellemeleri nasıl alırım?**  
`docker compose pull && docker compose up -d`

**Ücretsiz model kullanabilir miyim?**  
Evet. `config.toml`'da `fallback_model` olarak OpenRouter'daki ücretsiz modelleri tanımla (Llama, Mistral vb).
