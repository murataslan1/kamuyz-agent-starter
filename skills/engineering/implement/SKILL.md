---
name: implement
description: Bir spesifikasyonu veya görev listesini adım adım uygula. Her adımda test et, doğrula, commit'le. Use when bir spec veya ticket onaylandığında ve uygulama zamanı geldiğinde.
---

# Uygula (implement)

Bir spesifikasyonu, planı veya görev listesini adım adım uygula.

## Ne zaman kullanılır

- to-spec ile spesifikasyon onaylandığında
- Sprint planındaki bir görev uygulanacağında
- Bir hata düzeltmesi yapılacağında

## Süreç

1. Spesifikasyonu veya görev kartını oku
2. İşi bağımsız, küçük adımlara böl
3. Her adımda:
   a. Değişikliği yap
   b. Test/dogrula
   c. Commit'le
4. Tüm adımlar tamamlandığında code-review'a gönder

## Kalite Barı

- Her commit tek bir mantıksal değişiklik içerir
- CONTEXT.md ile çelişki yok
- Dosya yapısı repo standartlarına uygun
