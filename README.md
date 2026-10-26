# Otixe · Platform manual / Manual de la plataforma

Bilingual architecture and operations documentation for **Pi → Oficinas ↔ Cerebro ↔ Sinapsis**, with **AMA** as the tool-access layer. English is served at the site root; Spanish at `/es/`. Every chapter has a language counterpart.

## Preview / Vista local

Python 3.11+:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.lock.txt
python scripts/check_content.py
mkdocs build --strict
mkdocs serve --dev-addr localhost:8000
```

## Why a separate repository / Por qué otro repo

The platform is larger than its npm extensions. A dedicated documentation repository keeps the architecture, evidence, web interface and operating method versioned together without coupling editorial releases to npm packages. MkDocs Material provides responsive search and navigation; static-i18n pairs Markdown chapters without duplicating navigation code. Markdown and Mermaid remain readable in GitHub.

La plataforma excede las extensiones npm. Un repo independiente mantiene arquitectura, evidencia, interfaz web y método en una misma historia, sin atar revisiones editoriales a publicaciones npm. MkDocs Material aporta navegación y búsqueda responsive; static-i18n vincula capítulos Markdown equivalentes. No requiere backend para leer el manual.

## Publication / Publicación

This handoff is **not published**. The proposed repository is `otixe/plataforma`. The included workflow validates PRs and main; deployment only runs when a maintainer manually selects `publish=true` on main, after enabling GitHub Pages (Actions) and approving the environment. No repository, domain or release is created by a local build.

Esta entrega **no está publicada**. El workflow valida PRs y main. Sólo despliega cuando un responsable habilita Pages (Actions) y selecciona manualmente `publish=true` en main tras la QA. La URL prevista es `https://otixe.github.io/plataforma/`; no es un servicio activo demostrado por esta entrega.

## Content / Contenido

- `docs/en/`, `docs/es/`: ten equivalent chapters, component quickstarts and operational caveats.
- AMA chapter: the design and the cache rule only; **no savings figures** until a representative measurement exists (enforced by the content check).
- `scripts/check_content.py`: bilingual parity, local links and forbidden-data checks.
- `requirements.lock.txt`: exact preview/build dependencies.

No customer information, private deployment configuration, personal agent documents or credential material belongs here. Public code links describe their actual availability; do not promote a planned component to an installable release before its public source exists.
