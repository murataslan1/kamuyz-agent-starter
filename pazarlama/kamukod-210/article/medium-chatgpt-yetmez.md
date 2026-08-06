# Medium Makalesi — KamuKOD 210

---

# ChatGPT Yetmez: Kendi Yapay Zeka Ajanını Kurma Zamanı

ChatGPT'ye soru sorup cevap alıyorsun. Harika. Ama ya sana **senin yerine iş yapan** bir yapay zeka asistanın olsa?

Ben size bugün onu anlatacağım.

---

## ChatGPT'nin yapamadığı şey

ChatGPT bir kütüphane gibidir. Gidersin, sorarsın, cevap alırsın. Ama:

- Sabah 8'de maillerini özetleyip Telegram'dan gönderemez
- "Şu toplantının notlarını al, Slack'e at" diyemezsin
- "Son 1 aydaki Jira ticket'larını tara, tekrarlayan hataları bul" diyemezsin
- Bir kere öğrettiğin işi hatırlayıp, her seferinde daha iyi yapamaz

Bunları yapabilen sistemlere **yapay zeka ajanı (AI agent)** deniyor. Ve şu an bu alandaki en güçlü iki açık kaynak araç: **OpenClaw** ve **Hermes Agent.**

---

## OpenClaw: Her yere bağlanan asistan

OpenClaw, YC mezunu Peter Steinberger tarafından başlatıldı. GitHub'da 385.000+ yıldızı var. MIT lisanslı, tamamen açık kaynak.

Ne yapar? 50'den fazla platforma bağlanabilen bir **iletişim geçidi.** WhatsApp, Telegram, Slack, Discord, Signal, iMessage... hepsini tek bir ajan yönetebilir.

Şirketinde şöyle bir senaryo düşün: Slack'ten ajana "müşteri XYZ'nin son 3 aylık siparişlerini çıkar, PDF yap, bana WhatsApp'tan gönder" diyorsun. Ajan veritabanını sorguluyor, PDF oluşturuyor, WhatsApp'tan sana yolluyor. Hepsi tek komutla.

---

## Hermes Agent: Zamanla sana özel hale gelen asistan

Hermes, Nous Research tarafından geliştiriliyor. OpenClaw'dan temel farkı şu: **kendi kendine öğreniyor.**

OpenClaw'da bir işi her seferinde sıfırdan tarif etmen gerek. Hermes ise yaptığı işleri analiz ediyor, başarılı olanları "skill" adı verilen yeniden kullanılabilir yeteneklere dönüştürüyor.

Bir kez "şu formattaki mailleri şöyle özetle" dediğinde, ikinci seferde sorman gerekmiyor. Kendi yazdığı skill'i yüklüyor, senden hızlı ve doğru yapıyor.

> *"Hermes'e geçince aynı iş akışı ilk denemede sorunsuz çalıştı, bir hafta boyunca müdahalesiz devam etti."* — Reddit kullanıcısı

---

## Neden kendi başına öğrenmek zor?

Bu ajanları kurmayı deneyenlerin deneyimleri:

- OpenClaw kurulumu ortalama **4 saat** sürüyor (Reddit, 342 upvote)
- ClawHub'da (OpenClaw'un eklenti marketi) **%12 zararlı skill** tespit edildi
- Güvenlik ayarları **varsayılan olarak kapalı** geliyor — sandbox, onay mekanizması, audit log...
- Hermes'in hafıza modülü varsayılan olarak **kapalı** — öğrenemiyor
- Dokümantasyonun tamamı **İngilizce**

Kendi başına uğraşsan 20-40 saatini alır. Üstelik güvenli kurduğundan emin olamazsın.

---

## KamuKOD 210: 8 saatte, güvenli, çalışır sistem

KamuKOD Atölye 210, tam olarak bu sorunu çözmek için tasarlandı.

4 oturum, 8 saat:

1. **Oturum 1:** OpenClaw kurulumu, Telegram bot bağlantısı, ilk komut
2. **Oturum 2:** WhatsApp bağlantısı, ajan kimliği oluşturma, skill yükleme
3. **Oturum 3:** Google Workspace entegrasyonu, proaktif cron görevler
4. **Oturum 4:** Hermes Agent — learning loop, kendi skill'ini yazma, güvenlik

Her oturumda **sen yapıyorsun, biz kontrol ediyoruz.** Sonuç: çalışan, güvenli, sana özel bir yapay zeka ajanı.

---

## Kimler katılmalı?

- "Bu ajan olayını gerçekten öğreneyim" diyen yazılımcılar
- Ekibine agentic AI yetkinliği kazandırmak isteyen teknik liderler
- Tekrarlayan işlerini otomatize etmek isteyen girişimciler
- Kamu BT personeli — "kuruma alabilir miyiz?" sorusuna cevap arayanlar

Komut satırı biliyorsan yeter. Her şey Türkçe, adım adım.

---

## Son söz

2026'da yapay zeka ajansız kalmak, 2010'da akıllı telefonsuz kalmak gibi olacak.

Öğrenmek için bekleme. Gel, birlikte kuralım.

👉 **Kayıt:** https://kamukod.lovable.app/atolye/210

---

*Bu yazı KamuKOD ve KamuYZ APA Çalışma Grubu iş birliğiyle hazırlanmıştır. OpenClaw ve Hermes hakkında daha fazla bilgi için ücretsiz kaynaklarımız: [github.com/murataslan1/kamuyz-agent-starter](https://github.com/murataslan1/kamuyz-agent-starter)*
