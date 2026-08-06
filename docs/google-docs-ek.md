KamuYZ APA Çalışma Grubu
OpenClaw & Hermes — Açık Kaynak Agentic Framework Programı · Ağustos 2026 Güncellemesi

1. Amaç ve konumlanma (değişmedi)
KamuYZ APA çalışma grubu olarak OpenClaw ve Hermes üzerine kamuya açık etkinlikler düzenleyecek ve kalıcı Türkçe çıktılar üreteceğiz. Hedef hem öğrenmek hem öğretmek, hem de grubun ve KamuYZ'nin görünürlüğünü artırmak. Tüm çıktılar vendor-nötr ve açık erişimdir.
KamuKod ile iş bölümü: KamuKod üyelik bazlı 4 haftalık uygulamalı kurs ile "nasıl kurulur" sorusunu; biz kamuya açık etkinlikler ve yayınlarla "bu nedir, güvenli mi, kurum ne zaman kullanmalı" sorusunu cevaplıyoruz. Aynı kişiler iki tarafta da sunabilir; içerik çakışmaz, birbirini besler.

2. Etkinlikler (aylık ritim)

E1 — OpenClaw nedir, ne yapar? Hermes ve agentic dalga
İçerik: Kişisel AI agent kavramı, OpenClaw'un yükselişi, Hermes'in learning loop farkı, ekosistem manzarası. Teknik önkoşul yok.
Format: Webinar, 90 dk, kayıt YouTube'a
Durum: ✅ İçerik taslağı hazır

E2 — Otonom sistemlerin gerçeği: güvenlik ve zorluklar
İçerik: Prompt injection, veri sızıntısı, denetlenemeyen davranış riski; CVE dalgası, tedarik zinciri olayları, açıktaki instance'lar; credential ve yetki yönetimi; dikkat edilmesi gerekenler.
Format: Webinar / panel, 90 dk
Durum: ✅ İçerik taslağı hazır. Örnek vaka: Çin kısıtlaması + CVE-2026-25253 + ClawHavoc

E3 — Hands-on atölye
İçerik: kamuyz-agent-starter reposundan canlı kurulum: tek agent + Telegram + güvenlik checklist'i. Derinleşmek isteyen KamuKod kursuna yönlendirilir.
Format: Online atölye, 2-3 saat, sınırlı kontenjan
Durum: ✅ İçerik + demo script'i + güvenli kurulum paketi hazır

Not: Etkinlik saatleri KamuKod ders akşamlarıyla (20:30-22:30) çakıştırılmaz; sunucular ortak.

3. Kalıcı çıktılar — Durum Güncellemesi

kamuyz-agent-starter (GitHub) — ✅ TAMAM
github.com/murataslan1/kamuyz-agent-starter
40+ dosya. Türkçe README, GLOSSARY (80+ terim), SECURITY (24 maddelik kontrol listesi), LEARNING (2 haftalık plan), güvenli Hermes kurulum paketi (tek komutla), KamuYZ Agent Export (AGENT.md + 8 skill + heartbeat), etkinlik taslakları, sprint planı, araştırma raporları.

Yazı serisi — ✅ TAMAM (3 bölüm)
1. Yapay Zeka Ajanı Nedir? ChatGPT'den Ötesi
   github.com/murataslan1/kamuyz-agent-starter/blob/main/yazi-serisi/01-ajan-nedir.md
2. Otonom Sistemlerin Gerçeği: Güvenlik Riskleri
   github.com/murataslan1/kamuyz-agent-starter/blob/main/yazi-serisi/02-guvenlik-riskleri.md
3. Sıfırdan Ajan Kurulumu: Adım Adım Rehber
   github.com/murataslan1/kamuyz-agent-starter/blob/main/yazi-serisi/03-kurulum-rehberi.md

Whitepaper — ✅ TAMAM (TR + EN)
Türkçe: github.com/murataslan1/kamuyz-agent-starter/blob/main/docs/whitepaper/kamuyz-whitepaper-tr.md
English: github.com/murataslan1/kamuyz-agent-starter/blob/main/docs/whitepaper/kamuyz-whitepaper-en.md
İçerik: Yönetici özeti, ekosistem manzarası, OpenClaw & Hermes derin inceleme, 5 tehdit vektörü, 2 vaka analizi, 10 soruluk kurumsal benimseme çerçevesi, vendor-nötr gereksinim tablosu, KVKK/DDO/EU AI Act uyum haritası, sektörel stratejik öneriler.

YouTube kayıtları + LinkedIn özetleri — ⏳ Etkinlikler sonrası

Araştırma raporları (planlanmamış ek çıktı) — ✅ TAMAM
- Gemini Deep Research: 30 kaynaklı derin inceleme (mimari, güvenlik, regülasyon, KVKK/DDO)
- Grok Ekosistem Taraması: Teknik ekosistem, OpenClaw & Hermes karşılaştırması
- Grok Toplu Deneyim: Mayıs-Ağustos 2026, X/Reddit/Medium/YouTube gerçek kullanıcı deneyimleri

4. Ek Çıktılar (orijinal planda yoktu, süreçte eklendi)

Güvenli Hermes Paketi
Tek komutla kurulum, sandbox aktif, non-root, dışa kapalı, audit log. Production öncesi 24 maddelik kontrol.
github.com/murataslan1/kamuyz-agent-starter/tree/main/hermes-paket

KamuYZ Workshop Agent Export
AGENT.md + HEARTBEAT.md + RULES.md + 8 skill (müfredat, demo, lojistik, B2B teklif, içerik, değerlendirme, performans, topluluk). Meta Ads Agent Export yapısı referans alınarak.
github.com/murataslan1/kamuyz-agent-starter/tree/main/kamu-yz-agent-export

B2B Kullanım Vakaları (12 sektör)
Finans, İK, BT, hukuk, satış, kamu için somut senaryolar + ROI hesaplama şablonu.
(Private repoda: github.com/murataslan1/kamuyz-pazarlama)

Pazarlama Materyalleri (Private Repo)
10 MP4 video (farklı senaryo ve kurgularda), 12 PDF, 6 HTML sunum deck'i, 3 PPTX, LinkedIn/X/e-posta/landing page içerikleri.
github.com/murataslan1/kamuyz-pazarlama

KamuKOD 210 ile Çapraz Yönlendirme
KamuKOD 210 (ücretli kurs) ↔ KamuYZ E1-E2-E3 (ücretsiz) ↔ B2B Paketler (kurumsal). Birbirini besleyen zincir yapısı kuruldu.

5. Sonraki Adımlar
- E1, E2, E3 etkinliklerinin planlanması ve duyurulması (Ağustos/Eylül 2026)
- YouTube kanalı kurulumu ve etkinlik kayıtlarının yüklenmesi
- LinkedIn içerik takviminin başlatılması
- Medium/Substack'te yazı serisinin yayınlanması
- KamuKod 210'a katılımcı yönlendirme

Çalışma düzeni: 2 haftalık sprintler, haftada 1 kısa senkron (30 dk). Asenkron iş WhatsApp grubu ve GDrive üzerinden. Görev dağılımı kickoff toplantısında gönüllülük esasıyla belirlenir.
