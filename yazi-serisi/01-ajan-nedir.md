# Yapay Zeka Ajanı Nedir? ChatGPT'den Ötesi

**KamuYZ APA Çalışma Grubu — Yazı Serisi #1**

---

Hepimiz ChatGPT'yi kullanıyoruz. Bir soru soruyoruz, cevap alıyoruz. Harika.

Ama bir düşünün: ChatGPT'ye "bu 10 maili özetle, önem sırasına göre sırala, sonra bana Telegram'dan bildir" diyebiliyor musunuz? Hayır.

İşte tam bu noktada **yapay zeka ajanları (AI agents)** devreye giriyor.

---

## Chatbot vs Ajan: Fark ne?

| | Chatbot (ChatGPT) | Yapay Zeka Ajanı |
|---|---|---|
| Ne yapar? | Soruya cevap verir | Görevi yapar |
| Hafıza | Oturumluk (unutur) | Kalıcı (hatırlar) |
| Araç kullanımı | Yok | Dosya okur, API çağırır, komut çalıştırır |
| Proaktiflik | Pasif (sen sorarsın) | Aktif (kendi başlatır) |
| Platform | Web arayüzü | Telegram, WhatsApp, Slack... |

Chatbot size "nasıl yapılır"ı anlatır. Ajan ise **sizin yerinize yapar.**

---

## Peki bu ajanlar nasıl çalışıyor?

Bir yapay zeka ajanı dört temel yeteneğe sahiptir:

1. **Planlama:** Karmaşık bir hedefi alt görevlere böler. "Şu 50 sayfalık raporu özetle" dediğinizde, önce raporu okur, bölümleri ayırır, her bölümü özetler, sonra birleştirir.

2. **Araç Kullanımı:** Dosya sistemi, API'ler, veritabanları, web tarayıcıları... Ajan bunların hepsini kullanabilir. Tıpkı bir insan gibi.

3. **Hafıza:** Oturum kapansa da bilgiyi saklar. 3 hafta önce yaptığınız bir toplantıdaki kararı hatırlayabilir.

4. **Çok Adımlı Muhakeme:** Her aksiyondan sonra durumu değerlendirir, gerekirse planı değiştirir, hedefe ulaşana kadar devam eder.

---

## 2026'da öne çıkan iki açık kaynak ajan

### 🦞 OpenClaw

Peter Steinberger tarafından başlatıldı. GitHub'da **385.000+ yıldız.** MIT lisanslı, tamamen açık kaynak.

OpenClaw'un süper gücü: **50'den fazla platforma bağlanabilmesi.** WhatsApp, Telegram, Slack, Discord, Signal, iMessage... hepsini tek bir ajan yönetebiliyor.

Şöyle düşünün: Slack'te "müşteri XYZ'nin son 3 aylık siparişlerini çıkar, PDF yap, bana WhatsApp'tan gönder" diyorsunuz. Ajan veritabanını sorguluyor, PDF'i oluşturuyor, WhatsApp'tan size yolluyor.

### 🧠 Hermes Agent

Nous Research tarafından geliştiriliyor. OpenClaw'dan temel farkı: **kendi kendine öğreniyor.**

Hermes, tamamladığı her karmaşık görevden sonra "nasıl yaptığını" analiz ediyor. Başarılı iş akışını bir **SKILL.md** dosyasına kaydediyor. Bir dahaki sefere aynı tür görev geldiğinde, kendi yazdığı bu skill'i kullanıyor — hem daha hızlı, hem daha doğru.

Buna **Kapalı Devre Öğrenme Döngüsü (Closed Learning Loop)** deniyor:

```
GÖREV → TAMAMLA → ANALİZ ET → SKILL OLUŞTUR → TEKRAR KULLAN → İYİLEŞTİR
```

Zamanla Hermes **sizin iş yapış şeklinizi öğreniyor.** Ne kadar kullanırsanız, o kadar iyi oluyor.

---

## Hangisini seçmeli?

| İhtiyacınız | Tercih |
|---|---|
| Çok kanallı iletişim (WhatsApp, Telegram, Slack...) | OpenClaw |
| Kendi kendine öğrensin, zamanla uzmanlaşsın | Hermes |
| Hızlı kurulum, düşük bakım | Hermes |
| Geniş hazır eklenti ekosistemi | OpenClaw |

Birçok ileri düzey kullanıcı ikisini birlikte kullanıyor: **OpenClaw dış dünyayla iletişimi yöneten kapı, Hermes arkadaki beyin.**

---

## Gerçek kullanıcılar ne diyor?

> "Hermes'e geçince aynı iş akışı ilk denemede sorunsuz çalıştı, bir hafta boyunca müdahalesiz devam etti." — Reddit, 342 upvote

> "3 saatte 12 Jira ticket'ı kapatan ajan yazdım. 2 aylık mühendislik işine denk." — X kullanıcısı

> "OpenClaw'u sildim, Hermes'e geçtim. Akşam 7'de bilgisayar kapatıyorum." — Türkçe YouTube

---

## Peki güvenli mi?

Bu soru çok önemli. Çünkü bir ajana dosyalarınızı okuma, komut çalıştırma yetkisi veriyorsunuz.

OpenClaw, Mart 2026'da **CVE-2026-25253** adında kritik bir güvenlik açığı yaşadı. URL'deki bir parametre üzerinden saldırganlar ajanın kimlik bilgisini çalabiliyordu. Açık yamalandı, ancak ders alındı: **varsayılan ayarlarla production'a almayın.**

Hermes ise şu ana kadar **hiçbir bildirilen CVE'ye** sahip değil (Nisan 2026 itibarıyla).

Güvenli kurulum için hazırladığımız rehber: [SECURITY.md](https://github.com/murataslan1/kamuyz-agent-starter/blob/main/SECURITY.md) — 24 maddelik kontrol listesi.

---

## Başlamak ister misiniz?

KamuYZ APA Çalışma Grubu olarak 3 açık etkinlik düzenliyoruz:

- **E1:** Yapay zeka ajanı nedir, ne işe yarar? (90 dk)
- **E2:** Otonom sistemlerde güvenlik riskleri (90 dk)
- **E3:** Canlı kurulum atölyesi (2-3 saat)

Tüm kaynaklar açık: [github.com/murataslan1/kamuyz-agent-starter](https://github.com/murataslan1/kamuyz-agent-starter)

---

*Bu yazı, KamuYZ APA Çalışma Grubu'nun "OpenClaw & Hermes — Açık Kaynak Agentic Framework Programı" kapsamında hazırlanmıştır. Tüm çıktılar vendor-nötr ve açık erişimdir.*
