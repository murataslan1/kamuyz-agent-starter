---
name: research
description: Araştırma sorusunu birincil kaynaklara dayanarak araştır, bulguları alıntılı Markdown dosyası olarak kaydet. Arka plan ajanı olarak çalışır.
---

# Araştırma (Research)

Bir araştırma sorusunu **birincil kaynaklara** (resmi dokümanlar, kaynak kod, spesifikasyonlar, birincil API'ler) dayanarak incele. Bulguları, her iddianın kaynağını belirterek tek bir Markdown dosyasına yaz.

## Ne zaman kullanılır

- Kullanıcı bir konunun araştırılmasını istediğinde
- Dokümantasyon veya API bilgisi toplanması gerektiğinde
- Okuma yükünün arka plan ajanına devredilmesi gerektiğinde

## Süreç

1. Araştırma sorusunu netleştir
2. Birincil kaynakları tara (resmi doküman, kaynak kod, spec, API referansı)
3. Her iddiayı kaynağına kadar takip et
4. Bulguları `docs/research/YYYY-AA-GG-konu.md` formatında kaydet
5. Her iddiada kaynak belirt (URL, commit hash, belge bölümü)

## Çıktı

- `docs/research/` altında, tarih damgalı, alıntılı Markdown dosyası
- Dosya adı: `YYYY-AA-GG-<konu>.md`
