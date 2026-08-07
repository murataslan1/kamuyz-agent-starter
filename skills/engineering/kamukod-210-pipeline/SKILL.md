# KamuKOD 210 — Workshoptan Satışa Tam Sistem

Bu skill, OpenClaw & Hermes eğitiminden B2B satışa kadar tüm süreci belgeler.

## İçerik Üretim Pipeline'ı

```
ARAŞTIRMA           →    YAZI       →    VİDEO      →    SUNUM      →    DAĞITIM
Grok + Gemini       →   3 blog      →   18 video    →   HTML/PDF     →   LinkedIn/X
NotebookLM          →   whitepaper  →   VSL (4dk)   →   PPTX/PNG     →   E-posta
skills.sh           →   TR + EN     →   Gemini      →   infografik   →   WhatsApp
```

## Kullanılan Skill'ler

| Skill | Kaynak | Ne üretti? |
|---|---|---|
| event-marketer | skills.sh | EPIC checklist, funnel, lead scoring |
| webinar-plan | skills.sh | Run-of-show, promosyon takvimi, e-posta serisi |
| LinkedIn post | shared-skills | 5 gönderi + içerik takvimi |
| X thread | shared-skills | 8 tweet'lik thread |
| X tweet craft | shared-skills | 5 farklı hook tipi |
| short-form | shared-skills | 2 Reels/TikTok script'i |
| carousel | shared-skills | 8 slide Instagram/LinkedIn |
| thumbnail | shared-skills | 5 başlık + 3 konsept + A/B test |
| sales strategy | shared-skills | Huni, segmentasyon, itiraz yanıtları |
| lead intelligence | shared-skills | Skorlama matrisi |
| follow-up | shared-skills | Takip kuralları ve şablonlar |
| PIPELINE | shared-skills | Tam içerik zinciri |

## Kullanılan Araçlar

| Araç | Ne için? |
|---|---|
| Remotion | 10 B2B videosu (MP4) |
| Gemini Video | 7 tanıtım videosu |
| NotebookLM | Podcast + sunum (PPtx + PDF) |
| HyperFrames | HTML tabanlı video (hazır, FFmpeg bekliyor) |
| Playwright | HTML → PNG/PDF dönüşüm |
| python-pptx | MD → PPTX sunum |
| Apify | LinkedIn lead scraping |

## Repo Yapısı

```
kamuyz-agent-starter/          ← Public (eğitim, açık kaynak)
├── README.md                  ← Hermes öğrenme rehberi
├── hermes-paket/              ← Tek komutla güvenli kurulum
├── docs/research/             ← 4 araştırma raporu
├── docs/whitepaper/           ← TR + EN
├── docs/events/               ← E1, E2, E3 taslakları
├── yazi-serisi/               ← 3 blog yazısı
├── LEARNING.md                ← 2 haftalık plan
├── SECURITY.md                ← 24 maddelik kontrol
└── kamu-yz-agent-export/      ← AGENT.md + 8 skill

kamuyz-pazarlama/              ← Private (satış, B2B)
├── videolar/ (18 MP4)
├── sunumlar/ (HTML, PDF, PPTX, PNG)
├── etkinlik/ (LinkedIn, X, Luma, playbook)
├── kamukod-210/ (landing, SSS, karşılaştırma)
├── b2b/ (teklif, kullanım vakaları)
├── notebooklm/ (podcast + sunum)
├── kampanya/ (satış stratejisi, lead'ler)
└── plan.md (aksiyon planı)
```

## Dağıtım Zinciri

```
GitHub (açık repo) → KamuYZ E1-E2-E3 (ücretsiz) → KamuKOD 210 (ücretli) → B2B (kurumsal)
```
