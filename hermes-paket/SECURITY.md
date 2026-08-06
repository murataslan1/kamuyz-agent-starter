# Hermes Güvenlik Kontrol Listesi

Bu liste, Güvenli Hermes Paketi ile kurulan sistemin canlı ortama (production) alınmadan önce kontrol edilmesi gereken maddeleri içerir.

---

## Zorunlu Kontroller (10/10)

| # | Kontrol | Nasıl test edilir? | Durum |
|---|---|---|---|
| 1 | Gateway sadece loopback'te | `docker compose exec hermes-agent netstat -an \| grep 18789` → sadece 127.0.0.1 | [ ] |
| 2 | Non-root kullanıcı | `docker compose exec hermes-agent whoami` → root değil | [ ] |
| 3 | Sandbox aktif | `docker inspect hermes_secure \| grep -A5 SecurityOpt` → no-new-privileges | [ ] |
| 4 | Hafıza modülü açık | Config'te `memory.enabled = true` | [ ] |
| 5 | Skill üretimi açık | Config'te `skill_generation = true` | [ ] |
| 6 | Komut onayı açık | Config'te `require_approval = true` | [ ] |
| 7 | Token bütçesi limitli | Config'te `token_budget = 100000` | [ ] |
| 8 | Config salt okunur | `docker compose exec hermes-agent touch /home/hermes/config/test` → Permission denied | [ ] |
| 9 | Audit log yazıyor | `ls -la ~/.hermes-paket/logs/` → hermes.log mevcut | [ ] |
| 10 | Telegram pairing açık | Config'te `telegram_dm_policy = "pairing"` | [ ] |

---

## Önerilen Kontroller

| # | Kontrol | Nasıl test edilir? | Durum |
|---|---|---|---|
| 11 | API anahtarı bounded-scope | Sadece gerekli endpoint'lere erişimli anahtar kullan | [ ] |
| 12 | Güncel sürüm | `docker compose exec hermes-agent hermes --version` | [ ] |
| 13 | Hafıza çalışıyor | Bir görev ver, oturumu kapat, yeniden başlat, aynı görevi sor → hatırlıyor mu? | [ ] |
| 14 | Skill oluşuyor | Karmaşık bir görev ver, `~/.hermes-paket/data/skills/` altında SKILL.md oluştu mu? | [ ] |

---

## Acil Durum

```bash
# Hemen durdur
cd ~/.hermes-paket && docker compose down

# Log'ları incele
tail -f ~/.hermes-paket/logs/hermes.log

# Sıfırla (tüm veriler silinir)
docker compose down -v
rm -rf ~/.hermes-paket/data/*
```
