# SSS ve İtiraz Yanıtları — KamuKOD 210

---

## "Ben yazılımcı değilim, katılabilir miyim?"

Evet. Komut satırına yazı yazabiliyor olman yeterli.

Atölyede tüm kodları biz veriyoruz, her satırı açıklıyoruz. Teknik terimleri Türkçe anlatıyoruz. Ama "terminal" veya "komut satırı" nedir bilmiyorsan, önce temel bilgisayar kullanımını öğrenmeni öneririz.

---

## "Ücretsiz öğrenemez miyim?"

Öğrenebilirsin. KamuYZ APA olarak açık ve ücretsiz etkinlikler düzenliyoruz. GitHub'da tüm kaynaklar açık: [kamuyz-agent-starter](https://github.com/murataslan1/kamuyz-agent-starter)

Ama:
- Kendi başına OpenClaw kurmak ortalama 4 saat sürüyor (Reddit verisi)
- Güvenlik ayarları varsayılan olarak kapalı geliyor
- ClawHub'da %12 zararlı skill var, hangisinin güvenli olduğunu bilmek zor
- İngilizce dokümanları taramak, hataları çözmek saatler alıyor

KamuKOD 210: 8 saatte, güvenli, çalışır, üretime hazır sistem. Desteğiyle birlikte.

---

## "OpenClaw mu Hermes mi? Hangisini öğreteceksiniz?"

İkisini de. Atölyenin adı "OpenClaw-Hermes."

İlk 3 oturum OpenClaw (iletişim geçidi, çok kanallı kurulum), 4. oturum Hermes Agent (kendi kendine öğrenme, kapalı devre döngü).

Hangisinin ne zaman kullanılacağını da öğreniyorsun.

---

## "Kurdum, atölye bitti. Sonra ne olacak?"

- Oturum kayıtlarına süresiz erişim
- WhatsApp destek grubu (sorun yaşarsan sor)
- KamuKOD 220: Enterprise Agentic Design (kurumsal seviye)
- GitHub repo sürekli güncelleniyor

---

## "Kurumum için fatura kesebilir misiniz?"

Evet, kurumsal fatura düzenleniyor. Hatta şirketine geri ödetmek için [hazır talep mektubu](https://kamukod.lovable.app/geri-odeme) bile var.

---

## "Zaman ayıramam, 4 hafta uzun."

Her oturum 2 saat. Haftada 2 saat. Toplam 8 saat.

Kendi başına öğrenmeye kalksan, sadece kurulum 4 saat. Üstüne hata çözme, doküman okuma, güvenlik araştırma...

8 saatte çalışır sistem + destek + Türkçe anlatım.

---

## "Ben zaten ChatGPT kullanıyorum, bu ajanlar ne fark edecek?"

ChatGPT: soru sor, cevap al.

OpenClaw/Hermes: görev ver, **senin yerine yapsın.**

"Şu 10 maili özetle, takvime işle, sonra bana Telegram'dan bildir" → ChatGPT bunu yapamaz. Ajan yapar.

---

## "Güvenli mi? Verilerim nerede?"

Kendi sunucunda çalışıyor. Verilerin sana ait.

Bizim kurduğumuz sistem:
- Gateway sadece localhost'ta çalışır (dışarı kapalı)
- Non-root kullanıcı
- Sandbox aktif
- Kritik komutlarda onay sorar
- Audit log tutar

---

## "Kaçırdığım oturum olursa?"

Tüm oturumlar kaydediliyor. Kayıtlara süresiz erişimin var. WhatsApp grubundan soru sorabilirsin.

---

## "Daha önce Python/Node.js bilmiyorum, sorun olur mu?"

Hayır. Kod yazmayacaksın. Konfigürasyon yapacaksın.

Config dosyalarını düzenlemek, API anahtarı girmek, komut çalıştırmak. Hepsi bu.
