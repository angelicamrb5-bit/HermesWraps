# Hermes Wraps — sitio web

Sitio estático de **hermeswraps.com**. Todo lo que se publica está en `public/`.

- `public/index.html` — Inicio (con el video de fondo original del hero)
- `public/work.html` — Trabajos, con filtros y videos del proceso
- `public/book.html` — Reservar consulta gratuita (abre WhatsApp o el correo con la solicitud lista)
- `public/terms.html` — Términos y privacidad
- `public/404.html` — Página no encontrada
- `docs/website-solutions.md` — Documento de soluciones, sección por sección, que guía los cambios

El original de Muse está guardado sin cambios en el primer commit y en el tag `original-muse-v4`.

## Publicar en Cloudflare (cuenta de Hermes)

1. Cloudflare → **Workers & Pages** → **Create** → **Import a repository** → elige este repositorio.
2. Rama de producción: `main` (o la que se fusione). No hace falta comando de build; `wrangler.jsonc` ya indica que se publique `public/`.
3. En el Worker: **Settings → Domains & Routes → Add → Custom domain** → `hermeswraps.com` (y `www.hermeswraps.com`, con redirección a la versión sin www).
4. Activa **Web Analytics** (sin cookies) para el dominio.

## Datos de contacto

Teléfono y WhatsApp: +1 813 475 1311 · Correo: hermeswraps@gmail.com (cambiar por el correo del dominio cuando exista; buscar `hermeswraps@gmail.com` en `public/`).

Los datos pendientes del cliente están marcados en el código como comentarios `[CLIENT TO SUPPLY: …]`; no se muestran en la página.
