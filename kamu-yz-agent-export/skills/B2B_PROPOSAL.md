# B2B_PROPOSAL.md — Kurumsal Teklif Hazırlama

**Amaç:** Workshop katılımcılarından veya dış taleplerden gelen kurumsal ilgiyi B2B teklife dönüştür.

**Hizmet Ettiği KPIs:** B2B dönüşüm oranı

## Girdiler
- `../docs/B2B-paket.md` — Paket tanımları ve fiyatlandırma
- `../SECURITY.md` — Güvenlik checklist'i (teklife ek olarak)
- `journal/` — Workshop sinyalleri (hangi kurum ilgi gösterdi?)
- Müşteri bilgileri (sektör, çalışan sayısı, ihtiyaç)

## Süreç

### 1. İhtiyaç analizi
```
Kuruma sorulacak sorular:
1. Şu an hangi tekrarlayan iş süreçleriniz var?
2. Bu süreçlerde kaç kişi çalışıyor? Haftada kaç saat harcanıyor?
3. Verileriniz nerede? (on-premise / bulut / hibrit)
4. Daha önce AI/otomasyon denediniz mi? Ne oldu?
5. Güvenlik gereksinimleriniz neler? (KVKK, ISO 27001, DDO BİGR)
6. Karar verici kim? Bütçe onay süreci nasıl?
7. Zaman çizelgesi? Ne zaman başlamak istiyorsunuz?
```

### 2. Paket eşleştirme
| Kurum profili | Önerilen paket | Gerekçe |
|---|---|---|
| Hiç AI kullanmamış, merak ediyor | Paket 1: Farkındalık | Temel tanıtım + güven değerlendirmesi |
| Teknik ekip var, prototip istiyor | Paket 2: Prototip | Kurulum + 1 use-case |
| Daha önce denemiş, production istiyor | Paket 3: Entegrasyon | Tam entegrasyon + eğitim |

### 3. Teklif şablonu
```markdown
# Kurumsal Agentic AI Atölye Teklifi

**Hazırlayan:** KamuYZ APA Çalışma Grubu
**Tarih:** [tarih]
**Kurum:** [kurum adı]
**Paket:** [paket adı]

## Mevcut Durum
[Kurumun şu anki süreçleri, tekrarlayan işleri, harcanan insan-saat]

## Önerilen Çözüm
[Hangi ajan(lar), hangi süreçlerde, nasıl çalışacak?]

## Kapsam
| Aşama | İçerik | Süre | Çıktı |
|---|---|---|---|
| Keşif | Süreç analizi, uygunluk değerlendirmesi | 1 hafta | Fizibilite raporu |
| Kurulum | Güvenli Hermes paketi kurulumu | 2 gün | Çalışan sistem |
| Prototip | 1 use-case'in ajanla otomasyonu | 1 hafta | Çalışan prototip |
| Eğitim | Ekibe kullanım ve bakım eğitimi | 2 gün | Eğitimli ekip |
| Destek | 1 ay uzaktan destek | 1 ay | Sorunsuz işletim |

## Yatırım ve Geri Dönüş
| Kalem | Tutar |
|---|---|
| Toplam yatırım | [TL] |
| Tahmini aylık tasarruf | [insan-saat × saatlik maliyet] |
| Geri dönüş süresi | [ay] |

## Neden KamuYZ?
- Açık kaynak, vendor-nötr yaklaşım
- Güvenlik öncelikli kurulum (SECURITY.md 24 maddelik kontrol)
- ISO 42001 uyumlu işletim prosedürleri
- KVKK ve DDO BİGR değerlendirmesi dahil

## Sonraki Adım
1. Teklif onayı
2. Keşif toplantısı (1-2 saat)
3. Sözleşme
4. Başlangıç

**İletişim:** [iletişim bilgileri]
```

## Kalite Barı
- [ ] Kurum ihtiyaçları anlaşıldı (6 soru cevaplandı)
- [ ] Doğru paket eşleştirildi
- [ ] Yatırım/geri dönüş hesabı yapıldı
- [ ] Güvenlik ve uyumluluk (KVKK, ISO) belirtildi
- [ ] Rakip tekliflerden farkı net (açık kaynak, vendor-nötr)
- [ ] İnsan onayına sunuldu → HANDOFF: MURAT
