---
name: fscant-docs-i18n
description: >-
  Translate or add locales for the F-SCANT MkDocs user guide (fscant-docs).
  Use when translating documentation, adding a language folder under docs/,
  updating nav_translations, or syncing bold UI labels with the companion app.
---

# F-SCANT docs internationalization

## When to use

- Adding or updating a locale in this repo (`docs/<locale>/`)
- Translating guide pages or navigation labels
- Checking whether a term must stay in English

## Layout

```
docs/
  assets/          # shared images, videos, logo (never duplicate per locale)
  stylesheets/
  en/              # English (default) — site root /
  it/              # Italian — /it/
  # de/, pl/, cs/  # future
```

Plugin: `mkdocs-static-i18n` with `docs_structure: folder` in `mkdocs.yml`.

| App code | MkDocs / Material locale | Folder | URL prefix |
|----------|--------------------------|--------|------------|
| EN | `en` (default) | `docs/en/` | `/` |
| IT | `it` | `docs/it/` | `/it/` |
| DE | `de` | `docs/de/` | `/de/` |
| PL | `pl` | `docs/pl/` | `/pl/` |
| CZ | `cs` | `docs/cs/` | `/cs/` |

Only enable `build: true` for locales that have real translations. Do not advertise unfinished languages in the switcher.

## Adding a locale

1. Copy `docs/en/*.md` → `docs/<locale>/`.
2. Translate prose per rules below; keep media paths unchanged (`../assets/images/...`, `/fscant-docs/assets/videos/...`).
3. In `mkdocs.yml` under `plugins.i18n.languages`, add the locale with `name`, `build: true`, and `nav_translations` for every English nav title.
4. Set Material UI language via language override `theme.language: <locale>` when needed (Czech = `cs`).
5. Update video fallback absolute links to include the locale prefix (`…/fscant-docs/<locale>/…`).
6. `uv run mkdocs build` and spot-check language switcher, nav, images, videos, search.

## Translation rules

### Never translate (see also `glossary.md`)

Product names, procedure acronyms, metric labels, presets, file/format names, installer filenames, extension IDs, person names, pathogen names.

### Always translate

Running prose, headings, figure/video captions, nav titles, explanatory text around technical terms.

### Bold UI labels

Words in **bold** are on-screen control names. For each bold label, use the string from the companion app for that locale:

`../fscapp/frontend/contexts/LanguageContext.tsx` → `translations.<key>.<APP_CODE>`

Examples (Italian): Settings → **Impostazioni**, Connect → **Connetti**, Manage users → **Gestisci utenti**.

If the app leaves a token untranslated (DIRP, HITS, F-Code, CSV, …), keep it bold and untranslated in the docs too.

## Media paths

- Markdown images from a locale page: `../assets/images/...`
- Raw HTML `<video src>`: `/fscant-docs/assets/videos/...` (site-root absolute so `/it/` depth works)
- Screenshots/videos may stay English-UI until localized assets exist

## PDF

Each built locale gets its own PDF via staged single-locale `mkdocs-to-pdf` passes in `./scripts/build.sh` (also used by CI):

| Locale | File (site root) | Cover subtitle env |
|--------|------------------|--------------------|
| `en` (default) | `pdf/fscant-user-guide.pdf` | `Instruction manual` |
| `it` | `pdf/fscant-user-guide.it.pdf` | `Manuale di istruzioni` |
| future `<locale>` | `pdf/fscant-user-guide.<locale>.pdf` | translated subtitle |

`site_url` is `https://fscant-docs.fscan.com/`. Never hardcode `/fscant-docs/` in PDF (or other) hrefs — that 404s on the custom domain. Header uses `{{ 'pdf/…' | url }}`; index markdown uses `../pdf/…` from locale folders. `build.sh` installs binaries into `docs/pdf/` (gitignored) so `mkdocs serve` can serve them after one build.

Default language keeps the unsuffixed filename. Non-default locales use `fscant-user-guide.<locale>.pdf`.

Wire new locales by extending `scripts/build.sh` with another single-locale PDF pass (`BUILD_*=…`, promote that locale with `*_DEFAULT=true` because i18n requires the default language to build, plus `PDF_OUTPUT_PATH` / `PDF_COVER_SUBTITLE`), then updating the index download link and `overrides/partials/header.html` locale branch. Never run `ENABLE_PDF_EXPORT=1 mkdocs build` with multiple languages enabled — that mixes/overwrites the PDF. Do not switch to unmaintained `mkdocs-with-pdf` without an explicit decision.

## Checklist

- [ ] Locale folder mirrors all EN page filenames
- [ ] Prose translated; glossary terms untouched
- [ ] Bold labels match `LanguageContext.tsx` for that language
- [ ] `nav_translations` complete in `mkdocs.yml`
- [ ] `build: true` only when content is ready
- [ ] Images and videos resolve on locale URLs
- [ ] Language switcher jumps to the same page in the other language
- [ ] Locale PDF generated via `scripts/build.sh`; index + header link to the correct file

## Next locales after Italian

Deutsch (`de`), Polski (`pl`), Čeština (`cs` / app `CZ`).
