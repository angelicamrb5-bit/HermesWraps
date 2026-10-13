# Auditoría web — Hermes Wraps (hermeswraps.com) · primera pasada, versión borrador

> Documento de trabajo en bruto, sin pulir a propósito. Prioriza el detalle sobre el orden. Los duplicados y solapamientos son intencionales.
> Etiquetas de certeza: [VERIFIED] observado · [LIKELY] inferido de evidencia · [ASSUMPTION] suposición · [UNVERIFIED] no se pudo comprobar · [QUESTION] necesita respuesta del dueño
>
> Foco pedido por el usuario: **errores de interacción** y **fotos que se ven estiradas / mal dispuestas**. Esas dos áreas están desarrolladas en §5.3, §5.17 y §2.

## 0. Meta
- Fecha: 2026-10-13
- Auditor: Claude Code (skill website-audit)
- Alcance: **ambos**: sitio en vivo `https://hermeswraps.com/` y el código en `/home/user/HermesWraps` (rama `claude/quirky-planck-lc93ez`, HEAD `495de2e`)
- Páginas revisadas: `/`, `/work` (vista de tipos + catálogos `#commercial`, `#signs`, `#vinyl`, `#vehicle`), `/book`, `/terms`, 404
- Viewports: 320, 390 (móvil), 768 (tablet), 1440 (escritorio), 2560 (pantalla ancha)
- Herramientas usadas:
  - Firecrawl `scrape` del home en vivo (HTML renderizado + enlaces + captura): el HTML en vivo es **idéntico** al `public/index.html` del repo [VERIFIED]
  - Servidor local con URLs limpias (imita Cloudflare Pages: `/work` → `work.html`) + Playwright/Chromium: capturas, consola, solicitudes fallidas, señales de a11y
  - Script propio de interacciones con Playwright: menú móvil, foco, Escape, anclas, CTA fija, filtros, visor de fotos, atrás/adelante del navegador, validación del formulario vacío
  - Python/PIL + ImageMagick: dimensiones reales vs. atributos `width/height`, proporción miniatura vs. original, hojas de contacto
  - ffprobe: dimensiones y pistas de audio de los videos
  - grep/lectura completa de `site.css`, `site.js`, `work.js`, `book.js` y las páginas HTML
- Herramientas NO disponibles / limitaciones:
  - El proxy de red de este entorno devuelve **403** a `curl` hacia hermeswraps.com, así que las **cabeceras HTTP en vivo, las redirecciones http→https / www, el 404 en vivo, robots y sitemap en vivo** están [UNVERIFIED]. Se revisaron las versiones del repo (`public/_headers`, `robots.txt`, `sitemap.xml`, `404.html`).
  - Chromium de Playwright **no decodifica H.264** (no trae códecs propietarios), así que los videos no se reprodujeron en las pruebas; en las capturas se ve el `poster`. El comportamiento de reproducción viene de leer el código.
  - Sin Lighthouse/PSI ni axe: rendimiento y accesibilidad se revisaron a mano.
  - Formularios: **no se envió nada**. Solo se probó el envío vacío (validación local con `preventDefault`) y se anuló `window.open`.
- Fuera de alcance: perfiles sociales y Google Business, envío real por WhatsApp/correo.
- Carpeta de evidencias: fuera del repo, en el scratchpad de la sesión (`…/scratchpad/ev/` y `…/scratchpad/ev/ix/`). Se cita por nombre de archivo. No se añadió nada al repo salvo este informe.

## 1. Para qué creo que sirve el sitio [ASSUMPTION salvo donde se indique]
- Negocio / oferta: instalador de vinilo en Tampa Bay: rotulación de vehículos y flotas, letreros y vidrieras, gráficos comerciales, "all things vinyl" (neveras, calcomanías) [VERIFIED copy].
- Público: (a) negocios con vehículos de trabajo o flotas, que es el grueso del portafolio (20 de 30 proyectos) [VERIFIED]; (b) particulares con autos (cambio de color, techo, capó) (7 de 30) [VERIFIED]; (c) locales comerciales (2 de 30).
- Conversión principal: "Book a free consultation" → formulario que abre WhatsApp o el correo con el mensaje armado [VERIFIED `book.js`]. Secundarias: llamada, WhatsApp directo, email.
- Preguntas abiertas: ver §9.

## 2. Vista rápida: primeras impresiones sin filtrar
- **Hero de escritorio = mancha borrosa.** El video de fondo es **vertical (720×1280)** y en escritorio se estira a 1440×788 (×2) o a 2560×788 (×3,56). Solo se ve ~30 % del cuadro, ampliado y desenfocado. Es lo primero que se ve, y lo que más "estirado" parece. (F-001)
- En móvil el hero se ve bien, porque la caja (390×691) tiene casi la misma proporción que el video.
- Tarjetas de trabajos: todas las fotos se meten en marcos **horizontales 4:3**. 8 fotos son verticales (3:4 o similar) y pierden **~44 % de la imagen** al recortarse. En "Personal vehicles" son **5 de 7**. La del techo negro del sedán termina mostrando casi solo reflejos. (F-002, F-003)
- Las miniaturas **no están deformadas** técnicamente: la proporción de cada `-800.jpg` coincide con su original y los atributos `width/height` coinciden con el tamaño real [VERIFIED]. La sensación de "estirado" viene de (1) el hero vertical ampliado, (2) los recortes agresivos, (3) varias fotos tomadas muy de cerca o con gran angular (perspectiva exagerada) y (4) el zoom de 1,02 al pasar el mouse. (F-001 a F-004, F-007)
- Una foto del catálogo tiene **un dedo en el encuadre** (grúa "Cash for junk cars", 2.ª foto). (F-005)
- Móvil: la barra fija "Book free consultation" **tapa la barra de controles del video** de proceso. (F-008)
- Las tarjetas de servicio dicen "Explore …", pero toda la tarjeta lleva al **formulario de reserva**: esperas información y te abre un formulario. (F-009)
- El formulario exige **Company** y **Work email**, aunque un cuarto del portafolio son autos particulares. (F-013)
- Diseño general limpio, coherente con la marca, sin errores de consola, sin scroll horizontal ni en 320 px. Buena base.

## 3. Resumen de severidad
| Severidad | Cantidad | IDs |
|---|---|---|
| Critical | 0 | — |
| High | 4 | F-001, F-002, F-008, F-013 |
| Medium | 9 | F-003, F-004, F-005, F-006, F-009, F-014, F-016, F-018, F-021 |
| Low | 9 | F-010, F-011, F-012, F-015, F-017, F-019, F-020, F-022, F-023 |
| Note | 5 | F-007, F-024, F-025, F-026, F-027 |

Problemas principales (orden aproximado, no prioridad final):
1. F-001: hero de escritorio con video vertical ampliado ×2 a ×3,5, borroso e irreconocible.
2. F-002/F-003: fotos verticales recortadas ~44 % en tarjetas 4:3; el sujeto queda cortado.
3. F-008: en móvil, la CTA fija tapa los controles del video de proceso.
4. F-013: el formulario obliga a "Company" y "Work email": fricción o bloqueo para clientes particulares.
5. F-009: "Explore …" en las tarjetas de servicio lleva al formulario, no a información.
6. F-021: la caché de 7 días en `/assets/*` sin nombres versionados puede servir CSS/JS viejos con HTML nuevo tras cada despliegue. Posible fuente de "errores de interacción" que no se reproducen en todos los equipos.

## 4. Inventarios

### 4.1 Páginas / rutas
| URL | Archivo | Estado | Title | H1 | Meta desc | Canonical | Indexable | Notas |
|---|---|---|---|---|---|---|---|---|
| `/` | `public/index.html` | 200 en vivo (Firecrawl) [VERIFIED] | Vehicle Wraps, Fleet Graphics & Signs in Tampa Bay \| Hermes Wraps | Your brand standards, applied exactly. | Sí | `https://hermeswraps.com/` | Sí | HTML en vivo = repo |
| `/work` | `public/work.html` | 200 local; en vivo [LIKELY] 200 | Our Work: Vehicle Wraps & Commercial Graphics in Tampa Bay \| Hermes Wraps | Work measured against our clients' standards. | Sí | `/work` | Sí | Vista por tipos + catálogos por hash |
| `/book` | `public/book.html` | 200 local | (ver archivo) | Book a free consultation | Sí | — | Sí | Header compacto (logo + teléfono), sin navegación |
| `/terms` | `public/terms.html` | 200 local | Terms of Service & Privacy \| Hermes Wraps | Clear terms before work begins. | Sí | — | Sí | |
| 404 | `public/404.html` | 404 local | Page Not Found \| Hermes Wraps | This page isn't here. | — | — | `noindex` [VERIFIED] | Cloudflare Pages lo sirve solo [ASSUMPTION] |

### 4.2 Árbol del sitio vs sitemap.xml vs código
```
/            (Services, Process, About, FAQ = anclas)
├── /work    (#commercial #signs #vinyl #vehicle = estados JS)
├── /book    (?type=vehicle|signs|commercial|vinyl preselecciona)
└── /terms   (#privacy)
404
```
`sitemap.xml` lista `/`, `/work`, `/book`, `/terms` y coincide con el código [VERIFIED repo]. `robots.txt`: Allow all + Sitemap [VERIFIED repo]. Versión en vivo [UNVERIFIED] (403 del proxy).

### 4.3 Navegación
| Ubicación | Etiqueta | Destino | ¿Funciona? | Notas |
|---|---|---|---|---|
| Utility | (813) 475-1311 | tel: | Sí | |
| Utility | WhatsApp | wa.me con texto | Sí | `rel=noopener` OK |
| Utility | hermeswraps@gmail.com | mailto | Sí | oculto < 420 px |
| Header | Services / How we work / About / FAQ | `/#…` | Sí; deja la sección a 88 px del borde con un header de 65 px [VERIFIED] | estado activo por IntersectionObserver funciona [VERIFIED] |
| Header | Work | `/work` | Sí | `aria-current` en /work |
| Header | Book a free consultation | `/book` | Sí | |
| Menú móvil | igual que el header + contacto | | Abre, atrapa el foco, Escape cierra y devuelve el foco, bloquea el scroll, se cierra al tocar un enlace [VERIFIED] | Bien hecho |
| Footer · Services | 4 enlaces | **todos a `/#services`** | Sí | F-015 |
| Footer · Company | Work, How we work, About, FAQ, Book | | Sí | |
| Footer · Contact | tel, WhatsApp, email, Instagram, Facebook, TikTok | | Externos [UNVERIFIED] | Facebook usa un ID numérico |

### 4.4 CTAs (home)
| Posición | Etiqueta | Estilo | Destino | Notas |
|---|---|---|---|---|
| Header | Book a free consultation | primario | /book | |
| Hero | Book a free consultation | dorado (dark) | /book | |
| Hero | See our work → | link | /work | |
| Tras Selected work | See the full catalog → / Book a free consultation | link / primario | /work, /book | |
| Tarjetas de servicio ×4 | Explore … → | link que cubre toda la tarjeta | **/book?type=…** | F-009 |
| Story | See the work | secundario | /work | |
| Consultation | Book a free consultation | primario | /book | |
| Closing | Book a free consultation + tel/WA/email | dorado | /book | |
| Móvil fija | Book free consultation | dorado | /book | F-008 |
CTA de reserva repetida 6 veces en el home más la barra fija. Es consistente, aunque mucha repetición.

### 4.5 Formularios (NO enviados)
| Página | Propósito | Campos | Obligatorios | Etiquetas | Validación | Destino | Estados | Notas |
|---|---|---|---|---|---|---|---|---|
| /book | Solicitud de consulta | name, company, email, type, requirements, phone, quantity, timeline | name, **company**, **email ("Work email")**, type, requirements | `<label for>` en todos [VERIFIED] | JS propia; envío vacío → alerta + `aria-invalid` + mensajes + foco en el primer error [VERIFIED] | Abre `wa.me` (por defecto) o `mailto:` | Éxito "Almost done - press send" siempre; "Edit my request" | F-013, F-014. `?type=` preselecciona bien [VERIFIED] |

### 4.6 Componentes repetidos
| Bloque | Dónde | Variantes | Divergencias | ¿Compartir? | Notas |
|---|---|---|---|---|---|
| Header + menú móvil | index, work, terms, 404 | 1 + header compacto en book | copiado a mano en cada HTML | Sí (sitio estático: build simple o include) | Cambiar un enlace implica editar 4 archivos |
| Type tiles | index (h3) y work (h2) | 2 | nivel de encabezado; mismo contenido | Sí | contadores "20/2/1/7 projects" duplicados a mano |
| Project card | work | 1 | — | — | 30 tarjetas escritas a mano |
| Closing band | index, work | 1 | — | Sí | |
| Footer | index, work, terms, 404 completo; book reducido | 2 | | Sí | |
| FAQ (`details`) | index, book | 2 | preguntas distintas, mismo estilo | OK | |

### 4.7 Tokens de diseño en uso
| Tipo | Cantidad | Valores | Casi duplicados | ¿Fuente única? |
|---|---|---|---|---|
| Colores | 16 hex en CSS | paleta `--hw-*` + rgba de overlay | ninguno relevante | Sí, `:root` en `site.css` [VERIFIED] |
| Fuentes | 3 familias | Barlow, Barlow Semi Condensed, IBM Plex Mono | — | Sí |
| Tamaños de texto | ~10 tokens con clamp | | | Sí |
| Espaciado | escala 4–128 | | algunos px sueltos (6px, 10px, 14px) | Mayormente |
| Radios | pill, 12, 8, 8 | | `--hw-radius-input` = `--hw-radius-media` | Sí |
| Sombras | 2 | card, raised | | Sí |
| Breakpoints | 420, 520, 560, 640, 720, 760, 900, 960/961, 1100 | **9 distintos** | 520/560, 720/760, 900/960 | No: cada componente tiene el suyo |
| z-index | 1, 2, 40, 50, 100, 200 | | | ad hoc, pero ordenado |

### 4.8 Stack y terceros
| Cosa | Evidencia | Notas |
|---|---|---|
| HTML/CSS/JS estático, sin build | `wrangler.jsonc` → `pages_build_output_dir: ./public` | |
| Cloudflare Pages | wrangler + `_headers` | |
| Cloudflare Web Analytics | beacon en el HTML en vivo [VERIFIED Firecrawl], no está en el repo | lo inyecta Cloudflare |
| Google Fonts | `<link>` css2 con `display=swap` | 3 familias, ~130–190 KB de fuentes |
| Datos estructurados | JSON-LD `AutomotiveBusiness` | |

### 4.9 Chequeos técnicos
| Chequeo | Resultado | Evidencia | Etiqueta |
|---|---|---|---|
| HTTPS / redirecciones | no comprobable (403 del proxy) | curl | [UNVERIFIED] |
| robots.txt | OK en el repo | `public/robots.txt` | [VERIFIED repo] |
| sitemap.xml | OK, 4 URLs | `public/sitemap.xml` | [VERIFIED repo] |
| 404 | página propia con `noindex` | `public/404.html` | [VERIFIED repo] |
| Cabeceras de seguridad | `_headers`: solo `nosniff` y `Referrer-Policy`; sin CSP, HSTS, Permissions-Policy ni frame-ancestors | `public/_headers` | [VERIFIED repo] / vivo [UNVERIFIED] |
| Caché | `/assets/*` → `max-age=604800` (7 días) sin nombres versionados | `_headers` | [VERIFIED] → F-021 |
| Errores de consola | 0 en /, /work, /book, /terms (3 viewports) | `summary.json` | [VERIFIED local] |
| Solicitudes fallidas | solo `hero-loop.mp4` abortado (Chromium sin H.264) | `summary.json` | artefacto de la herramienta |
| Scroll horizontal a 320 px | ninguno (scrollWidth = 320 en las 4 páginas) | ix2 | [VERIFIED] |
| Lighthouse / PSI | no ejecutado | — | [UNVERIFIED] |

## 5. Hallazgos por área

### 5.1 Primera impresión / test de 5 segundos
- Mensaje claro: qué hacen, dónde y cuál es la CTA. En móvil todo cabe sobre el pliegue [VERIFIED `01-localhost-mobile.png`].
- En escritorio, el fondo del hero no dice nada (ver F-001): no se reconoce ningún vehículo ni trabajo de vinilo.

#### F-001 · El video del hero es vertical y en escritorio se amplía ×2 a ×3,5: se ve borroso y "estirado"  `[VERIFIED]`
- **Área(s):** Primera impresión, UI/imágenes, Rendimiento percibido
- **Qué noté:** `hero-loop.mp4` y `hero-loop-poster.jpg` miden **720×1280 (9:16, vertical)**. El hero de escritorio mide 1440×788 (caja 1,83:1). Con `object-fit: cover` el navegador escala el video a 1440 px de ancho (×2) y muestra solo la franja central de ~31 % de su altura. En 2560 px de ancho el aumento es **×3,56**.
- **Dónde:** `public/index.html:83-85`, `public/assets/site.css:255` (`.hero-media { object-fit: cover }`); capturas `01-localhost-desktop.png`, `ix/hero-2560.png`
- **Evidencia:** ffprobe `hero-loop.mp4 h264,720,1280`; caja medida en Playwright `{"box":[1440,788]}` y `[2560,788]`. A la vista: textura oscura desenfocada sin sujeto reconocible.
- **Por qué es un problema:** es la primera imagen del sitio y transmite "baja calidad" en un negocio que vende calidad de acabado. Es el efecto "estirado/pixelado" más visible.
- **Impacto en el usuario:** no ve ningún vehículo ni trabajo; el fondo distrae en vez de demostrar.
- **Impacto en el negocio:** contradice la promesa "applied exactly" en el primer pliegue (sin cifras).
- **Severidad:** High: afecta a todo visitante de escritorio en la pantalla más importante.
- **Esfuerzo:** S–M [ASSUMPTION]
- **Posibles soluciones:**
  - A) Grabar o conseguir un clip **horizontal 16:9, ≥1920 px** para escritorio y conservar el vertical para móvil: `<video>` con dos `<source media="(orientation: portrait)">` o dos elementos mostrados por media query.
  - B) Escritorio: hero en dos columnas (texto a la izquierda, video vertical a la derecha a su tamaño natural, ~400×710, en un marco). No hace falta material nuevo.
  - C) Escritorio: usar una **foto horizontal nítida** (p. ej. `commercial-suv-side-hero.jpg`, 2000×1500, que ya es la og:image) y dejar el video solo en móvil.
- **Notas de implementación:** el JS de pausa/reproducción (`site.js:57-88`) asume un único `#heroVideo`; con la opción A o C hay que ajustar los selectores. Revisar el `preload` del poster (hoy precarga el poster vertical también en escritorio).
- **Relacionado:** F-002, F-027
- **Investigar / preguntas:** [QUESTION] ¿Existe el clip original en mayor resolución u horizontal?

### 5.2 UX
- Patrones consistentes: botón píldora, link con flecha, estados hover, `focus-visible` con anillo dorado [VERIFIED CSS:115].
- Sorpresas: F-009 (Explore → formulario) y F-014 (éxito sin confirmación real).
- La reproducción automática del fondo tiene botón de pausa y respeta `prefers-reduced-motion` [VERIFIED `site.js:74`]. Bien.

### 5.3 Diseño UI: imágenes y fotos (foco del usuario)

Medición de cada imagen en pantalla vs. su tamaño real (Playwright, 1440 px):

| Imagen | Real | Caja mostrada | % recortado | Dónde |
|---|---|---|---|---|
| display-fridge-desserts-2-800.jpg | 600×800 (vertical) | 282×212 (home) / 4:3 | **44 %** | Tile "Other vinyl" (home y /work) |
| promaster-van-electric-800.jpg | 581×800 | 384×288 | **46 %** | Catálogo comercial |
| transit-van-decor-800.jpg | 600×800 | 384×288 | **44 %** | Catálogo comercial |
| tucson-pink-front.jpg | 1200×1600 | 384×288 | **44 %** | Personal vehicles |
| corolla-roof-angle.jpg | 1200×1600 | 384×288 | **44 %** | Personal vehicles |
| sedan-roof-black.jpg | 1200×1600 | 384×288 | **44 %** | Personal vehicles |
| silverado-hood-angle.jpg | 1200×1600 | 384×288 | **44 %** | Personal vehicles |
| bmw-x1-hood-front.jpg | 1200×1600 | 384×288 | **44 %** | Personal vehicles |
| Resto (22) | 4:3 horizontal | 4:3 | 0 % | |

Proporciones comprobadas: cada `*-800.jpg` tiene exactamente la proporción de su original y los atributos `width/height` del HTML coinciden con los píxeles reales → **no hay deformación por CSS ni por atributos** [VERIFIED `imgcheck.py`]. En la hoja de contactos las ruedas se ven redondas y las proporciones naturales [VERIFIED `sheet1.jpg`, `sheet2.jpg`].

#### F-002 · 8 fotos verticales encajadas en marcos horizontales 4:3 pierden ~44 % de la imagen  `[VERIFIED]`
- **Área(s):** UI/imágenes, Layout, Contenido
- **Qué noté:** todas las tarjetas (`.type-card .media`, `.project-card .media`) fuerzan `aspect-ratio: 4/3` + `object-fit: cover`. Las fotos verticales (3:4) pierden casi la mitad de su altura. En "Personal vehicles" afecta a **5 de 7** tarjetas.
- **Dónde:** `site.css:294-295`, `site.css:311-312`; `work.html` (catálogos `#vehicle` y `#commercial`); `index.html` tile "Other vinyl". Capturas `ix/work-vehicle-desktop.png`, `ix/home-tiles-desktop.png`
- **Evidencia:** tabla anterior (medido con Playwright: `crop44%`).
- **Por qué es un problema:** el auto queda cortado (techo, capó o paragolpes fuera de cuadro) y aparecen encuadres "raros" que se perciben como zoom o estiramiento. Junto con F-001, es la causa más probable de "las fotos lucen estiradas".
- **Impacto en el usuario:** no ve el trabajo completo hasta abrir el visor.
- **Impacto en el negocio:** el portafolio es la prueba principal; los recortes malos restan credibilidad.
- **Severidad:** High: afecta a la sección de prueba y a la mayoría de una categoría.
- **Esfuerzo:** S–M [ASSUMPTION]
- **Posibles soluciones:**
  - A) **Generar recortes 4:3 a mano** de cada foto vertical (`-card.jpg`) eligiendo el encuadre, y mantener la vertical completa solo para el visor. Es lo más limpio y no toca el layout.
  - B) Usar la foto horizontal del mismo proyecto como portada cuando exista. Varias tarjetas tienen 2 fotos; p. ej. `corvette-side.jpg` es 4:3.
  - C) `object-position` por imagen (p. ej. `style="object-position:50% 70%"`) para centrar el sujeto. Es rápido, pero sigue perdiendo el 44 %.
  - D) Rejilla tipo "masonry" o marcos 3:4 para las verticales: cambia el ritmo de la rejilla y puede verse desordenado. No la recomiendo con tan pocas fotos.
- **Notas de implementación:** si se eligen recortes nuevos, conservar 800 px para la tarjeta y 1600 px para el visor (F-006). Los `width/height` del `<img>` deben reflejar el recorte nuevo.
- **Relacionado:** F-003, F-006
- **Investigar:** [QUESTION] ¿Hay versiones horizontales de Tucson, Corolla, Sedan, Silverado y BMW?

#### F-003 · El recorte centrado corta el sujeto: el "Sedan gloss black roof" muestra casi solo reflejos y la nevera de "Other vinyl" no se lee  `[VERIFIED]`
- **Área(s):** UI/imágenes, Contenido
- **Qué noté:** al recortar al centro, la tarjeta del sedán muestra el techo negro reflejando árboles y no se reconoce el auto. El tile "Other vinyl" del home muestra la parte media de la nevera; el diseño envuelto completo (lo que se vende) no se aprecia.
- **Dónde:** `ix/work-vehicle-desktop.png` (fila 2, centro); `ix/home-tiles-desktop.png` (tercer tile)
- **Evidencia:** capturas.
- **Por qué es un problema:** la miniatura no comunica qué trabajo se hizo.
- **Severidad:** Medium
- **Esfuerzo:** S
- **Posibles soluciones:** como F-002 A/B/C. Para "Other vinyl", usar `display-fridge-desserts-1` o `-3`, donde la nevera completa encaja mejor, recortada a 4:3, o una foto horizontal de un decal.
- **Relacionado:** F-002

#### F-004 · Varias fotos de origen están tomadas muy de cerca o con lente gran angular: perspectiva exagerada que se lee como "estirada"  `[LIKELY]`
- **Área(s):** UI/imágenes, Contenido
- **Qué noté:** p. ej. `transit-van-hvac-rear` (Bosch), `wrecker-junk-cars-side`, `wrecker-towing-front`, `tank truck`: cámara baja y cercana, el lado cercano del vehículo se agranda y el lejano se encoge, como en el modo 0,5× del móvil.
- **Dónde:** `public/assets/work/*.jpg`; hoja `sheet2.jpg`
- **Evidencia:** inspección visual. Sin EXIF para confirmar la lente (los JPG redimensionados no conservan metadatos) → [LIKELY], no [VERIFIED].
- **Por qué es un problema:** visualmente parecen deformadas aunque el sitio no las deforme.
- **Severidad:** Medium
- **Esfuerzo:** M (requiere fotos nuevas o una selección distinta)
- **Posibles soluciones:** a futuro, una guía de fotos para el cliente: lente 1× (no 0,5×), 3–5 m de distancia, a la altura de la mitad del vehículo, de lado y en ¾ delantero. Mientras tanto, elegir como portada la foto menos distorsionada de cada proyecto.
- **Investigar:** [QUESTION] ¿Están en Drive los originales con EXIF?

#### F-005 · Una foto del catálogo tiene un dedo en el encuadre  `[VERIFIED]`
- **Área(s):** Contenido, Confianza
- **Dónde:** `public/assets/work/wrecker-junk-cars-side.jpg` (y `-800`), 2.ª foto del proyecto "Wrecker | cash-for-cars graphics"
- **Evidencia:** mancha rosada desenfocada en la esquina inferior izquierda (se ve en el `-800.jpg`).
- **Por qué es un problema:** un descuido visible en un portafolio que vende precisión.
- **Severidad:** Medium
- **Esfuerzo:** S (recortar o quitar la foto)
- **Posibles soluciones:** recortar la esquina, sustituirla o eliminarla del visor (el proyecto tiene otra foto).

#### F-006 · Siete tarjetas cargan la foto de 1600 px (300–600 KB) como miniatura; no hay `srcset`  `[VERIFIED]`
- **Área(s):** Rendimiento, Imágenes
- **Qué noté:** las 22 fotos nuevas tienen versión `-800`; las 7 "antiguas" (`corvette-front`, `tucson-pink-front`, `corolla-roof-angle`, `sedan-roof-black`, `silverado-hood-angle`, `bmw-x1-hood-front`, `commercial-suv-side`) se usan a 1600 px en tarjetas de 384×288. `corvette-front.jpg` (450 KB) es además un tile del home. No hay `srcset`/`sizes` ni WebP/AVIF.
- **Dónde:** `index.html` tile "Personal vehicles"; `work.html` catálogo `#vehicle` y última tarjeta de `#commercial`
- **Evidencia:** `imgcheck.py` → p. ej. `tucson-pink-front.jpg 1200x1600 605KB` mostrada a 384×288.
- **Impacto en el usuario:** el catálogo "Personal vehicles" descarga ~3 MB en fotos en móvil [LIKELY, suma de tamaños].
- **Severidad:** Medium
- **Esfuerzo:** S
- **Posibles soluciones:** generar `-800.jpg` (y opcionalmente `.webp`) para esas 7; añadir `srcset="…-800.jpg 800w, ….jpg 1600w" sizes="(max-width:640px) 100vw, 33vw"`.
- **Relacionado:** F-002 (conviene hacer los recortes y las versiones 800 juntos)

#### F-007 · El hover hace zoom 1,02 a la foto dentro del recorte  `[VERIFIED]`
- **Área(s):** Interacción, Imágenes
- **Dónde:** `site.css:296`, `site.css:313`
- **Qué noté:** al pasar el mouse, la imagen crece un 2 %. Sumado a fotos ya recortadas y ampliadas, refuerza la sensación de "estirado".
- **Severidad:** Note
- **Posibles soluciones:** quitarlo o reemplazarlo por un cambio de borde o sombra.

### 5.4 Layout
- Rejilla de 1200 px, gutters con clamp; sin desbordes a 320 px [VERIFIED].
- En 2560 px el contenido queda centrado a 1200 px y el hero ocupa todo el ancho (agrava F-001).
- `/work`: tres videos de proceso en columnas de 384×640, muy altos en escritorio (F-017).
- Tile grid del home: 4 columnas ≥1100 px, 2 en tablet, 1 en móvil. Cuatro fotos de 358×269 apiladas en móvil: mucho scroll, pero aceptable.

### 5.5 Jerarquía visual
- Una CTA primaria clara por vista. En el hero de escritorio el texto destaca bien sobre el overlay (el fondo borroso hasta "ayuda" al contraste, pero ver F-001).
- Proof strip: "Tampa Bay" como "estadística" se lee raro junto a números. [QUESTION] ¿Sustituir por reseñas cuando existan? (ya hay un comentario en el código)

### 5.6 Navegación
- Funciona bien: anclas con `scroll-padding`, estado activo, menú móvil accesible [VERIFIED].
- `/book` quita la navegación completa (patrón de "landing"); solo queda el logo para volver. Intencional [ASSUMPTION].
- F-015: enlaces de servicios del footer duplicados.

### 5.7 Arquitectura de información
- 4 páginas + anclas. Faltan páginas por servicio (SEO local), "About" con persona/foto y reseñas (ocultas).
- Categorías del catálogo desbalanceadas: 20 / 2 / 1 / 7 (F-016).

### 5.8 Recorridos de usuario
**J1: dueño de flota en escritorio, quiere ver si hacen vans como la suya.**
1. Home → hero borroso (F-001) → baja → tile "Commercial & work vehicles" → /work#commercial (catálogo de 20) → abre el visor → cierra → "Book".
Fricción: el hero no muestra nada; en el catálogo, 2 portadas recortadas. Buen flujo en general.

**J2: particular en móvil con un Tucson, quiere un cambio de color.**
1. Home → "Personal vehicles" → 5 de 7 portadas recortadas (F-002) → Book → el formulario pide **Company** y **Work email** (F-013) → inventa una empresa o abandona [ASSUMPTION sobre el abandono].
Riesgo alto de caída en el formulario.

**J3: visitante móvil que quiere ver el video del proceso.**
1. Home → "How we work" → video → al bajar, la barra fija tapa los controles (F-008) → tiene que mover el scroll para alcanzar play/volumen.

**J4: usuario de teclado en /work.**
Tab a un tile → Enter → foco en el título del catálogo [VERIFIED] → Tab a una tarjeta → Enter abre el visor con foco en "Close" [VERIFIED] → flechas cambian de foto [VERIFIED] → Escape cierra y devuelve el foco al botón [VERIFIED]. Bien.

**J5: hispanohablante.**
"Hablamos español" visible; FAQ y WhatsApp en español [VERIFIED]. El sitio no tiene versión en español. [QUESTION] ¿Qué proporción de clientes es hispanohablante?

### 5.9 Contenido
- 14 marcadores `[CLIENT TO SUPPLY: …]` en comentarios (horarios, tiempo de respuesta, nombre/foto del dueño, áreas, método de color, etc.) [VERIFIED grep]. No se muestran, pero el contenido sigue incompleto.
- F-005 (dedo en la foto), F-016 (categorías delgadas), F-019 ("exigencies").

#### F-016 · Categorías con 1 y 2 proyectos se presentan al mismo nivel que la de 20  `[VERIFIED]`
- **Área(s):** Contenido, AI
- **Dónde:** tiles en home y /work: "Signs & storefronts · 2 projects", "Other vinyl · 1 project"
- **Por qué:** abrir un "catálogo" de 1 elemento se siente vacío y resalta la falta de trabajos.
- **Severidad:** Medium
- **Posibles soluciones:** fusionar "Signs" y "Other vinyl" en "Storefronts & other vinyl" (3 proyectos) hasta tener más; o mostrar las fotos directamente sin la capa "catálogo".

### 5.10 Mensaje
#### F-019 · "We focus on your quality exigencies." suena poco natural en inglés y se repite 4 veces  `[VERIFIED]`
- **Dónde:** hero, closing, footer y /book
- **Por qué:** "exigencies" significa "urgencias o necesidades apremiantes"; parece una traducción literal de "exigencias". Repetido 4 veces llama la atención.
- **Severidad:** Low
- **Posibles soluciones:** [QUESTION] ¿Es un eslogan aprobado por el cliente? Si no: "We work to your quality standards." / "Your standards, met exactly."

### 5.11 CTAs
- Ver 4.4. CTA consistente y repetida.
#### F-009 · Las tarjetas de servicio dicen "Explore …" pero toda la tarjeta lleva al formulario de reserva  `[VERIFIED]`
- **Área(s):** Interacción, CTAs, UX
- **Dónde:** `index.html` tarjetas de servicio (`href="/book?type=…"`); `site.css:381` (`.service-card .text-link::after { position:absolute; inset:0 }` convierte toda la tarjeta en enlace)
- **Qué noté:** el usuario hace clic para "explorar" (espera ver trabajos o detalles) y aterriza en un formulario. Cualquier clic en la tarjeta, incluso para seleccionar texto, navega.
- **Severidad:** Medium
- **Esfuerzo:** S
- **Posibles soluciones:** A) etiqueta honesta: "Request a quote for vehicle wraps →"; B) enlazar a `/work#vehicle` o `#commercial` / `#signs` / `#vinyl` (sí existen catálogos por tipo) y dejar un segundo enlace "Book"; C) quitar el `::after` para que solo el link sea clicable.

### 5.12 Confianza
#### F-018 · Faltan señales de confianza: sin reseñas visibles, sin nombre ni foto del responsable, sin dirección ni horario  `[VERIFIED]`
- **Dónde:** `index.html` bloque `#reviews` con `hidden` (plantilla con `[x.x]`), comentarios `[CLIENT TO SUPPLY]` en Story/footer
- **Por qué:** el texto dice "one person accountable", pero no se dice quién es. Para un negocio nuevo, la persona es la prueba.
- **Severidad:** Medium
- **Posibles soluciones:** foto del instalador trabajando + nombre; enlace a Google Business; 3 reseñas reales cuando existan (ya está el componente).
- Correo @gmail.com (F-024).

### 5.13 Conversión
#### F-013 · El formulario exige "Company" y "Work email": bloquea o desanima a clientes particulares  `[VERIFIED]`
- **Área(s):** Conversión, Formularios
- **Dónde:** `book.html` campos `f-company` (required) y `f-email` (label "Work email", required); mensaje de error "Enter a work email so we can send your consultation details."
- **Evidencia:** envío vacío → errores en name, company, email y requirements [VERIFIED Playwright].
- **Por qué:** 7 de 30 proyectos del portafolio son autos particulares (Corvette, Tucson, Corolla…) y el sitio ofrece "color change", pero un particular no tiene "company" ni "work email".
- **Severidad:** High: obstáculo directo en la conversión principal para un segmento entero.
- **Esfuerzo:** S
- **Posibles soluciones:** Company opcional ("Company (if any)"); "Email" en vez de "Work email"; o preguntar primero "¿Para un negocio o para tu vehículo personal?" y mostrar u ocultar Company.
- **Notas:** `book.js:239-245` (mensajes), `book.js:248-257` (check), `book.html` labels.

#### F-014 · La pantalla de éxito aparece aunque WhatsApp o el correo no se hayan abierto  `[LIKELY]`
- **Área(s):** Conversión, Estados, Interacción
- **Dónde:** `book.js:297-308`
- **Qué noté:** tras validar, se muestra "Almost done - press send" sin saber si la app abrió. En escritorio sin WhatsApp instalado, `wa.me` lleva a una página intermedia; con `mailto:` sin cliente de correo configurado, no pasa nada. Si el navegador bloquea la ventana emergente, el código navega fuera (`location.href = url`) y la pantalla de éxito ni se ve.
- **Por qué:** el usuario cree que envió, cierra la pestaña y no llega nada. No se puede confirmar sin datos [ASSUMPTION sobre la frecuencia].
- **Severidad:** Medium
- **Posibles soluciones:** a corto plazo, en la pantalla de éxito mostrar el texto del mensaje con un botón "Copy" y el teléfono visible ("¿No se abrió? Copia esto y envíalo a…"). A medio plazo, la decisión D5 ya prevista en el código: envío real a un endpoint (Cloudflare Worker → correo).

### 5.14 Accesibilidad
- Puntos fuertes [VERIFIED]: skip link, landmarks, un H1 por página, `lang`, `focus-visible`, menú con focus trap y Escape, `details/summary` para la FAQ, `<dialog>` nativo, errores con `aria-invalid` + `aria-describedby` + alerta `role=alert`, botón de pausa del video, reduced-motion.
- La barra fija oculta tiene `aria-hidden` y `tabindex=-1` cuando no se ve [VERIFIED].
#### F-023 · Enlace en línea "terms of service" con área táctil pequeña  `[VERIFIED]`
- **Dónde:** `index.html` FAQ intro; detectado por `capture.mjs` (`smallTapTargets`)
- **Severidad:** Low
- **Solución:** `padding-block` en enlaces en línea, o aceptar la excepción de WCAG 2.5.8 para enlaces dentro de texto.
- Contraste: no medido con herramienta [UNVERIFIED]. A ojo: el texto muted sobre `--hw-stone` y el dorado sobre marfil parecen correctos.

### 5.15 Móvil
- Sin scroll horizontal en 320–390 [VERIFIED]; CTA a ancho completo; enlaces tel/WhatsApp presentes.
- F-008 (barra fija sobre los controles del video), F-012 (sin swipe en el visor).

### 5.16 Formularios
Ver 4.5, F-013 y F-014. Además:
- `book.js:248` deduce el id del mensaje de error con `el.id.slice(2)`: funciona porque todos los ids siguen el patrón `f-xxx`/`e-xxx`, pero es frágil al renombrar [VERIFIED code]. Nota de código.
- Sin subida de archivos (se envían por WhatsApp o correo), y está explicado en un hint. OK.

### 5.17 Interacciones y movimiento (foco del usuario)

Pruebas automatizadas (Playwright) y resultado:
| Interacción | Resultado | Etiqueta |
|---|---|---|
| Menú móvil: abrir, foco dentro, 12×Tab sigue dentro, Escape cierra y devuelve el foco, scroll bloqueado | OK | [VERIFIED] |
| Menú móvil → enlace `/#faq` | cierra la hoja y FAQ queda a 80 px | [VERIFIED] |
| Nav de escritorio a anclas | sección a 88 px bajo un header de 65 px; estado activo correcto | [VERIFIED] |
| FAQ con Enter | abre | [VERIFIED] |
| CTA fija móvil | aparece tras el hero y se oculta cerca del cierre | [VERIFIED] |
| CTA fija vs controles del video | **la tapa 54 px** | [VERIFIED] → F-008 |
| /work tile → catálogo | hash `#commercial`, 20 tarjetas, foco en el título | [VERIFIED] |
| Filtro a otra categoría | OK | [VERIFIED] |
| "All types of work" | vuelve a los tiles, pero **el filtro queda marcado `aria-pressed=true`** | [VERIFIED] → F-011 |
| Botón Atrás del navegador | restaura `#vehicle` correctamente | [VERIFIED] |
| Carga directa `/work#signs` | abre el catálogo (2) | [VERIFIED] |
| Visor: abrir, flechas, Escape, devolver foco | OK; foto vertical 540×720 y horizontal 960×720 sin deformar | [VERIFIED] |
| Visor en móvil | 367×275, caption y Close OK; **sin swipe** | [VERIFIED] → F-012 |
| Formulario vacío | alerta, mensajes, foco en el primer error | [VERIFIED] |
| `?type=signs` preselecciona | OK | [VERIFIED] |
| Reproducción de videos | no comprobable (Chromium de prueba sin H.264) | [UNVERIFIED] |

#### F-008 · En móvil la barra fija "Book free consultation" tapa los controles del video de proceso  `[VERIFIED]`
- **Área(s):** Interacción, Móvil
- **Dónde:** home `#process` (`.video-card video`) y /work `.video-grid`; `site.css:450-457` (`.sticky-cta` fija abajo, z-index 40)
- **Evidencia:** con el borde inferior del video en el borde de la pantalla: `videoBottom: 834`, `stickyTop: 780` → **54 px solapados**; captura `ix/video-vs-sticky-mobile.png` (la barra cubre justo la franja de controles nativos).
- **Por qué es un problema:** los controles nativos (play, barra de progreso, volumen, pantalla completa) están en el borde inferior del video, debajo de la CTA. Es un error de interacción real en móvil.
- **Severidad:** High: el video de proceso es contenido clave de la sección "How we work".
- **Esfuerzo:** S
- **Posibles soluciones:** A) ocultar la barra mientras un `.video-card` está en pantalla (el IntersectionObserver ya existe, basta con añadir los videos a `ends`); B) ocultarla mientras un video se reproduce; C) dejar margen inferior en `.video-card` igual a la altura de la barra (paliativo).
- **Notas de implementación:** `site.js:91-108`: añadir `$$('.video-card')` a la lista observada.

#### F-010 · Al pausarse un video de proceso, el video del hero se reanuda aunque esté fuera de pantalla  `[LIKELY]`
- **Dónde:** `site.js:118-122` (en `pause` reanuda `hv.play()`) y `site.js:124-128` (el observer pausa los clips al salir de pantalla)
- **Qué noté:** al bajar más allá del video de proceso, este se pausa → el handler `pause` hace `hv.play()` → el hero vuelve a reproducirse fuera de vista. El observer del hero no lo corrige porque solo dispara cuando cambia la intersección. Lo mismo ocurre al cambiar de pestaña (`visibilitychange` pausa los clips → reanuda el hero en una pestaña oculta).
- **Evidencia:** lectura del código; no ejecutado por la limitación de H.264.
- **Severidad:** Low (batería/CPU; no visible)
- **Solución:** en el handler `pause`, reanudar solo si el hero está visible (guardar `heroVisible` desde su IntersectionObserver) y si `!document.hidden`.

#### F-011 · Tras "All types of work" el filtro anterior sigue marcado (`aria-pressed=true`)  `[VERIFIED]`
- **Dónde:** `work.js:159-163` (rama sin categoría no reinicia `aria-pressed`)
- **Evidencia:** `RESET {"pressed":1}`
- **Severidad:** Low (invisible hoy porque los filtros quedan ocultos, pero el estado es incorrecto y los lectores de pantalla lo anuncian si se vuelve a mostrar)
- **Solución:** en `apply('')` poner todos los filtros a `false`.

#### F-012 · El visor de fotos no tiene gesto de deslizar en móvil y carga la foto de 1600 px  `[VERIFIED code]`
- **Dónde:** `work.js:189-222` (solo botones y flechas del teclado)
- **Severidad:** Low
- **Solución:** handlers `touchstart/touchend` con umbral de 40 px; precargar la foto siguiente.

#### F-017 · En /work los tres videos de proceso se muestran como columnas de 384×640  `[VERIFIED]`
- **Dónde:** `site.css:356-360`
- **Qué noté:** en escritorio ocupan más de una pantalla de alto. `process-corolla-roof.mp4` es 480×854 (baja resolución) y pesa 5 MB / 80 s.
- **Severidad:** Low
- **Solución:** limitar `max-height` a ~70vh en escritorio o mostrar el poster con un botón play que abra el video en el `<dialog>`.

### 5.18 Estados: vacío / carga / error / éxito
| Área | Carga | Vacío | Error | Éxito | Otros | Notas |
|---|---|---|---|---|---|---|
| Hero video | poster | — | si autoplay falla → estado "Play" [VERIFIED code] | — | reduced-motion | OK |
| Catálogo /work | imágenes lazy con fondo `--hw-bg-alt` | hash desconocido → vista de tipos [VERIFIED code] | — | — | sin JS: [UNVERIFIED]; `#catalog` está `hidden` en el HTML → **sin JS no se ve el catálogo** [LIKELY] | Nota |
| Visor | sin indicador mientras carga la foto de 1600 px | — | imagen rota no gestionada | — | fallback a `window.open` si no hay `<dialog>` | |
| Formulario | — | — | sí, accesible | ver F-014 | sin estado offline | |
| Reseñas | — | bloque oculto | — | — | — | intencional |

### 5.19 SEO
- Title/description únicos en home y work; canonical; OG; JSON-LD `AutomotiveBusiness`; sitemap y robots OK [VERIFIED repo].
#### F-020 · og:title y og:image iguales en todas las páginas  `[VERIFIED]`
- **Dónde:** `work.html:12-15` (og:title del home), og:image siempre `commercial-suv-side-hero.jpg`
- **Severidad:** Low
- **Solución:** og:title por página; para /work usar una foto de flota.
- Sin páginas por servicio ni por zona (Tampa, St. Pete, Clearwater…) para SEO local. Oportunidad (§5.27).
- Alt text descriptivo y específico [VERIFIED]. Bien.

### 5.20 Rendimiento
- Home móvil: ~0,9 MB de imágenes + 1,7 MB de video + ~190 KB de fuentes [VERIFIED `summary.json`]. Aceptable.
- F-006 (miniaturas de 1600 px), F-017 (video de 5 MB, con `preload="none"`: bien).
- Sin `srcset` ni formatos modernos.
- Lighthouse [UNVERIFIED].

### 5.21 Problemas técnicos
#### F-021 · `/assets/*` se cachea 7 días con nombres de archivo fijos: tras un despliegue, los visitantes recurrentes pueden mezclar CSS/JS viejos con HTML nuevo  `[LIKELY]`
- **Área(s):** Técnico, Interacción
- **Dónde:** `public/_headers` → `/assets/* Cache-Control: public, max-age=604800`; `site.css`, `site.js`, `work.js` y `book.js` sin hash ni `?v=`
- **Qué noté:** el commit `495de2e` cambió `work.js` (+47 líneas) y `site.css` y añadió marcado nuevo (`#types`, `#catalog`, `data-type-reset`). Un navegador con el `work.js` anterior en caché ejecutaría JS viejo sobre HTML nuevo. Ese JS no conoce `#types`/`#catalog`, así que los filtros y el visor podrían fallar o comportarse raro durante hasta 7 días.
- **Evidencia:** cabecera en el repo [VERIFIED]; cabecera efectiva en vivo [UNVERIFIED] (403 del proxy). Que esto explique los errores de interacción que vio el usuario es una hipótesis [ASSUMPTION].
- **Severidad:** Medium
- **Esfuerzo:** S
- **Posibles soluciones:** A) añadir versión en las URLs (`/assets/site.css?v=495de2e`) y subirla en cada despliegue; B) bajar a `max-age=3600, must-revalidate` para CSS/JS y dejar 7 días solo para imágenes y videos; C) renombrar con hash.
- **Investigar:** [QUESTION] ¿Los errores aparecieron en un equipo que ya había visitado el sitio? Probar en ventana privada: si ahí no ocurren, es la caché.

#### F-022 · Cabeceras de seguridad mínimas  `[VERIFIED repo]`
- `_headers` solo define `X-Content-Type-Options` y `Referrer-Policy`. Faltan `Strict-Transport-Security`, `Content-Security-Policy` (o al menos `frame-ancestors`) y `Permissions-Policy`. Cloudflare puede añadir HSTS desde el panel [UNVERIFIED].
- **Severidad:** Low

### 5.22 Calidad del código
- JS pequeño, sin dependencias, en IIFEs con `'use strict'`, con fallbacks (sin IntersectionObserver, sin `<dialog>`) [VERIFIED].
- HTML duplicado entre páginas (header, footer, closing) y 30 tarjetas escritas a mano con contadores manuales "20 projects / 7 projects" → riesgo de desincronización (hoy coinciden: 20+2+1+7 = 30 [VERIFIED]).
- 13 `style=""` inline (book: 5, work: 3) [VERIFIED grep]; 2 `!important` (utilidades, OK).
- 9 breakpoints distintos (ver 4.7).
- Sin lint, tests ni CI. README claro.

### 5.23 Consistencia del sistema de diseño
- Tokens bien centralizados en `:root`; los componentes usan tokens de rol [VERIFIED].
- Divergencias: los type tiles usan `h3` en el home y `h2` en /work (correcto para la jerarquía, pero el CSS duplica selectores `h2, h3`); `.alt-send` redefinido inline en `book.html` (`#editAgain`).

### 5.24 Componentes repetidos
- Ver 4.6. La CTA de reserva aparece 6 veces + barra fija en el home; el eslogan, 4 (F-019).

### 5.25 Páginas / estados / funciones que faltan
- Páginas por servicio y por zona; "About" con persona; reseñas; política de privacidad separada (hoy es un ancla en /terms); versión en español.
- Estado "no se abrió WhatsApp/correo" (F-014). Catálogo sin JS.

### 5.26 Decisiones confusas
- "Explore …" → formulario (F-009).
- "4 services" como estadística en el proof strip.
- Categoría "Personal vehicles" empieza con un UTV de gráficos personalizados (F-026).
- [QUESTION] ¿Por qué el hero conserva el video vertical? El comentario dice "kept by client request": ¿el cliente aceptaría un recorte horizontal o una foto en escritorio?

### 5.27 Oportunidades
- **Quick wins (S):** F-008, F-013, F-009, F-011, F-005, versionar los assets (F-021), `-800` de 7 fotos (F-006), recortes 4:3 a mano (F-002).
- **Mayor alcance:** clip horizontal para el hero (F-001); sesión de fotos con guía (F-004); páginas por servicio y zona; reseñas de Google.
- **Hipótesis para probar:** hacer Company opcional aumenta los envíos de particulares; un hero con un trabajo real visible aumenta los clics en "See our work".

### 5.28 Legal / cumplimiento (no es asesoría legal)
- Terms + privacidad en una página [VERIFIED]. Cloudflare Web Analytics no usa cookies, así que no se requiere banner [LIKELY].
- F-025: matrículas legibles en varias fotos (p. ej. Bosch "Lakeland", grúa) [VERIFIED visual]. [QUESTION] ¿Hay permiso de los clientes para publicar sus vehículos y marcas?

### 5.29 Analítica y medición
- `data-track` en todas las CTAs, pero `window.hwTrack` no está definido: los clics no se registran en ningún sitio [VERIFIED `site.js:12-17`]. Cloudflare Web Analytics solo cuenta páginas vistas.
- Para validar este informe convendría medir: clics en `submit-whatsapp`/`submit-email`, aperturas del visor, reproducciones de video, abandonos del formulario por campo.

#### F-024 · Correo de contacto @gmail.com  `[VERIFIED]` · Note
README y código ya lo marcan como pendiente de dominio propio.

#### F-025 · Matrículas visibles en fotos de clientes  `[VERIFIED]` · Note
Ver 5.28.

#### F-026 · "Personal vehicles" abre con el UTV de gráficos personalizados  `[VERIFIED]` · Note
El primer proyecto de la categoría no es un auto ni un cambio de color típico. Considerar abrir con el Corvette o el Tucson.

#### F-027 · Videos solo en MP4/H.264, sin WebM/AV1 alternativo  `[VERIFIED]` · Note
Los navegadores comunes lo reproducen; Chromium sin códecs propietarios (usado en estas pruebas) no. Bajo impacto real.

## 6. Notas crudas página por página
### `/`
- escritorio: hero borroso (F-001); tiles OK salvo "Other vinyl" (F-003); proceso: video vertical bien proporcionado (461×640 a partir de 480×854); servicios con "Explore" (F-009).
- móvil: hero correcto; la barra fija tapa los controles del video (F-008).
- copy: "We focus on your quality exigencies." ×4.
### `/work`
- tiles → catálogo por hash; filtros; visor bien hecho.
- "Personal vehicles": 5/7 portadas verticales recortadas, la del sedán ilegible.
- videos de proceso altos (F-017).
### `/book`
- formulario claro, accesible; Company y Work email obligatorios (F-013); éxito optimista (F-014).
### `/terms`, 404
- sin problemas notables; 404 con `noindex`.

## 7. Diferencias vivo vs código
- Home en vivo = `public/index.html` de HEAD `495de2e` (Firecrawl). Única diferencia: el beacon de Cloudflare Web Analytics inyectado en vivo [VERIFIED].
- Resto de páginas: [LIKELY] iguales (mismo despliegue); no comprobado una a una.
- Cabeceras en vivo vs `_headers`: [UNVERIFIED].

## 8. Parking lot
- Probar en Safari iOS real: autoplay del hero, `<dialog>`, controles del video bajo la barra fija.
- Lighthouse en vivo cuando haya acceso de red.
- ¿Convertir el catálogo en un JSON + render JS o en un build mínimo (Eleventy) para no editar 30 tarjetas a mano?
- Hoja de contacto de portadas candidatas para elegir los recortes con el cliente.
- Revisar si `commercial-suv-side-hero.jpg` (2000×1500) serviría como hero de escritorio.

## 9. Preguntas para el dueño
- [QUESTION] ¿Qué errores de interacción viste exactamente (página, dispositivo, navegador)? ¿Pasan también en ventana privada? (para descartar F-021)
- [QUESTION] ¿Hay un clip horizontal o de mayor resolución para el hero?
- [QUESTION] ¿Hay fotos horizontales de Tucson, Corolla, Sedan, Silverado y BMW?
- [QUESTION] ¿Aceptan clientes particulares? Si sí, ¿Company opcional?
- [QUESTION] ¿"quality exigencies" es un eslogan fijo?
- [QUESTION] ¿Permiso para publicar matrículas y marcas de clientes?
- Pendientes del código: horario, tiempo de respuesta, nombre y foto del dueño, zonas atendidas, reseñas.

## 10. Registro de suposiciones
| # | Suposición | Por qué | Cómo verificar |
|---|---|---|---|
| 1 | La conversión principal es la consulta por WhatsApp | CTA dominante y `data-send` por defecto | Preguntar / analítica |
| 2 | Los particulares abandonan por Company/Work email | Formulario orientado a empresas | Medir abandonos por campo |
| 3 | Los errores que vio el usuario pueden venir de la caché de 7 días | `_headers` + cambios recientes en JS | Probar en ventana privada / cabeceras en vivo |
| 4 | Algunas fotos son de lente gran angular | Perspectiva visual | EXIF de los originales |
| 5 | 404 servido por Cloudflare Pages | Convención de Pages | Visitar una URL inexistente en vivo |

## 11. No verificado
| Ítem | Por qué no | Qué lo verificaría |
|---|---|---|
| Cabeceras, redirecciones, 404, robots y sitemap en vivo | Proxy 403 a curl | `curl -sIL` desde otra red |
| Reproducción de videos y su interacción (F-010) | Chromium sin H.264 | Chrome/Safari reales |
| Lighthouse / Core Web Vitals | No ejecutado | PSI |
| Contraste exacto | Sin axe | axe / Lighthouse |
| Funcionamiento sin JS de /work | No probado | Desactivar JS |
| Enlaces sociales activos | Fuera de alcance | Abrirlos |

## 12. Índice de hallazgos
| ID | Título | Área(s) | Severidad | Esfuerzo | Etiqueta | Dónde |
|---|---|---|---|---|---|---|
| F-001 | Video vertical del hero ampliado ×2–×3,5 en escritorio | Imágenes, 1.ª impresión | High | S–M | VERIFIED | index.html:83, site.css:255 |
| F-002 | 8 fotos verticales recortadas ~44 % en marcos 4:3 | Imágenes, Layout | High | S–M | VERIFIED | site.css:294,311; work.html |
| F-003 | El recorte centrado corta el sujeto (sedán, nevera) | Imágenes | Medium | S | VERIFIED | work #vehicle, home tiles |
| F-004 | Fotos de origen con gran angular o muy de cerca | Imágenes | Medium | M | LIKELY | assets/work |
| F-005 | Dedo en el encuadre de una foto | Contenido | Medium | S | VERIFIED | wrecker-junk-cars-side |
| F-006 | 7 miniaturas a 1600 px, sin srcset | Rendimiento | Medium | S | VERIFIED | work.html, index.html |
| F-007 | Zoom 1,02 al pasar el mouse sobre fotos recortadas | Interacción | Note | S | VERIFIED | site.css:296,313 |
| F-008 | La CTA fija tapa 54 px de los controles del video en móvil | Interacción, Móvil | High | S | VERIFIED | site.css:450; site.js:91 |
| F-009 | "Explore …" lleva al formulario; toda la tarjeta es enlace | Interacción, CTA | Medium | S | VERIFIED | index.html servicios; site.css:381 |
| F-010 | El hero se reanuda fuera de pantalla al pausar un clip | Interacción | Low | S | LIKELY | site.js:118 |
| F-011 | aria-pressed no se reinicia al volver a los tipos | Interacción, a11y | Low | S | VERIFIED | work.js:159 |
| F-012 | Visor sin swipe en móvil | Interacción, Móvil | Low | S | VERIFIED | work.js:189 |
| F-013 | Company y Work email obligatorios | Conversión, Formularios | High | S | VERIFIED | book.html, book.js |
| F-014 | Éxito mostrado sin confirmar el envío | Conversión, Estados | Medium | S–M | LIKELY | book.js:297 |
| F-015 | Footer: 4 enlaces de servicios al mismo ancla | Navegación | Low | S | VERIFIED | footer |
| F-016 | Categorías de 1 y 2 proyectos | Contenido, AI | Medium | S | VERIFIED | tiles |
| F-017 | Videos de proceso muy altos en /work | Layout | Low | S | VERIFIED | site.css:356 |
| F-018 | Faltan señales de confianza (persona, reseñas) | Confianza | Medium | M | VERIFIED | index.html |
| F-019 | "quality exigencies" poco natural, ×4 | Mensaje | Low | S | VERIFIED | varias |
| F-020 | og:title / og:image repetidos | SEO | Low | S | VERIFIED | work.html:12 |
| F-021 | Caché de 7 días en assets sin versión | Técnico, Interacción | Medium | S | LIKELY | public/_headers |
| F-022 | Cabeceras de seguridad mínimas | Técnico | Low | S | VERIFIED repo | public/_headers |
| F-023 | Enlace en línea con área táctil pequeña | a11y | Low | S | VERIFIED | index.html FAQ |
| F-024 | Correo @gmail | Confianza | Note | S | VERIFIED | todo el sitio |
| F-025 | Matrículas visibles | Legal | Note | S | VERIFIED | fotos |
| F-026 | Personal vehicles abre con un UTV | Contenido | Note | S | VERIFIED | work #vehicle |
| F-027 | Solo MP4/H.264 | Técnico | Note | S | VERIFIED | assets/*.mp4 |
