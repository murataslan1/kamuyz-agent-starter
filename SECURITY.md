# SECURITY.md — Üretim Öncesi Güvenlik Kontrol Listesi

Bu belge, OpenClaw veya Hermes tabanlı bir agentic AI sistemini canlı ortama (production) almadan önce tamamlanması gereken güvenlik kontrollerini listeler.

## Zorunlu Kontroller

Bu maddelerin tamamı karşılanmadan sistem canlı ortama alınmamalıdır.

### Ağ Güvenliği

| # | Kontrol | Açıklama |
|---|---|---|
| 1 | Gateway portu (18789) dış internete kapalı | Sadece `127.0.0.1` veya VPN üzerinden erişilebilir olmalı |
| 2 | Egress filtreleme aktif | Ajanın internet erişimi sadece yetkili model sağlayıcı IP'lerine sınırlı |
| 3 | Origin doğrulaması aktif | `allowedOrigins` listesi tanımlı ve sadece güvenilir domain'leri içeriyor |

### Yama Yönetimi

| # | Kontrol | Açıklama |
|---|---|---|
| 4 | OpenClaw >= 2026.1.29 | CVE-2026-25253 yaması uygulanmış |
| 5 | Tüm bağımlılıklar güncel | `npm audit` temiz, kritik zafiyet yok |
| 6 | Otomatik güncelleme politikası tanımlı | Güvenlik yamaları için güncelleme takvimi var |

### Kimlik ve Erişim

| # | Kontrol | Açıklama |
|---|---|---|
| 7 | dmPolicy "pairing" modunda | Tüm kanallarda kullanıcı eşleştirme onayı zorunlu |
| 8 | Ajan non-root kullanıcı ile çalışıyor | `user: "1000:1000"` Docker'da, servis hesabı native kurulumda |
| 9 | API anahtarları bounded-scope | Minimum yetkili, sadece gerekli endpoint'lere erişim |
| 10 | Token rotasyonu tanımlı | API anahtarları ve pairing token'ları için periyodik yenileme |

### Çalışma Zamanı İzolasyonu

| # | Kontrol | Açıklama |
|---|---|---|
| 11 | Docker/sandbox izolasyonu aktif | `no-new-privileges:true`, `cap_drop: ALL` |
| 12 | Shell komutları isolated modda | `execute_code` tool'u sandbox içinde çalışıyor |
| 13 | Dosya sistemi salt okunur (read-only) | Konfigürasyon dizinleri dışında yazma izni yok |

### Tedarik Zinciri

| # | Kontrol | Açıklama |
|---|---|---|
| 14 | ClawHub doğrudan erişimi kapalı | Halka açık pazardan skill indirme engelli |
| 15 | Özel skill registry kullanılıyor | Kod incelemesinden geçmiş onaylı skill'ler dahili depoda |
| 16 | Skill imza doğrulaması aktif | Yüklenen her skill'in bütünlüğü ve kaynağı doğrulanıyor |

### HITL (Human-In-The-Loop)

| # | Kontrol | Açıklama |
|---|---|---|
| 17 | Kritik araçlarda onay kapısı | Veri silme, finansal işlem, dışarı e-posta/mesaj gönderme |
| 18 | Sistem yapılandırma değişiklikleri onaylı | Gateway konfigürasyonu değişiklikleri insan onayı gerektiriyor |

### Denetim ve İzleme

| # | Kontrol | Açıklama |
|---|---|---|
| 19 | Merkezi loglama aktif | Gateway logları SIEM/Syslog'a aktarılıyor |
| 20 | Alarm kuralları tanımlı | Anormal davranış (yüksek tool kullanımı, beklenmeyen ağ bağlantısı) için alarm |
| 21 | Audit trail değişmez (immutable) | Loglar silinemez/değiştirilemez depoda saklanıyor |

### Regülasyon Uyumu

| # | Kontrol | Açıklama |
|---|---|---|
| 22 | DDO BİGR uyumu | Kamu kurumu ise DDO Rehberi kriterleri karşılanıyor |
| 23 | KVKK uyumu | Kişisel veri işleniyorsa KVKK Madde 9 yurtdışı aktarım kısıtlamalarına uygun |
| 24 | Veri saklama politikası | MEMORY.md ve oturum arşivleri için saklama süresi ve silme prosedürü tanımlı |

## Durum Göstergeleri

- [ ] Zorunlu kontrollerin tamamı (24/24) karşılandı
- [ ] Son güvenlik denetimi tarihi: ________
- [ ] Denetimi yapan: ________
- [ ] Bir sonraki denetim tarihi: ________

## Acil Durum Prosedürü

1. **Ajanı durdur:** `openclaw gateway stop` veya `docker compose down`
2. **Erişim token'larını iptal et:** Tüm API anahtarlarını rotate et
3. **Logları incele:** Son 24 saatlik audit log'ları tara
4. **Olayı raporla:** SOME/SOC ekibine bildir
5. **Kök neden analizi:** Olay çözüldükten sonra ADR olarak belgele
