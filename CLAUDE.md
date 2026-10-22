# Hermes Wraps

Sitio en `public/`, worker en `worker/`, despliegue con `wrangler.jsonc`.

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

Las de SaaS (`paywalls`, `signup`, `onboarding`, `churn-prevention`, `aso`, `free-tools`, `revops`) no aplican a un taller de vinilo; no las recomiendes salvo que el pedido lo justifique.
