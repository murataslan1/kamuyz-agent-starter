# Kurumsal B2B Kullanım Vakaları — OpenClaw & Hermes

Bu doküman, kurumsal satış görüşmelerinde kullanılmak üzere sektör bazlı kullanım senaryolarını içerir. Her vaka: sorun → çözüm → sonuç formatında.

---

## Finans / Bankacılık

### Vaka 1: Mevzuat Takip Ajanı
**Sorun:** Haftalık SPK, BDDK, TCMB düzenlemelerini 3 kişilik ekip tarıyor. 120+ sayfa/hafta.
**Çözüm:** Hermes ajanı, yayınlanan mevzuatı otomatik tarar, kurumu ilgilendiren maddeleri işaretler, özet çıkarır, ilgili departmanlara Slack'ten gönderir.
**Sonuç:** Haftada 15 insan-saat tasarruf. Gözden kaçan düzenleme riski sıfıra indi.

### Vaka 2: Kredi Başvuru Ön Değerlendirme
**Sorun:** Günlük 200+ kredi başvurusu manuel ön değerlendirmeden geçiyor.
**Çözüm:** OpenClaw ajanı, başvuruları okuyor, kredi skoru, gelir belgesi, kefil durumunu kontrol ediyor, uygun olmayanları eliyor, uygun olanları ilgili birime Slack'ten bildiriyor.
**Sonuç:** Ön değerlendirme süresi %70 kısaldı. 2 kişilik ekip, 200 başvuru yerine sadece uygun olan 40 başvuruya odaklanıyor.

---

## İK / İnsan Kaynakları

### Vaka 3: Aday Ön Eleme Asistanı
**Sorun:** Her pozisyon için 300+ başvuru. İK ekibi CV okumaktan işe odaklanamıyor.
**Çözüm:** Hermes ajanı, gelen CV'leri pozisyon kriterlerine göre puanlıyor, uygun adayları sıralıyor, standart ret/görüşme mail'lerini atıyor.
**Sonuç:** Ön eleme 3 günden 2 saate indi. Yanlış eleme oranı %15'ten %3'e düştü (ajan kriterleri tutarlı uyguluyor).

### Vaka 4: Oryantasyon Botu
**Sorun:** Yeni başlayanlar aynı soruları soruyor, İK tekrar tekrar cevaplıyor.
**Çözüm:** OpenClaw ajanı, şirket wiki'sini, politikaları, sık sorulan soruları öğreniyor. Yeni başlayanlar Slack/WhatsApp'tan soruyor, anında cevap alıyor.
**Sonuç:** İK'nın oryantasyon yükü %60 azaldı. Yeni başlayan memnuniyeti arttı (anında cevap).

---

## BT / IT Operasyon

### Vaka 5: Incident Response Ajanı
**Sorun:** Gece 3'te gelen sunucu alarmına 30 dk içinde müdahale gerekiyor. Nöbetçi ekip yorgun.
**Çözüm:** Hermes ajanı, alarmı alıyor → log'ları tarıyor → kök nedeni analiz ediyor → bilinen çözümü uyguluyor veya nöbetçiye özetle bildiriyor.
**Sonuç:** Gece müdahale süresi 30 dk'dan 5 dk'ya indi. Kritik olmayan alarmların %70'i insansız çözülüyor.

### Vaka 6: SLA Takip ve Raporlama
**Sorun:** 50+ müşteri için aylık SLA raporu hazırlamak 3 gün sürüyor.
**Çözüm:** OpenClaw ajanı, her ayın 1'inde tüm müşterilerin SLA verilerini çekiyor, raporu oluşturuyor, PDF yapıp ilgili hesap yöneticisine mail atıyor.
**Sonuç:** 3 günlük iş 1 saatte bitiyor. Raporlar standart formatta, hatasız.

---

## Hukuk / Uyum

### Vaka 7: Sözleşme İnceleme Asistanı
**Sorun:** Her sözleşme 2-3 saat avukat mesaisi. Standart maddeler tekrar tekrar okunuyor.
**Çözüm:** Hermes ajanı, sözleşmeyi tarıyor → riskli maddeleri işaretliyor → şirket politikasına aykırı maddeleri belirtiyor → avukata özet sunuyor.
**Sonuç:** Sözleşme başına 2 saat tasarruf. Avukatlar sadece riskli maddelere odaklanıyor.

### Vaka 8: KVKK Uyum Denetimi
**Sorun:** KVKK uyum denetimi için yüzlerce doküman taranması gerekiyor.
**Çözüm:** Ajan, tüm dokümanları tarıyor → kişisel veri içeren bölümleri işaretliyor → açık rıza eksikliklerini belirtiyor → uyum raporu çıkarıyor.
**Sonuç:** Denetim hazırlığı 2 haftadan 2 güne indi.

---

## Satış / CRM

### Vaka 9: Müşteri İçgörü Raporu
**Sorun:** Satış görüşmesi öncesi müşteri hakkında bilgi toplamak 45 dk sürüyor.
**Çözüm:** Hermes ajanı, "Yarın XYZ şirketiyle görüşmem var" dendiğinde → CRM'den geçmişi çekiyor → son haberleri tarıyor → LinkedIn'den muhatabın profilini getiriyor → tek sayfalık brifing hazırlıyor → WhatsApp'tan gönderiyor.
**Sonuç:** Görüşme hazırlığı 45 dk'dan 2 dk'ya indi. Kapanan anlaşma oranı %22 arttı.

### Vaka 10: Teklif Takip Asistanı
**Sorun:** Gönderilen 50+ teklifin durumu manuel takip ediliyor. Cevaplanmayanlar unutuluyor.
**Çözüm:** OpenClaw ajanı, teklifleri takip ediyor → 3 gün cevap gelmezse hatırlatma mail'i atıyor → 7 gün olursa satışçıya Slack'ten bildiriyor → 14 gün olursa yöneticiye eskalasyon.
**Sonuç:** Cevapsız teklif oranı %40'tan %8'e düştü.

---

## Kamu

### Vaka 11: Vatandaş Başvuru Ön İşleme
**Sorun:** Günlük 500+ vatandaş başvurusu manuel sınıflandırılıp yönlendiriliyor.
**Çözüm:** Ajan, başvuruyu okuyor → türüne göre sınıflandırıyor → eksik evrak varsa otomatik bilgilendirme → uygunsa ilgili birime yönlendirme.
**Sonuç:** İşlem süresi 3 günden 4 saate indi. Vatandaş memnuniyeti arttı.

### Vaka 12: Meclis/Belediye Karar Takibi
**Sorun:** Belediye meclis kararlarını takip etmek için 2 personel görevli.
**Çözüm:** Hermes ajanı, yayınlanan kararları tarıyor → kurumu ilgilendirenleri işaretliyor → özet çıkarıyor → ilgili müdürlüğe mail atıyor.
**Sonuç:** 2 personel başka göreve kaydırıldı. Kararların atlanma riski sıfırlandı.

---

## ROI Hesaplama Şablonu

```
Kurum: [Adı]
Süreç: [Hangi süreç otomatize edilecek?]

Mevcut durum:
- Çalışan kişi sayısı: [N]
- Haftalık harcanan saat: [S]
- Aylık maliyet (brüt): [S × 4 × saatlik_maliyet × N]

Ajanlı durum:
- İnsan müdahalesi: [S'] (sadece kontrol/onay)
- Aylık maliyet: [S' × 4 × saatlik_maliyet × N] + [API/VPS maliyeti]

Tasarruf:
- Aylık: [mevcut - ajanlı]
- Yıllık: [aylık × 12]
- Geri dönüş süresi: [yatırım / aylık_tasarruf] ay
```
