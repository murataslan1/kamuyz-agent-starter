---
name: code-review
description: Yapılan değişiklikleri iki eksende incele: Standartlar (repo kurallarına uygunluk) ve Spesifikasyon (orijinal spec/göreve sadakat). Use when bir implementasyon tamamlandığında, merge öncesi.
---

# Kod İncelemesi (code-review)

Yapılan değişiklikleri merge öncesi iki eksende incele.

## Ne zaman kullanılır

- implement tamamlandığında
- PR merge öncesi
- Bir görev kartı kapatılmadan önce

## Süreç

### Eksen 1: Standartlar

- Dosya adlandırma ve dizin yapısı doğru mu?
- CONTEXT.md'deki terimler doğru kullanılmış mı?
- YAML frontmatter (`name`, `description`) eksiksiz mi?
- Markdown formatı tutarlı mı?

### Eksen 2: Spesifikasyon

- Orijinal spec'teki tüm maddeler karşılanmış mı?
- Kapsam dışı denilen hiçbir şey eklenmemiş mi?
- Bağımlılıklar doğru belirtilmiş mi?

## Çıktı

- Sorun listesi (kritik, orta, düşük)
- Kritik sorun varsa merge engellenir
