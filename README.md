# Hermes Wraps — sitio web

Sitio estático de **hermeswraps.com**. Todo lo que se publica está en `public/`.

- `public/index.html` — Inicio (con el video de fondo original del hero)
- `public/work.html` — Trabajos, con filtros y videos del proceso
- `public/book.html` — Reservar consulta gratuita (abre WhatsApp o el correo con la solicitud lista)
- `public/terms.html` — Términos y privacidad
- `public/404.html` — Página no encontrada
- `docs/website-solutions.md` — Documento de soluciones, sección por sección, que guía los cambios

El original de Muse está guardado sin cambios en el commit `144b4e9` ("Add original Hermes Wraps site…").

## Publicar en Cloudflare Pages (cuenta de Hermes)

1. Proyecto Pages `hermeswraps` conectado a este repositorio. Rama de producción: `main`.
2. No hace falta comando de build: `wrangler.jsonc` indica que se publique la carpeta `public/`.
3. **Custom domains** → `hermeswraps.com` y `www.hermeswraps.com` (redirigir www a la versión sin www con una regla de redirección).
4. Activa **Web Analytics** (sin cookies) para el dominio.

## Datos de contacto

Teléfono y WhatsApp: +1 813 475 1311 · Correo: hermeswraps@gmail.com (cambiar por el correo del dominio cuando exista; buscar `hermeswraps@gmail.com` en `public/`).

Los datos pendientes del cliente están marcados en el código como comentarios `[CLIENT TO SUPPLY: …]`; no se muestran en la página.

## Editar el sitio

- `public/index.html` y `public/book.html` se editan a mano.
- `work.html`, `terms.html` y `404.html` se generan: edita `scripts/pages.py` (proyectos, textos) y ejecuta `python3 scripts/build.py` (requiere Pillow).
- El build también agrega `srcset` a las fotos (versión `-800.jpg` + 1600 px) y `?v=<hash>` a CSS/JS para que los navegadores no mezclen versiones.
- Fotos nuevas: guárdalas en `public/assets/work/nombre.jpg` (1600 px) y `nombre-800.jpg` (800 px).
