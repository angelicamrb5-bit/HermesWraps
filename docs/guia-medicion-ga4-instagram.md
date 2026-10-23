# Guía: medir la web de Hermes Wraps (GA4 + Instagram)

Para: Hermes. Tiempo: unos 20 minutos. Costo: $0.

## Qué es y para qué sirve

Google Analytics 4 (GA4) es gratis y cuenta cuántas personas visitan hermeswraps.com, de dónde llegan (Instagram, Google, WhatsApp, directo) y qué hacen. Las tres acciones que importan:

1. **Envió una cotización** desde el formulario.
2. **Tocó WhatsApp.**
3. **Tocó llamar.**

El visitante no ve nada distinto: no aparece ningún banner ni cambia el diseño. Lo único que cambia es una frase de la sección de privacidad de `terms.html`, que hoy dice que no se usan cookies. Además, cuando Hermes empiece con anuncios, Google Ads usa esta misma cuenta para saber qué anuncio trajo cada cliente.

## Reparto de tareas

| Quién | Qué |
|---|---|
| Hermes | Crear la cuenta (pasos 1 a 6) y dar acceso. La cuenta tiene que ser **suya**, porque es del negocio. |
| El editor de la web | Pegar el código en el sitio y configurar las tres acciones. |
| Hermes, después | Marcar las tres acciones como "eventos clave" (paso 8). |

## Pasos para Hermes

1. Entrar en **analytics.google.com** con la cuenta de Google del negocio, la misma del perfil de Google Maps si es posible.
2. Pulsar **Empezar a medir** (o **Admin → Crear → Cuenta**).
   - Nombre de la cuenta: `Hermes Wraps`.
   - Dejar las casillas de compartir datos como vienen y pulsar **Siguiente**.
3. **Crear propiedad:**
   - Nombre: `hermeswraps.com`
   - Zona horaria: **Estados Unidos – Hora del Este (New York)**
   - Moneda: **Dólar estadounidense (USD)**
4. **Detalles del negocio:**
   - Sector: *Automoción* o *Servicios empresariales*.
   - Tamaño: *Pequeño*.
   - Objetivo: **Generar clientes potenciales** ("Generate leads").
5. **Plataforma: Web.**
   - URL: `https://hermeswraps.com`
   - Nombre del flujo: `Web Hermes Wraps`
   - Dejar activada la **Medición mejorada**: ya cuenta sola los clics a enlaces externos, como WhatsApp.
   - Pulsar **Crear flujo**.
6. Copiar el **ID de medición**. Empieza por `G-` (por ejemplo `G-AB12CD34EF`) y aparece arriba a la derecha de la pantalla del flujo. **Enviárselo al editor.**
7. Dar acceso al editor:
   - Ir a **Admin → Gestión del acceso a la propiedad → + → Añadir usuarios**.
   - Escribir su correo y elegir el rol **Editor**.

> En ningún momento hay que pasar la contraseña de Google. Basta con el ID `G-…` y el acceso de Editor.

## Lo que hace el editor (el visitante no lo nota)

- Pega el código de GA4 en todas las páginas de `public/` y actualiza la frase de privacidad de `terms.html`, ya aprobada por Hermes.
- Crea tres eventos:
  - `generate_lead`: solo cuando el formulario **se envió con éxito**, no al pulsar el botón.
  - `click_whatsapp`: al tocar cualquier enlace a `wa.me`.
  - `click_call`: al tocar cualquier enlace `tel:`.
- Comprueba en **Admin → DebugView** que los tres eventos llegan.

## Paso 8 para Hermes (al día siguiente)

Ir a **Admin → Eventos** (o **Eventos clave**) y activar la estrella o el interruptor de **evento clave** en `generate_lead`, `click_whatsapp` y `click_call`. Desde ahí GA4 cuenta cada uno como un cliente potencial.

## Dónde mirar los resultados

| Pregunta | Dónde en GA4 |
|---|---|
| ¿Cuánta gente entró esta semana? | **Inicio**, o **Informes → Tiempo real** para verlo en el momento |
| ¿De dónde vienen? | **Informes → Adquisición → Adquisición de tráfico**, columna *Fuente/medio de la sesión* |
| ¿Cuántos pidieron cotización, escribieron o llamaron? | **Informes → Interacción → Eventos clave** |
| ¿Qué canal trae más clientes potenciales? | En *Adquisición de tráfico*, añadir la columna **Eventos clave** |

---

## Instagram: saber cuántas visitas vienen de ahí

**El problema:** Instagram abre los enlaces en su propio navegador y a menudo no avisa de dónde viene la visita. Sin una etiqueta, GA4 la cuenta como "directo" y no se sabe que vino de Instagram.

**La solución** es usar enlaces con etiqueta UTM. Son el mismo enlace con información extra al final. No cambian la página y no rompen nada.

### Enlaces listos para copiar

| Dónde | Enlace |
|---|---|
| Bio de Instagram | `https://hermeswraps.com/?utm_source=instagram&utm_medium=social&utm_campaign=bio` |
| Sticker de enlace en una historia | `https://hermeswraps.com/book.html?utm_source=instagram&utm_medium=social&utm_campaign=historia&utm_content=NOMBRE-DEL-TRABAJO` |
| Bio de TikTok | `https://hermeswraps.com/?utm_source=tiktok&utm_medium=social&utm_campaign=bio` |
| Facebook | `https://hermeswraps.com/?utm_source=facebook&utm_medium=social&utm_campaign=bio` |
| Mensaje de WhatsApp que se reenvía | `https://hermeswraps.com/work.html?utm_source=whatsapp&utm_medium=referral&utm_campaign=compartido` |

Reglas:
- Todo en minúsculas y sin espacios. Usar guiones, por ejemplo `utm_content=van-plomeria-brandon`.
- Cambiar `utm_content` en cada historia o reel promocionado. Así se sabe qué video trajo la visita.
- No poner etiquetas UTM en enlaces internos de la web, solo en los que se publican fuera.

### Qué mide cada herramienta

| Herramienta | Qué dice |
|---|---|
| **Estadísticas de Instagram**, en la app: *Panel profesional → Estadísticas* | Reproducciones de cada reel, visitas al perfil y **toques en el enlace** |
| **GA4** | Cuántas de esas personas **llegaron de verdad a la web** y cuántas pidieron cotización, escribieron o llamaron |

Si Instagram dice 40 toques en el enlace y GA4 muestra 30 visitas desde `instagram / social`, todo está bien. Siempre se pierde una parte cuando alguien cierra la página antes de que cargue.

### Revisión semanal (5 minutos)

1. En Instagram: anotar las reproducciones de los reels de la semana y los toques en el enlace.
2. En GA4 → *Adquisición de tráfico*: anotar las visitas desde `instagram / social`.
3. En GA4 → *Eventos clave*: anotar las cotizaciones, los WhatsApp y las llamadas que vinieron de Instagram.
4. Comparar con la semana anterior. Al mes se ve qué tipo de reel trae más clientes, no solo más reproducciones.

---

## Más adelante: cuando empiecen los anuncios

- **Google Ads:** en GA4, ir a **Admin → Vinculación de productos → Google Ads** y vincular la cuenta. Los tres eventos clave se importan como conversiones.
- **Meta (Instagram y Facebook):** hay que añadir el *píxel de Meta*. Es otro código invisible que pega el editor.
- No hace falta rehacer nada de esta guía. Todo se monta sobre ella.
