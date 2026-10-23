# Hermes Wraps

Sitio en `public/`, worker en `worker/`, despliegue con `wrangler.jsonc`.

## Skills del proyecto

Todo vive en el repo, así que cualquier editor con Claude Code las tiene al abrirlo:

- `.claude/skills/hermes-wraps/` — marca y diseño (fuente de verdad: tokens, voz, componentes, guía de color).
- `.claude/skills/quality-insurance/` — revisión de que el trabajo no se aparte de la marca.
- `.claude/skills/<resto>/` — skills de marketing de coreyhaines31/marketingskills (`skills-lock.json` registra la versión; `npx skills update -p` las actualiza).
- `.claude/skills/grill-me`, `grilling`, `teach`, `handoff`, `to-questionnaire`, `research` — skills de trabajo de mattpocock/skills (misma actualización con `npx skills update -p`).
- `.claude/agents/impeccable-qa.md` — agente de QA del sitio.
- `.claude/agents/researcher.md` — investigador general: aplica la skill `research` y guarda lo que encuentra en `docs/research/`.
- `.agents/product-marketing.md` — ficha base del negocio que leen las skills de marketing. Actualízala con la skill `product-marketing`.

## Qué skill usar (marketing, web y redes)

Ante cualquier pedido de marketing, recomienda la skill antes de empezar y explica en una frase por qué, sobre todo si conviene más que las propias del cliente.

Reglas:

- `hermes-wraps` manda en todo lo visual y de marca: colores, tipografía, componentes, tono, CTA y layouts (web, emails, piezas para redes y anuncios). Si una skill de marketing choca con ella, gana `hermes-wraps`.
- Las skills de marketing (`.claude/skills/`, de coreyhaines31/marketingskills) deciden la estrategia, el canal y la estructura. Úsalas junto con `hermes-wraps`, no en su lugar.
- Tras cualquier cambio en `public/`, corre `quality-insurance` (o el agente `impeccable-qa`).
- Casi todas las skills de marketing leen `.agents/product-marketing.md`. Si no existe, el primer paso es `product-marketing`, rellenado a partir de `hermes-wraps` para que el posicionamiento coincida con la marca.

| Pedido | Skill |
|---|---|
| Posicionamiento, cliente ideal, voz de marca (base para el resto) | `product-marketing` + `hermes-wraps` |
| Plan de marketing general (90 días, 12 meses) | `marketing-plan` |
| Ideas sueltas de crecimiento | `marketing-ideas` |
| Contrastar una decisión desde varios ángulos | `marketing-council` |
| Pilares de contenido, calendario editorial, blog | `content-strategy` |
| Posts, carruseles, Reels/TikTok, calendario de redes | `social` (copy y estructura) + `hermes-wraps` (diseño) |
| Guiones y producción de vídeo | `video` |
| Imágenes generadas para piezas | `image` + `hermes-wraps` |
| Anuncios pagados (Meta, Google) | `ads`, `ad-creative` + `hermes-wraps` |
| Textos de páginas web | `copywriting` + `hermes-wraps` |
| Pulir un texto ya escrito | `copy-editing` |
| Que la web convierta más (formulario de cotización, reservas) | `cro`, `popups` |
| Medir formularios, llamadas, WhatsApp | `conversion-tracking`, `analytics` |
| SEO del sitio y SEO local | `seo-audit`, `schema`, `site-architecture`, `ai-seo` |
| Directorios y perfiles (Google Business, etc.) | `directory-submissions` |
| Email y SMS | `emails`, `sms` |
| Clientes que recomiendan clientes | `referrals` |
| Flotas y cuentas comerciales (B2B) | `prospecting`, `cold-email`, `sales-enablement` |
| Promociones, garantías, paquetes | `offers`, `pricing` |
| Competencia | `competitors`, `competitor-profiling` |
| Prensa, eventos, alianzas | `public-relations`, `events`, `co-marketing` |

## Skills de trabajo (mattpocock/skills)

No deciden marketing ni marca; ayudan a pensar, investigar y pasar el trabajo.

| Pedido | Skill |
|---|---|
| Poner a prueba un plan antes de ejecutarlo (por ejemplo, el de `marketing-plan`) | `/grill-me` |
| Aprender un tema en varias sesiones | `/teach` |
| Preguntas que solo puede contestar el cliente u otra persona | `/to-questionnaire` (guárdalo en `docs/`) |
| Dejar el trabajo listo para el otro editor | `/handoff` (en sesiones en la nube, `/tmp` se borra: guárdalo en `docs/handoffs/` y súbelo) |
| Investigar mercado, competencia, plataformas, normas o herramientas | `research` |

Investigación: cualquier encargo de investigar se delega al agente `researcher`, no a un agente `general-purpose`. Si hace falta un agente genérico, que siga `.claude/skills/research/SKILL.md`: fuentes primarias, una cita por afirmación y el resultado en `docs/research/`.

Las de SaaS (`paywalls`, `signup`, `onboarding`, `churn-prevention`, `aso`, `free-tools`, `revops`) no aplican a un taller de vinilo; no las recomiendes salvo que el pedido lo justifique.
