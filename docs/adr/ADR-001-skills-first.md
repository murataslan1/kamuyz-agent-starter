# ADR-001: Skill-tabanlı repo mimarisi

**Tarih:** 2026-08-06
**Durum:** Kabul edildi
**Karar veren:** KamuYZ APA Çalışma Grubu

## Bağlam

`kamuyz-agent-starter` reposu yalnızca bir OpenClaw/Hermes kurulum şablonu değil, aynı zamanda ekibin agentic AI geliştirme sürecinde kullanacağı yetenekleri (skills) barındıran bir sistem olmalı. İki referans mimari incelendi:

1. **obra/superpowers:** Agent coding metodolojisi — 14 skill, auto-trigger, TDD-zorunlu pipeline
2. **mattpocock/skills:** Mühendislik skill'leri — user-invoked/model-invoked ayrımı, build chain (`grill-with-docs → to-spec → to-tickets → implement → code-review`)

Ayrıca mevcut `shared-skills/` dizininde 60+ içerik üretim, sosyal medya ve üretkenlik skill'i bulunuyor.

## Karar

Repo 3 katmanlı skill mimarisi kullanacak:

1. **skills/engineering/** — Geliştirme süreci skill'leri (superpowers + mattpocock desenleri)
2. **skills/content/** — İçerik üretim skill'leri (shared-skills'ten seçilenler)
3. **skills/productivity/** — Ekip yönetimi skill'leri (shared-skills'ten seçilenler)

Her skill `SKILL.md` formatında, `name` + `description` YAML frontmatter ile.

## Sonuçlar

- Skill'ler OpenClaw SOUL.md/MEMORY.md'e reference olarak eklenebilir
- Hermes learning loop ile skill'ler zamanla iyileşir
- Ekip yeni skill ekleyebilir (contributing guide ile)
- CONTEXT.md glossary skill'lerle birlikte büyür
