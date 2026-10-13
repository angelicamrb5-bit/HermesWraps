# Auditoría web — Hermes Wraps (primera pasada, desordenada a propósito)

> Documento de trabajo en bruto, sin pulir. Más detalle > más orden. Hay duplicados y solapamientos a propósito (se cruzan con IDs).
> Etiquetas de certeza: **[VERIFICADO]** observado directamente · **[PROBABLE]** inferido de evidencia · **[SUPUESTO]** suposición razonable sin comprobar · **[NO VERIFICADO]** no se pudo comprobar · **[PREGUNTA]** necesita respuesta del dueño/equipo

---

## 0. Meta

- **Fecha:** 2026-10-13
- **Auditor:** Claude Code (skill `website-audit`)
- **Alcance:** solo sitio en vivo → `https://muddy-glitter-1944.josedavidmm9511.workers.dev/`
  - El repo `HermesWraps` (donde se guarda este informe) **no contiene el código del sitio**: solo `README.md` y la skill. Por eso no hubo auditoría de código fuente real; las observaciones de "código" salen del HTML/CSS/JS que sirve el sitio en vivo. [VERIFICADO]
- **Páginas revisadas:** 1 (es una landing de una sola página con anclas) + `/robots.txt` + `/sitemap.xml` (404) + una URL inventada para probar el 404 + el dominio `hermeswraps.com` (no resuelve).
- **Viewports revisados:** escritorio 1440×900 (captura de página completa, 1440×8441 px) y móvil (captura de Firecrawl en modo móvil, 360 px de ancho, 13 484 px de alto). Tablet no capturada. [VERIFICADO]
- **Herramientas usadas:**
  - Firecrawl `scrape` (markdown, links, rawHtml, screenshot escritorio y móvil) — fuente principal.
  - Firecrawl `search` (una búsqueda para presencia externa).
  - Python para: cálculo de contraste WCAG, conteo de tokens CSS, detección de CSS no usado, conteos de copy.
  - Lectura visual de las capturas (cortadas en franjas).
- **Herramientas NO disponibles / no usadas y qué significa:**
  - `curl` directo y el script Playwright de la skill → **bloqueados** por el proxy del contenedor (`CONNECT tunnel failed, 403`). Consecuencia: **no tengo cabeceras HTTP** (caché, compresión, HSTS, CSP, etc.), ni tamaños de archivos (imágenes/vídeos), ni errores de consola, ni peticiones fallidas, ni orden de tabulación real. Todo eso queda [NO VERIFICADO].
  - Lighthouse / PageSpeed / axe → no ejecutados. Puntuaciones de rendimiento y accesibilidad automáticas [NO VERIFICADO]. Hice comprobaciones manuales en su lugar.
  - Modo oscuro: el sitio declara `color-scheme: light dark` y tiene tokens oscuros, pero las capturas salieron en modo claro. Aspecto visual en oscuro [NO VERIFICADO].
- **Nota sobre el HTML analizado:** el `rawHtml` de Firecrawl parece un DOM serializado (URLs absolutizadas a `https://muddy-glitter-…/#process`, CSS normalizado a `0px`, `rgb(…)`, `<style rel="stylesheet">` con `@charset`). **[PROBABLE]** que el CSS original sea un archivo externo o esté escrito distinto. Las observaciones de formato de código se refieren a esa serialización, no necesariamente al archivo fuente exacto.
- **Fuera de alcance / no hecho:** no envié el formulario (ni email, ni WhatsApp, ni copiar). No probé redes sociales a fondo. No contacté al negocio.
- **Carpeta de evidencias:** capturas y HTML guardados solo en el scratchpad de la sesión (temporal, no en el repo): `desktop-full.png`, `mobile-full.png`, `home.html`, `home.md`, `meta.json`, `links.txt`. Si se quieren conservar, hay que pedirlo.

---

## 1. Qué creo que es este sitio [SUPUESTO salvo donde se indica]

- **Negocio:** Hermes Wraps — instalación de vinilo para vehículos (wraps parciales, cambio de color completo, capós/techos/chrome delete, gráficos comerciales/flotas, retirada de wraps) + rótulos y vinilos (ventanas, paredes, calcomanías). [VERIFICADO, del copy]
- **Modelo:** "owner-operated", una sola persona que cotiza, instala y revisa. [VERIFICADO, del copy] El copy usa "his" y "Tell Hermes…" → [PREGUNTA] ¿"Hermes" es el nombre del dueño o solo la marca?
- **Zona:** Tampa Bay, FL y "surrounding communities". El JSON-LD además menciona "Brandon, FL" (no aparece en el texto visible). [VERIFICADO]
- **Audiencias candidatas** [SUPUESTO]:
  1. Dueños de negocios pequeños con 1 vehículo de trabajo (rotulación comercial).
  2. Gestores de flotas (el sitio insiste mucho: "fleet" aparece 17 veces).
  3. Particulares que quieren personalizar su coche (techo negro, capó, cambio de color).
  4. Hispanohablantes de Tampa Bay (hay una franja "¿Prefieres hablar en español?").
- **Conversión principal** [PROBABLE]: solicitud de presupuesto vía el formulario que abre email/WhatsApp del usuario. Secundarias: llamada (`tel:`), redes sociales.
- **Estado del proyecto** [PROBABLE]: el sitio está en un subdominio temporal de Cloudflare Workers, todas las URL canónicas apuntan a `hermeswraps.com`, que **no resuelve** (DNS falla). Parece una versión de preproducción/staging a punto de lanzarse… o un lanzamiento con el dominio aún sin conectar. → [PREGUNTA] ¿Este workers.dev es el sitio "oficial" que se comparte hoy con clientes?
- **Preguntas abiertas para el dueño:**
  - ¿Cuál es el objetivo nº1: flotas/comerciales o particulares? El copy habla de flotas, pero la galería es casi toda de particulares.
  - ¿Hay rangos de precios que se puedan publicar?
  - ¿Hay reseñas en Google/Facebook que se puedan mostrar?
  - ¿Es instalador certificado por 3M o solo usa material 3M?
  - ¿Trabajo en taller (dirección) o servicio móvil?

---

## 2. Escaneo rápido — impresiones crudas (sin filtrar)

- Primera impresión en escritorio: estética "premium oscuro" (vino/dorado/negro), tipografía condensada en mayúsculas grande, se ve profesional y cuidado. Bien.
- El vídeo de fondo del hero, en el fotograma capturado, es un **primer plano borroso de un brazo/mano** sobre un coche; no se entiende qué es. En móvil el fotograma capturado sí muestra coches. [VERIFICADO para esos fotogramas]
- El H1 "ONE STANDARD. ACROSS EVERY VEHICLE." es bonito pero abstracto. No dice "vehicle wraps" ni "Tampa". El párrafo debajo sí lo explica.
- El botón dorado (primario) dice **"Watch the process"**, el de pedir presupuesto es el secundario con borde. Raro para un negocio que vive de presupuestos.
- Logo aparece **5 veces** en la página (cabecera, hero, tarjeta de rótulos, bloque "Personal attention", footer). El logo es detallado y a 44–60 px no se lee.
- No hay **ni una reseña**, ni estrellas, ni testimonios, ni nombre/cara del dueño, ni dirección, ni horario, ni precios.
- Hay un bloque entero de **"Terms of service"** (8 términos) en la página principal, en la navegación principal y antes de las FAQ y del formulario. Transparente, sí, pero pesa.
- El formulario es ingenioso (abre email o WhatsApp con el texto ya escrito; "Nothing is stored on this website") pero **no permite adjuntar fotos**, y las FAQ dicen que hay que mandar fotos.
- En móvil la página mide ~13 500 px (≈ 20 pantallas). El formulario está al final. **No hay botón fijo** de llamar/WhatsApp/presupuesto.
- La galería se mueve sola cada 4,5 s. Intentando leer un pie de foto, cambia.
- En las fotos de trabajos comerciales se ve el **teléfono de otra empresa** ("(813) 756-4171" de Tampa PC Consultants) en grande. Es el trabajo hecho, pero en móvil compite con el teléfono propio.
- Las etiquetas doradas pequeñas ("SERVICES", "WHY HERMES WRAPS"…) sobre fondo claro tienen poco contraste.
- El 404 es una página en blanco.
- Positivo: HTML semántico, textos alternativos descriptivos, soporte de `prefers-reduced-motion`, enlace de teléfono clicable, labels en el formulario, sin frameworks pesados, sin trackers.

---

## 3. Resumen de severidad

| Severidad | Nº | IDs |
|---|---|---|
| Crítica | 2 | F-001, F-002 |
| Alta | 11 | F-005, F-012, F-014, F-015, F-018, F-024, F-054, F-057, F-033, F-028, F-068 |
| Media | 33 | F-003, F-004, F-008, F-009, F-011, F-013, F-016, F-019, F-022, F-025, F-026, F-029, F-038, F-039, F-041, F-043, F-045, F-048, F-050, F-055, F-056, F-058, F-060, F-061, F-062, F-063, F-069, F-074, F-079, F-006, F-035, F-032, F-027 |
| Baja | 29 | F-007, F-017, F-020, F-021, F-023, F-030, F-031, F-034, F-037, F-040, F-042, F-044, F-046, F-047, F-049, F-051, F-052, F-059, F-064, F-065, F-066, F-067, F-070, F-072, F-073, F-075, F-076, F-077, F-078 |
| Nota | 4 | F-010, F-036, F-053, F-071 |

(Los recuentos son aproximados; algunas severidades son discutibles y están marcadas así en cada hallazgo. La severidad de "Media" incluye cosas que podrían ser "Alta" según el objetivo de negocio.)

**Top problemas (orden provisional, no final):**
1. **F-001** — Canonical, og:url, og:image y JSON-LD apuntan a `hermeswraps.com`, que no existe (DNS). SEO y previsualizaciones sociales rotas.
2. **F-012 / F-013** — En móvil no hay forma persistente de llamar/escribir/pedir presupuesto; el formulario está a ~20 pantallas.
3. **F-024** — Cero prueba social (reseñas, valoraciones, testimonios).
4. **F-015 / F-018** — El formulario no permite fotos y el envío por email puede fallar en silencio (sin estado de error/éxito).
5. **F-014** — Ninguna orientación de precio.
6. **F-054 / F-057** — Fallos WCAG: contraste del dorado en fondos claros, carruseles y vídeo en movimiento sin botón de pausa.
7. **F-005** — Sitio de una sola página: casi imposible posicionar por servicio + ciudad.

---

## 4. Inventarios

### 4.1 Inventario de páginas / rutas

| URL | Estado | Título | H1 | Meta desc | Canonical | Indexable | Notas |
|---|---|---|---|---|---|---|---|
| `/` | 200 [VERIFICADO] | "Hermes Wraps — Fleet Graphics & Vehicle Wraps \| Tampa Bay, FL" (61 car.) | "One standard. Across every vehicle." | Sí, 194 car. | `https://hermeswraps.com/` (**no resuelve**) | Sin `meta robots` → sí por defecto | Landing única con anclas `#process #work #services #why #terms #faq #contact` |
| `/robots.txt` | 200 [VERIFICADO] | — | — | — | — | — | Solo comentarios de "content signals" de Cloudflare; sin líneas `User-agent`, `Disallow` ni `Sitemap` en la respuesta obtenida |
| `/sitemap.xml` | **404** [VERIFICADO] | — | — | — | — | — | No existe |
| `/this-page-does-not-exist-404-test` | **404** [VERIFICADO] | — | — | — | — | — | Cuerpo vacío (sin marca, sin navegación) |
| `https://hermeswraps.com/` | **DNS no resuelve** [VERIFICADO vía Firecrawl] | — | — | — | — | — | Dominio usado en canonical/OG/JSON-LD/footer |
| `/favicon.ico`, `/site.webmanifest`, `/.well-known/security.txt` | [NO VERIFICADO] | | | | | | No probados (límite de herramientas). El HTML enlaza `favicon-32.png` y `apple-touch-icon.png`; no enlaza manifest |

### 4.2 Árbol del sitio (navegado) vs sitemap vs código

```
/ (única página)
├── header: logo → #top · PROCESS · WORK · SERVICES · WHY HERMES · TERMS · [Request a quote]
├── #top  (hero, main)
├── #process  "See how the work is done."   (3 vídeos verticales en carrusel)
├── #work     "Projects by type."           (13 fotos en carrusel 3D, 4 categorías)
├── #services "What Hermes Wraps installs." (6 tarjetas)
├── #why      "Quality with a name behind it." (5 razones + bloque CTA)
├── #terms    "Clear terms before work begins." (8 términos)
├── #faq      "Common questions." (6 preguntas, acordeón)  ← NO está en la nav principal, sí en el footer
├── aside     "¿Prefieres hablar en español?"
├── #contact  "Tell us what you want to wrap." (datos + formulario)
└── footer: Explore (Process, Work, Services, Terms, FAQ) · Contact
```
- sitemap.xml: no existe.
- Código fuente: no disponible en el repo. [PREGUNTA] ¿Dónde vive el código del Worker?
- "WHY HERMES" está en la nav principal pero **no** en el footer; "FAQ" está en el footer pero **no** en la nav principal. Inconsistencia menor.

### 4.3 Inventario de navegación

| Ubicación | Etiqueta | Destino | ¿Funciona? | Notas |
|---|---|---|---|---|
| Header | Logo + "Hermes Wraps" | `#top` | Sí [PROBABLE] | `aria-label="Hermes Wraps — back to top"` |
| Header | PROCESS | `#process` | Sí [PROBABLE] | Texto en mayúsculas en el propio HTML (no con CSS) |
| Header | WORK | `#work` | Sí [PROBABLE] | |
| Header | SERVICES | `#services` | Sí [PROBABLE] | Orden: Work antes que Services |
| Header | WHY HERMES | `#why` | Sí [PROBABLE] | |
| Header | TERMS | `#terms` | Sí [PROBABLE] | ¿Merece estar en la nav principal? |
| Header | Request a quote (botón dorado) | `#contact` | Sí [PROBABLE] | En móvil queda escondido dentro del menú ☰ |
| Header móvil | ☰ / × | abre/cierra `.nav-links` | [PROBABLE] por código | `aria-expanded` se actualiza; `aria-label` no cambia |
| Footer | Process, Work, Services, Terms, FAQ | anclas | Sí [PROBABLE] | Falta "Why Hermes" y "Contact/Quote" |
| Footer | Teléfono, email, Instagram, Facebook, TikTok | externos | Enlaces presentes [VERIFICADO]; destinos no probados [NO VERIFICADO] | Abren en pestaña nueva con `rel="noopener"` |
| Contacto | YouTube | `#` con `target="_blank"` | En el HTML [VERIFICADO]; **no se ve** en las capturas [VERIFICADO] | Probablemente oculto con `hidden` por JS (youtube vacío). Ver F-076 |

### 4.4 Inventario de CTAs

| Sección | Etiqueta CTA | Estilo | Posición | Destino | Notas |
|---|---|---|---|---|---|
| Header | Request a quote | Primario (dorado) | Arriba derecha | `#contact` | Oculto en móvil tras ☰ |
| Hero | Watch the process | **Primario (dorado)** | Bajo el párrafo | `#process` | CTA más visible = ver vídeos, no pedir presupuesto |
| Hero | Request a quote | Secundario (borde blanco) | Al lado | `#contact` | |
| Hero meta | (813) 475-1311 | Enlace texto | Debajo de los botones | `tel:8134751311` | Bien para móvil, poco visible |
| Process | ← → y puntos | Controles | Bajo el vídeo | Cambia vídeo | Puntos de 9×9 px |
| Process | Sound on | Botón pequeño | Sobre el vídeo | Activa sonido | |
| Work | Pestañas (Commercial, Partial & accents, Color change, Hoods & roofs) | Botones | Columna izq. | Salta a la primera foto de la categoría | |
| Work | ← → | Controles | | Cambia foto | |
| Work | Tocar foto | Implícito | | Abre lightbox | Solo la foto activa |
| Services | Ask about a sign | Primario (dorado) | Solo tarjeta de rótulos | `#contact` | Las otras 5 tarjetas no tienen CTA ni enlace |
| Why | Start the conversation | Primario (dorado) | Bloque vino | `#contact` | |
| Spanish | Escribir mensaje | Primario (dorado) | Franja vino | `#contact` | Lleva a un formulario solo en inglés |
| Contact | Send by email | Primario vino | Formulario | `mailto:` | |
| Contact | Send by WhatsApp | Verde WhatsApp | Formulario | `wa.me/18134751311` | |
| Contact | Copy details | Botón "quiet" | Formulario | Portapapeles | |
| Contact | Teléfono / email / redes | Enlaces | Columna izquierda | externos | |

→ 5 etiquetas distintas que llevan a `#contact`: "Request a quote", "Start the conversation", "Ask about a sign", "Escribir mensaje" (+ el enlace de nav). Ver F-023.

### 4.5 Inventario de formularios (NO enviado)

| Página | Propósito | Campos | Requeridos | ¿Labels bien? | Validación | Endpoint | Estados éxito/error | Notas |
|---|---|---|---|---|---|---|---|---|
| `/#contact` (`#quoteForm`) | Pedir presupuesto | Project type (select: Business / fleet, Personal vehicle) · Number of vehicles (input, `inputmode=numeric`, sin `type`) · Your name (`autocomplete=name`) · Company (optional, `autocomplete=organization`) · Year / make / model · Service needed (select, 7 opciones) · Project details (textarea) | name, vehicle | Sí, `<label for>` en todos [VERIFICADO] | `novalidate` + `form.reportValidity()` en JS → burbujas nativas del navegador | Ninguno: construye texto y abre `mailto:hermeswraps@gmail.com`, `https://wa.me/18134751311?text=…` o copia al portapapeles | Texto en `#formStatus` (`role=status`, `aria-live=polite`): "Opening your email app…", "Opening WhatsApp…", "Details copied…", "Copy was blocked…", "Copy is not available…" | Sin adjuntar fotos; sin campo de teléfono/email del cliente; selects con valor preseleccionado |

### 4.6 Inventario de componentes / bloques repetidos

| Componente / bloque | Dónde se usa | Variantes | Divergencias | ¿Compartir? | Notas |
|---|---|---|---|---|---|
| Eyebrow (línea dorada + texto mayúsculas) | Hero, Process, Work, Services, Why, Terms, FAQ, Contact | 1 | Contraste insuficiente en fondos claros | Ya es una clase (`.eyebrow`) | F-054 |
| H2 de sección (Barlow Condensed, mayúsculas, gigante) | 7 secciones | 3 definiciones (`.section h2`, `.vids h2`, `.process-feature h2` sin uso) | Tamaños `clamp(2.6rem,6vw,5.4rem)` vs `clamp(2.8rem,6vw,5.4rem)` vs `clamp(2.8rem,6vw,5.6rem)` | Unificar | F-075 |
| Botón `.btn` | 10 instancias | gold, outline, wine, quiet, whatsapp | WhatsApp verde fuera de la paleta | OK | F-051 |
| Carrusel 3D | Process (vídeos) y Work (fotos) | 2 implementaciones distintas (`.vid-*` y `.showroom-*`) | Distinto comportamiento: vídeos avanzan al terminar; fotos cada 4,5 s; flechas reutilizan `.showroom-arrow` | Podría ser un solo componente | F-043, F-050, F-073 |
| Tarjeta con imagen + gradiente + pie | Showroom card, service card, (project, process-project sin uso) | 2 vivas + 2 muertas | | | F-072 |
| Lista numerada 01–05 | Why | 1 | Números dorados con contraste bajo | | F-054 |
| Bloque CTA vino con logo | Signs card, Why-sign | 2 | Mismo patrón, CSS duplicado (`.service-text`, `.why-sign`) | Unificar | |
| Logo circular | Header, hero, signs card, why-sign, footer | 5 | 5 tamaños: 44/50/54/60, 84/112, 96, 78, 70 px | Demasiadas repeticiones | F-046 |
| Línea de contacto | Contacto, footer, hero meta | 3 | Teléfono en 3 sitios + config JS | | F-077 |
| Acordeón FAQ | FAQ | 1 | | | F-067 |

### 4.7 Tokens de diseño realmente usados

| Tipo | Valores distintos | Valores | Casi duplicados | ¿Fuente única? |
|---|---|---|---|---|
| Colores (literales en CSS) | **82** | Tokens `:root`: `--bg #f4f1ed`, `--surface #fff`, `--surface-2 #ebe6e0`, `--text #191315`, `--muted #665b5e`, `--wine #691c2a`, `--wine-deep #3a0d16`, `--gold #bb8b38`, `--gold-soft #d8b875`, `--line`. Más ~60 `rgb()/rgba()` sueltos | Muchísimos "casi blancos rosados": `rgb(234,217,208)`, `rgb(234,222,222)`, `rgb(234,223,225)`, `rgb(233,220,223)`, `rgb(238,223,225)`, `rgb(228,217,220)`, `rgb(226,212,215)`, `rgb(217,201,204)`, `rgb(218,204,205)`, `rgb(215,198,198)`, `rgb(215,199,202)`, `rgb(212,196,199)`, `rgb(203,191,194)`… y casi negros: `rgb(13,9,10)`, `rgb(20,8,11)`, `rgb(22,11,14)`, `rgb(23,16,18)`, `rgb(27,18,21)`, `rgb(33,20,23)`, `rgb(36,25,28)`, `rgb(39,28,31)` | Parcial: hay tokens pero se saltan mucho |
| Familias tipográficas | 2 | Barlow Condensed (títulos), Manrope (texto) | — | Google Fonts |
| Tamaños de fuente | **46** | de 0.66rem a `clamp(4.2rem,9vw,7.8rem)` | 0.68/0.69/0.70/0.72/0.73/0.74/0.76/0.78rem; 0.82/0.84/0.85/0.86rem; 0.9/0.92/0.93rem; 1.4/1.45/1.5/1.55rem; 1.6/1.65/1.7rem; 1.8/1.9/2/2.05/2.1rem | No hay escala |
| Pesos | 500, 700, 800 (CSS) | Manrope se carga solo 400–700 | 800 de Manrope no cargado → negrita sintética | F-070 |
| Letter-spacing | 9 | 0.03–0.16em, -0.025em | 0.08/0.09/0.1/0.11/0.12em | No |
| Espaciado (gap) | 20 | 1px…70px | 7/8/9/10px; 14/15/16px; 24/26px; 50/54px | No |
| Padding | 30 valores distintos | | | No |
| Radios | 2 | `0` (todo cuadrado) y `50%` (logos/puntos) | — | Consistente ✔ |
| Sombras | 5 | | | Parcial (`--shadow` existe) |
| Breakpoints | 2 + 1 | `max-width:900px`, `max-width:620px`, `min-width:901px` | — | Consistente ✔ |
| z-index | 0,1,2,3,4,20,100 | | | OK |

### 4.8 Stack técnico y terceros

| Cosa | Evidencia | Notas |
|---|---|---|
| Hosting: Cloudflare Workers | Subdominio `*.workers.dev` [VERIFICADO]; robots.txt con texto de "content signals" típico de Cloudflare [VERIFICADO] | Edge/CDN [SUPUESTO] |
| HTML/CSS/JS a mano, sin framework | Un solo `<script>` inline de ~9,6 KB, vanilla JS (IIFE) [VERIFICADO] | Ligero ✔ |
| Google Fonts | `fonts.googleapis.com/css2?family=Barlow+Condensed:…&family=Manrope:…&display=swap` + preconnect [VERIFICADO] | Transferencia de IP a Google (nota de privacidad) |
| Analítica / píxeles / GTM | **Ninguno** [VERIFICADO en el HTML] | Sin medición de leads. F-009 |
| Formulario | Sin backend; `mailto:`, `wa.me`, Clipboard API [VERIFICADO] | |
| Datos estructurados | JSON-LD `AutomotiveBusiness` [VERIFICADO] | F-008 |
| Vídeo | 4 `<video>` mp4 propios (hero + 3 de proceso), sin `<track>` [VERIFICADO] | F-062, F-068 |

### 4.9 Comprobaciones técnicas

| Check | Resultado | Evidencia | Etiqueta |
|---|---|---|---|
| HTTPS | La URL https responde 200 | Firecrawl `statusCode: 200` | [VERIFICADO] |
| Redirección http→https | No probado | curl bloqueado | [NO VERIFICADO] |
| Dominio propio `hermeswraps.com` | **No resuelve DNS** | Error de Firecrawl "DNS resolution failed" | [VERIFICADO] (en el momento de la auditoría) |
| robots.txt | Existe; solo comentarios (sin directivas) en la respuesta | rawHtml de `/robots.txt` | [VERIFICADO] |
| sitemap.xml | 404 | Firecrawl | [VERIFICADO] |
| Página 404 | Cuerpo vacío | Firecrawl markdown vacío | [VERIFICADO] |
| Cabeceras de seguridad (HSTS, CSP, X-Frame-Options, Referrer-Policy, Permissions-Policy) | Desconocido | — | [NO VERIFICADO] |
| Caché / compresión | Desconocido | — | [NO VERIFICADO] |
| Errores de consola | Desconocido | — | [NO VERIFICADO] |
| Peticiones fallidas (4xx/5xx de assets) | Desconocido; las imágenes se ven en las capturas | Capturas | [PROBABLE] sin roturas visibles |
| Lighthouse / PSI / CWV | No ejecutado | — | [NO VERIFICADO] |
| `lang` | `<html lang="en">`; franja española con `lang="es"` | HTML | [VERIFICADO] |
| Viewport meta | `width=device-width,initial-scale=1,viewport-fit=cover` | HTML | [VERIFICADO] ✔ |

---

## 5. Hallazgos por área

> Cada hallazgo tiene un ID único. Muchos aparecen en varias áreas; se cruzan con "Relacionado".

### 5.1 Primera impresión / test de 5 segundos

#### F-033 · El H1 es un eslogan abstracto: no dice qué, ni dónde `[VERIFICADO]`
- **Área(s):** Mensajes, SEO, Primera impresión, Jerarquía visual
- **Qué noté:** El H1 es "One standard. Across every vehicle." Lo más grande de la pantalla no dice "vehicle wraps", ni "Tampa", ni a quién va dirigido. Lo concreto está en el eyebrow pequeño ("Owner-operated · Tampa Bay area, Florida") y en el párrafo.
- **Dónde:** Hero, `<h1>`; escritorio y móvil.
- **Evidencia:** `<h1>One standard.<br>Across every vehicle.</h1>`; captura escritorio franja 1.
- **Por qué puede ser un problema:** En 5 s un visitante nuevo lee el H1 y como mucho el primer botón. "One standard" no comunica el servicio. Además el H1 es la señal on-page más fuerte para SEO.
- **Impacto en el usuario:** Tiene que leer el párrafo para entender qué ofrece el negocio. Más carga cognitiva y más riesgo de rebote [SUPUESTO].
- **Impacto en el negocio:** Peor relevancia para búsquedas tipo "vehicle wraps Tampa" [PROBABLE]. Menos claridad = menos presupuestos [SUPUESTO].
- **Severidad:** Alta — es la pieza de mensaje más visible del sitio (discutible: Media si el tráfico llega casi todo de Instagram, donde ya saben qué hacen).
- **Esfuerzo:** S [SUPUESTO]
- **Posibles soluciones:** (A) H1 descriptivo + eslogan como subtítulo: "Vehicle Wraps & Fleet Graphics in Tampa Bay" / "One standard across every vehicle". (B) Mantener eslogan pero en el eyebrow poner "Vehicle wraps · Tampa Bay, FL" con más tamaño.
- **Notas de implementación:** Cambiar solo el texto del `<h1>`/eyebrow; el estilo `.hero h1` ya soporta textos largos con `clamp()`; revisar el corte de línea en 360 px.
- **Relacionado:** F-006, F-045, F-011
- **Investigar / preguntas:** [PREGUNTA] ¿El eslogan es parte de la marca registrada/branding en otros canales?

#### F-045 · El vídeo de fondo del hero no enseña claramente un coche envuelto `[VERIFICADO para el fotograma capturado]`
- **Área(s):** UI, Primera impresión, Rendimiento
- **Qué noté:** En la captura de escritorio, el fotograma del vídeo es un primer plano borroso de un antebrazo/mano sobre la carrocería; con el overlay oscuro no se reconoce el producto. En móvil, el fotograma capturado muestra un aparcamiento con coches (más legible).
- **Dónde:** `.hero-video` (`assets/hero-loop.mp4`, póster `hero-loop-poster.jpg`).
- **Evidencia:** Capturas escritorio y móvil, primera franja.
- **Por qué puede ser un problema:** El primer visual tendría que vender el resultado (coche acabado, brillo, antes/después). Un brazo borroso puede parecer amateur o confuso.
- **Impacto en el usuario:** No ve el producto final arriba del todo.
- **Impacto en el negocio:** Primera impresión menos "premium" de lo que el resto del diseño promete [SUPUESTO].
- **Severidad:** Media — depende del fotograma; no vi el vídeo completo.
- **Esfuerzo:** S–M
- **Posibles soluciones:** Póster = foto del mejor trabajo terminado (por ejemplo el Corvette o el Tucson rosa); vídeo con planos del resultado; o hero estático con foto + vídeo solo en la sección de proceso.
- **Notas de implementación:** Cambiar `poster` y/o el mp4; considerar `preload="metadata"` (ver F-068).
- **Relacionado:** F-068, F-057
- **Investigar / preguntas:** Ver el vídeo entero en un navegador real; cuánto dura y qué enseña.

#### F-011 · El CTA primario del hero es "Watch the process", no pedir presupuesto `[VERIFICADO]`
- **Área(s):** CTAs, Conversión, Jerarquía visual
- **Qué noté:** Botón dorado sólido = "Watch the process" (ancla a vídeos). "Request a quote" = botón con borde (secundario). En móvil ambos a ancho completo, el dorado primero.
- **Dónde:** `.hero-actions`.
- **Evidencia:** `<a class="btn btn-gold" href="#process">Watch the process</a><a class="btn btn-outline" href="#contact">Request a quote</a>`
- **Por qué puede ser un problema:** La acción más visual empuja a un contenido intermedio (vídeos) en lugar de a la conversión. Es una decisión intencional (el sitio apuesta por "mira cómo trabajo"), pero cuesta clics.
- **Impacto en el usuario:** Quien ya viene decidido (por ejemplo, desde Instagram) tiene que elegir el botón menos visible.
- **Impacto en el negocio:** Posible pérdida de presupuestos [SUPUESTO; no hay analítica para comprobarlo — F-009].
- **Severidad:** Media
- **Esfuerzo:** S
- **Posibles soluciones:** Invertir estilos (quote dorado, process con borde). O probar ambos como experimento si se instala analítica.
- **Notas de implementación:** Intercambiar `btn-gold`/`btn-outline`.
- **Relacionado:** F-012, F-023, F-009
- **Investigar / preguntas:** [PREGUNTA] ¿Fue intencional priorizar los vídeos?

### 5.2 UX (general)

#### F-053 · Página única muy larga: ~13 500 px en móvil, ~8 400 px en escritorio `[VERIFICADO]`
- **Área(s):** UX, Móvil, Arquitectura de información
- **Qué noté:** La captura móvil (360 px) mide 13 484 px ≈ 20 pantallas; escritorio 8 441 px. Contacto está al ~85 % del recorrido.
- **Dónde:** Toda la página.
- **Evidencia:** Dimensiones de las capturas.
- **Por qué puede ser un problema:** Mucho scroll antes de convertir, sin atajos persistentes (F-012).
- **Impacto en el usuario:** Fatiga; puede perderse.
- **Impacto en el negocio:** [SUPUESTO] abandono antes de llegar al formulario.
- **Severidad:** Nota (la longitud en sí no es mala; lo malo es no tener atajo → F-012)
- **Esfuerzo:** —
- **Posibles soluciones:** CTA fijo; mover Terms a página propia o acordeón; acortar secciones.
- **Notas de implementación:** —
- **Relacionado:** F-012, F-035, F-005
- **Investigar / preguntas:** Con analítica, medir profundidad de scroll.

#### F-043 · La galería avanza sola cada 4,5 s y no tiene botón de pausa `[VERIFICADO por código]`
- **Área(s):** UX, Interacciones, Accesibilidad
- **Qué noté:** `setInterval(render(active+1), 4500)`. Se pausa con hover/focus del escenario y durante el toque, pero se reanuda al soltar (`touchend` → `start()`). No hay botón de pausa visible. El copy lo avisa: "The showcase moves on its own".
- **Dónde:** `#work`, `#showroomStage`.
- **Evidencia:** JS `function start(){stop();if(!reduced)timer=setInterval(…,4500);}`; en las capturas el contador aparece en "02 / 13" (ya había avanzado).
- **Por qué puede ser un problema:** Los pies de foto tienen 3 líneas (categoría, vehículo, descripción); 4,5 s es poco para leer y mirar la foto. En móvil, tras deslizar, vuelve a moverse.
- **Impacto en el usuario:** Pierde la foto que miraba; frustración.
- **Impacto en el negocio:** El portfolio es la prueba principal; si molesta, se mira menos [SUPUESTO].
- **Severidad:** Media (en accesibilidad es más grave → F-057)
- **Esfuerzo:** S
- **Posibles soluciones:** Sin autoplay; o autoplay solo hasta la primera interacción; o botón pausa/play visible; o cuadrícula filtrable en lugar de carrusel.
- **Notas de implementación:** Hay CSS sin usar de una cuadrícula filtrable (`.gallery`, `.project`, `.filters`) → parece que existió esa versión antes (F-072).
- **Relacionado:** F-057, F-058, F-044, F-072
- **Investigar / preguntas:** ¿Por qué se cambió de cuadrícula a carrusel?

#### F-044 · El contador global "02 / 13" no encaja con las pestañas por categoría `[VERIFICADO]`
- **Área(s):** UX, Interacciones
- **Qué noté:** Las pestañas muestran "(2)", "(5)"… pero el contador cuenta las 13. Al pulsar "Color change (2)" el contador salta a "08 / 13". Al avanzar, el carrusel sale de la categoría sin avisar (la pestaña activa cambia sola).
- **Dónde:** `.showroom-tabs`, `#showroomCount`.
- **Evidencia:** JS `render()` usa índice global; las pestañas solo saltan a la primera foto de la categoría.
- **Por qué puede ser un problema:** Las pestañas parecen filtros pero no filtran. Modelo mental confuso.
- **Impacto en el usuario:** Cree que filtra "Color change" y aparecen otros trabajos.
- **Impacto en el negocio:** Bajo.
- **Severidad:** Baja
- **Esfuerzo:** S–M
- **Posibles soluciones:** Filtrar de verdad (contador "1 / 2" dentro de la categoría) o quitar los números de las pestañas y llamarlas "Jump to…".
- **Notas de implementación:** `cards.filter(c=>c.dataset.cat===cat)`.
- **Relacionado:** F-043, F-059
- **Investigar / preguntas:** —

### 5.3 Diseño UI

#### F-046 · El logo se repite 5 veces y su detalle no se lee en tamaños pequeños `[VERIFICADO]`
- **Área(s):** UI, Marca, Componentes repetidos
- **Qué noté:** `assets/logo.jpg` aparece en cabecera (44–60 px), hero (84–112 px), tarjeta de rótulos (96 px), bloque "Personal attention" (78 px) y footer (70 px). El logo es un emblema detallado con texto pequeño ("HERMES WRAPS · VINYL SPECIALISTS") que a 44–60 px es ilegible. En la tarjeta "Signs & Vinyl Graphics" se usa el logo en lugar de una foto de un rótulo.
- **Dónde:** ver arriba.
- **Evidencia:** 5 ocurrencias de `assets/logo.jpg` en el HTML; capturas.
- **Por qué puede ser un problema:** Repetición = ruido; además el logo en JPG (no SVG) puede verse borroso en pantallas retina [PROBABLE].
- **Impacto en el usuario:** Poco; sensación de "relleno".
- **Impacto en el negocio:** Marca menos nítida.
- **Severidad:** Baja
- **Esfuerzo:** S–M
- **Posibles soluciones:** Versión simplificada (monograma/wordmark) para tamaños pequeños; logo en SVG; quitar el logo del hero (ya está en la cabecera); foto real de un rótulo en la tarjeta de signs (F-041).
- **Notas de implementación:** `.hero-logo`, `.service-logo`, `.why-sign img`.
- **Relacionado:** F-041, F-073
- **Investigar / preguntas:** ¿Existe el logo en vectorial?

#### F-047 · Pies de foto sobre imágenes claras pierden legibilidad `[VERIFICADO en captura móvil]`
- **Área(s):** UI, Accesibilidad
- **Qué noté:** En la galería móvil, el pie "COMMERCIAL GRAPHICS / BUSINESS SUV · HOOD" se superpone a un capó blanco con logo verde; el degradado (`.showroom-card::after` desde el 55 %) no basta y el texto dorado/blanco compite con el logo verde de la foto.
- **Dónde:** `.showroom-caption` sobre fotos claras (capós blancos, Corolla blanco, Corvette blanco).
- **Evidencia:** Captura móvil, hoja 1, columna 2 abajo.
- **Por qué puede ser un problema:** Contraste variable sobre fotos.
- **Impacto en el usuario:** Cuesta leer.
- **Impacto en el negocio:** Bajo.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Degradado más alto/opaco, o pie debajo de la foto (no encima).
- **Notas de implementación:** `inset: 55% 0 0` → `35%` y opacidad mayor; o mover la figcaption fuera.
- **Relacionado:** F-054
- **Investigar / preguntas:** —

#### F-051 · Botón de WhatsApp verde fuera de la paleta; 3 botones de envío con peso parecido `[VERIFICADO]`
- **Área(s):** UI, Formularios, Sistema de diseño
- **Qué noté:** "Send by email" (vino), "Send by WhatsApp" (verde `rgb(31,122,77)`), "Copy details" (gris). El verde es el único color fuera de la paleta vino/dorado.
- **Dónde:** `.form-actions`.
- **Evidencia:** CSS `.btn-whatsapp`.
- **Por qué puede ser un problema:** El verde tiene sentido (reconocimiento de WhatsApp), pero tres opciones de envío = decisión extra en el momento de convertir.
- **Impacto en el usuario:** Duda "¿cuál uso?".
- **Impacto en el negocio:** Bajo.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Un botón principal (el canal preferido por el negocio) + uno secundario; "Copy details" como enlace pequeño.
- **Notas de implementación:** —
- **Relacionado:** F-018, F-019, F-022
- **Investigar / preguntas:** [PREGUNTA] ¿Por qué canal prefiere el dueño recibir los leads?

#### F-052 · Los selects usan el estilo nativo del navegador `[VERIFICADO]`
- **Área(s):** UI, Formularios
- **Qué noté:** Los `<select>` muestran la flecha nativa (diferente en Safari/Chrome/Android) mientras el resto es cuadrado y personalizado.
- **Dónde:** `#clientType`, `#service`.
- **Evidencia:** Capturas escritorio/móvil.
- **Por qué puede ser un problema:** Pequeña inconsistencia visual.
- **Impacto en el usuario:** Mínimo.
- **Impacto en el negocio:** Mínimo.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** `appearance:none` + flecha propia; o radios/botones segmentados para "Project type" (solo 2 opciones).
- **Notas de implementación:** —
- **Relacionado:** F-016
- **Investigar / preguntas:** —

### 5.4 Layout

- Ancho máximo `min(1180px, 100% - 40px)`; en móvil margen de 13 px por lado (`100% - 26px`) → **más estrecho que los 16 px habituales**; el texto queda pegado al borde en 360 px. [VERIFICADO por CSS + captura] → Baja, ver F-075.
- Escritorio: rejillas asimétricas (0.8fr/1.2fr, 0.75fr/1.25fr…) bien resueltas. ✔
- Servicios: el CSS original tenía 2 tarjetas grandes (span 6) + 4 pequeñas (span 4), pero una regla posterior `@media (min-width:901px){.service-card:nth-child(n){grid-column:span 4}}` lo anula → todas iguales (3×2). Visualmente funciona; es deuda de código (F-073).
- Gran hueco en blanco entre Services y Why en escritorio (~130 px extra) por padding de sección de 94 px arriba y abajo. Menor.
- Header en `position:absolute` (no fijo) → al bajar desaparece (F-012).
- No observé scroll horizontal en las capturas [VERIFICADO para 360 y 1440 px]; `body{overflow-x:hidden}` podría estar tapando algún desbordamiento (el carrusel 3D usa `translateX(118%)`) [PROBABLE]; no es un problema visible.

### 5.5 Jerarquía visual

- Los H2 son enormes (hasta 5.4rem) y todos iguales → cada sección "grita" igual; nada destaca como la sección clave (contacto). [VERIFICADO] Nota.
- Ver F-033 (H1), F-011 (CTA primario), F-054 (eyebrows con bajo contraste = la capa de "wayfinding" es la más débil).
- Las tarjetas de servicio tienen buena jerarquía (título grande, una línea).
- En "Why", el bloque vino con CTA destaca bien. ✔

### 5.6 Navegación

#### F-012 · No hay CTA persistente: el header no es fijo y la página es muy larga `[VERIFICADO]`
- **Área(s):** Navegación, Conversión, Móvil
- **Qué noté:** `.nav{position:absolute}` → la cabecera (con "Request a quote") se va al hacer scroll. No hay barra inferior fija con Llamar / WhatsApp / Presupuesto. En móvil son ~20 pantallas hasta el formulario.
- **Dónde:** Toda la página, sobre todo móvil.
- **Evidencia:** CSS `.nav { position: absolute; … }`; captura móvil 13 484 px.
- **Por qué puede ser un problema:** En un negocio local de servicios en móvil, la acción "llamar/escribir ahora" debe estar siempre a mano. El usuario que se convence en la galería tiene que buscar cómo contactar.
- **Impacto en el usuario:** Scroll largo o volver arriba; puede abandonar.
- **Impacto en el negocio:** Probablemente es el mayor freno de conversión en móvil [SUPUESTO; sin datos].
- **Severidad:** Alta
- **Esfuerzo:** S–M
- **Posibles soluciones:** (A) Barra fija inferior en móvil: "Call" · "WhatsApp" · "Quote". (B) Header fijo compacto que aparece al subir. (C) Botón flotante de WhatsApp.
- **Notas de implementación:** `position:sticky/fixed`, respetar `env(safe-area-inset-bottom)` (ya usan `viewport-fit=cover`); que no tape el lightbox ni el `Sound on`; ocultarla cuando `#contact` está visible (IntersectionObserver ya se usa en el código).
- **Relacionado:** F-013, F-022, F-053, F-011
- **Investigar / preguntas:** Medir clics en `tel:` y WhatsApp antes/después (F-009).

#### F-013 · En móvil, "Request a quote" está escondido dentro del menú ☰ `[VERIFICADO por CSS]`
- **Área(s):** Navegación, Móvil, CTAs
- **Qué noté:** Por debajo de 900 px `.nav-links` (que incluye el botón dorado) pasa a `display:none` y solo se ve el ☰.
- **Dónde:** Header móvil.
- **Evidencia:** CSS `@media (max-width:900px){ .nav-links{display:none…} }`; captura móvil.
- **Por qué puede ser un problema:** El CTA principal de la cabecera desaparece en el dispositivo donde más se usa [SUPUESTO sobre el tráfico].
- **Impacto en el usuario:** Un toque extra; menos descubrible.
- **Impacto en el negocio:** Menos clics al formulario [SUPUESTO].
- **Severidad:** Media
- **Esfuerzo:** S
- **Posibles soluciones:** Dejar un botón compacto "Quote" o un icono de teléfono visible junto al ☰.
- **Notas de implementación:** Sacar el `.btn` fuera del `<nav>` colapsable.
- **Relacionado:** F-012
- **Investigar / preguntas:** —

#### F-065 · Menú móvil: sin Escape, sin gestión del foco, `aria-label` fijo `[VERIFICADO por código]`
- **Área(s):** Navegación, Accesibilidad
- **Qué noté:** El botón ☰ cambia su texto a × y `aria-expanded`, pero el `aria-label` siempre dice "Open navigation". No se cierra con Escape. El foco no se mueve al menú. El menú se cierra al pulsar un enlace ✔.
- **Dónde:** `.menu-btn`, JS "mobile menu".
- **Evidencia:** JS: `menuBtn.textContent=open?'×':'☰'` (el `aria-label` tiene prioridad sobre el texto).
- **Por qué puede ser un problema:** El lector de pantalla anuncia "Open navigation, expanded" al estar abierto: contradictorio pero entendible.
- **Impacto en el usuario:** Menor.
- **Impacto en el negocio:** Mínimo.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** `aria-label="Menu"` fijo (el estado ya lo da `aria-expanded`); cerrar con Escape; `aria-controls`.
- **Notas de implementación:** —
- **Relacionado:** F-055
- **Investigar / preguntas:** —

#### F-066 · Etiquetas de navegación en MAYÚSCULAS dentro del HTML `[VERIFICADO]`
- **Área(s):** Accesibilidad, Navegación, Código
- **Qué noté:** El HTML dice literalmente "PROCESS", "WORK", "WHY HERMES" (en el resto del sitio se usa `text-transform:uppercase` con texto normal). El footer usa "Process", "Work"…
- **Dónde:** `.nav-links`.
- **Evidencia:** HTML.
- **Por qué puede ser un problema:** Algunos lectores de pantalla deletrean palabras en mayúsculas; inconsistente con el footer.
- **Impacto en el usuario:** Menor.
- **Impacto en el negocio:** Ninguno.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Texto normal + `text-transform` en CSS.
- **Notas de implementación:** —
- **Relacionado:** —
- **Investigar / preguntas:** —

- Nota extra de navegación: "FAQ" falta en la nav principal (está en el footer) y "Why Hermes" falta en el footer. "TERMS" sí está en la nav principal. Orden "Process → Work → Services": el usuario ve vídeos y fotos antes de saber qué servicios hay. [VERIFICADO] → ver F-035.
- Sin "skip link" → F-056.

### 5.7 Arquitectura de información

#### F-005 · Sitio de una sola página: sin páginas por servicio ni por zona `[VERIFICADO]`
- **Área(s):** AI, SEO, Contenido, Oportunidades
- **Qué noté:** Todo está en `/`. Cada servicio tiene 1 frase ("Roof, pillars, mirrors or selected panels."). No hay URL para "fleet graphics", "color change wrap", "chrome delete", "wrap removal", "signs", ni para ciudades (Tampa, Brandon, St. Petersburg, Clearwater… [SUPUESTO sobre las zonas]).
- **Dónde:** Arquitectura general.
- **Evidencia:** Enlaces: solo anclas + externos.
- **Por qué puede ser un problema:** Para SEO local, Google posiciona páginas, no secciones; una sola página compite por todas las búsquedas con muy poco texto por tema (~1 300 palabras visibles en total).
- **Impacto en el usuario:** Quien busca "chrome delete" no encuentra información específica (precio, tiempo, ejemplos).
- **Impacto en el negocio:** Menos tráfico orgánico [PROBABLE]; dependencia de redes sociales.
- **Severidad:** Alta (en negocio); Media si el canal es casi todo Instagram/Facebook.
- **Esfuerzo:** M–L
- **Posibles soluciones:** Páginas: `/fleet-graphics`, `/color-change-wraps`, `/partial-wraps` (techo, capó, chrome delete), `/wrap-removal`, `/signs`, `/es/` (español). Cada una con fotos propias, FAQ específica, CTA.
- **Notas de implementación:** Al ser Worker + HTML a mano, conviene una plantilla/SSG simple (Astro, Eleventy) para no duplicar cabecera/footer; añadir sitemap.xml.
- **Relacionado:** F-003, F-006, F-038, F-039
- **Investigar / preguntas:** [PREGUNTA] ¿Qué servicios dan más margen? Priorizar esas páginas.

#### F-035 · "Terms of service" está en la nav principal y ocupa una sección completa antes de FAQ y contacto `[VERIFICADO]`
- **Área(s):** AI, Contenido, Conversión, Mensajes
- **Qué noté:** 8 términos (presupuesto, depósito, estado del vehículo, garantía, cuidado, plazos, fotos, flotas) entre "Why" y "FAQ". El eyebrow dice "Terms of service" (suena legal). Es la 6ª sección de 8.
- **Dónde:** `#terms`.
- **Evidencia:** HTML + capturas.
- **Por qué puede ser un problema:** Positivo: transparencia, filtra clientes. Negativo: poner condiciones legales antes del contacto puede enfriar al visitante; parte del contenido (cuidado de la película, garantía) responde preguntas típicas y encaja mejor como FAQ.
- **Impacto en el usuario:** Más texto antes de actuar; tono de contrato.
- **Impacto en el negocio:** [SUPUESTO] posible fricción; también menos discusiones posteriores (positivo).
- **Severidad:** Media (discutible)
- **Esfuerzo:** S–M
- **Posibles soluciones:** Renombrar a "How it works" / "What to expect" con pasos (presupuesto → depósito → entrega → instalación → revisión → cuidados); mover los términos completos a `/terms` y enlazarlos desde el footer y el formulario.
- **Notas de implementación:** Hay CSS sin usar de una sección de pasos (`.steps`, `.step` con contador "01, 02…") → parece que existía y se quitó (F-072).
- **Relacionado:** F-053, F-039, F-078
- **Investigar / preguntas:** [PREGUNTA] ¿Los términos generaron problemas antes (clientes que se quejaban del depósito, etc.)?

- Más notas de AI:
  - "Hoods, Roofs & Chrome Delete" como servicio vs. "chrome delete… quoted separately" en los términos → F-037.
  - "Wrap Removal" es servicio y tiene vídeo, pero no es pestaña en la galería → F-042.
  - La sección Process (vídeos) va antes de Work (fotos): son dos portfolios seguidos; podrían unificarse o separarse más.

### 5.8 Recorridos de usuario

> Sin analítica ni research: todo lo de abandono es [SUPUESTO].

**Recorrido 1 — Particular, móvil, viene de Instagram, quiere saber cuánto cuesta un techo negro.**

| Paso | Qué hace | Fricción |
|---|---|---|
| 1 | Llega al hero | El H1 no dice "wraps" (F-033) pero ya sabe qué es por Instagram |
| 2 | Baja buscando precio | No hay precios en ninguna parte (F-014) |
| 3 | Ve vídeos (autoplay al entrar en pantalla) | Bien; consume datos (F-068) |
| 4 | Ve galería: Corolla, sedán, Corvette con techo negro | Buen ejemplo relevante ✔; se mueve sola (F-043) |
| 5 | Servicios: "Partial Wraps — Roof, pillars, mirrors…" | Sin precio ni tiempo; tarjeta no clicable (F-048) |
| 6 | Why / Terms / FAQ | Mucho texto; la FAQ no responde precio ni duración de la instalación (F-039) |
| 7 | Formulario: tipo preseleccionado "Business / fleet" | Tiene que cambiarlo (F-016) |
| 8 | Quiere mandar foto del coche | No hay forma en el formulario (F-015). Si pulsa WhatsApp puede adjuntarla después, pero nadie se lo dice |
| 9 | Pulsa "Send by WhatsApp" | Se abre WhatsApp con el texto ✔ |
- Pasos: ~9; pantallas de scroll: ~18–20; riesgo de abandono en pasos 2 y 6 [SUPUESTO].
- Atajo existente: el teléfono en el hero (pequeño).

**Recorrido 2 — Gestor de flota (10 furgonetas), escritorio, desde Google.**

| Paso | Qué hace | Fricción |
|---|---|---|
| 1 | Busca "fleet graphics Tampa" | Probablemente no encuentra el sitio: canonical a dominio inexistente (F-001), una sola página (F-005), sin sitemap (F-003) |
| 2 | Si llega: hero "from a single branded vehicle to an ongoing fleet program" ✔ | |
| 3 | Busca pruebas de flotas | La galería "Commercial (2)" son 2 fotos del **mismo** SUV; ninguna flota (F-028) |
| 4 | Busca referencias de empresas, seguro, facturación, plazos por vehículo | No hay (F-024, F-025, F-039) |
| 5 | Formulario: "Number of vehicles" ✔, Company ✔ | No hay campo para email/teléfono de empresa; depende del canal (F-019) |
| 6 | "Send by email" en un PC de oficina sin cliente de correo configurado | No pasa nada visible salvo "Opening your email app…" (F-018) |
- Riesgo alto de abandono en 3, 4 y 6 [SUPUESTO].

**Recorrido 3 — Hispanohablante, móvil.**
- El hero está solo en inglés. El eyebrow de Process tiene "Síguenos en el proceso" (sin `lang="es"`). La franja española aparece después de las FAQ (~75 % del scroll). "Escribir mensaje" lleva a un formulario con todas las etiquetas en inglés. Ver F-038.

**Recorrido 4 — Usuario de teclado/lector de pantalla quiere ver los trabajos y pedir presupuesto.**
- Sin skip link (F-056) → tabula por 7 enlaces de nav.
- Process: puede usar flechas/puntos; no puede pausar el vídeo con teclado (F-062).
- Work: pestañas con `role="tab"` sin el patrón de teclado completo (F-059); el escenario anuncia cambios cada 4,5 s (F-058).
- Lightbox: el foco puede escaparse detrás (F-060).
- Formulario: labels correctos ✔; campos obligatorios no marcados visualmente (F-021).
- Foco visible: depende del navegador (F-055).

**Recorrido 5 — Cliente que vuelve para pedir otro trabajo o reclamar garantía.**
- No hay información de contacto para garantías ni de cuál es el periodo ("within the period stated on the quote"). Contacto genérico. Bajo impacto. → F-029.

**Recorrido 6 — Alguien comparte el enlace por WhatsApp/Facebook.**
- La previsualización pide `og:image` en `https://hermeswraps.com/assets/...` → el dominio no resuelve → **sin imagen** [PROBABLE] y quizá con la URL canónica rota (F-001).

### 5.9 Contenido

#### F-039 · Las FAQ no responden las preguntas que más deciden: precio, tiempo de instalación, duración, garantía `[VERIFICADO]`
- **Área(s):** Contenido, Conversión, SEO
- **Qué noté:** 6 FAQ: duración del vinilo ("It depends…"), leasing, quitar vinilo, qué mandar, rótulos, flotas. Faltan: ¿cuánto cuesta (rango)?, ¿cuánto tarda la instalación (horas/días)?, ¿cuánto dura el vinilo (un rango típico según el material, con el dato que dé el fabricante/dueño — no lo invento aquí)?, ¿cuánto dura la garantía?, ¿es en taller o a domicilio?, ¿dañará la pintura?, ¿formas de pago?, ¿ceramic coating/PPF? (si no se ofrece, decirlo).
- **Dónde:** `#faq`.
- **Evidencia:** HTML.
- **Por qué puede ser un problema:** Las respuestas evasivas ("It depends… Your quote names…") son honestas pero no ayudan a decidir; generan un contacto con una pregunta básica o, peor, un abandono.
- **Impacto en el usuario:** No puede autocalificarse.
- **Impacto en el negocio:** Más consultas de baja calidad, o menos consultas [SUPUESTO].
- **Severidad:** Media
- **Esfuerzo:** S (solo copy, si el dueño da los datos)
- **Posibles soluciones:** Añadir 4–6 FAQ con rangos ("Most roof wraps take X hours"); FAQ por página de servicio (F-005).
- **Notas de implementación:** El acordeón actual lo soporta; considerar `<details>/<summary>` nativo (F-067).
- **Relacionado:** F-014, F-029, F-026
- **Investigar / preguntas:** [PREGUNTA] ¿Qué película usa normalmente (3M 2080?) y qué duración/garantía tiene? (no inventar).

#### F-041 · El servicio de rótulos no tiene ni una foto de un rótulo `[VERIFICADO]`
- **Área(s):** Contenido, Confianza, Servicios
- **Qué noté:** "Signs & Vinyl Graphics" usa el logo como imagen. La galería no tiene categoría de rótulos, ventanas ni paredes.
- **Dónde:** Última tarjeta de servicios; galería.
- **Evidencia:** `<img class="service-logo" src=".../logo.jpg" alt="">`.
- **Por qué puede ser un problema:** Se ofrece un servicio sin prueba visual; parece secundario o recién añadido.
- **Impacto en el usuario:** Duda de si realmente lo hacen bien.
- **Impacto en el negocio:** Menos leads de rótulos [SUPUESTO].
- **Severidad:** Media
- **Esfuerzo:** S (si hay fotos)
- **Posibles soluciones:** Foto real de un trabajo de rótulos/ventanas; categoría "Signs" en la galería; si aún no hay trabajos, decirlo con honestidad o quitar el énfasis.
- **Notas de implementación:** —
- **Relacionado:** F-046, F-042, F-028
- **Investigar / preguntas:** [PREGUNTA] ¿Hay trabajos de rótulos hechos?

#### F-042 · Wrap removal y chrome delete se ofrecen pero no aparecen en la galería `[VERIFICADO]`
- **Área(s):** Contenido, AI
- **Qué noté:** Pestañas: Commercial, Partial & accents, Color change, Hoods & roofs. "Wrap removal" solo está en un vídeo de proceso y en una tarjeta. "Chrome delete" no tiene ningún ejemplo visible.
- **Dónde:** `#work`.
- **Evidencia:** HTML.
- **Por qué puede ser un problema:** Incongruencia servicios ↔ pruebas.
- **Impacto en el usuario:** Menor.
- **Impacto en el negocio:** Menor.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Añadir categorías o explicar.
- **Notas de implementación:** —
- **Relacionado:** F-041, F-037
- **Investigar / preguntas:** —

#### F-032 · Información contradictoria sobre la Silverado `[VERIFICADO]`
- **Área(s):** Contenido, Confianza
- **Qué noté:** Galería: "Chevrolet Silverado — Gloss black hood". Servicios: alt "Chevrolet Silverado with a gloss black hood wrap". Vídeo de proceso: kicker "Color change", texto "A black hood returned to a clean, gloss white finish", aria-label "hood changing from black to gloss white". En la foto de servicios la camioneta es beige/arena con capó oscuro.
- **Dónde:** `#process` (3er vídeo), `#work`, `#services`.
- **Evidencia:** HTML (data-text, alt).
- **Por qué puede ser un problema:** Si es el mismo vehículo, el texto está mal (negro→blanco vs capó negro). Si son dos Silverado distintas, no queda claro. Un lector atento puede dudar de la veracidad del portfolio.
- **Impacto en el usuario:** Confusión leve.
- **Impacto en el negocio:** Leve pérdida de credibilidad [SUPUESTO].
- **Severidad:** Media (por el tema de la confianza; Baja si nadie lo nota)
- **Esfuerzo:** S
- **Posibles soluciones:** Corregir el texto; usar nombres de proyecto únicos ("Silverado #1 — black hood", "Silverado #2 — hood back to white").
- **Notas de implementación:** —
- **Relacionado:** F-031
- **Investigar / preguntas:** [PREGUNTA] ¿Son el mismo vehículo?

#### F-031 · Nombre del color del Tucson distinto entre web y Facebook `[VERIFICADO en ambos, sin confirmar que sea el mismo vehículo]`
- **Área(s):** Contenido, Consistencia
- **Qué noté:** Web: "Gloss laser flip pink". Un post de Facebook de Hermes Wraps: "Space Candy Pink" con hashtags de cambio de color.
- **Dónde:** `#work` vs facebook.com/61583325997708.
- **Evidencia:** Búsqueda Firecrawl (extractos).
- **Por qué puede ser un problema:** Si es el mismo coche, el nombre del material debería coincidir (los clientes buscan colores por nombre).
- **Impacto en el usuario:** Mínimo.
- **Impacto en el negocio:** Mínimo; oportunidad SEO por nombre de color.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Usar el nombre comercial exacto de la película (marca + serie + color).
- **Notas de implementación:** —
- **Relacionado:** F-032, F-029
- **Investigar / preguntas:** [PREGUNTA] ¿Mismo vehículo? ¿Cuál es el nombre correcto del vinilo?

#### F-034 · Repetición de frases ("premium 3M vinyl", "all things vinyl", "fleet") `[VERIFICADO]`
- **Área(s):** Contenido, Mensajes
- **Qué noté:** En el texto visible: "3M" ×4 (hero, hero-meta, why 04 título y cuerpo), "all things vinyl" ×3, "fleet" ×17, "Hermes" ×14. "Premium 3M vinyl, written scope" + "Premium 3M vinyl, with coverage…" seguidos en el mismo ítem.
- **Dónde:** Por toda la página.
- **Evidencia:** Conteo sobre el texto del HTML.
- **Por qué puede ser un problema:** Suena a relleno y diluye el mensaje.
- **Impacto en el usuario:** Menor.
- **Impacto en el negocio:** Menor.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Edición de copy; en Why 04 no repetir el título en la primera frase.
- **Notas de implementación:** —
- **Relacionado:** F-029
- **Investigar / preguntas:** —

#### F-040 · El texto dice "tap" también en escritorio `[VERIFICADO]`
- **Área(s):** Contenido, UX
- **Qué noté:** "or tap the photo to see it full size" y "Tap the photo to enlarge" se muestran en escritorio.
- **Dónde:** `#work`.
- **Evidencia:** Captura escritorio.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Microcopy pensado solo para móvil; en escritorio es "click". Impacto mínimo.
- **Posibles soluciones:** "Select the photo to enlarge" o cambiar el texto por CSS/JS según el puntero (`@media (hover:hover)`).
- **Notas de implementación:** —
- **Relacionado:** —
- **Investigar / preguntas:** —

#### F-036 · Afirmaciones absolutas difíciles de cumplir siempre `[VERIFICADO el texto; cumplimiento NO VERIFICADO]`
- **Área(s):** Contenido, Confianza
- **Qué noté:** "Every project is recorded from start to finish." "Every surface is cleaned and inspected…" Solo hay 3 vídeos.
- **Dónde:** `#process`, `#why`.
- **Evidencia:** Copy.
- **Por qué puede ser un problema:** Si un cliente pide ver la grabación de su proyecto y no existe, se pierde confianza. También choca un poco con el término "Let Hermes know… if you prefer your vehicle not to appear" (entonces no todo se graba/publica).
- **Impacto en el usuario:** Ninguno inmediato.
- **Impacto en el negocio:** Riesgo de promesa incumplida.
- **Severidad:** Nota
- **Esfuerzo:** S
- **Posibles soluciones:** "Projects are filmed…" o "Most projects…"; o cumplirlo y ofrecer el vídeo al cliente como valor añadido (¡buena idea de diferenciación!).
- **Notas de implementación:** —
- **Relacionado:** F-035
- **Investigar / preguntas:** [PREGUNTA] ¿Se graba realmente todo?

#### F-037 · "Chrome delete" es titular de servicio pero los términos lo tratan como "extra" `[VERIFICADO]`
- **Área(s):** Contenido, Mensajes
- **Qué noté:** Servicio: "Hoods, Roofs & Chrome Delete". Términos: "Door jambs, chrome delete and other extras are quoted separately."
- **Dónde:** `#services`, `#terms`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Lectura confusa: ¿es un servicio principal o un extra? Probablemente quiere decir "no incluido en un wrap completo", pero no lo dice.
- **Posibles soluciones:** "Chrome delete is quoted separately when added to a full wrap."
- **Notas de implementación:** —
- **Relacionado:** F-042
- **Investigar / preguntas:** —

### 5.10 Mensajes

- Promesa central consistente entre title, meta description, OG y hero: "owner-operated", "premium 3M vinyl", "Tampa Bay", "fleet". ✔ [VERIFICADO]
- Diferenciación clara y creíble: **una sola persona responsable** + **proceso visible en vídeo** + **condiciones por escrito**. Es un buen ángulo. ✔
- Pero el ángulo "flotas" está sobrerrepresentado respecto a las pruebas (F-028), y el ángulo "personal attention" no tiene persona (F-025).
- Tono: sobrio, algo corporativo ("accountable specialist", "ongoing fleet program") para un negocio de una persona que en Facebook usa hashtags y fotos de coches de particulares. Posible desajuste de voz entre la web y las redes [SUPUESTO].
- Objeciones tratadas: calidad (vídeos, preparación), alcance (presupuesto escrito), riesgo de pintura (estado del vehículo), leasing. No tratadas: precio, tiempo, duración real, garantía concreta, ubicación. → F-014, F-039, F-026, F-029.

#### F-028 · El mensaje apuesta por flotas, pero no hay ninguna prueba de trabajo con flotas `[VERIFICADO]`
- **Área(s):** Mensajes, Confianza, Contenido
- **Qué noté:** Title: "Fleet Graphics & Vehicle Wraps". Hero: "…to an ongoing fleet program". Why 05: "Consistency for fleets". Términos y FAQ hablan de flotas. Galería "Commercial (2)": 2 fotos del **mismo** SUV (lateral + capó) de Tampa PC Consultants. El vídeo de retirada es de un sedán con gráficos comerciales antiguos (retirada, no instalación de flota).
- **Dónde:** Title, hero, why, terms, FAQ, galería.
- **Evidencia:** HTML; capturas.
- **Por qué puede ser un problema:** Un comprador B2B busca casos: nº de vehículos, empresa, plazo. Sin eso, la promesa "fleet program" suena aspiracional.
- **Impacto en el usuario:** El gestor de flotas no ve evidencia y se va [SUPUESTO].
- **Impacto en el negocio:** El segmento que más vale (flotas) es el peor respaldado.
- **Severidad:** Alta (si flotas es el objetivo); Media si no.
- **Esfuerzo:** M (depende de tener casos)
- **Posibles soluciones:** Caso de estudio de un trabajo comercial (aunque sea 1 vehículo): problema → diseño → instalación → resultado + cita del cliente; foto de varios vehículos si existe; si aún no hay flotas, reformular ("Ready for fleets: one approved layout per vehicle type").
- **Notas de implementación:** —
- **Relacionado:** F-024, F-005, F-030
- **Investigar / preguntas:** [PREGUNTA] ¿Cuántos clientes comerciales/flotas reales hay hoy?

### 5.11 CTAs

#### F-023 · Cinco etiquetas distintas para la misma acción (ir al formulario) `[VERIFICADO]`
- **Área(s):** CTAs, Consistencia
- **Qué noté:** "Request a quote" (×2), "Start the conversation", "Ask about a sign", "Escribir mensaje" → todas a `#contact`. En el formulario la acción final es "Send by email/WhatsApp".
- **Dónde:** Ver 4.4.
- **Evidencia:** HTML.
- **Por qué puede ser un problema:** Variar el texto según el contexto no es malo ("Ask about a sign" es bueno). Pero "Start the conversation" es vago.
- **Impacto en el usuario:** Menor.
- **Impacto en el negocio:** Menor.
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Unificar en "Get a free quote" [SUPUESTO: confirmar si el presupuesto es gratis] + variantes contextuales específicas.
- **Notas de implementación:** —
- **Relacionado:** F-011
- **Investigar / preguntas:** [PREGUNTA] ¿El presupuesto es gratis? Si sí, decirlo en el CTA.

#### F-048 · Las tarjetas de servicio no llevan a ningún sitio (5 de 6 sin CTA) `[VERIFICADO]`
- **Área(s):** CTAs, Servicios, Interacciones
- **Qué noté:** Las tarjetas tienen efecto hover (zoom de la imagen, `cursor` normal) pero no son enlaces. Solo "Signs" tiene botón.
- **Dónde:** `#services .service-card`.
- **Evidencia:** HTML (`<article>` sin `<a>`); CSS `.service-card:hover img{transform:scale(1.035)}`.
- **Por qué puede ser un problema:** El hover sugiere que son clicables (affordance falsa); y cada servicio es un punto natural de "quiero esto".
- **Impacto en el usuario:** Clic sin respuesta; tiene que buscar el formulario y elegir el servicio otra vez.
- **Impacto en el negocio:** Oportunidad de conversión perdida [SUPUESTO].
- **Severidad:** Media
- **Esfuerzo:** S
- **Posibles soluciones:** Tarjeta entera clicable → `#contact` con el servicio preseleccionado (`?service=partial` → JS selecciona la opción); o → página del servicio (F-005); o → la categoría correspondiente de la galería.
- **Notas de implementación:** El `<select id="service">` ya tiene opciones equivalentes.
- **Relacionado:** F-005, F-016
- **Investigar / preguntas:** —

### 5.12 Confianza

#### F-024 · Cero prueba social: ni reseñas, ni estrellas, ni testimonios `[VERIFICADO en la página]`
- **Área(s):** Confianza, Conversión
- **Qué noté:** No hay reseñas, puntuación de Google, citas de clientes, número de proyectos ni años de experiencia. El CSS contiene `.review-placeholder` / `.placeholder` y `.instagram-card` **sin usar** → [PROBABLE] hubo una sección de reseñas "pendiente" que se quitó.
- **Dónde:** Toda la página.
- **Evidencia:** HTML; lista de CSS sin usar (F-072).
- **Por qué puede ser un problema:** En servicios para el coche (caros, con riesgo para la pintura) la prueba social es uno de los factores de decisión más fuertes [SUPUESTO general del sector]. Los vídeos ayudan, pero son autoafirmación.
- **Impacto en el usuario:** Menos confianza para un gasto alto.
- **Impacto en el negocio:** Menos conversión, sobre todo de quien no viene por recomendación [SUPUESTO].
- **Severidad:** Alta
- **Esfuerzo:** S–M (depende de tener reseñas)
- **Posibles soluciones:** Perfil de Google Business + pedir reseñas a cada cliente (enlace directo); mostrar 3–5 reseñas reales con nombre y fuente; incrustar o enlazar las reseñas de Facebook; cita corta del cliente comercial (Tampa PC Consultants) si lo autoriza.
- **Notas de implementación:** No inventar ni "maquillar" reseñas; enlazar a la fuente; añadir `aggregateRating` en el JSON-LD solo si las reseñas están en la propia página y son reales.
- **Relacionado:** F-025, F-028, F-008
- **Investigar / preguntas:** [NO VERIFICADO] Una búsqueda web solo devolvió la página de Facebook y vídeos; no apareció perfil de Google con reseñas (no significa que no exista). [PREGUNTA] ¿Hay reseñas en Google/Facebook?

#### F-025 · "Owner-operated" sin dueño: no hay nombre, cara ni historia `[VERIFICADO]`
- **Área(s):** Confianza, Mensajes
- **Qué noté:** "Quality is his personal standard, and each client gets his direct attention." "Tell Hermes about your vehicle…" No hay foto del instalador, ni nombre completo, ni años de experiencia, ni formación/certificaciones.
- **Dónde:** `#why`, `#terms`, `#faq`.
- **Evidencia:** Copy.
- **Por qué puede ser un problema:** Toda la propuesta es "una persona con nombre detrás" ("Quality with a name behind it"), pero el nombre/rostro no aparece. Contradicción directa con el titular de la sección.
- **Impacto en el usuario:** "¿Quién es 'his'?"; menos conexión humana.
- **Impacto en el negocio:** Desaprovecha el diferenciador principal.
- **Severidad:** Media (casi Alta por ser el mensaje central)
- **Esfuerzo:** S
- **Posibles soluciones:** Foto del dueño trabajando (ya hay vídeos: un fotograma sirve), nombre, 2–3 líneas de historia, años de experiencia; firma en "Personal attention is the standard".
- **Notas de implementación:** El bloque `.why-sign` ya tiene sitio (ahora pone el logo).
- **Relacionado:** F-024, F-046
- **Investigar / preguntas:** [PREGUNTA] ¿El dueño quiere aparecer con nombre y cara? ¿"Hermes" es su nombre?

#### F-026 · Ni dirección, ni horario, ni "¿taller o a domicilio?" — y los términos hablan de "drop-off" `[VERIFICADO]`
- **Área(s):** Confianza, Contenido, SEO local
- **Qué noté:** Solo "Tampa Bay area & surrounding communities". Términos: "Existing damage is noted and photographed at drop-off." Sin dirección, mapa ni horario. El JSON-LD solo tiene ciudad Tampa.
- **Dónde:** `#contact`, footer, JSON-LD.
- **Evidencia:** HTML.
- **Por qué puede ser un problema:** El usuario no sabe adónde llevar el coche ni si el instalador va a su casa. Para SEO local, una dirección/área de servicio coherente con Google Business importa.
- **Impacto en el usuario:** Pregunta extra; duda de la legitimidad.
- **Impacto en el negocio:** Fricción; peor visibilidad local [PROBABLE].
- **Severidad:** Media
- **Esfuerzo:** S
- **Posibles soluciones:** Si es un taller en casa y no se quiere publicar la dirección: "Shop in [barrio/ciudad], exact address shared when booking" + horario de atención + "mobile service available in X" si aplica.
- **Notas de implementación:** Añadir `openingHoursSpecification` y `areaServed` coherentes en el JSON-LD.
- **Relacionado:** F-008, F-039
- **Investigar / preguntas:** [PREGUNTA] ¿Taller fijo, servicio móvil o ambos?

#### F-027 · Email de Gmail y dominio propio inexistente `[VERIFICADO]`
- **Área(s):** Confianza, Técnico
- **Qué noté:** `hermeswraps@gmail.com`; el footer dice "hermeswraps.com" en texto, pero el dominio no resuelve; la web vive en `muddy-glitter-1944.josedavidmm9511.workers.dev`.
- **Dónde:** Contacto, footer, URL.
- **Evidencia:** HTML; DNS.
- **Por qué puede ser un problema:** Para clientes B2B/flotas, Gmail + URL aleatoria resta seriedad. La URL de workers.dev incluye un nombre de persona ("josedavidmm9511") y un nombre aleatorio ("muddy-glitter") → parece una prueba o, peor, phishing [SUPUESTO sobre la percepción].
- **Impacto en el usuario:** Desconfianza al compartir o al recibir el enlace.
- **Impacto en el negocio:** Credibilidad, sobre todo B2B.
- **Severidad:** Media (la parte de dominio es Crítica → F-001/F-002)
- **Esfuerzo:** S (una vez exista el dominio)
- **Posibles soluciones:** Conectar `hermeswraps.com`; email `info@hermeswraps.com` (puede reenviar a Gmail).
- **Notas de implementación:** Cloudflare Email Routing es gratis si el dominio está en Cloudflare [PROBABLE].
- **Relacionado:** F-001, F-002
- **Investigar / preguntas:** [PREGUNTA] ¿El dominio está comprado?

#### F-029 · "Premium 3M vinyl" sin detalle: ¿certificado?, ¿qué serie?, ¿qué garantía? `[VERIFICADO el texto]`
- **Área(s):** Confianza, Contenido, Legal (no es consejo legal)
- **Qué noté:** Se repite "premium 3M vinyl" pero no se dice si el instalador es certificado por 3M, qué serie de película se usa, ni la duración de la garantía ("within the period stated on the quote").
- **Dónde:** Hero, why, meta description, JSON-LD.
- **Evidencia:** Copy.
- **Por qué puede ser un problema:** "3M" es un nombre de marca de un tercero; si se insinúa una afiliación que no existe, puede haber problemas de uso de marca [NO VERIFICADO — no es consejo legal]. Si sí es certificado, se está perdiendo una señal de confianza fuerte. La garantía vaga resta.
- **Impacto en el usuario:** No puede comparar con otros instaladores.
- **Impacto en el negocio:** Diferenciación desaprovechada o riesgo.
- **Severidad:** Media
- **Esfuerzo:** S
- **Posibles soluciones:** Si hay certificación: logo/badge oficial + enlace de verificación. Si no: "We install 3M™ 2080 series film" (o la que sea). Publicar la garantía estándar ("X months on installation; manufacturer warranty on film per 3M terms").
- **Notas de implementación:** —
- **Relacionado:** F-039, F-034
- **Investigar / preguntas:** [PREGUNTA] ¿Certificación 3M? ¿Periodo estándar de garantía?

#### F-030 · Fotos con marca y teléfono de un cliente tercero muy visibles `[VERIFICADO]`
- **Área(s):** Confianza, Contenido, Legal (no es consejo legal)
- **Qué noté:** La tarjeta "Fleet & Commercial Graphics" y la galería muestran "Tampa PC Consultants" y el teléfono "(813) 756-4171" en grande; la de retirada muestra otro rótulo antiguo ("VILO…" + un teléfono parcial).
- **Dónde:** `#services`, `#work`.
- **Evidencia:** Capturas.
- **Por qué puede ser un problema:** Es el trabajo real (bien). Pero: (1) [PREGUNTA] ¿hay permiso del cliente? (2) En móvil, un teléfono ajeno grande al lado del propio puede confundir.
- **Impacto en el usuario:** Confusión mínima.
- **Impacto en el negocio:** Riesgo bajo; también oportunidad (si el cliente lo autoriza, convertirlo en caso de estudio/testimonio).
- **Severidad:** Baja
- **Esfuerzo:** S
- **Posibles soluciones:** Confirmar permiso; mencionar al cliente ("Graphics for Tampa PC Consultants") como prueba.
- **Notas de implementación:** —
- **Relacionado:** F-028, F-024
- **Investigar / preguntas:** —

- Otras señales de confianza presentes ✔: términos claros, honestidad ("Final answers depend on…"), vídeos de proceso reales, aviso de privacidad del formulario ("Nothing is stored on this website"), redes sociales activas (Facebook con publicaciones recientes según la búsqueda [VERIFICADO por extractos]).
- Señales ausentes: reseñas (F-024), persona (F-025), dirección (F-026), dominio/email propios (F-027), certificaciones/seguro (F-029), política de privacidad (F-078).

### 5.13 Conversión

#### F-014 · No hay ninguna orientación de precio `[VERIFICADO]`
- **Área(s):** Conversión, Contenido
- **Qué noté:** Ni "desde", ni rangos, ni factores de precio. El CSS contiene `.pricing`, `.price-grid`, `.price-card`, `.price-note` **sin usar** → [PROBABLE] existió una sección de precios y se eliminó.
- **Dónde:** Toda la página.
- **Evidencia:** HTML/CSS.
- **Por qué puede ser un problema:** "¿Cuánto cuesta?" es la primera pregunta en servicios de personalización [SUPUESTO]. Sin ancla, unos se van y otros piden presupuesto sin presupuesto real.
- **Impacto en el usuario:** No puede autocalificarse.
- **Impacto en el negocio:** Leads menos calificados y/o abandono [SUPUESTO].
- **Severidad:** Alta
- **Esfuerzo:** S (si el dueño da los rangos)
- **Posibles soluciones:** "Starting at $X" por servicio; "Typical range: roof $X–$Y"; o al menos los factores del precio (tamaño, película, complejidad, estado de la pintura).
- **Notas de implementación:** Reutilizar el CSS `.price-grid` que ya existe.
- **Relacionado:** F-039, F-072
- **Investigar / preguntas:** [PREGUNTA] ¿Por qué se quitó la sección de precios?

#### F-009 · Sin analítica ni seguimiento de conversiones `[VERIFICADO]`
- **Área(s):** Conversión, Analítica
- **Qué noté:** No hay GA4/GTM/píxel de Meta/Cloudflare Web Analytics en el HTML. Los envíos (mailto/wa.me/copiar) y los clics en `tel:` no se miden.
- **Dónde:** `<head>`, JS.
- **Evidencia:** Solo 2 `<script>` (JSON-LD y el JS propio).
- **Por qué puede ser un problema:** Imposible saber cuántos leads trae la web, desde qué canal, ni validar ninguna recomendación de este informe.
- **Impacto en el usuario:** Ninguno (positivo para la privacidad).
- **Impacto en el negocio:** Decisiones a ciegas.
- **Severidad:** Media
- **Esfuerzo:** S
- **Posibles soluciones:** Cloudflare Web Analytics (sin cookies, encaja con "Nothing is stored") + eventos propios (por ejemplo, contar clics en `tel:`, WhatsApp, email con un endpoint del Worker). O GA4 con consentimiento.
- **Notas de implementación:** Si se añaden cookies de terceros → banner/política (F-078).
- **Relacionado:** F-078, F-018
- **Investigar / preguntas:** [PREGUNTA] ¿Cómo llegan hoy los clientes (Instagram, boca a boca, Google)?

- Fricciones de conversión adicionales: F-012 (sin CTA fijo), F-015 (sin fotos), F-016 (valores preseleccionados), F-018 (email falla en silencio), F-022 (WhatsApp escondido), F-024 (sin reseñas).
- Oportunidades (hipótesis, sin cifras inventadas): botón fijo de WhatsApp; "Get a free quote in 24h" [SUPUESTO: solo si es verdad]; tarjetas de servicio que preseleccionan el servicio; prueba social cerca del formulario.

### 5.14 Accesibilidad (referencia WCAG 2.2 AA)

#### F-054 · El texto dorado sobre fondos claros no pasa el contraste mínimo `[VERIFICADO por cálculo]`
- **Área(s):** Accesibilidad, UI
- **Qué noté:** `--gold #bb8b38` sobre `--bg #f4f1ed` = **2.72:1**; sobre `#fff` = **3.06:1**; sobre `--surface-2 #ebe6e0` = **2.47:1**. Se usa en los eyebrows (0.76rem ≈ 12 px, peso 800) de Services, Why, Terms, FAQ y Contact, y en los números "01–05" de Why (≈ 34 px bold). Texto pequeño necesita 4.5:1; texto grande, 3:1.
- **Dónde:** `.eyebrow` en secciones claras; `.why-item b`; `.term::before` (decorativo, no aplica).
- **Evidencia:** Cálculo WCAG (fórmula de luminancia relativa).
- **Por qué puede ser un problema:** Falla el criterio 1.4.3 (AA) en elementos de navegación visual de todas las secciones claras.
- **Impacto en el usuario:** Personas con baja visión o con el móvil al sol no leen las etiquetas.
- **Impacto en el negocio:** Riesgo de accesibilidad/ADA [NO VERIFICADO legalmente]; menos legibilidad.
- **Severidad:** Alta
- **Esfuerzo:** S
- **Posibles soluciones:** Un dorado más oscuro para fondos claros (por ejemplo `#7d5a1c`: 5.57:1 sobre `--bg`, 6.27:1 sobre blanco, 5.05:1 sobre `--surface-2` — calculado; ojo, `#8a6420` no basta sobre `--surface-2`: 4.31:1) como token `--gold-text`; mantener `#bb8b38` para fondos oscuros (ahí pasa: 5.49–6.47:1).
- **Notas de implementación:** Token nuevo + `.section:not(.showroom) .eyebrow{color:var(--gold-text)}` o similar. En modo oscuro el dorado sí pasa (8.43:1).
- **Relacionado:** F-063, F-064, F-074
- **Investigar / preguntas:** Pasar axe para confirmar.

Tabla de contraste calculada:

| Par | Ratio | ¿Pasa? |
|---|---|---|
| Eyebrow dorado `#bb8b38` / `--bg #f4f1ed` | 2.72 | ❌ (texto pequeño) |
| Dorado / `#fff` (Terms) | 3.06 | ❌ |
| Dorado / `--surface-2` (Contact) | 2.47 | ❌ |
| Números 01–05 dorado / `--bg` (texto grande) | 2.72 | ❌ (necesita 3:1) |
| `--muted #665b5e` / `--bg` | 5.79 | ✔ |
| `--muted` / `--surface-2` (`.fine`) | 5.25 | ✔ |
| Texto botón dorado `#1b1113` / `#bb8b38` | 6.04 | ✔ |
| Blanco / botón vino `#691c2a` | 11.67 | ✔ |
| Blanco / botón WhatsApp | 5.32 | ✔ |
| `.showroom-hint` / `--wine-deep` | 7.94 | ✔ |
| Eyebrow dorado / `--wine-deep` | 5.49 | ✔ |
| Eyebrow dorado / `.vids` negro | 6.47 | ✔ |
| Copyright `rgb(143,129,132)` / footer | 5.32 | ✔ |
| Borde de inputs (~`#e3dcdd`) / `#fff` | ~1.35 | ❌ (1.4.11, 3:1) |
| Borde de inputs / fondo `--surface-2` | ~1.23 | ❌ |
| Placeholder (gris por defecto ~`#757575`) / `#fff` | ~4.61 | ✔ (justo) [SUPUESTO sobre el color por defecto] |
| OSCURO: dorado `#d2a451` / `#110d0e` | 8.43 | ✔ |
| OSCURO: `--muted` / `--bg` | 10.75 | ✔ |
| OSCURO: estado del formulario `--wine #8b2639` / `--surface-2 #24191c` | **1.98** | ❌ |

#### F-057 · Contenido en movimiento sin forma de pausarlo (hero en bucle + 2 carruseles) `[VERIFICADO por código]`
- **Área(s):** Accesibilidad, Interacciones
- **Qué noté:** (1) Vídeo del hero `autoplay muted loop` sin control. (2) Galería que avanza cada 4,5 s sin botón de pausa (solo se pausa con hover/foco). (3) Vídeos de proceso que se reproducen solos al entrar en pantalla y pasan al siguiente al terminar. Se respeta `prefers-reduced-motion` (oculta el hero, no autoavanza) ✔.
- **Dónde:** `.hero-video`, `#showroomStage`, `#vidStage`.
- **Evidencia:** HTML/JS.
- **Por qué puede ser un problema:** WCAG 2.2.2 (Pause, Stop, Hide, nivel A): contenido que se mueve automáticamente durante más de 5 s y se muestra junto a otro contenido necesita un mecanismo de pausa. `prefers-reduced-motion` ayuda, pero no sustituye un control visible.
- **Impacto en el usuario:** Distracción (TDAH, trastornos vestibulares, lectores de pantalla).
- **Impacto en el negocio:** Riesgo de accesibilidad [NO VERIFICADO legalmente].
- **Severidad:** Alta
- **Esfuerzo:** S–M
- **Posibles soluciones:** Botón pausa/play en el hero y en la galería; o quitar el autoplay de la galería; vídeos de proceso con `controls` o un botón de play claro.
- **Notas de implementación:** Botón con `aria-pressed`; persistir la preferencia en `localStorage` (opcional).
- **Relacionado:** F-043, F-058, F-062, F-068
- **Investigar / preguntas:** —

#### F-055 · No hay estilos de foco propios (`:focus`/`:focus-visible` = 0 reglas) `[VERIFICADO por CSS]`
- **Área(s):** Accesibilidad
- **Qué noté:** El CSS no define ningún estilo de foco. Depende del anillo por defecto del navegador, que sobre botones dorados, fondos vino oscuros y vídeo puede verse poco [PROBABLE]. Las tarjetas de la galería (`figure tabindex=0`) y los botones tienen foco por defecto.
- **Dónde:** Todo.
- **Evidencia:** Búsqueda en el CSS: 0 coincidencias de `:focus`.
- **Por qué puede ser un problema:** WCAG 2.4.7 (Focus Visible, AA) y 2.4.11/2.4.13 (2.2) → riesgo; el anillo por defecto de Chrome suele ser visible, pero no siempre sobre fondos con poco contraste.
- **Impacto en el usuario:** El usuario de teclado se pierde.
- **Impacto en el negocio:** Riesgo de accesibilidad.
- **Severidad:** Media (podría ser Alta tras probarlo)
- **Esfuerzo:** S
- **Posibles soluciones:** `:focus-visible{outline:3px solid var(--gold-soft);outline-offset:3px}` + una variante para fondos claros.
- **Notas de implementación:** —
- **Relacionado:** F-056, F-060
- **Investigar / preguntas:** [NO VERIFICADO] Probar con teclado en un navegador real.

#### F-056 · No hay enlace "Saltar al contenido" `[VERIFICADO]`
- **Área(s):** Accesibilidad
- **Qué noté:** No hay skip link; la cabecera tiene logo + 5 enlaces + botón.
- **Dónde:** `<header>`.
- **Evidencia:** HTML.
- **Severidad:** Media (Baja por ser solo 7 elementos; WCAG 2.4.1 se puede cumplir también con landmarks, y aquí `<main>` existe)
- **Esfuerzo:** S
- **Por qué / impacto:** Molestia menor para usuarios de teclado.
- **Posibles soluciones:** `<a class="skip" href="#main">Skip to content</a>`.
- **Notas de implementación:** `main` ya tiene `id="top"` (raro: "top" lo usa el logo para volver arriba).
- **Relacionado:** F-055
- **Investigar / preguntas:** —

#### F-058 · `aria-live` en un carrusel que cambia solo cada 4,5 s `[VERIFICADO por código]`
- **Área(s):** Accesibilidad
- **Qué noté:** `#showroomStage` tiene `aria-live="polite"`. Las clases cambian cada 4,5 s → algunos lectores de pantalla anuncian contenido continuamente [PROBABLE; depende del lector y de si cambia texto o solo clases/opacidad].
- **Dónde:** `#showroomStage`.
- **Evidencia:** HTML.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Interrumpe la lectura del resto de la página con lector de pantalla.
- **Posibles soluciones:** Quitar `aria-live` mientras rota sola; ponerlo solo cuando el usuario navega (patrón de carrusel de la APG de W3C: `aria-live="off"` en rotación, `"polite"` en manual).
- **Notas de implementación:** —
- **Relacionado:** F-057, F-043
- **Investigar / preguntas:** Probar con VoiceOver/NVDA.

#### F-059 · Pestañas con `role="tab"` sin el patrón completo `[VERIFICADO por código]`
- **Área(s):** Accesibilidad
- **Qué noté:** `role="tablist"` + `role="tab"` + `aria-selected`, pero sin `role="tabpanel"`, sin `aria-controls`, sin navegación con flechas entre pestañas, y todas son tabulables. Además no filtran (F-044).
- **Dónde:** `.showroom-tabs`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** El lector anuncia "tab, 1 of 4" y el usuario espera el comportamiento de pestañas; no lo hay.
- **Posibles soluciones:** Quitar los roles y usar botones normales con `aria-pressed`; o implementar el patrón completo.
- **Notas de implementación:** —
- **Relacionado:** F-044
- **Investigar / preguntas:** —

#### F-060 · El lightbox no atrapa el foco ni bloquea el fondo `[VERIFICADO por código]`
- **Área(s):** Accesibilidad, Interacciones
- **Qué noté:** `role="dialog" aria-modal="true"`, mueve el foco al botón cerrar ✔, Escape cierra ✔, devuelve el foco ✔. Pero Tab sale del diálogo al contenido de detrás (no hay trampa de foco ni `inert`). El `<img>` del lightbox empieza con `alt=""` y luego toma el título ✔.
- **Dónde:** `#lightbox`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** El usuario de teclado acaba navegando una página invisible detrás del overlay.
- **Posibles soluciones:** Usar `<dialog>` nativo con `showModal()` (trampa de foco incluida) o `inert` en `main`/`header`/`footer` mientras está abierto.
- **Notas de implementación:** —
- **Relacionado:** F-049, F-055
- **Investigar / preguntas:** —

#### F-061 · Puntos del carrusel de vídeos de 9×9 px `[VERIFICADO por CSS]`
- **Área(s):** Accesibilidad, Móvil
- **Qué noté:** `.vid-dots button{width:9px;height:9px}` con 7 px de separación. WCAG 2.5.8 (AA, 2.2) pide 24×24 px (o espaciado equivalente).
- **Dónde:** `#vidDots`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Difícil de tocar en móvil. Hay flechas de 46 px como alternativa (eso mitiga).
- **Posibles soluciones:** Área táctil de 24 px con el punto visual de 9 px (padding transparente).
- **Notas de implementación:** —
- **Relacionado:** F-050
- **Investigar / preguntas:** —

#### F-062 · Vídeos de proceso sin subtítulos/transcripción y sin control de teclado `[VERIFICADO por código; contenido del audio NO VERIFICADO]`
- **Área(s):** Accesibilidad, Interacciones
- **Qué noté:** 3 `<video>` sin `<track>`, sin `controls`. Play/pausa solo con clic en el vídeo (el `<video>` no es enfocable). Hay botón "Sound on" → tienen audio.
- **Dónde:** `#vidStage`.
- **Severidad:** Media · **Esfuerzo:** S–M
- **Por qué / impacto:** Si el audio tiene voz → WCAG 1.2.2 (subtítulos). Si solo es música → menos grave, pero falta una alternativa textual/descripción. El usuario de teclado no puede pausar.
- **Posibles soluciones:** Botón play/pausa accesible; subtítulos `.vtt` si hay voz; descripción breve (ya existe `data-text` ✔).
- **Notas de implementación:** —
- **Relacionado:** F-057, F-050
- **Investigar / preguntas:** [PREGUNTA] ¿Los vídeos tienen voz o solo música?

#### F-063 · Bordes de los campos del formulario casi invisibles (~1.2–1.35:1) `[VERIFICADO por cálculo aproximado]`
- **Área(s):** Accesibilidad, Formularios
- **Qué noté:** `border:1px solid var(--line)` con `--line: rgba(68,23,31,.18)` → muy suave; el campo se distingue sobre todo por el fondo blanco frente al gris claro de la sección.
- **Dónde:** `.field input/select/textarea`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** WCAG 1.4.11 (contraste no textual 3:1 para identificar componentes). En las capturas los campos se ven, pero por el relleno, no por el borde.
- **Posibles soluciones:** Borde más oscuro (por ejemplo, `--muted`) en los inputs.
- **Notas de implementación:** —
- **Relacionado:** F-054
- **Investigar / preguntas:** —

#### F-064 · Modo oscuro: el texto de estado del formulario tiene 1.98:1 `[VERIFICADO por cálculo; visual NO VERIFICADO]`
- **Área(s):** Accesibilidad, Formularios, Modo oscuro
- **Qué noté:** `.status{color:var(--wine)}` → en oscuro `#8b2639` sobre `--surface-2 #24191c`.
- **Dónde:** `#formStatus`.
- **Severidad:** Baja (solo modo oscuro, pero afecta justo al mensaje de confirmación) · **Esfuerzo:** S
- **Por qué / impacto:** El usuario en modo oscuro no lee "Opening WhatsApp…" ni "Details copied".
- **Posibles soluciones:** Usar `--gold-soft` o `--text` en oscuro.
- **Notas de implementación:** —
- **Relacionado:** F-018, F-054
- **Investigar / preguntas:** Revisar el modo oscuro entero en un navegador.

#### F-067 · FAQ: el "+" se lee en voz alta y no hay `aria-controls` `[VERIFICADO]`
- **Área(s):** Accesibilidad
- **Qué noté:** `<button class="faq-q" aria-expanded="false"><span>Pregunta</span><span>+</span></button>` → el lector dice "How long does a vinyl wrap last? plus, collapsed". Sin `type="button"` (no está en un form → sin impacto). Respuesta oculta con `display:none` ✔.
- **Dónde:** `#faq`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Posibles soluciones:** `aria-hidden="true"` en el span "+"; o `<details><summary>` nativo.
- **Notas de implementación:** —
- **Relacionado:** —
- **Investigar / preguntas:** —

- **Cosas bien hechas** ✔ [VERIFICADO]: landmarks (`header`, `nav aria-label`, `main`, `aside aria-label`, `footer`); un solo H1; jerarquía H2/H3 lógica; `alt` descriptivos en todas las fotos de trabajos; `alt=""` en logos decorativos; vídeo del hero `aria-hidden`; `aria-label` en los vídeos de proceso; `lang="es"` en la franja española; labels de formulario reales; `role="status"` en el mensaje del formulario; soporte de `prefers-reduced-motion`; flechas con `aria-label`.
- Pequeño: "Síguenos en el proceso" dentro del eyebrow de Process sin `lang="es"` → pronunciación incorrecta con lector de pantalla. Baja. (Ver F-038)

### 5.15 Responsive móvil

- Captura móvil a 360 px: sin scroll horizontal visible ✔; botones del hero a ancho completo ✔; formulario a una columna ✔; carruseles simplificados (sin tarjetas laterales) ✔; tamaños de texto legibles ✔. [VERIFICADO]
- Inputs con `font: 500 1rem` → 16 px → evita el zoom automático de iOS ✔.
- `tel:` clicable ✔ (hero, contacto, footer).
- Problemas: F-012 (sin CTA fijo), F-013 (quote escondido), F-053 (largo), F-061 (puntos pequeños), F-068 (vídeo en datos móviles), F-047 (pies de foto).
- Márgenes laterales de 13 px en < 620 px (más estrechos de lo habitual) → Baja.
- El eyebrow del hero en móvil ocupa 2 líneas ("OWNER-OPERATED · TAMPA BAY AREA / FLORIDA") en dorado sobre vídeo → contraste variable [VERIFICADO en captura].
- Tablet (768 px) no capturada → [NO VERIFICADO]. Por CSS, entre 621 y 900 px: galería de una columna, "process" en 1 columna; parece razonable [PROBABLE].
- Altura del hero en móvil: `min-height:720px` → en un iPhone SE (667 px de alto) el hero no cabe y los CTA pueden quedar justo en el borde [PROBABLE].

### 5.16 Formularios

#### F-015 · El formulario no permite adjuntar fotos, pero las FAQ dicen que son necesarias `[VERIFICADO]`
- **Área(s):** Formularios, Conversión, Contenido
- **Qué noté:** FAQ: "What should I send for a quote? The year, make and model, **clear photos** of the outside of the vehicle… and reference images". Rótulos: "Send… a photo of the space". El formulario no tiene campo de archivos, y `mailto:` no puede adjuntar archivos. Nada dice "attach photos after the app opens".
- **Dónde:** `#quoteForm`, `#faq`.
- **Evidencia:** HTML.
- **Por qué puede ser un problema:** El negocio necesita fotos para cotizar; el lead llega sin fotos → otra ronda de mensajes. El usuario puede no saber que tiene que añadirlas.
- **Impacto en el usuario:** Paso extra no anunciado.
- **Impacto en el negocio:** Presupuestos más lentos; leads que se enfrían [SUPUESTO].
- **Severidad:** Alta
- **Esfuerzo:** S (texto) / M (subida real)
- **Posibles soluciones:** (A) Rápido: texto junto a los botones: "After WhatsApp/email opens, attach 3–4 photos of your vehicle." y añadir esa línea al mensaje generado ("Photos: I'll attach them in this chat"). (B) Subida de fotos al Worker (R2) y enlace en el mensaje → contradice "Nothing is stored on this website" (habría que cambiar el aviso).
- **Notas de implementación:** Para (A): añadir la línea al array `text` del JS.
- **Relacionado:** F-018, F-039, F-022
- **Investigar / preguntas:** —

#### F-018 · "Send by email" puede fallar en silencio; no hay estado de error, ni de éxito, ni alternativa `[PROBABLE por código]`
- **Área(s):** Formularios, Estados, Conversión
- **Qué noté:** `location.href='mailto:…'` + `status.textContent='Opening your email app…'`. Si el equipo no tiene cliente de correo (habitual en PCs con webmail) no pasa nada y el mensaje se queda en "Opening…". No hay "Didn't open? Email us at… / Copy the details". No hay estado final "Sent" (imposible saber si el usuario realmente envió).
- **Dónde:** `#quoteForm`, modo email.
- **Evidencia:** JS.
- **Por qué puede ser un problema:** Es el botón más destacado del formulario (primario, primero).
- **Impacto en el usuario:** Rellena todo y no ocurre nada → frustración.
- **Impacto en el negocio:** Lead perdido justo en el último paso [SUPUESTO sobre la frecuencia].
- **Severidad:** Alta
- **Esfuerzo:** S
- **Posibles soluciones:** Tras pulsar, mostrar un panel: "If your email app didn't open: copy the details [Copy] and send them to hermeswraps@gmail.com" + enlace a WhatsApp. Alternativa robusta: endpoint del Worker que envíe el email (MailChannels/Resend…) y muestre un éxito real.
- **Notas de implementación:** Los mailto largos pueden truncarse en algunos clientes (~2 000 caracteres) [PROBABLE, depende del cliente].
- **Relacionado:** F-019, F-064, F-051, F-020
- **Investigar / preguntas:** Probar en Windows sin Outlook, ChromeOS, iOS sin Mail.

#### F-016 · Los selects vienen con un valor ya elegido ("Business / fleet", "Commercial / fleet graphics") `[VERIFICADO]`
- **Área(s):** Formularios, Calidad de datos
- **Qué noté:** Ninguna opción "Choose…". Un particular que no toca los selects envía "Business / fleet" + "Commercial / fleet graphics".
- **Dónde:** `#clientType`, `#service`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Datos erróneos en el lead; el negocio puede responder con la información equivocada.
- **Posibles soluciones:** Opción vacía `<option value="" disabled selected>Choose…</option>` + `required`; o preseleccionar "Personal vehicle" si es el caso más común [PREGUNTA].
- **Notas de implementación:** `reportValidity()` ya validará el `required`.
- **Relacionado:** F-017, F-048
- **Investigar / preguntas:** ¿Qué proporción de leads son personales vs comerciales?

#### F-017 · "Number of vehicles" se pide también a particulares; sin lógica condicional `[VERIFICADO]`
- **Área(s):** Formularios
- **Qué noté:** Siempre visible; `inputmode="numeric"` sin `type="number"`/`pattern` → acepta texto. Company también aparece siempre (pone "optional" ✔).
- **Dónde:** `#vehicleCount`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Posibles soluciones:** Mostrar "Number of vehicles" y "Company" solo con "Business / fleet".
- **Notas de implementación:** —
- **Relacionado:** F-016
- **Investigar / preguntas:** —
- **Por qué / impacto:** Ruido para el particular.

#### F-019 · "Copy details" deja al usuario sin siguiente paso claro `[VERIFICADO]`
- **Área(s):** Formularios, Estados
- **Qué noté:** Copia el texto y muestra "Details copied. Paste them into your message." ¿Qué mensaje? ¿A quién? No hay enlace al lado. Además el texto generado no incluye datos de contacto del cliente (no hay campos de teléfono/email), así que si lo pega en un DM de Instagram funciona, pero si lo pega en otro sitio el negocio no sabe cómo responder.
- **Dónde:** `#quoteForm`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Callejón sin salida.
- **Posibles soluciones:** "Copied! Paste it in an Instagram DM / text to (813) 475-1311" con enlaces; o quitar este botón.
- **Notas de implementación:** —
- **Relacionado:** F-018, F-051
- **Investigar / preguntas:** —

#### F-020 · Navegadores sin `e.submitter` copian en lugar de enviar, en silencio `[PROBABLE por código]`
- **Área(s):** Formularios, Técnico
- **Qué noté:** `var mode=(e.submitter&&e.submitter.getAttribute('data-send'))||'copy';` → si el navegador no soporta `SubmitEvent.submitter` (por ejemplo, Safari anterior a 15.4 [PROBABLE]), pulsar "Send by WhatsApp" copia al portapapeles.
- **Dónde:** JS del formulario.
- **Severidad:** Baja (navegadores antiguos) · **Esfuerzo:** S
- **Por qué / impacto:** Comportamiento inesperado para una minoría.
- **Posibles soluciones:** Usar `type="button"` + listeners por botón en lugar de `submit`.
- **Notas de implementación:** Llamar a `reportValidity()` en cada handler.
- **Relacionado:** F-018
- **Investigar / preguntas:** —

#### F-021 · Los campos obligatorios no están marcados (solo el opcional) `[VERIFICADO]`
- **Área(s):** Formularios, Accesibilidad
- **Qué noté:** Name y Year/make/model son `required`, pero visualmente no se marcan; solo "Company (optional)".
- **Dónde:** `#quoteForm`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Marcar los opcionales es un patrón válido si se hace con todos; aquí "Project details" y "Number of vehicles" también son opcionales y no lo dicen → inconsistente. El usuario descubre lo obligatorio al fallar.
- **Posibles soluciones:** Marcar todos los opcionales o todos los obligatorios.
- **Notas de implementación:** —
- **Relacionado:** —
- **Investigar / preguntas:** —

#### F-022 · WhatsApp solo existe como botón dentro del formulario `[VERIFICADO]`
- **Área(s):** Conversión, Contacto
- **Qué noté:** El número de WhatsApp (18134751311) está solo en la configuración JS; no hay enlace "Chat on WhatsApp" en el hero, la cabecera, el contacto ni el footer. Para usar WhatsApp hay que rellenar el formulario (el nombre y el vehículo son obligatorios).
- **Dónde:** `#contact`, JS `CONTACT.whatsapp`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Muchos clientes de este tipo de servicio prefieren escribir directamente [SUPUESTO]; obligar a rellenar un formulario es un paso extra.
- **Posibles soluciones:** Enlace directo `https://wa.me/18134751311?text=Hi%20Hermes…` en el hero, en la barra fija (F-012) y en las líneas de contacto.
- **Notas de implementación:** —
- **Relacionado:** F-012, F-015
- **Investigar / preguntas:** —

### 5.17 Interacciones y movimiento

#### F-050 · Vídeos de proceso: controles ocultos y sonido global `[VERIFICADO por código]`
- **Área(s):** Interacciones, UX
- **Qué noté:** Play/pausa = tocar el vídeo (sin indicación visual). "Sound on" activa el sonido de **todos** los vídeos (estado global). Las tarjetas laterales se pueden tocar para cambiar. Avanza solo al terminar. Barra de progreso de 3 px ✔.
- **Dónde:** `#vidStage`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** El usuario no sabe que puede pausar; tampoco puede avanzar/retroceder dentro del vídeo.
- **Posibles soluciones:** Icono de play/pausa visible; opción de `controls` nativos en el lightbox/pantalla completa.
- **Notas de implementación:** —
- **Relacionado:** F-062, F-057
- **Investigar / preguntas:** ¿Cuánto duran los vídeos? (Facebook muestra uno de 0:26 [VERIFICADO por extracto]).

#### F-049 · El lightbox no permite navegar entre fotos `[VERIFICADO]`
- **Área(s):** Interacciones
- **Qué noté:** Solo muestra la foto activa con título y la ×. Para ver la siguiente hay que cerrar, avanzar y volver a abrir.
- **Dónde:** `#lightbox`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Posibles soluciones:** Flechas y deslizar dentro del lightbox.
- **Notas de implementación:** —
- **Relacionado:** F-060
- **Investigar / preguntas:** —
- **Por qué / impacto:** Fricción al revisar el portfolio.

- Otras: hover con zoom en las tarjetas de servicio que no son clicables (F-048); scroll suave (`scroll-behavior:smooth`) desactivado con reduced motion ✔; el menú móvil se cierra al elegir un enlace ✔.
- Sin JS: los carruseles mostrarían 1 tarjeta activa (las demás tienen opacidad 0 por CSS) → solo 1 de 13 fotos visible; el formulario no haría nada (`preventDefault` sin JS no aplica → el `<form>` sin `action` haría GET a la misma página con parámetros) [PROBABLE]. Caso raro; Baja.

### 5.18 Estados: vacío, carga, error, éxito

| Área | Carga | Vacío | Error | Éxito | Otros estados | Notas |
|---|---|---|---|---|---|---|
| Vídeo del hero | Póster ✔ | — | Si falla el mp4: póster [PROBABLE] | — | Reduced motion: oculto ✔ | Fondo de color si falla todo |
| Vídeos de proceso | Póster ✔, `preload=none` | — | Sin manejo (`play().catch` vacío) | — | Autoplay bloqueado → queda el póster sin indicación de play [PROBABLE] | F-050 |
| Galería | `loading=lazy` sin placeholder; fondo `rgb(33,20,23)` | — | Imagen rota → caja oscura sin aviso [PROBABLE] | — | Sin JS: 1 foto | |
| Lightbox | Sin spinner (imagen ya cargada normalmente) | — | — | — | — | |
| Formulario: validación | — | — | Burbujas nativas de `reportValidity()` ✔ (idioma = navegador) | — | | Mensajes nativos poco personalizables |
| Formulario: email | — | — | **Ninguno** (F-018) | "Opening your email app…" (no es éxito real) | | |
| Formulario: WhatsApp | — | — | Popup bloqueado → nada [PROBABLE] | "Opening WhatsApp…" | | |
| Formulario: copiar | — | — | "Copy was blocked…" ✔ / "Copy is not available…" ✔ | "Details copied…" ✔ | | Bien cubierto |
| 404 | — | — | **Página en blanco** (F-004) | — | | |
| Error del servidor (5xx) | — | — | [NO VERIFICADO] | — | | |
| Contacto sin datos | El JS oculta líneas si `CONTACT.x` está vacío ✔ | | | | | Buen patrón para el YouTube vacío |

#### F-004 · La página 404 está vacía `[VERIFICADO]`
- **Área(s):** Estados, SEO, UX
- **Qué noté:** Cualquier URL inexistente devuelve 404 con cuerpo vacío (sin marca, navegación, ni enlace a inicio).
- **Dónde:** `/cualquier-cosa`.
- **Evidencia:** Firecrawl: `statusCode 404`, markdown vacío.
- **Por qué puede ser un problema:** Enlaces antiguos, errores de escritura o URLs compartidas mal acaban en una pantalla en blanco. Más relevante si en el futuro hay páginas por servicio (F-005).
- **Impacto en el usuario:** Callejón sin salida; parece que la web está rota.
- **Impacto en el negocio:** Visitas perdidas.
- **Severidad:** Media
- **Esfuerzo:** S
- **Posibles soluciones:** 404 con marca: "Page not found" + botones a Inicio, Trabajos, Presupuesto, teléfono.
- **Notas de implementación:** En el Worker: devolver HTML de 404 con status 404 (no 200).
- **Relacionado:** F-003
- **Investigar / preguntas:** —

### 5.19 SEO

#### F-001 · Canonical, og:url, og:image y JSON-LD apuntan a `hermeswraps.com`, que no resuelve `[VERIFICADO]`
- **Área(s):** SEO, Técnico, Redes sociales
- **Qué noté:** `<link rel="canonical" href="https://hermeswraps.com/">`, `og:url` = `https://hermeswraps.com/`, `og:image` = `https://hermeswraps.com/assets/commercial-suv-side-hero.jpg`, JSON-LD `url`, `logo`, `image` = `hermeswraps.com/...`. El DNS de `hermeswraps.com` **no resuelve** (comprobado con Firecrawl el 2026-10-13).
- **Dónde:** `<head>`, JSON-LD.
- **Evidencia:** HTML; error de Firecrawl "DNS resolution failed for hostname hermeswraps.com".
- **Por qué puede ser un problema:**
  - Google: el canonical dice "la página real está en otro sitio" (que no existe). Lo más probable es que ignore el canonical o que no indexe bien ninguna de las dos URLs [PROBABLE].
  - Al compartir el enlace en WhatsApp/Facebook/iMessage, la imagen de previsualización (`og:image`) no carga → enlace sin foto [PROBABLE].
  - Datos estructurados con logo/imagen rotos.
- **Impacto en el usuario:** Enlaces compartidos poco atractivos.
- **Impacto en el negocio:** Visibilidad orgánica y social muy reducida mientras siga así.
- **Severidad:** Crítica (si el workers.dev es el sitio en uso); Baja si es solo staging y el dominio se conecta antes del lanzamiento.
- **Esfuerzo:** S (conectar el dominio) / S (o cambiar las URLs temporalmente)
- **Posibles soluciones:** (A) Conectar `hermeswraps.com` al Worker (Custom Domain en Cloudflare) — arregla todo de golpe. (B) Si se va a seguir en workers.dev un tiempo: canonical/OG relativos o al workers.dev, y `noindex` en workers.dev cuando exista el dominio para evitar duplicados.
- **Notas de implementación:** Después: redirección 301 de workers.dev → dominio (o desactivar la ruta workers.dev en Cloudflare); comprobar con el Sharing Debugger de Facebook y la Rich Results Test de Google.
- **Relacionado:** F-002, F-027, F-008, F-003
- **Investigar / preguntas:** [PREGUNTA] ¿El dominio está comprado? ¿En qué registrador? ¿Está en Cloudflare?

#### F-002 · El sitio vive en un subdominio aleatorio de workers.dev con un nombre personal `[VERIFICADO]`
- **Área(s):** SEO, Confianza, Marca
- **Qué noté:** `muddy-glitter-1944.josedavidmm9511.workers.dev`. Si es la URL que se comparte con clientes, no es memorable, no transmite la marca, y lleva el nombre de cuenta de una persona.
- **Dónde:** URL.
- **Evidencia:** —
- **Por qué puede ser un problema:** Confianza (parece una prueba o un enlace sospechoso [SUPUESTO sobre la percepción]); SEO (si Google indexa esta URL y luego se cambia al dominio → migración).
- **Impacto en el usuario:** Desconfianza; difícil de recordar o teclear.
- **Impacto en el negocio:** Credibilidad; autoridad SEO acumulada en una URL temporal.
- **Severidad:** Crítica (junto con F-001) si es la URL pública actual.
- **Esfuerzo:** S
- **Posibles soluciones:** Ver F-001. Mientras tanto, no compartir la URL de workers.dev en redes/tarjetas.
- **Notas de implementación:** —
- **Relacionado:** F-001, F-027
- **Investigar / preguntas:** [PREGUNTA] ¿Esta URL está en la bio de Instagram/Facebook/Google?

#### F-003 · Sin sitemap.xml; robots.txt sin directivas `[VERIFICADO]`
- **Área(s):** SEO, Técnico
- **Qué noté:** `/sitemap.xml` → 404. `/robots.txt` → 200, pero en la respuesta solo hay comentarios de "content signals" de Cloudflare; ni `User-agent`, ni `Sitemap:`.
- **Dónde:** Raíz.
- **Severidad:** Media (Baja con una sola página; sube a Media/Alta si se crean páginas por servicio — F-005) · **Esfuerzo:** S
- **Por qué / impacto:** Con una sola URL Google la encuentra igual; pero es higiene básica y necesaria si crece.
- **Posibles soluciones:** `sitemap.xml` con las URL canónicas del dominio final; `robots.txt` con `User-agent: *`, `Allow: /`, `Sitemap: https://hermeswraps.com/sitemap.xml`.
- **Notas de implementación:** Revisar la configuración de "Managed robots.txt" de Cloudflare (puede estar inyectando el texto).
- **Relacionado:** F-001, F-005
- **Investigar / preguntas:** [NO VERIFICADO] Si Cloudflare añade bloques para bots de IA que no salieron en la respuesta.

#### F-006 · El H1 no contiene palabras clave; el título sí `[VERIFICADO]`
- **Área(s):** SEO
- **Qué noté:** Title (61 car.) ✔: "Hermes Wraps — Fleet Graphics & Vehicle Wraps | Tampa Bay, FL". H1: "One standard. Across every vehicle." Los H2 tampoco tienen términos de búsqueda ("See how the work is done.", "Projects by type."…). "Tampa" aparece solo 4 veces en el texto visible.
- **Dónde:** Encabezados.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Señales on-page débiles para "car wrap Tampa", "vinyl wrap Tampa", "fleet graphics Tampa" [SUPUESTO sobre las palabras clave objetivo].
- **Posibles soluciones:** Ver F-033; H2 tipo "Vehicle wrap services in Tampa Bay".
- **Notas de implementación:** —
- **Relacionado:** F-033, F-005
- **Investigar / preguntas:** [PREGUNTA] ¿Palabras clave objetivo? ¿Hay datos de Search Console?

#### F-007 · Meta description de 194 caracteres `[VERIFICADO]`
- **Área(s):** SEO
- **Qué noté:** 194 caracteres → Google suele cortar alrededor de 150–160 [PROBABLE]. OG description (103) es distinta y más corta ✔.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Se corta "…review clear terms before you book." (la parte menos importante, así que el impacto es pequeño).
- **Posibles soluciones:** ~150 caracteres con CTA.
- **Notas de implementación:** —
- **Relacionado:** —
- **Investigar / preguntas:** —

#### F-008 · JSON-LD incompleto e incoherente `[VERIFICADO]`
- **Área(s):** SEO, SEO local
- **Qué noté:** `AutomotiveBusiness` con nombre, descripción, url, teléfono, email, `areaServed:["Tampa Bay area, FL","Brandon, FL"]`, dirección (solo ciudad/estado/país), logo, imagen, `sameAs` (IG, FB, TikTok). Faltan: `openingHoursSpecification`, `geo`, `priceRange`, `hasOfferCatalog`/servicios, `founder`. "Brandon, FL" no aparece en el texto visible. `url`/`logo`/`image` en el dominio roto (F-001). FAQ sin `FAQPage` (nota: Google ya casi no muestra resultados enriquecidos de FAQ para la mayoría de sitios [PROBABLE], así que el beneficio es bajo).
- **Dónde:** `<script type="application/ld+json">`.
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Datos estructurados más pobres para Google; incoherencia web ↔ schema.
- **Posibles soluciones:** Completar con datos reales; alinearlo con Google Business Profile; mencionar Brandon en el texto si es una zona real de servicio (o quitarlo).
- **Notas de implementación:** Validar con la Rich Results Test / validator.schema.org.
- **Relacionado:** F-001, F-026, F-024
- **Investigar / preguntas:** [PREGUNTA] ¿Por qué Brandon? ¿Es donde está el taller?

- Más SEO, sueltos:
  - `og:image` es una foto 4:3 o vertical [NO VERIFICADO el tamaño]; lo recomendable es 1200×630.
  - No hay `twitter:title/description/image` (Twitter/X usa los OG como respaldo → OK).
  - Nombres de imagen descriptivos (`corvette-front.jpg`, `tucson-pink-rear.jpg`) ✔.
  - Alt text descriptivo ✔ (sin relleno de palabras clave ✔).
  - Contenido en el HTML inicial (no depende de JS para el texto) ✔ [PROBABLE] → indexable.
  - Sin `hreflang` ni versión en español (F-038).
  - Enlaces internos: solo anclas. Sin enlaces a perfiles de reseñas.

### 5.20 Rendimiento

#### F-068 · Vídeo del hero con `preload="auto"` y autoplay, también en móvil `[VERIFICADO por HTML; peso NO VERIFICADO]`
- **Área(s):** Rendimiento, Móvil
- **Qué noté:** `<video class="hero-video" autoplay muted loop playsinline preload="auto" poster="…hero-loop-poster.jpg">`. No hay versión ligera para móvil ni `media`/`source` alternativa. El peso del mp4 no se pudo medir (curl bloqueado).
- **Dónde:** Hero.
- **Evidencia:** HTML.
- **Por qué puede ser un problema:** Un vídeo en bucle suele pesar varios MB [SUPUESTO]; se descarga nada más entrar, también con datos móviles, y compite con el LCP (póster/H1).
- **Impacto en el usuario:** Carga más lenta y consumo de datos.
- **Impacto en el negocio:** Rebote en móviles con mala conexión [SUPUESTO].
- **Severidad:** Alta [hasta medir el peso; podría bajar a Media si el vídeo es pequeño]
- **Esfuerzo:** S–M
- **Posibles soluciones:** Comprimir (H.264 ~1–2 Mbps, 720p, 6–10 s) [SUPUESTO sobre los objetivos]; `preload="metadata"` o `none` + iniciar tras `load`; no cargar el vídeo en `prefers-reduced-data`/conexiones lentas (`navigator.connection.saveData`); póster en WebP/AVIF con `fetchpriority="high"`.
- **Notas de implementación:** Con reduced motion el vídeo se oculta con `display:none`, pero con `preload=auto` puede que se descargue igual [PROBABLE].
- **Relacionado:** F-045, F-057, F-071
- **Investigar / preguntas:** Medir el peso real de `hero-loop.mp4` y de los 3 mp4 de proceso; ejecutar PageSpeed Insights.

#### F-069 · Imágenes solo en JPG, sin `srcset`/`sizes`, sin WebP/AVIF `[VERIFICADO]`
- **Área(s):** Rendimiento
- **Qué noté:** 24 `<img>`, 21 con `loading="lazy"` ✔, 0 `srcset`, 0 WebP. El mismo archivo sirve para 360 px y 1440 px.
- **Dónde:** Galería, servicios, logos.
- **Severidad:** Media · **Esfuerzo:** S–M
- **Por qué / impacto:** El móvil descarga fotos de tamaño escritorio [PROBABLE; tamaños reales NO VERIFICADOS].
- **Posibles soluciones:** Cloudflare Images / Image Resizing (`/cdn-cgi/image/width=…`) o generar 2–3 tamaños en AVIF/WebP + `srcset`.
- **Notas de implementación:** Las imágenes de la galería y servicios van en cajas de tamaño fijo con `object-fit:cover` → sin CLS aunque no tengan width/height ✔.
- **Relacionado:** F-068
- **Investigar / preguntas:** Pesos reales.

#### F-070 · Fuentes: Manrope 800 se usa pero no se carga; se cargan pesos que no se usan `[VERIFICADO por código]`
- **Área(s):** Rendimiento, UI
- **Qué noté:** Google Fonts carga Manrope 400/500/600/700 y Barlow Condensed 500/600/700/800 + 600 itálica. El CSS usa `font-weight:800` con Manrope en eyebrows, botones, labels, pestañas, etc. (16 usos de 800). Manrope 800 no se pide → el navegador usa 700 o sintetiza la negrita [PROBABLE]. Barlow 500/600/itálica: no encontré usos en el CSS [PROBABLE: no se usan].
- **Dónde:** `<link href="https://fonts.googleapis.com/css2?…">`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Peso de fuentes innecesario + render distinto al diseñado.
- **Posibles soluciones:** Pedir Manrope 400;500;700;800 y Barlow Condensed 700;800; o autoalojar las fuentes (privacidad, F-078).
- **Notas de implementación:** `display=swap` ✔; preconnect ✔.
- **Relacionado:** F-078, F-075
- **Investigar / preguntas:** —

#### F-071 · Métricas reales (LCP/CLS/INP) sin medir `[NO VERIFICADO]`
- **Área(s):** Rendimiento
- **Qué noté:** No pude ejecutar Lighthouse ni PSI desde el entorno.
- **Severidad:** Nota · **Esfuerzo:** S
- **Por qué / impacto:** Todo lo de rendimiento son inferencias.
- **Posibles soluciones:** PageSpeed Insights (móvil) + Cloudflare Web Analytics (Core Web Vitals reales).
- **Notas de implementación:** —
- **Relacionado:** F-068, F-069
- **Investigar / preguntas:** —

- Positivo ✔: sin frameworks; ~9,6 KB de JS; CSS ~29 KB (24 % no usado → F-072); vídeos de proceso con `preload="none"`; imágenes lazy; edge de Cloudflare [SUPUESTO].
- LCP probable: póster del vídeo del hero o el H1 [PROBABLE]. El póster no tiene `preload`/`fetchpriority`.
- Galería: 13 imágenes lazy dentro de un escenario de 500 px; las 13 están en el DOM con `opacity:0` → el navegador podría cargarlas todas al entrar en pantalla (las cartas se superponen) [PROBABLE].

### 5.21 Problemas técnicos

#### F-010 · Cabeceras de seguridad, caché y compresión sin verificar `[NO VERIFICADO]`
- **Área(s):** Técnico, Seguridad
- **Qué noté:** No pude leer las cabeceras HTTP (curl bloqueado; Firecrawl no las devuelve).
- **Severidad:** Nota · **Esfuerzo:** S
- **Por qué / impacto:** Desconocido. Workers no añade HSTS/CSP por defecto [PROBABLE].
- **Posibles soluciones:** Revisar con `curl -I` o securityheaders.com: HSTS, `Content-Security-Policy` (inline script/style → necesita hash o `unsafe-inline`), `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, `frame-ancestors`. Caché larga para `/assets/*` con nombres versionados.
- **Notas de implementación:** —
- **Relacionado:** —
- **Investigar / preguntas:** —

- `target="_blank"` ×7, todos con `rel="noopener"` ✔.
- `tel:8134751311` sin `+1` → funciona en EE. UU.; `tel:+18134751311` es más robusto internacionalmente. Baja.
- `CONTACT.phone.replace(/[^\d+]/g,'')` reescribe el href → coherente ✔.
- `new Date().getFullYear()` para el © ✔ (si falla el JS queda 2026, correcto hoy).

### 5.22 Calidad de código (solo lo observable del HTML servido; no hay repo fuente)

#### F-079 · El código del sitio no está en este repositorio `[VERIFICADO]`
- **Área(s):** Código, Proceso
- **Qué noté:** `angelicamrb5-bit/HermesWraps` solo tiene `README.md` (+ la skill). El Worker se despliega desde otro lugar (otra cuenta: `josedavidmm9511`).
- **Severidad:** Media · **Esfuerzo:** S
- **Por qué / impacto:** Sin control de versiones visible: difícil revisar cambios, revertir o colaborar; el conocimiento depende de una cuenta personal.
- **Posibles soluciones:** Subir el código del Worker al repo; desplegar con `wrangler` desde GitHub Actions.
- **Notas de implementación:** —
- **Relacionado:** F-076
- **Investigar / preguntas:** [PREGUNTA] ¿Quién mantiene el Worker? ¿Dónde está el código?

#### F-072 · ~24 % del CSS es de secciones eliminadas (28 clases sin usar) `[VERIFICADO por análisis]`
- **Área(s):** Código, Rendimiento
- **Qué noté:** Clases sin usar en el HTML: `pricing, price-grid, price-card, price-note, review-placeholder, placeholder, instagram-card, instagram-content, proof, trust, trust-inner, trust-item, process, steps, step, process-feature, process-feature-head, process-gallery, process-project, process-video, process-caption, gallery, gallery-section, gallery-top, filters, filter, project, project-info`. ≈ 7 KB de ~29 KB.
- **Dónde:** `<style>`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Peso muerto; confunde al mantener. **Pista de producto:** existieron (o se planearon) secciones de **precios, reseñas, Instagram, franja de confianza, pasos del proceso y galería filtrable**, y se quitaron → ver F-014, F-024, F-035.
- **Posibles soluciones:** Borrar o recuperar las secciones con contenido real.
- **Notas de implementación:** —
- **Relacionado:** F-014, F-024, F-043, F-073
- **Investigar / preguntas:** [PREGUNTA] ¿Por qué se quitaron esas secciones?

#### F-073 · Reglas que se sobrescriben unas a otras (parches sucesivos) `[VERIFICADO]`
- **Área(s):** Código, Sistema de diseño
- **Qué noté:** `.brand img` definida 4 veces (60 → 54 → 50 → 44 px); `.brand-copy` 4 veces (incluido `display:none` en móvil y luego `display:block`); `.hero` 4 veces (fondo repetido); `.service-card:nth-child(1),(2){span 6}` anulado por `@media (min-width:901px){.service-card:nth-child(n){span 4}}`; `.vid-card` 3 veces; `.why-grid`, `.footer-grid`, `.gallery` 3 veces.
- **Severidad:** Baja · **Esfuerzo:** S–M
- **Por qué / impacto:** Difícil saber qué estilo gana; riesgo de regresiones.
- **Posibles soluciones:** Consolidar, un bloque por componente.
- **Notas de implementación:** —
- **Relacionado:** F-072, F-074
- **Investigar / preguntas:** —

#### F-076 · Restos de plantilla/configuración visibles en producción `[VERIFICADO]`
- **Área(s):** Código, Contenido
- **Qué noté:** Comentario en el JS público: "HERMES CONTACT DETAILS — fill these in before publishing. Leave a value empty ("") to hide it…" y `youtube: ""`. En el HTML hay un enlace YouTube con `href="#"` y `target="_blank"` (no visible en las capturas → oculto por `hidden` [PROBABLE], pero Firecrawl lo incluyó en el markdown → algunos rastreadores pueden verlo).
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Señal de "plantilla"; un enlace vacío para quien navegue sin CSS/JS.
- **Posibles soluciones:** Quitar el enlace de YouTube del HTML hasta que exista el canal; limpiar el comentario.
- **Notas de implementación:** —
- **Relacionado:** F-077, F-079
- **Investigar / preguntas:** [PREGUNTA] ¿Hay canal de YouTube previsto?

#### F-077 · Datos de contacto duplicados en HTML y en la configuración JS `[VERIFICADO]`
- **Área(s):** Código
- **Qué noté:** Teléfono/email/redes escritos en el HTML (5+ sitios) y otra vez en `var CONTACT`. El JS sobrescribe los href al cargar.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Si se cambia el teléfono solo en un lado, el HTML sin JS (y lo que ven los rastreadores sin JS) queda desactualizado.
- **Posibles soluciones:** Una sola fuente (generar el HTML en build/en el Worker).
- **Notas de implementación:** —
- **Relacionado:** F-076
- **Investigar / preguntas:** —

- Otros: JS en una IIFE, ES5, legible pero minificado a mano en líneas larguísimas (difícil de mantener) [VERIFICADO en la serialización; el original puede ser distinto]; `main id="top"` usado para "volver arriba" (semántica rara); comentarios de sección numerados (`<!-- 1. PRESENTATION -->`) ✔ útiles.

### 5.23 Consistencia del sistema de diseño

#### F-074 · 82 colores literales; los tokens existen pero se saltan `[VERIFICADO]`
- **Área(s):** Sistema de diseño, Modo oscuro
- **Qué noté:** Hay 10 tokens en `:root` (+ versión oscura), pero hay ~60 `rgb()/rgba()` sueltos, sobre todo blancos rosados para texto sobre fondos oscuros y negros vino para fondos (ver 4.7). Varias secciones oscuras (`.vids`, footer, `.lightbox`, `.process-feature`) usan `rgb(13,9,10)` fijo, no `var(--…)`.
- **Dónde:** CSS.
- **Severidad:** Media · **Esfuerzo:** M
- **Por qué / impacto:** Cambios de marca costosos; el modo oscuro solo cambia parte del diseño (secciones con colores fijos quedan igual) → posibles combinaciones raras [NO VERIFICADO visualmente].
- **Posibles soluciones:** Tokens semánticos: `--on-dark-text`, `--on-dark-muted`, `--surface-dark`, `--gold-text` (F-054)… y sustituir los literales.
- **Notas de implementación:** —
- **Relacionado:** F-054, F-064, F-075
- **Investigar / preguntas:** ¿Hay guía de marca (colores oficiales)?

#### F-075 · 46 tamaños de fuente, 9 letter-spacings, 20 gaps, 30 paddings: sin escala `[VERIFICADO]`
- **Área(s):** Sistema de diseño
- **Qué noté:** Ver 4.7. Ejemplos de casi duplicados: 0.68/0.69/0.70/0.72/0.73/0.74/0.76/0.78rem para "texto pequeño en mayúsculas"; 3 `clamp()` distintos para los H2.
- **Severidad:** Baja · **Esfuerzo:** M
- **Por qué / impacto:** Inconsistencias sutiles; más difícil de mantener.
- **Posibles soluciones:** Escala tipográfica (por ejemplo, 6–8 pasos) y de espaciado (4/8/12/16/24/32/48/64/96).
- **Notas de implementación:** —
- **Relacionado:** F-074, F-073
- **Investigar / preguntas:** —

- Lo que sí es consistente ✔: radio 0 en todo (estética "cuadrada" deliberada), círculos solo para logos/puntos; 2 familias tipográficas; botones con la misma altura (50 px) y estilo de letra; eyebrow como patrón repetido; 2 breakpoints claros.

### 5.24 Componentes repetidos

- Ver 4.6. Resumen:
  - **Dos carruseles 3D** con lógica casi igual implementados por separado (vídeos y fotos) → candidato a un componente común (F-073).
  - **Bloque CTA vino con logo** ×2 (Signs card y Why-sign) con CSS separado.
  - **Logo** ×5 (F-046).
  - **Teléfono** ×3 visibles + config JS (F-077).
  - **Botón a `#contact`** ×5 con distintos textos (F-023).
  - **Mismo vehículo repetido**: el Business SUV aparece en galería (×2), en servicios y en el `og:image`; Corvette ×3; Tucson ×3; Silverado ×4 (galería ×2, servicios, vídeo). Con 13 fotos de ~7 vehículos, el portfolio parece más pequeño al repetir [VERIFICADO]. → [PREGUNTA] ¿Hay más trabajos fotografiados?

### 5.25 Páginas / estados / funcionalidades que faltan

- Páginas: servicios individuales (F-005), versión en español (F-038), política de privacidad (F-078), términos completos (`/terms`) (F-035), 404 con marca (F-004), sitemap.xml (F-003), "About/owner" (F-025), casos de estudio (F-028), guía de cuidados descargable (oportunidad).
- Estados: error/éxito real del formulario (F-018), autoplay bloqueado en vídeos, imagen rota.
- Funcionalidades: subida de fotos (F-015), WhatsApp directo (F-022), CTA fijo (F-012), pausa de carruseles (F-057), filtro real en la galería (F-044), mapa/zona de servicio (F-026), enlace a reseñas (F-024), botón de reservar/calendario (oportunidad; [PREGUNTA] ¿se quiere?).
- Metadatos: `og:image` 1200×630 [NO VERIFICADO el tamaño actual], manifest (no enlazado), favicon.ico/SVG (solo PNG de 32 px enlazado).

### 5.26 Decisiones confusas

- ¿Por qué el CTA principal del hero es "ver vídeos"? (F-011)
- ¿Por qué "Terms of service" en la nav principal y "FAQ" no? (F-035)
- ¿Por qué se quitaron precios, reseñas y la franja de confianza (CSS huérfano)? (F-072)
- ¿Las pestañas de la galería son filtros o atajos? (F-044)
- ¿"Hermes" es una persona o la marca? (F-025)
- ¿Por qué aparece "Brandon, FL" solo en el schema? (F-008)
- ¿Por qué el email es la opción primaria del formulario si el mailto es el método menos fiable? (F-018, F-051)
- ¿Por qué el texto "Síguenos en el proceso" en español dentro de un eyebrow en inglés, si el resto no es bilingüe? (F-038)
- ¿Por qué el logo en el hero si ya está en la cabecera? (F-046)
- ¿Silverado: negro→blanco o blanco→negro? (F-032)

#### F-038 · El soporte en español es superficial y llega tarde `[VERIFICADO]`
- **Área(s):** Contenido, Mensajes, Accesibilidad, SEO
- **Qué noté:** Franja "¿Prefieres hablar en español?" después de las FAQ (~75 % del scroll); el botón "Escribir mensaje" lleva al formulario con todas las etiquetas, opciones y botones en inglés; el mensaje generado es en inglés ("Vehicle wrap project request…"). Eyebrow de Process mezcla "Follow the process · Síguenos en el proceso" sin `lang="es"`.
- **Dónde:** `.spanish-strip`, `#process` eyebrow, `#quoteForm`.
- **Severidad:** Media · **Esfuerzo:** S (mínimo) / M (página `/es/`)
- **Por qué / impacto:** Si los hispanohablantes son un público objetivo (la existencia de la franja lo sugiere), la experiencia actual es "puedes escribir en español… en un formulario en inglés". Sin una página en español no hay posicionamiento para búsquedas en español ("rotulación de vehículos Tampa", "wrap de carros Tampa") [SUPUESTO sobre el volumen].
- **Posibles soluciones:** (A) Mínimo: subir el aviso en español al hero/cabecera ("Hablamos español") + botón de WhatsApp con mensaje en español. (B) Página `/es/` completa con `hreflang`.
- **Notas de implementación:** `lang="es"` en el `<span>` español del eyebrow.
- **Relacionado:** F-005, F-022
- **Investigar / preguntas:** [PREGUNTA] ¿Qué proporción de clientes habla español? ¿El dueño atiende en español?

### 5.27 Oportunidades

**Ganancias rápidas (esfuerzo S, impacto visible):**
- Conectar `hermeswraps.com` y arreglar el canonical/OG (F-001/F-002).
- Barra fija en móvil: Call · WhatsApp · Quote (F-012).
- Invertir los estilos de los CTA del hero (F-011).
- Texto "adjunta fotos después" + línea en el mensaje (F-015).
- Alternativa visible si el mailto no abre (F-018).
- Oscurecer el dorado de los eyebrows en fondos claros (F-054).
- Botón de pausa en la galería (F-057).
- Opciones vacías "Choose…" en los selects (F-016).
- 404 con marca (F-004).
- Arreglar el texto de la Silverado (F-032).
- Cloudflare Web Analytics + eventos de clic en tel/WhatsApp/email (F-009).

**Apuestas más grandes:**
- Páginas por servicio + página en español (F-005, F-038).
- Programa de reseñas (Google Business Profile) + sección de reseñas reales (F-024).
- Caso de estudio comercial/flota (F-028).
- Sección del dueño: foto, nombre, historia (F-025).
- Rangos de precio publicados (F-014).
- Envío del formulario por el servidor con subida de fotos a R2 (F-015/F-018) — cambiaría el aviso de privacidad.

**Experimentos (hipótesis, sin cifras inventadas):**
- H1: "Si el CTA primario del hero es 'Get a quote', aumentan los clics al formulario." (requiere F-009)
- H2: "Con un botón fijo de WhatsApp en móvil, aumentan los contactos desde móvil."
- H3: "Publicar un 'desde $X' reduce los leads de baja calidad sin bajar el total."

**Ideas sueltas:**
- Entregar a cada cliente su vídeo del proceso como "certificado de calidad" (convierte F-036 en un diferenciador real).
- Guía de cuidado del vinilo (PDF/página) como recurso SEO y para después de la venta.
- Antes/después con deslizador para los cambios de color.
- Galería de colores disponibles (muestras 3M) → contenido SEO por nombre de color.
- Enlazar las publicaciones/vídeos de Facebook/TikTok en el sitio (prueba social de actividad reciente).
- QR en el vehículo propio/tarjetas → página con UTM.

### 5.28 Pistas legales / cumplimiento (no es consejo legal)

#### F-078 · Sin política de privacidad; Google Fonts externo; "Nothing is stored" `[VERIFICADO]`
- **Área(s):** Legal, Confianza
- **Qué noté:** No hay política de privacidad ni términos de uso del sitio (los "Terms of service" son condiciones comerciales). El sitio no usa cookies propias ni analítica [VERIFICADO en el HTML], pero carga Google Fonts (envía la IP del visitante a Google). El aviso "Nothing is stored on this website" es correcto hoy [PROBABLE].
- **Dónde:** Footer, `<head>`.
- **Severidad:** Baja · **Esfuerzo:** S
- **Por qué / impacto:** Si se añade analítica o envío por servidor (F-009, F-015, F-018), hará falta una política de privacidad y quizá aviso de cookies [NO VERIFICADO legalmente; depende de la jurisdicción — Florida/EE. UU.].
- **Posibles soluciones:** Política de privacidad corta; autoalojar las fuentes.
- **Notas de implementación:** —
- **Relacionado:** F-009, F-070, F-035
- **Investigar / preguntas:** [PREGUNTA] ¿Se van a añadir analítica o un envío por servidor?

- Accesibilidad/ADA: los fallos de F-054, F-057, F-055, F-060 son riesgos en EE. UU. [NO VERIFICADO legalmente].
- Uso de la marca "3M" (F-029).
- Permiso de clientes para mostrar sus vehículos/marcas (F-030) — el término "Photos & video" cubre el portfolio, ✔ bien pensado.

### 5.29 Analítica y medición

- Estado: sin analítica (F-009).
- Qué medir para validar este informe:
  - Clics en `tel:`, WhatsApp (form y directo), mailto, "Copy details".
  - Envíos válidos por modo (email/WhatsApp/copy) y errores de validación por campo.
  - Profundidad de scroll (¿cuántos llegan a `#contact`?).
  - Interacción con los vídeos (play, sonido, avance) y la galería (pestañas, lightbox).
  - Fuente del tráfico (Instagram, Facebook, Google, directo) con UTMs en la bio.
  - Core Web Vitals reales en móvil.
  - Proporción de visitas en español (idioma del navegador).

---

## 6. Notas crudas por sección (página única)

### Header
- Escritorio: logo + "HERMES WRAPS" + 5 enlaces + botón dorado; borde inferior blanco al 18 %. Se superpone al vídeo. Bien.
- Móvil: logo 44 px + texto + ☰ 44×44 ✔ (tamaño táctil correcto).
- No es fijo.

### Hero
- Copy: "Owner-operated · Tampa Bay area, Florida" / "One standard. Across every vehicle." / "Vehicle wraps, signs and commercial graphics in premium 3M vinyl, by one accountable specialist, from a single branded vehicle to an ongoing fleet program." / [Watch the process] [Request a quote] / • Premium 3M vinyl • Direct, personal attention • (813) 475-1311
- "accountable specialist" suena a traducción/corporativo.
- Logo grande de 112 px encima del eyebrow (repetido).
- Degradado inferior hacia `--bg` → transición suave ✔.

### Process (vídeos)
- "Follow the process · Síguenos en el proceso" / "See how the work is done." / "Every project is recorded from start to finish…"
- 3 vídeos verticales 9:16 (Corolla roof, Fleet wrap removal, Silverado hood); el del centro activo; laterales inclinados en 3D.
- Pie dinámico: kicker/título/texto ✔ (`aria-live`).
- Fondo negro `rgb(13,9,10)` fijo.

### Work (galería)
- "Selected work" / "Projects by type." / "Real Hermes Wraps projects, labeled by vehicle and service. The showcase moves on its own; choose a type to jump to it, or tap the photo to see it full size."
- 13 fotos; 4 categorías; contador; flechas; "Tap the photo to enlarge".
- Fondo vino oscuro.

### Services
- 6 tarjetas de 3×2 (escritorio), 1 columna (móvil). Fotos con degradado, título y 1 línea.
- "Signs & Vinyl Graphics" con logo + botón.

### Why
- "Why Hermes Wraps" / "Quality with a name behind it." / párrafo "his".
- Cuadrícula de 5 ítems numerados + bloque vino "Personal attention is the standard." + [Start the conversation].

### Terms
- "Terms of service" / "Clear terms before work begins." / 8 términos en 2 columnas con línea dorada / nota final.

### FAQ
- "Before you book" / "Common questions." / 6 preguntas en acordeón con "+".

### Spanish strip
- "¿Prefieres hablar en español?" + [Escribir mensaje].

### Contact
- "Start your project" / "Tell us what you want to wrap." / "Fill in the details and send them by email or WhatsApp. The message arrives ready to read, with everything needed for a quote."
- Service area / Phone / Email / Instagram · Facebook · TikTok.
- Formulario (ver 4.5) + "Your details open in your own email or WhatsApp app. Nothing is stored on this website."

### Footer
- Logo + "Hermes Wraps" + descripción; Explore; Contact; "© 2026 Hermes Wraps · hermeswraps.com · Vehicle wraps, signs & commercial graphics."
- "hermeswraps.com" sin enlace (y el dominio no existe).

### Lightbox
- Overlay negro al 94 %, imagen contenida, título, botón ×.

---

## 7. Diferencias entre el sitio en vivo y el código

- N/A: el código fuente no está en el repo (F-079). Solo se puede decir que el HTML servido contiene CSS de secciones que ya no están en la página (F-072) → la versión actual sale de una versión anterior más completa (precios, reseñas, Instagram, pasos, galería filtrable) [PROBABLE].

---

## 8. Parking lot

- Ideas sin pulir:
  - ¿Combinar Process + Work en una sola sección "Work" con fotos y vídeos y filtro por tipo?
  - ¿Hero con 3 fotos de "resultado" en lugar de un vídeo?
  - ¿"Configurador" simple: elige vehículo + tipo de wrap → rango de precio + CTA?
  - ¿Instagram embebido (o los últimos posts) como prueba de actividad? (había CSS `.instagram-card`).
  - Página "For fleets" con proceso B2B: auditoría de flota → diseño → vehículo piloto → despliegue → mantenimiento/retirada.
- Pensamientos a medio terminar:
  - La estética oscura/vino/dorado se parece más a un estudio de lujo que a un taller local; ¿encaja con el público (particulares de techo negro, pymes)? Puede ser una ventaja (posicionarse premium) o una barrera ("serán caros"). Sin datos → [PREGUNTA].
  - El modelo "mailto/WhatsApp sin backend" es elegante y barato, pero frágil (F-018). Trade-off consciente probablemente.
- Para revisar con más acceso o herramientas:
  - Cabeceras HTTP, pesos de los assets, Lighthouse, axe, teclado real, VoiceOver/TalkBack, modo oscuro, tablet, Safari iOS (autoplay, `e.submitter`), comportamiento sin JS.
  - Perfil de Google Business, reseñas, coherencia NAP en directorios.
  - Que los enlaces de Instagram/TikTok funcionen y estén activos.
- Hipótesis a probar: ver 5.27.

---

## 9. Preguntas para el dueño / equipo

- [PREGUNTA] ¿`hermeswraps.com` está comprado? ¿Cuándo se conecta?
- [PREGUNTA] ¿La URL de workers.dev ya se comparte públicamente (bio, tarjetas, Google)?
- [PREGUNTA] ¿Objetivo principal: flotas/comercial o particulares?
- [PREGUNTA] ¿Se pueden publicar rangos de precio? ¿Por qué se quitó la sección de precios?
- [PREGUNTA] ¿Hay reseñas (Google/Facebook)? ¿Por qué se quitó la sección de reseñas?
- [PREGUNTA] ¿"Hermes" es el nombre del dueño? ¿Quiere aparecer con foto?
- [PREGUNTA] ¿Taller fijo, servicio móvil o ambos? ¿Horario?
- [PREGUNTA] ¿Instalador certificado por 3M? ¿Qué película se usa normalmente? ¿Garantía estándar?
- [PREGUNTA] ¿Qué canal prefiere para recibir leads (WhatsApp/email/llamada)?
- [PREGUNTA] ¿Proporción de clientes hispanohablantes? ¿Atiende en español?
- [PREGUNTA] ¿Permiso de Tampa PC Consultants (y otros) para mostrar sus vehículos?
- [PREGUNTA] ¿Silverado: mismo vehículo en el vídeo y en las fotos?
- [PREGUNTA] ¿Tucson: "Gloss laser flip pink" o "Space Candy Pink"?
- [PREGUNTA] ¿Por qué "Brandon, FL" en el schema?
- [PREGUNTA] ¿Dónde está el código del Worker y quién lo mantiene?
- [PREGUNTA] ¿Los vídeos tienen voz (para subtítulos)?
- [PREGUNTA] ¿El presupuesto es gratis?
- [PREGUNTA] ¿Hay más trabajos fotografiados para ampliar el portfolio (rótulos, chrome delete, flotas)?

---

## 10. Registro de suposiciones

| # | Suposición | Por qué la asumo | Cómo verificarla |
|---|---|---|---|
| 1 | La conversión principal es pedir presupuesto por el formulario/WhatsApp | Estructura de la página y CTAs | Preguntar al dueño; analítica |
| 2 | El tráfico es mayoritariamente móvil y viene de redes | Negocio local con fuerte presencia en Facebook/TikTok/IG | Analítica (F-009) |
| 3 | El workers.dev es (o será pronto) la URL pública | Es lo que se pidió auditar; el dominio no resuelve | Preguntar |
| 4 | El rawHtml de Firecrawl es un DOM serializado, no el archivo fuente literal | URLs absolutizadas, CSS normalizado, `<style rel=stylesheet>` | Ver el código fuente real |
| 5 | El vídeo del hero pesa varios MB | Habitual en vídeos de fondo | Medir el archivo |
| 6 | El enlace de YouTube está oculto con `hidden` | No aparece en las capturas pero sí en el HTML | Inspeccionar en un navegador |
| 7 | Los precios y las reseñas existieron y se quitaron | CSS huérfano con esos nombres | Preguntar / historial |
| 8 | Muchos clientes prefieren WhatsApp | Contexto local/hispano | Analítica / preguntar |
| 9 | Google ignora un canonical a un dominio sin DNS | Comportamiento habitual con canonicals inválidos | Search Console |
| 10 | La negrita 800 de Manrope se sintetiza | No se carga el peso 800 | Inspeccionar el render |

## 11. No se pudo verificar

| Ítem | Por qué no | Qué lo verificaría |
|---|---|---|
| Cabeceras HTTP (seguridad, caché, compresión) | curl bloqueado por el proxy; Firecrawl no las devuelve | `curl -I`, securityheaders.com |
| Peso de imágenes y vídeos | Igual | DevTools / `curl -I` |
| Lighthouse / Core Web Vitals | Sin herramienta | PageSpeed Insights |
| Errores de consola / peticiones fallidas | Script Playwright bloqueado | DevTools / script `capture.mjs` en local |
| Orden de tabulación y foco visible reales | Sin navegador interactivo | Prueba manual con teclado |
| Lector de pantalla | — | VoiceOver / NVDA / TalkBack |
| Modo oscuro (visual) | Capturas en modo claro | Navegador con tema oscuro |
| Tablet 768 px | No capturada | Captura / DevTools |
| Comportamiento del mailto/WhatsApp | No envío formularios (regla) | Prueba manual |
| Contenido de audio de los vídeos | No reproducidos | Ver los vídeos |
| Perfil de Google Business y reseñas | Una sola búsqueda sin resultados de Google | Buscar en Google Maps |
| Destino real de los enlaces sociales | No probados | Abrir cada enlace |
| Redirección http→https y www | Sin curl | `curl -I http://…` |
| Que `hermeswraps.com` no exista de forma permanente | Solo una consulta DNS en un momento | `dig hermeswraps.com`, whois |

## 12. Índice de hallazgos

| ID | Título | Área(s) | Severidad | Esfuerzo | Etiqueta | Dónde |
|---|---|---|---|---|---|---|
| F-001 | Canonical/OG/JSON-LD → dominio que no resuelve | SEO, Técnico | Crítica | S | VERIFICADO | `<head>` |
| F-002 | Sitio en subdominio aleatorio de workers.dev | SEO, Confianza | Crítica | S | VERIFICADO | URL |
| F-003 | Sin sitemap; robots.txt sin directivas | SEO | Media | S | VERIFICADO | raíz |
| F-004 | 404 vacío | Estados, SEO | Media | S | VERIFICADO | rutas inexistentes |
| F-005 | Una sola página: sin páginas de servicio/zona | AI, SEO | Alta | M–L | VERIFICADO | global |
| F-006 | H1/H2 sin palabras clave | SEO | Media | S | VERIFICADO | encabezados |
| F-007 | Meta description de 194 car. | SEO | Baja | S | VERIFICADO | `<head>` |
| F-008 | JSON-LD incompleto/incoherente | SEO local | Media | S | VERIFICADO | JSON-LD |
| F-009 | Sin analítica | Conversión | Media | S | VERIFICADO | global |
| F-010 | Cabeceras sin verificar | Técnico | Nota | S | NO VERIFICADO | HTTP |
| F-011 | CTA primario del hero = vídeos | CTA | Media | S | VERIFICADO | hero |
| F-012 | Sin CTA persistente | Navegación, Conversión | Alta | S–M | VERIFICADO | global/móvil |
| F-013 | Quote escondido en el ☰ | Navegación | Media | S | VERIFICADO | header móvil |
| F-014 | Sin precios | Conversión | Alta | S | VERIFICADO | global |
| F-015 | Sin fotos en el formulario | Formularios | Alta | S/M | VERIFICADO | #contact |
| F-016 | Selects preseleccionados | Formularios | Media | S | VERIFICADO | #contact |
| F-017 | Sin lógica condicional | Formularios | Baja | S | VERIFICADO | #contact |
| F-018 | Mailto falla en silencio | Formularios, Estados | Alta | S | PROBABLE | #contact |
| F-019 | "Copy details" sin siguiente paso | Formularios | Media | S | VERIFICADO | #contact |
| F-020 | `e.submitter` en navegadores antiguos | Formularios | Baja | S | PROBABLE | JS |
| F-021 | Obligatorios sin marcar | Formularios | Baja | S | VERIFICADO | #contact |
| F-022 | WhatsApp solo dentro del formulario | Conversión | Media | S | VERIFICADO | #contact |
| F-023 | 5 etiquetas de CTA distintas | CTA | Baja | S | VERIFICADO | global |
| F-024 | Sin prueba social | Confianza | Alta | S–M | VERIFICADO | global |
| F-025 | Dueño sin nombre/cara | Confianza | Media | S | VERIFICADO | #why |
| F-026 | Sin dirección/horario | Confianza, SEO local | Media | S | VERIFICADO | #contact |
| F-027 | Gmail + sin dominio | Confianza | Media | S | VERIFICADO | contacto |
| F-028 | Mensaje de flotas sin pruebas | Mensajes, Confianza | Alta | M | VERIFICADO | global |
| F-029 | "3M" sin detalle; garantía vaga | Confianza | Media | S | VERIFICADO | hero/why/terms |
| F-030 | Marca/teléfono de un cliente en las fotos | Confianza | Baja | S | VERIFICADO | services/work |
| F-031 | Nombre del color distinto web/FB | Contenido | Baja | S | VERIFICADO | #work |
| F-032 | Silverado contradictoria | Contenido | Media | S | VERIFICADO | process/work |
| F-033 | H1 abstracto | Mensajes | Alta | S | VERIFICADO | hero |
| F-034 | Frases repetidas | Contenido | Baja | S | VERIFICADO | global |
| F-035 | Terms en la nav y antes del contacto | AI, Contenido | Media | S–M | VERIFICADO | #terms |
| F-036 | Afirmaciones absolutas | Contenido | Nota | S | VERIFICADO | process/why |
| F-037 | Chrome delete: ¿servicio o extra? | Contenido | Baja | S | VERIFICADO | services/terms |
| F-038 | Español superficial y tardío | Contenido, SEO | Media | S/M | VERIFICADO | strip/form |
| F-039 | FAQ sin precio/tiempo/garantía | Contenido | Media | S | VERIFICADO | #faq |
| F-040 | "Tap" en escritorio | Contenido | Baja | S | VERIFICADO | #work |
| F-041 | Rótulos sin fotos | Contenido | Media | S | VERIFICADO | services |
| F-042 | Removal/chrome delete fuera de la galería | Contenido | Baja | S | VERIFICADO | #work |
| F-043 | Galería que avanza sola | UX | Media | S | VERIFICADO | #work |
| F-044 | Contador global vs pestañas | UX | Baja | S–M | VERIFICADO | #work |
| F-045 | Fotograma del hero confuso | UI | Media | S–M | VERIFICADO (fotograma) | hero |
| F-046 | Logo ×5, ilegible pequeño | UI | Baja | S–M | VERIFICADO | global |
| F-047 | Pies de foto sobre fotos claras | UI | Baja | S | VERIFICADO | #work |
| F-048 | Tarjetas de servicio no clicables | CTA | Media | S | VERIFICADO | services |
| F-049 | Lightbox sin navegación | Interacciones | Baja | S | VERIFICADO | lightbox |
| F-050 | Vídeos: controles ocultos | Interacciones | Media | S | VERIFICADO | #process |
| F-051 | Botón WhatsApp fuera de la paleta / 3 botones | UI | Baja | S | VERIFICADO | form |
| F-052 | Selects nativos | UI | Baja | S | VERIFICADO | form |
| F-053 | Página muy larga | UX | Nota | — | VERIFICADO | global |
| F-054 | Contraste del dorado en fondos claros | A11y | Alta | S | VERIFICADO | eyebrows |
| F-055 | Sin estilos de foco | A11y | Media | S | VERIFICADO | global |
| F-056 | Sin skip link | A11y | Media | S | VERIFICADO | header |
| F-057 | Movimiento sin pausa | A11y | Alta | S–M | VERIFICADO | hero/carruseles |
| F-058 | `aria-live` en autorrotación | A11y | Media | S | VERIFICADO | #work |
| F-059 | Patrón de pestañas incompleto | A11y | Baja | S | VERIFICADO | #work |
| F-060 | Lightbox sin trampa de foco | A11y | Media | S | VERIFICADO | lightbox |
| F-061 | Puntos de 9 px | A11y | Media | S | VERIFICADO | #process |
| F-062 | Vídeos sin subtítulos/teclado | A11y | Media | S–M | VERIFICADO/NO VERIF. | #process |
| F-063 | Bordes de inputs con contraste bajo | A11y | Media | S | VERIFICADO (aprox.) | form |
| F-064 | Estado del formulario en oscuro 1.98:1 | A11y | Baja | S | VERIFICADO (cálculo) | form |
| F-065 | Menú móvil: Escape/foco/label | A11y | Baja | S | VERIFICADO | header |
| F-066 | Nav en mayúsculas en el HTML | A11y | Baja | S | VERIFICADO | header |
| F-067 | "+" leído en las FAQ | A11y | Baja | S | VERIFICADO | #faq |
| F-068 | Vídeo del hero `preload=auto` | Rendimiento | Alta | S–M | VERIFICADO/NO VERIF. peso | hero |
| F-069 | Imágenes sin srcset/WebP | Rendimiento | Media | S–M | VERIFICADO | global |
| F-070 | Pesos de fuente mal cargados | Rendimiento | Baja | S | VERIFICADO | `<head>` |
| F-071 | CWV sin medir | Rendimiento | Nota | S | NO VERIFICADO | — |
| F-072 | 24 % de CSS muerto | Código | Baja | S | VERIFICADO | CSS |
| F-073 | Reglas sobrescritas | Código | Baja | S–M | VERIFICADO | CSS |
| F-074 | 82 colores literales | Sistema de diseño | Media | M | VERIFICADO | CSS |
| F-075 | Sin escala tipográfica/espaciado | Sistema de diseño | Baja | M | VERIFICADO | CSS |
| F-076 | Restos de plantilla (YouTube "#", comentario) | Código | Baja | S | VERIFICADO | HTML/JS |
| F-077 | Contacto duplicado HTML/JS | Código | Baja | S | VERIFICADO | HTML/JS |
| F-078 | Sin política de privacidad | Legal | Baja | S | VERIFICADO | footer |
| F-079 | Código no está en el repo | Código, Proceso | Media | S | VERIFICADO | repo |
