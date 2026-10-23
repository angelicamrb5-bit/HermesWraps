---
name: plan-optimizacion
description: Applies the Hermes Wraps website optimization plan (docs/plan-optimizacion-web.md) one phase at a time - Google Business Profile and reviews, GA4 measurement and UTM, schema and llms.txt, the 10-email outreach test, the automatic Drive catalog and the CRO/ads review. Use when the user says "/plan-optimizacion", "aplica el plan", "siguiente fase", "estado del plan" or asks to continue the optimization plan.
---

# Aplicar el plan de optimización

El plan es `docs/plan-optimizacion-web.md`. Esta skill lo ejecuta **una fase por sesión**, sin saltarse las reglas.

## Al invocarla

1. Lee estos tres documentos completos:
   - `docs/plan-optimizacion-web.md`
   - `docs/pendientes-del-cliente.md`
   - `.agents/product-marketing.md`
2. Si el usuario nombra una fase (`/plan-optimizacion 3`), trabaja esa. Si no, propón la primera fase pendiente que no esté bloqueada, según la tabla **Estado**. Las fases 1 y 3 se pueden hacer en paralelo con las demás.
3. Antes de tocar nada, muéstrale al usuario:
   - Qué fase vas a hacer.
   - Qué skills vas a usar y por qué, en una frase.
   - Qué archivos vas a cambiar.

   Espera a que diga que sí.

## Bloqueos

- Cada fase dice qué puntos de `docs/pendientes-del-cliente.md` la bloquean.
- Si un punto 🔴 sigue pendiente, **no lo inventes ni lo rodees**. Pregunta al usuario si ya está resuelto. Si no lo está, prepara solo lo que no dependa de ese punto (borradores en `docs/`) y deja la fase como 🟡 En curso.
- Nunca inventes datos del negocio: horario, garantía, zonas, nombres de clientes, reseñas. Lo que falte va como `[CLIENT TO SUPPLY: …]`.
- Los hechos técnicos que dependen de plataformas externas los comprueba el agente `matt-researcher`, en segundo plano, antes de construir. Por ejemplo, los límites de las Routines o del conector de Drive (fase 5).

## Reglas que no se rompen

1. **Experiencia del usuario primero.** No cambies el diseño, el copy visible ni el flujo de `book.html` salvo que la fase lo pida explícitamente. Si lo pide, pasa por la skill `hermes-wraps`, y gana `hermes-wraps` si choca con una skill de marketing.
2. **Los cambios invisibles están permitidos:** scripts de medición, JSON-LD, `llms.txt`.
3. **Después de cualquier cambio en `public/`,** corre `quality-insurance` o el agente `impeccable-qa`, y no des la fase por terminada hasta que pase.
4. **Nada sale en nombre de Hermes sin su aprobación.** Emails, respuestas a reseñas y textos de privacidad se dejan como borradores en `docs/`.
5. **Medición:** los eventos de conversión se disparan al confirmar el éxito (`show('sent')` en `book.js`), nunca al hacer clic en enviar. No se mandan datos personales a GA4.
6. **El texto de privacidad de `terms.html`** tiene que cambiar el mismo día que GA4, con el texto aprobado. Hoy dice "cookie-free analytics".
7. **No agregues un banner de cookies** ni scripts de terceros que no pida el plan.
8. **Presupuesto:** $20 USD al mes. Nada de pago sin que el usuario lo apruebe.

## Al terminar una fase

1. Comprueba la condición de "Está terminada cuando" de la fase. Si no se cumple, la fase queda 🟡 En curso con una nota de lo que falta.
2. Actualiza la tabla **Estado** de `docs/plan-optimizacion-web.md`:
   - ⏳ Pendiente, 🟡 En curso o ✅ Hecha.
   - Lo que la bloquea.
   - La fecha.
3. Si Hermes resolvió algún punto, márcalo en `docs/pendientes-del-cliente.md` añadiendo ✅ al principio de la fila.
4. Haz commit con un mensaje que nombre la fase y push a la rama de trabajo de la sesión. No abras un PR salvo que el usuario lo pida.
5. Dile al usuario en español:
   - Qué se hizo.
   - Qué quedó pendiente y de quién depende.
   - Cuál es la siguiente fase recomendada.

## Si el plan necesita cambiar

Si aparece un hecho que contradice el plan (un límite técnico, una norma, un dato de Hermes), **no lo cambies por tu cuenta**. Explícale al usuario el conflicto y propón el ajuste. Si lo aprueba, edita el plan y anota el cambio en "Decisiones tomadas", con la fecha.
