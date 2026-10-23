# Plan de optimización de la web de Hermes Wraps

Fecha: 23 de octubre de 2026. Decidido en una sesión de `/grill-me` con Angelica.
Se aplica con la skill `/plan-optimizacion`, una fase por sesión.

Documentos relacionados:
- `docs/pendientes-del-cliente.md`: lo que solo puede hacer Hermes. Los puntos 🔴 bloquean fases.
- `docs/guia-medicion-ga4-instagram.md`: guía de GA4 e Instagram para Hermes.
- `docs/research/2026-10-22-optimizacion-web.md`: la investigación de la que sale este plan.

---

## Estado

La skill `/plan-optimizacion` actualiza esta tabla al terminar cada fase.

| Fase | Estado | Bloqueada por | Última actualización |
|---|---|---|---|
| 1. Perfil de Google y reseñas | ⏳ Pendiente | A1 y A2 (Hermes/Angelica) | 2026-10-23 |
| 2. Medición GA4 + UTM | ⏳ Pendiente | B0, B1 y B2 | 2026-10-23 |
| 3. Schema y `llms.txt` | ⏳ Pendiente | Nada, se puede empezar ya | 2026-10-23 |
| 4. 10 emails a pymes | ⏳ Pendiente | D1, D2 y D3 | 2026-10-23 |
| 5. Catálogo automático desde Drive | ⏳ Pendiente | C1 y C2, y comprobar los hechos técnicos (ver fase 5) | 2026-10-23 |
| 6. Auditoría CRO y decisión de anuncios | ⏳ Pendiente | 4 a 6 semanas de datos de la fase 2 | 2026-10-23 |
| En pausa | — | Visualizador con IA y correo con el dominio | 2026-10-23 |

---

## Meta y reglas

**Meta:**
- Más visitas medibles desde Instagram y Google.
- Más clientes potenciales: cotizaciones enviadas, clics a WhatsApp y llamadas.
- **1 contrato con una pyme estadounidense en 6 meses, mejor si es antes de año nuevo.**

**Presupuesto:** $20 USD al mes para herramientas de pago. Sube solo cuando haya resultados medidos.

**Reglas que no se rompen:**
1. La experiencia del usuario es la prioridad.
2. Los cambios invisibles (scripts de medición, schema, `llms.txt`) están permitidos.
3. Todo lo visible (diseño, copy, flujo de `book.html`) pasa por `hermes-wraps`. Si choca con una skill de marketing, gana `hermes-wraps`.
4. Después de cualquier cambio en `public/`, se corre `quality-insurance` o el agente `impeccable-qa`.
5. Nada se manda en nombre de Hermes sin su aprobación: emails, respuestas a reseñas, textos.

**Contexto del negocio que cambia el plan:**
- Hermes tiene taller e imprenta, y ya trabajó para empresas.
- La web ya muestra 9 trabajos comerciales en `work.html#commercial`.
- El perfil de Google tiene unas 12 reseñas, todas de los últimos días y casi todas de carros particulares. Ninguna es de una empresa.
- Ningún competidor revisado ofrece atención en español. La mitad de las reseñas de Hermes están en español.
- Las ideas que suben el costo (visualizador con IA, correo con el dominio) quedan para cuando haya volumen.

---

## Fase 1. Perfil de Google y reseñas

**Por qué primero:** no toca la web, no cuesta nada y protege el activo local más valioso.
**Skills:** `directory-submissions` (estrategia del perfil) + `hermes-wraps` (voz de las respuestas).

1. **Lo que hace Hermes/Angelica (A1 y A2):**
   - Angelica borra su propia reseña. Google prohíbe las reseñas de quien trabaja con el negocio.
   - De aquí en adelante se piden 1 o 2 reseñas por semana, solo a clientes reales y después de cada entrega.
2. **Lo que hace el editor:**
   - Redactar en `docs/gbp/respuestas-resenas.md` una respuesta corta por reseña, en el idioma del cliente. Cada una menciona el servicio y la zona, sin sonar a relleno de palabras clave.
   - Reseñas a responder:
     - Ilia Graupera: diseño del auto y entrega rápida (ES)
     - Jose David Milian (ES)
     - Daypanman: quiere volver con sus próximos carros (ES/EN)
     - Armando Garcia: garantía y calidad (ES)
     - Gaban yt: instalación rápida (EN)
     - Benito Perez (ES)
     - Daniel Morales: precio y trato (ES)
     - Patty Pink: techo y espejos en negro brillante (EN)
     - eddie salazar (EN)
     - Carlos Garcia
     - Alina Suarez
   - Pedirle a Angelica el texto completo de las dos últimas, que llegó incompleto.
3. **Lista para el perfil (A4):**
   - Categoría principal "Vehicle wrapping service" y secundarias de letreros y gráficos. Verificar los nombres exactos en el perfil.
   - Servicios con descripción.
   - Zona de servicio (Brandon, Riverview, Valrico, Tampa…).
   - Horario.
   - Atributo "Se habla español".
   - Fotos de los trabajos comerciales del catálogo.
4. **Un mensaje para pedir reseñas,** que Hermes manda por WhatsApp al entregar. En inglés y en español, con el enlace directo `https://g.page/r/Cee8rYVGvW4pECE/review`.

**Está terminada cuando:** las respuestas y la lista del perfil están en `docs/gbp/` y Hermes confirma que las aplicó.

---

## Fase 2. Medición: GA4 y UTM

**Por qué:** sin medición no se puede saber si las demás fases funcionan. Además, deja todo listo para los anuncios.
**Skills:** `analytics` (plan de medición) + `conversion-tracking` (eventos al confirmar el éxito, nunca al hacer clic).

**Bloqueada hasta tener:**
- El ID `G-…` (B1 y B2).
- El texto de privacidad aprobado por Hermes (B0).

**Lo que ya existe en el código:**
- `public/assets/site.js` reenvía cada clic sobre un elemento `[data-track]` a `window.hwTrack(name)`, si esa función existe. Hoy no existe.
- Todos los CTA ya tienen `data-track`: `whatsapp-*`, `call-*`, `email-*`, `cta-*`, `instagram-*`, `maps-*`, `submit-*`…
- `public/assets/book.js` llama a `show('sent')` cuando `/api/consult` responde bien, y a `show('whatsapp')` cuando el visitante elige WhatsApp.
- Cloudflare Web Analytics ya cuenta las páginas vistas. Se mantiene.
- `public/_headers` no tiene CSP. Si algún día se agrega, tiene que permitir `googletagmanager.com` y `google-analytics.com`.

**Qué cambiar (todo invisible menos el punto 4):**
1. Poner el snippet de `gtag.js` con el ID en el `<head>` de las 5 páginas: `index`, `work`, `book`, `terms` y `404`.
2. Definir `window.hwTrack` para que traduzca los nombres que ya existen:

   | `data-track` | Evento GA4 |
   |---|---|
   | `whatsapp-*` | `click_whatsapp` (con `location` igual al sufijo) |
   | `call-*` | `click_call` |
   | `email-*` | `click_email` |
   | `cta-*` | `click_cta` |
   | `instagram-*`, `facebook-*`, `tiktok-*` | `click_social` |
   | `maps-*` | `click_maps` |

   No hay que cambiar ningún HTML.
3. En `book.js`, disparar `generate_lead` dentro de `show()`:
   - Cuando el estado es `'sent'`, con `method: 'form'`.
   - Cuando el estado es `'whatsapp'`, con `method: 'whatsapp'`.
   - Nunca en el clic de `submit-*`.
   - Mandar el tipo de proyecto, sin datos personales.
4. **Texto visible:** cambiar la frase de privacidad de `terms.html` ("This site uses cookie-free analytics…"). Se redacta con `copywriting` + `hermes-wraps` y Hermes la aprueba antes. El cambio sale el mismo día que GA4, nunca después.
5. No poner banner de cookies. No es obligatorio para un negocio de este tamaño en Florida y empeora la experiencia del usuario.
6. Verificar en GA4 → DebugView que llegan `generate_lead`, `click_whatsapp` y `click_call`. Después correr `quality-insurance`.
7. Recordarle a Hermes el paso 8 de la guía: marcar los eventos clave. Y que ponga los enlaces UTM en las bios (B4).

**Está terminada cuando:** DebugView muestra los 3 eventos, `quality-insurance` sale bien, las bios tienen UTM y los eventos clave están marcados.

---

## Fase 3. Schema y `llms.txt`

**Por qué:** mejora Google y las respuestas de las IAs ("wrap shop near Brandon") y es invisible para el visitante. No depende del cliente.
**Skills:** `schema` + `ai-seo` (y `seo-audit` si aparece algo más).

**Lo que hay hoy:** un único JSON-LD `AutomotiveBusiness` en `index.html`. Ya incluye `knowsLanguage: en, es`, `geo`, `hasMap` y `sameAs`. Las demás páginas no tienen JSON-LD.

**Qué hacer:**
1. `index.html`:
   - Añadir `hasOfferCatalog` con los servicios reales: fleet wraps, color change, partial wraps, chrome delete, signs y window graphics.
   - Añadir `openingHours` cuando Hermes lo confirme.
   - Añadir un nodo `WebSite`.
   - **No** añadir `aggregateRating` con las reseñas de Google. Google no muestra las reseñas que un negocio pone sobre sí mismo y puede tomarlo como marcado engañoso.
2. `work.html`: `CollectionPage` + `ItemList` con los proyectos. Se genera desde `scripts/build.py` y `scripts/pages.py`, para que la fase 5 lo mantenga sola.
3. `book.html`: `ContactPage`.
4. `BreadcrumbList` en las páginas internas.
5. `public/llms.txt`:
   - Qué es Hermes Wraps, zona, servicios, idiomas, cómo pedir cotización y enlaces a las páginas.
   - En inglés, con la voz de `hermes-wraps`.
   - Solo hechos que estén en `.agents/product-marketing.md`.
6. Validar con el Rich Results Test y el Schema Markup Validator. Después correr `quality-insurance`.

**Está terminada cuando:** las 4 páginas públicas validan sin errores y `llms.txt` está publicado.

---

## Fase 4. Prueba de 10 emails a pymes

**Por qué:** es lo único que puede dar un contrato antes de año nuevo. La web sirve como prueba de confianza.
**Skills:** `prospecting` (lista), `cold-email` (texto y secuencia), `hermes-wraps` (voz). `sales-enablement` solo si alguien pide una hoja de presentación.

**Bloqueada hasta tener:**
- Los casos elegidos (D1).
- El compromiso de hacer maquetas (D2).
- La aprobación del texto (D3).

1. **Lista de 10 contactos** en `docs/outreach/lista.md`:
   - Pymes de Brandon, Riverview y Valrico con 1 a 3 vehículos sin rotular o con rotulación vieja: plomería, aire acondicionado, limpieza, paisajismo, eléctricos.
   - Para cada una: nombre del negocio, dueño o encargado si se encuentra, email, fuente y por qué encaja.
   - Fuentes públicas: Google Maps, la web del negocio y Sunbiz (registro de empresas de Florida).
   - Evitar los correos genéricos cuando haya un nombre.
2. **Secuencia** en `docs/outreach/emails.md`:
   - Día 0: email inicial.
   - Día 3: seguimiento corto.
   - Día 8: cierre amable.
   - Si alguien responde, se para.
   - Es inglés profesional y directo, sin frases típicas de IA.
   - Gancho: *"Send us your logo and a photo of your van and we'll send you a free mockup."* Hermes hace la maqueta a mano, así que cuesta $0. Es la idea 3 sin IA.
   - Prueba: 2 o 3 trabajos comerciales con enlace a `https://hermeswraps.com/work.html#commercial`.
   - Firma de Hermes con teléfono y WhatsApp.
3. **Envío:** a mano, desde `hermeswraps@gmail.com`. Sin apertura rastreada ni herramientas de envío masivo.
4. **Seguimiento** en `docs/outreach/lista.md`: enviado, respondió, pidió maqueta, cotización, cerrado.
5. **Respuesta en menos de 24 horas** (D4).

**Está terminada cuando:** los 10 contactos tienen la secuencia completa.
**Qué cuenta como éxito:** al menos 1 maqueta pedida. Si alguien responde, se pasa a un correo con el dominio (pendiente F3).

---

## Fase 5. Catálogo automático desde Drive

**Decidido:**
- Revisión cada 48 a 72 horas.
- **Publica sin aprobación manual**, pero solo las fotos que pasan los filtros.
- Las que fallan quedan apartadas y aparecen en el informe.
- Al terminar, una notificación al teléfono, solo si hubo fotos.
- Los textos salen de la subcarpeta, nada más.

**Estructura en Drive (C1):** `Hermes Wraps/Nuevos/` con exactamente las categorías de la web:
- `commercial/`
- `vehicle/`
- `signs/`

**Antes de construir, comprobar estos hechos con el agente `matt-researcher`** (resultado en `docs/research/`):
1. Si una Routine en la nube puede **mergear a `main`** o hacer push fuera de las ramas `claude/…`. Si no puede: PR con auto-merge cuando pasan los checks, o un permiso de push sin restricción.
2. Si el conector de Google Drive **descarga archivos binarios** (JPG y HEIC) dentro de la Routine.
3. Si `scripts/enhance.py` corre en Linux sin GPU en un tiempo razonable. Hoy lee rutas `G:/My Drive/...` de Windows, así que hay que pasarlas a variable o argumento.

**Qué hace cada ejecución:**
1. Lista los archivos de `Nuevos/` que todavía no están en un manifiesto (`scripts/drive_manifest.json`, con id y hash de cada archivo).
2. Aplica los filtros. Si alguno falla, la foto se aparta:
   - Resolución mínima.
   - Que no esté borrosa (varianza del laplaciano).
   - Subcarpeta válida.
   - Que no sea un duplicado (hash perceptual).
3. Convierte la foto y corre `enhance.py` para generar las versiones `.jpg`/`.webp` y la de 800 px, igual que las actuales.
4. Agrega la entrada a `projects` en `scripts/pages.py`:
   - La categoría sale de la subcarpeta.
   - El título, la etiqueta, la descripción y el `alt` se escriben en inglés con la voz de `hermes-wraps`.
   - Lo que no se ve en la foto no se inventa.
5. Corre `scripts/build.py` y la revisión `quality-insurance`. Si algo falla, no publica nada en esa ejecución y lo avisa.
6. Commit y publicación según lo que resulte del punto 1 de la comprobación.
7. Mueve el archivo en Drive a `Publicadas/`, o lo registra en el manifiesto.
8. Manda la notificación al teléfono: qué publicó, qué apartó y por qué.

**Horario:** `CRON_TZ=America/New_York 17 9 */2 * *`, es decir, cada dos días a las 9:17. Son unas 15 ejecuciones al mes y entran en Pro o en Max.

**Está terminada cuando:** una foto de prueba en `Nuevos/vehicle/` aparece en `work.html` sin intervención, y otra borrosa queda apartada con su aviso.

---

## Fase 6. Auditoría CRO y decisión de anuncios

**Cuándo:** con 4 a 6 semanas de datos de GA4.
**Skills:** `cro` (solo un informe), `ads`, `ad-creative` + `hermes-wraps`.

1. Informe `cro` de `index.html`, `work.html` y `book.html` en `docs/`. No se cambia nada sin aprobación, y todo lo que se apruebe pasa por `hermes-wraps` y `quality-insurance`.
2. Con los números de GA4, decidir con Hermes (F1):
   - El presupuesto.
   - El primer canal. La recomendación es Google Search con "fleet wraps Tampa" para B2B; Meta, más adelante.
   - El costo aceptable por consulta.
3. Si se aprueban anuncios: vincular Google Ads en GA4 e importar los eventos clave. Para Meta, añadir el píxel. Las dos cosas sobre la medición de la fase 2.
4. Recalcular los $20 al mes según los resultados.

---

## En pausa

| Idea | Por qué espera | Cuándo se retoma |
|---|---|---|
| Visualizador con IA (idea 3) | Cuesta dinero por uso y todavía no hay volumen. Mientras tanto se cubre con las maquetas a mano de la fase 4. | Cuando haya tráfico medido y se quiera escalar. Empezar por la prueba de unas 20 fotos de la investigación. |
| Correo `@hermeswraps.com` | Para 10 emails, Gmail alcanza. | Cuando la fase 4 consiga respuestas. |
| `programmatic-seo` (páginas por ciudad y servicio) | Crea páginas nuevas visibles. | Después de la fase 6. |

## Decisiones tomadas en el grill (23 de octubre de 2026)

- El éxito se mide en clientes potenciales (formulario, WhatsApp y llamadas) **más** tráfico desde Instagram y Google.
- La meta principal es el B2B, con 1 contrato con una pyme. Mientras tanto, cualquier trabajo sirve.
- Las ideas nuevas son bienvenidas si respetan los guardrails y la experiencia del usuario.
- Habrá anuncios cuando se aprenda a hacerlos. El canal y el presupuesto se deciden con Hermes.
- Guardrail: lo invisible se permite y lo visible pasa por `hermes-wraps` y `quality-insurance`.
- Presupuesto: $20 USD al mes, ampliable si hay resultados.
- Instagram: Angelica ya hace los reels. Solo falta medirlos con UTM.
- Catálogo: cada 48 a 72 horas, sin aprobación manual, con filtros, notificación y textos que salen de la subcarpeta.
- Hermes imprime y tiene taller (opción d), y ya trabajó para empresas.
- Contacto: 10 emails profesionales desde Gmail, con la maqueta gratis como gancho.
- Perfil de Google: borrar la reseña propia, pedir reseñas con calma, responderlas todas y marcar "Se habla español".
