# Lo que depende de Hermes

Esta es la parte del plan que solo puede resolver Hermes. Hasta que no estén estos puntos, las tareas que dependen de ellos no pueden empezar. Todavía no se ha ejecutado nada. El plan completo está en `docs/plan-optimizacion-web.md`.

Leyenda: 🔴 bloquea el plan · 🟡 mejora el resultado · ⚪ más adelante

---

## A. Perfil de Google (reseñas)

| # | Qué | Prioridad | Detalle |
|---|---|---|---|
| A1 | **Borrar la reseña de Angelica Bosch** | 🔴 | Google no permite reseñas de quien trabaja con el negocio. Si se dejan, se arriesga el resto de reseñas. La borra Angelica desde su cuenta. |
| A2 | **Pedir reseñas con calma** | 🔴 | 1 o 2 por semana y solo a clientes reales, después de cada entrega. Nada de pedir en tanda a conocidos. 12 reseñas en 3 días ya puede llamar la atención del filtro de Google. |
| A3 | **Pegar las respuestas a las reseñas** | 🟡 | Las redactamos nosotros, una por reseña y en el idioma del cliente. Hermes solo las copia y las pega. |
| A4 | **Revisar y completar el perfil** | 🟡 | Comprobar las categorías: la principal "Vehicle wrapping service" y, como secundarias, letreros o gráficos. Además: lista de servicios, zona de servicio, horario, fotos de trabajos de flota y el atributo **"Se habla español"**. |
| A5 | **Confirmar que se puede citar reseñas en la web** | 🟡 | Son públicas, pero conviene que Hermes esté de acuerdo. Así se pueden citar tal cual con el nombre del cliente. |

## B. Medición (GA4 e Instagram)

Guía paso a paso: `docs/guia-medicion-ga4-instagram.md`

| # | Qué | Prioridad | Detalle |
|---|---|---|---|
| B0 | **Aprobar el nuevo texto de privacidad** | 🔴 | Hoy `terms.html` dice que el sitio usa analítica sin cookies y ninguna cookie publicitaria. GA4 sí usa cookies, así que esa frase tiene que cambiar el mismo día que se instale GA4. La redactamos nosotros y Hermes la aprueba. |
| B1 | **Crear la cuenta de GA4** con la cuenta de Google del negocio | 🔴 | Pasos 1 a 6 de la guía. |
| B2 | **Mandar el ID `G-…` y dar acceso de Editor** | 🔴 | Sin el ID no se puede instalar la medición. No hay que compartir la contraseña. |
| B3 | **Marcar los 3 eventos clave** al día siguiente de instalar | 🔴 | Paso 8 de la guía. |
| B4 | **Poner los enlaces con UTM** en las bios de Instagram, TikTok y Facebook | 🔴 | Los enlaces están en la guía, listos para copiar. |
| B5 | **Revisar los números cada semana** (5 minutos) | 🟡 | Rutina descrita en la guía. |

## C. Catálogo automático desde Drive

| # | Qué | Prioridad | Detalle |
|---|---|---|---|
| C1 | **Crear la carpeta `Nuevos`** en Drive con subcarpetas por tipo | 🔴 | Exactamente las tres categorías que ya usa la web: `commercial/` (vehículos de empresas y flotas), `vehicle/` (carros particulares: color, parciales, chrome delete) y `signs/` (letreros, vidrieras, fachadas). |
| C2 | **Dar acceso a la carpeta** a la cuenta de Google conectada a Claude | 🔴 | Sin acceso, la revisión cada 48 a 72 horas no puede leer las fotos. |
| C3 | **Subir solo fotos terminadas y nítidas**, cada una en su subcarpeta | 🔴 | Las fotos borrosas, repetidas o fuera de subcarpeta se apartan y no se publican. |
| C4 | **Subir los trabajos para empresas que no estén en la web** a `commercial/` | 🟡 | La web ya muestra 9 trabajos comerciales: furgoneta de construcción, grúas, camión de caja, Cybertruck, volquete, Transit de aire acondicionado, tienda de mascotas y otros. Solo faltan los que no aparezcan ahí. |

## D. Prueba de 10 emails a empresas

| # | Qué | Prioridad | Detalle |
|---|---|---|---|
| D1 | **Elegir 2 o 3 de los trabajos comerciales del catálogo como caso de éxito** y decir si se puede nombrar al cliente | 🔴 | Sin permiso se describe genérico, por ejemplo "HVAC van, Brandon FL". |
| D2 | **Comprometerse a hacer maquetas gratis**: el logo del cliente sobre la foto de su vehículo | 🔴 | Es el gancho del email. Hay que fijar en cuánto tiempo la entrega, por ejemplo 48 horas, y cuántas puede hacer por semana. |
| D3 | **Aprobar el texto del email** y enviarlo desde `hermeswraps@gmail.com` | 🔴 | Lo redactamos nosotros. Decidir quién lo envía: Hermes o Angelica, en nombre de Hermes. |
| D4 | **Responder rápido** a quien conteste | 🔴 | Lo ideal es en menos de 24 horas. En B2B, una respuesta lenta pierde el contacto. |
| D5 | **Confirmar qué ofrece a una empresa** | 🟡 | Impresión e instalación propias, instalación en el local del cliente (sí o no), plazos habituales y cuántos vehículos puede hacer por semana. |

## E. Datos del negocio pendientes

Estos datos completan `.agents/product-marketing.md`, que es la ficha que leen todas las skills de marketing.

| # | Qué | Prioridad |
|---|---|---|
| E1 | **Zonas que atiende**: ciudades y hasta qué distancia | 🟡 |
| E2 | **Plazo y condiciones de la garantía** | 🟡 |
| E3 | **Número aproximado de proyectos y vehículos rotulados** | 🟡 |
| E4 | **Consultas al mes hoy y de dónde llegan** (Instagram, boca a boca, Google) | 🟡 |
| E5 | **Seguidores por red** | 🟡 |
| E6 | **Competidores** contra los que más gana o pierde clientes | 🟡 |
| E7 | **Frases reales de clientes** (WhatsApp, llamadas), sobre por qué lo eligieron | 🟡 |
| E8 | **Si se puede publicar contenido también en español**, en redes y en la web | 🟡 |

## F. Más adelante

| # | Qué | Prioridad |
|---|---|---|
| F1 | **Anuncios**: presupuesto mensual, primer canal (Google Search o Meta) y cuánto está dispuesto a pagar por cada consulta | ⚪ |
| F2 | **Visualizador con IA**: retomarlo cuando haya volumen y resultados medidos | ⚪ |
| F3 | **Correo con el dominio** (`@hermeswraps.com`), si la prueba de emails consigue respuestas | ⚪ |

---

## Orden sugerido para Hermes

1. **Esta semana:** A1, A2, B0, B1, B2, C1, C2, D1 y D2.
2. **La semana siguiente:** B3, B4, A3, A4, C4, D3 y D5.
3. **Cuando pueda:** la sección E.
