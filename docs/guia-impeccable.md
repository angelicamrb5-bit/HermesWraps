# Guía fácil: cómo usar Impeccable en todos tus proyectos

Explicada paso a paso, sin saber programar.

---

## 1. Primero, ¿qué es todo esto? (explicado como un cuento)

Imagina que Claude es un **cocinero** muy bueno.

- Un **proyecto** (como HermesWraps) es una **cocina**. Cada cliente tiene su propia cocina.
- Una **skill** es un **libro de recetas**. Si el libro está en la cocina, el cocinero lo usa.
- **Impeccable** es un libro de recetas de **diseño**: le enseña a Claude a hacer páginas web más bonitas, ordenadas y fáciles de usar.
- Un **comando** es pedirle una receta concreta. Escribes `/impeccable` en el chat y Claude abre ese libro.

El truco importante:

> **El libro solo sirve en la cocina donde lo dejaste.**
> Si lo pones en la cocina de HermesWraps, Claude lo usa en HermesWraps.
> En la cocina de ShipShop no estará, a menos que también lo pongas ahí.

Hay **dos sitios** donde puedes guardar el libro:

| Dónde lo guardas | Qué pasa | Cuándo conviene |
|---|---|---|
| **Dentro de un proyecto** (carpeta `.claude/` del repositorio) | Funciona en ese proyecto, desde cualquier computadora y también en las sesiones en la nube de claude.ai | Quieres que cada proyecto lo tenga siempre, aunque cambies de computadora |
| **En tu computadora** (instalación "global") | Funciona en todos los proyectos que abras **en esa computadora** | Trabajas siempre desde la misma computadora |

---

## 2. Lo que ya hice en HermesWraps

Ya guardé el libro dentro del proyecto HermesWraps:

- `.claude/skills/impeccable/` → el libro de recetas
- `.claude/agents/impeccable-*.md` → 4 ayudantes que Impeccable usa para tareas especiales
- `CLAUDE.md` → una nota que dice: "Claude, usa Impeccable, pero respeta siempre los colores, la frase y el botón de Hermes Wraps"

No instalé los **hooks** de Impeccable (revisiones automáticas cada vez que Claude edita un archivo). Son opcionales, y así todo es más simple. Si un día los quieres, pídeselo a Claude (ver sección 6).

Cuando abras una sesión nueva sobre HermesWraps, el comando `/impeccable` ya aparecerá.

---

## 3. Cómo ponerlo en tus otros proyectos

Elige **UNA** de estas maneras. La más fácil es la A.

### Manera A: pídeselo a Claude (no hace falta tocar código)

1. Abre una sesión de Claude Code sobre el proyecto que quieras (por ejemplo, ShipShop).
2. Escribe esto en el chat, tal cual:

   ```
   Instala Impeccable (https://github.com/pbakaus/impeccable) en este proyecto, igual que lo hiciste en HermesWraps: copia .claude/skills/impeccable y los agentes impeccable-*.md, sin hooks, crea un CLAUDE.md que diga que la skill de marca de este cliente tiene prioridad, y haz commit y push.
   ```
3. Espera a que Claude termine y te diga "listo".
4. Abre una sesión **nueva** sobre ese proyecto. Ya puedes usar `/impeccable`.

Repite esto una vez por cada proyecto. Cada proyecto es una cocina distinta y necesita su propio libro.

### Manera B: desde Claude Code en tu computadora (sirve para todos los proyectos de esa computadora)

Si usas Claude Code instalado en tu computadora (la app de escritorio o la terminal):

1. En el chat de Claude Code escribe:
   ```
   /plugin marketplace add pbakaus/impeccable
   ```
   Así le dices a Claude dónde está la "tienda" de Impeccable.
2. Escribe:
   ```
   /plugin
   ```
3. En el menú que aparece, entra en **Discover**, busca **Impeccable** y pulsa **Install**.
4. Elige instalarlo para tu usuario (todos los proyectos), no solo para uno.
5. Cierra y vuelve a abrir Claude Code.

Desde ahora, en esa computadora, `/impeccable` funciona en cualquier proyecto.

Ojo: esto **no** llega a las sesiones en la nube de claude.ai/code. Para esas, usa la manera A en cada proyecto.

### Manera C: con un comando en la terminal de tu computadora

Solo si te sientes cómoda con la terminal (la ventana negra donde se escriben comandos):

1. Abre la terminal.
2. Escribe y pulsa Enter:
   ```
   npx impeccable install
   ```
3. Te hará preguntas:
   - **¿Qué herramienta usas?** → elige **Claude Code**.
   - **¿Para este proyecto o para todos?** → "global" o "user" = todos los proyectos; "project" = solo la carpeta donde estás.
4. Para actualizarlo más adelante:
   ```
   npx impeccable update
   ```

Necesitas tener **Node.js** instalado (es gratis, en nodejs.org). Si al escribir `npx` te sale "command not found", no lo tienes instalado.

---

## 4. Cómo usarlo, paso a paso

### Paso 1: preséntale tu proyecto (una sola vez por proyecto)

```
/impeccable init
```

Claude te hará preguntas sobre el negocio: quién es el cliente, a quién le vende y qué quiere que haga la gente en la web. Las respuestas se guardan en un archivo llamado `PRODUCT.md`. Es como darle al cocinero la lista de gustos del cliente antes de cocinar.

Para HermesWraps puedes decirle: *"usa la skill hermes-wraps como fuente de verdad para la marca"*.

### Paso 2: pídele cosas con palabras normales

```
/impeccable mejora la página de trabajos, las fotos deben verse ordenadas y completas
```

```
/impeccable revisa la página de reservar consulta y dime qué la hace difícil de usar
```

### Recetas más útiles (comandos)

| Escribe… | Para… |
|---|---|
| `/impeccable` (solo) | Que mire el proyecto y te sugiera qué hacer primero |
| `/impeccable critique` | Que revise el diseño y diga qué mejorar primero |
| `/impeccable audit` | Que busque problemas técnicos (accesibilidad, velocidad…) |
| `/impeccable polish` | Que pula detalles para que se vea terminado |
| `/impeccable layout` | Que ordene mejor dónde va cada cosa |
| `/impeccable typeset` | Que mejore los textos (tamaños, lectura) |
| `/impeccable clarify` | Que los mensajes y botones se entiendan mejor |
| `/impeccable adapt` | Que se vea bien en el móvil |
| `/impeccable quieter` | Que quite ruido visual |
| `/impeccable document` | Que escriba las reglas visuales del proyecto (`DESIGN.md`) |

La lista completa está en https://impeccable.style/docs/

---

## 5. Reglas de oro para tus clientes

1. **La marca del cliente manda.** Impeccable da buenos consejos generales, pero cada cliente tiene su skill de marca (`hermes-wraps`, `shipshop-design`…). Escribe siempre algo como: *"respeta la skill de marca de este cliente"*. En HermesWraps ya lo dice el archivo `CLAUDE.md`.
2. **Un proyecto = una instalación.** Si quieres Impeccable en 5 proyectos, hay que ponerlo 5 veces (manera A), o una vez en tu computadora (manera B), que solo funciona en esa computadora.
3. **Revisa antes de publicar.** Lo que Claude cambie se guarda en una "rama" (una copia de trabajo). La web real no cambia hasta que esa rama se une con la principal (`main`).
4. **Después de usarlo, pide una revisión de marca:** `/quality-insurance` en HermesWraps comprueba que nada se salió de la marca.

---

## 6. Si algo no funciona

| Problema | Qué hacer |
|---|---|
| `/impeccable` no aparece | Abre una sesión **nueva**. Los comandos se cargan al empezar. |
| Dice que falta `PRODUCT.md` | Es normal la primera vez: ejecuta `/impeccable init`. |
| Quieres las revisiones automáticas (hooks) | Pídele a Claude: *"activa los hooks de Impeccable en este proyecto"* |
| Quieres actualizarlo | Pídele a Claude: *"actualiza Impeccable a la última versión desde GitHub"* (o `npx impeccable update` en tu computadora) |
| Quieres quitarlo de un proyecto | Pídele a Claude: *"quita Impeccable de este proyecto"* (borra `.claude/skills/impeccable` y los agentes `impeccable-*`) |
| Algo se ve raro después de un cambio | Abre la web en una ventana privada o de incógnito: a veces el navegador guarda una copia vieja. |

---

**Resumen en una frase:** Impeccable es un libro de recetas de diseño. Ya está en la cocina de HermesWraps. Para tus otras cocinas, abre una sesión en cada proyecto y pídele a Claude que lo instale igual (manera A).
