# Investigación: ideas para optimizar la web de Hermes Wraps

Fecha: 22 de octubre de 2026. Solo investigación y plan; no se modificó código.

Contexto revisado del repo: `scripts/` (build.py, pages.py, enhance.py, cutouts.py), `public/assets/work.js` y `worker/src/index.js`.

**Sobre X:** las herramientas de búsqueda casi no indexan publicaciones de X. Se buscó con `site:x.com` en las tres ideas y no apareció ningún post concreto. Lo que sigue viene de documentación oficial, blogs técnicos y productos ya lanzados. Si hay hilos de X guardados, conviene revisarlos uno por uno.

---

## 1. Catálogo que se actualiza solo desde Drive

**Así funciona hoy:** las fotos están en Drive (`G:/My Drive/Hermes Wraps/`). `enhance.py` y `cutouts.py` las retocan, el catálogo es una lista escrita a mano en `scripts/pages.py` y `build.py` genera `work.html`. Al hacer merge a la rama principal, Cloudflare Pages publica el sitio.

**Cómo hacerlo de la forma más eficaz:**

- **Una Routine de Claude Code en la nube.** Corre aunque la computadora esté apagada, puede leer Drive y hacer push a ramas `claude/…`. Límites: se puede programar como máximo una vez por hora, hay un tope de ejecuciones diarias según el plan (Pro 5, Max 15) y además puede arrancarse con una llamada HTTP.
- **Lo más eficiente no es revisar cada hora.** Un Google Apps Script pequeño en el Drive de Hermes mira la carpeta "Nuevos" cada 15 minutos (gratis). Solo cuando aparece una foto, llama a la Routine. Así no se gastan ejecuciones ni tokens en revisiones que no encuentran nada.
- **Lo que haría la Routine:** descargar la foto, correr `enhance.py`, agregar la entrada en `pages.py`, correr `build.py` y abrir un PR. Ese PR **no** se publica solo: se aprueba a mano y después corre `impeccable-qa`. Eso protege la marca.
- **Punto a resolver antes:** cada foto necesita título, categoría y texto alternativo. Lo más fiable es que Hermes nombre el archivo o la subcarpeta con el tipo de trabajo (por ejemplo `commercial/ford-transit-plomeria.heic`). La Routine redacta el resto con la voz de la skill `hermes-wraps`.
- **Descartado:** los webhooks nativos de Drive (`changes.watch`). Caducan cada 7 días, hay que renovarlos y no avisan cuando entra un archivo nuevo a una carpeta, solo cuando algo cambia. Dan más trabajo que el Apps Script y no aportan nada extra.

## 2. Skills de marketing que mejoran el sitio sin tocar la UX

Ordenadas por impacto real y bajo riesgo:

1. **`conversion-tracking` + `analytics`.** Medir envíos del formulario de cotización, clics a WhatsApp y llamadas. Sin esto no se puede saber si las demás mejoras funcionan. Solo agrega eventos, no cambia nada visible.
2. **`schema` + `ai-seo`.** Revisar y ampliar el JSON-LD que ya está en `index.html` (LocalBusiness, Service, reseñas) y agregar `llms.txt` para que ChatGPT, Gemini o Perplexity citen a Hermes cuando alguien pregunte "wrap shop near me". Cambios invisibles para el visitante.
3. **`cro` en modo solo auditoría.** Informe con recomendaciones para `book.html` y el catálogo. Se decide qué aplicar, siempre pasando antes por `hermes-wraps` y `quality-insurance`.
4. **`directory-submissions` (Google Business Profile).** Todo fuera del código y pesa mucho en el SEO local.
5. **Más adelante, `programmatic-seo`:** páginas por servicio y ciudad ("fleet wraps [ciudad]"). Crea páginas nuevas, así que conviene dejarlo para cuando las métricas del punto 1 estén funcionando.

## 3. Ver el wrap o sticker sobre el carro del cliente

**Sí se puede, y ya existe.** Wrap Up! (2wrap.com) usa catálogos reales de 3M e Inozetek y tarda menos de un minuto. wrapmyride.ai es un visualizador que se inserta en la web del taller. Visualizee devuelve el resultado en unos 10 a 15 segundos y respeta el ángulo y las líneas del carro.

**Tres caminos:**

| Opción | Costo | Control de marca | Fidelidad |
|---|---|---|---|
| A. Insertar un servicio de terceros (wrapmyride) | Suscripción | Bajo | Buena en cambio de color |
| B. Propio: Worker + modelo de imagen (Gemini "Nano Banana") | ~$0.02–0.04 por imagen | Total | Muy buena en color; regular con logos y textos |
| C. Híbrido: B para color + montaje real del sticker | Más desarrollo | Total | La mejor para stickers y gráficos |

**Hasta qué punto funciona:**

- Para **cambio de color o acabado** (mate, satinado, cromo) los resultados ya son muy realistas.
- Para **un sticker o logo específico**, los modelos de imagen todavía deforman letras y logos. Por eso conviene la opción C: recortar el carro y deformar el sticker según la perspectiva de la foto, la misma técnica que `cutouts.py` ya usa con BiRefNet.
- Las condiciones del cliente (luz, perfil, terreno) mejoran mucho el resultado. Lo ideal: foto de 3/4 o de lado, luz de día y el carro completo en el encuadre.
- Las guías de prompts indican que describir el material con detalle (tipo de vinilo, brillo, cómo cae la luz) da resultados realistas en unas 8 de cada 10 imágenes, contra 3 de cada 10 con prompts simples.
- **Como herramienta de venta:** pedir WhatsApp o email antes de mostrar el resultado lo convierte en una forma de conseguir contactos que alimenta `book.html`.
- **Riesgos:** costo por abuso (se controla con Turnstile, límite por IP y fotos borradas a las 24 horas) y expectativa del cliente (avisar que es una aproximación).

## Orden recomendado

1. **Idea 2, puntos 1 y 2:** lo más barato y con resultados inmediatos.
2. **Idea 1:** primero el Apps Script, después la Routine con PR y luego QA.
3. **Idea 3, una prueba antes de construir nada:** pasar unas 20 fotos reales del catálogo por Gemini con 2 o 3 prompts fijos (solo color, y color + sticker) y ver la calidad. Si el color sale bien y los stickers no, se confirma la opción C. La prueba cuesta menos de $1 en uso de la API.

Skills por parte: `conversion-tracking` / `schema` / `ai-seo` con `hermes-wraps` para la idea 2, y `free-tools` + `cro` + `hermes-wraps` para la idea 3 (`free-tools` trata justamente sobre herramientas interactivas para conseguir clientes).

## Fuentes

- [Claude Code Routines (guía)](https://computingforgeeks.com/claude-code-routines-setup/) · [Lanzamiento de Routines](https://codex.danielvaughan.com/2026/04/14/claude-code-routines-launch/)
- [Drive push notifications (Google)](https://developers.google.com/workspace/drive/api/guides/push?hl=en) · [Caducidad de los webhooks de Drive](https://fast.io/resources/google-drive-webhook/) · [Apps Script + Drive (Labnol)](https://Labnol.org/google-drive-push-notifications-230826)
- [Wrap Up! / 2wrap.com](https://www.techdogs.com/tech-news/ein-presswire/2wrapcom-becomes-first-wrap-shop-to-provide-customers-with-an-ai-tool-that-visualizes-wrap-colors-on-their-own-vehicle) · [wrapmyride.ai](https://www.accessnewswire.com/newsroom/en/automotive/wrap-shops-are-calling-this-the-most-powerful-sales-tool-ever-built-1112004) · [Visualizee](https://visualizee.ai/try/car-wrap-visualizer) · [CarConceptsAI](https://topai.tools/t/carconceptsai) · [Visualizadores IA de wraps (Metro Restyling)](https://metrorestyling.com/blogs/news/ai-and-car-wrapping-how-technology-is-changing-the-game)
- [Prompts de Nano Banana para carros](https://morphed.app/blog/nano-banana-prompts-for-cars) · [Precio de Gemini 2.5 Flash Image](https://pricepertoken.com/image/model/google-gemini-2-5-flash-image) · [Estado del modelo (preview deprecado)](https://llmgateway.io/models/gemini-2.5-flash-image-preview)
- [Marketing Skills de Corey Haines](https://aiengineerguide.com/til/marketing-skills-for-claude-code/)
