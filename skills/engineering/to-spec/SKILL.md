---
name: to-spec
description: Mevcut konuşmayı veya araştırma bulgularını yapılandırılmış bir spesifikasyona dönüştür ve docs/ altına kaydet. Use when tasarım veya plan netleştiğinde, yazılı hale getirilmesi gerektiğinde.
---

# Spesifikasyona Dönüştür (to-spec)

Mevcut konuşma, araştırma veya planı yapılandırılmış bir spesifikasyon dosyasına dönüştür.

## Ne zaman kullanılır

- CONTEXT.md glossary oluştuktan sonra
- Araştırma sonuçları toplandığında
- Etkinlik/sunum içeriği netleştiğinde
- Bir özellik veya değişiklik tasarlandığında

## Süreç

1. Mevcut bağlamı tara (CONTEXT.md, araştırma dosyaları, konuşma)
2. Spesifikasyonun kapsamını belirle
3. Yapılandırılmış formatta yaz:
   - Amaç
   - Hedef kitle
   - Kapsam / kapsam dışı
   - Detaylı içerik
   - Bağımlılıklar
   - Kaynaklar
4. `docs/` altında uygun dizine kaydet
5. CONTEXT.md'de yeni terim varsa ekle

## Çıktı

- `docs/` altında yapılandırılmış spesifikasyon dosyası
