# Mühendislik Skill'leri

Bu dizin, KamuYZ agent-starter geliştirme sürecinde kullanılan mühendislik skill'lerini içerir. Skill mimarisi **mattpocock/skills** ve **obra/superpowers** referans alınarak tasarlanmıştır.

## Skill Zinciri

```
research → to-spec → implement → code-review
```

| Skill | Tetikleyici | Açıklama |
|---|---|---|
| [research](research/SKILL.md) | Araştırma ihtiyacı | Birincil kaynaklara dayalı araştırma, arka plan ajanı |
| [to-spec](to-spec/SKILL.md) | Plan netleştiğinde | Konuşmayı/araştırmayı yapılandırılmış spec'e dönüştür |
| [implement](implement/SKILL.md) | Spec onaylandığında | Adım adım uygula, test et, commit'le |
| [code-review](code-review/SKILL.md) | Merge öncesi | Standartlar + spesifikasyon iki eksenli inceleme |

## Skill Formatı

Her skill `SKILL.md` dosyasıdır, YAML frontmatter içerir:

```yaml
---
name: skill-adi
description: Use when [tetikleyici koşullar]. Eylemi değil tetikleyiciyi tarif et.
---
```

## Referanslar

- [mattpocock/skills](https://github.com/mattpocock/skills) — Skill mimarisi referansı
- [obra/superpowers](https://github.com/obra/superpowers) — Agent coding metodolojisi
- [agentskills.io](https://agentskills.io) — Skill format standardı
