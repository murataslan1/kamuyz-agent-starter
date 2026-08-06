# B2B Satış Konuşma Rehberi — KamuKOD 210

Bu doküman, kurumsal müşterilerle yapılacak ilk görüşmede kullanılacak konuşma akışını ve itiraz yanıtlarını içerir.

---

## İlk Görüşme Akışı (30 dk)

### 1. Açılış (2 dk)
"Bize [kanal] üzerinden ulaştığınız için teşekkürler. Ben [isim], KamuKOD tarafında [rol]. Bugünkü amacım sizi ve ihtiyaçlarınızı anlamak, sonra nasıl yardımcı olabileceğimizi konuşmak. 30 dakika yeterli olur mu?"

### 2. Keşif (10 dk)
```
Sorulacak sorular:

1. "Şu anda en çok zamanınızı alan tekrarlayan işler neler?"
   → Somut örnekler al: "Şu süreç haftada kaç saat?"

2. "Bu işleri yapan ekip kaç kişi?"
   → Maliyet hesabı için gerekli

3. "Daha önce otomasyon veya yapay zeka denediniz mi?"
   → Ne oldu? Neden çalışmadı?

4. "Verileriniz nerede? (kendi sunucunuz / bulut / hibrit)"
   → Güvenlik ve uyumluluk için kritik

5. "Karar verme süreciniz nasıl? Kimler dahil?"
   → Satış döngüsünü anlamak için

6. "Zaman çizelgeniz nedir? Ne zaman başlamak istersiniz?"
   → Aciliyet seviyesi
```

### 3. Çözüm Sunumu (10 dk)
```
Keşifteki 1-2 somut soruna odaklan:

"Bahsettiğiniz [süreç] için şöyle bir çözüm olabilir:

• [Ajan türü] bu süreci şu şekilde otomatize eder: [akış]
• Tahmini tasarruf: [insan-saat] / ay
• Kurulum: [paket] kapsamında [süre] içinde

İlgili bir vaka: [sektör]'deki [şirket] benzer bir süreci otomatize etti, [sonuç]."
```

### 4. Sonraki Adım (5 dk)
```
"Size özel bir teklif hazırlayıp [tarih]'e kadar gönderebilirim. Bunun için şu bilgilere ihtiyacım var: [liste].

Bu arada, ajansız bir şekilde denemek isterseniz açık kaynak repomuzu inceleyebilirsiniz:
github.com/murataslan1/kamuyz-agent-starter

Ücretsiz etkinliklerimize de katılabilirsiniz [link]."
```

### 5. Kapanış (3 dk)
```
"Bugün konuştuklarımızı özetlersem:

• Sorun: [1 cümle]
• Çözüm: [1 cümle]
• Sonraki adım: [teklife kadar süreç]

[Gün] günü teklifi göndereceğim. O zamana kadar sorunuz olursa [iletişim]."
```

---

## Sık Karşılaşılan İtirazlar

### "Bizim için erken, önce biraz daha araştıralım."
→ "Anlıyorum. Araştırmanıza yardımcı olması için açık kaynak repomuzu ve ücretsiz etkinliklerimizi önerebilirim. Bu arada, [sektördeki benzer şirket] şu anda [çözüm] kullanıyor. İsterseniz onların deneyimini paylaşabilirim."

### "Bütçe onayı zor, özellikle yeni teknoloji için."
→ "Haklısınız. Şöyle yapabiliriz: Önce Paket 1 (Farkındalık) ile başlayalım. 90 dakikalık bir oturumda yönetim ekibinize ajansız bir demo yapalım, güvenlik değerlendirmesi sunalım. Bu ücretsiz. Değer görürlerse Paket 2'ye geçeriz."

### "Güvenlik ekibimiz izin vermez."
→ "Güvenlik ekibinizle birlikte çalışalım. Size ISO 42001 uyumlu işletim prosedürlerimizi, KVKK ve DDO BİGR değerlendirmemizi, 24 maddelik güvenlik kontrol listemizi göndereyim. Güvenlik ekibiniz incelesin, sorularını cevaplayalım."

### "Zaten RPA kullanıyoruz."
→ "RPA kural tabanlıdır: 'Eğer A ise B yap.' Ajanlar ise anlamsaldır: 'Şu tür mailleri önem sırasına göre sırala, özetle, sadece acil olanları bana bildir.' RPA'nın yapamadığı karar gerektiren işleri ajanlar yapar. İkisi birlikte çalışabilir."

### "Veri güvenliği nedeniyle buluta çıkamayız."
→ "OpenClaw ve Hermes tamamen sizin sunucunuzda çalışır. Veri dışarı çıkmaz. İnternet bağlantısı olmadan, yerel modellerle (Ollama) bile çalıştırabilirsiniz."

---

## Takip Mail Şablonları

### Görüşme sonrası (aynı gün)
```
Konu: Görüşmemiz hakkında — [Şirket]

Merhaba [isim],

Bugünkü görüşme için teşekkürler. Konuştuklarımızı özetliyorum:

[3 madde]

Söz verdiğim gibi:
• [Döküman/link]
• [Vaka çalışması]
• [Teklif taslağı] — [tarih]'e kadar göndereceğim

Bu arada açık kaynak repomuzu inceleyebilirsiniz:
github.com/murataslan1/kamuyz-agent-starter

Sorunuz olursa her zaman yazabilirsiniz.

[isim]
```

### Teklif takibi (1 hafta sonra)
```
Konu: Teklif hakkında — [Şirket]

Merhaba [isim],

Geçen hafta gönderdiğim teklifle ilgili bir sorunuz oldu mu?

Bu arada ilginizi çekebilecek bir gelişme: [güncel haber/vaka — örn: "X sektöründe bir şirket benzer bir çözümle şu sonucu aldı"]

Müsait olduğunuzda kısaca konuşabilir miyiz?

[isim]
```
