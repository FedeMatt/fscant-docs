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
  assets/          # shared images, videos, logo
  pdf/             # generated PDFs (gitignored)
  stylesheets/
  en/              # English (default) — /
  it/              # Italian — /it/
  de/              # Deutsch — /de/
  pl/              # Polski — /pl/
  cs/              # Čeština — /cs/ (app code CZ)
```

Plugin: `mkdocs-static-i18n` with `docs_structure: folder` in `mkdocs.yml`.

| App code | MkDocs / Material locale | Folder | URL prefix |
|----------|--------------------------|--------|------------|
| EN | `en` (default) | `docs/en/` | `/` |
| IT | `it` | `docs/it/` | `/it/` |
| DE | `de` | `docs/de/` | `/de/` |
| PL | `pl` | `docs/pl/` | `/pl/` |
| CZ | `cs` | `docs/cs/` | `/cs/` |

**Always translate from `docs/en/`** (never from another locale).

## Adding a locale

1. Copy `docs/en/*.md` → `docs/<locale>/`.
2. Run **App string cross-check**; translate prose per rules below; bold labels from LanguageContext for that app code.
3. In `mkdocs.yml`, add the locale with `BUILD_*` / `*_DEFAULT` env hooks and full `nav_translations`.
4. Extend `scripts/build.sh` `LOCALES` table (pdf name + cover subtitle).
5. Extend `overrides/partials/header.html` language → PDF path map.
6. Video `src`: `/assets/videos/...`; fallbacks: `https://fscant-docs.fscan.com/<locale>/…`.
7. Index PDF: `../pdf/fscant-user-guide.<locale>.pdf` (EN unsuffixed).
8. Extend tests; run `./scripts/build.sh` and pytest.

## Translation rules

### Never translate (see `glossary.md`)

Product names, procedure acronyms, metric labels, presets, file/format names, installer filenames, extension IDs, person names, pathogen names.

### Always translate

Running prose, headings, figure/video captions, nav titles.

### Bold UI labels

Must match the companion app. See **App string cross-check** below.

## App string cross-check (mandatory)

Before translating or polishing any locale, locate the app translation stores and verify bold UI labels against them. Do not invent or “correct” app copy.

1. **Find the stores** under the sibling app frontend (prefer `../fscapp/frontend`, or `/Users/…/fscant/fscapp/frontend`):
   - **Canonical UI strings:** `contexts/LanguageContext.tsx` — object `translations`, fields `EN` / `IT` / `DE` / `PL` / `CZ`.
   - **Error key map only:** `localization/errors.ts` — maps machine/error ids to LanguageContext keys; it does **not** define separate user-facing copy. Resolve display text via LanguageContext.
2. **Map docs locale → app code:** `en`→`EN`, `it`→`IT`, `de`→`DE`, `pl`→`PL`, `cs`→`CZ`.
3. **For every bold UI label** in `docs/<locale>/*.md`, require an exact match to `translations.<key>.<APP_CODE>`. Keep odd app grammar (e.g. DE `Zur Program wechseln`). Allow non-app bold: glossary tokens, `Needs F-SCAN`, installer filenames, macOS/Windows OS paths, Apple `Open Anyway` link text.
4. Re-check after editorial polish so prose changes did not alter UI strings.

## Media paths

- Images: `../assets/images/...`
- Videos: `/assets/videos/...` (custom-domain root; never `/fscant-docs/…`)
- Screenshots/videos may stay English-UI until localized assets exist

## PDF

`scripts/build.sh` loops single-locale PDF passes, installs into `docs/pdf/`, then full site build.

| Locale | File | Cover subtitle |
|--------|------|----------------|
| `en` | `pdf/fscant-user-guide.pdf` | Instruction manual |
| `it` | `pdf/fscant-user-guide.it.pdf` | Manuale di istruzioni |
| `de` | `pdf/fscant-user-guide.de.pdf` | Bedienungsanleitung |
| `pl` | `pdf/fscant-user-guide.pl.pdf` | Instrukcja obsługi |
| `cs` | `pdf/fscant-user-guide.cs.pdf` | Návod k použití |

`site_url` is `https://fscant-docs.fscan.com/`. Never hardcode `/fscant-docs/` in hrefs. Header uses `{{ path | url }}`.

## Checklist

- [ ] Locale folder mirrors all EN page filenames
- [ ] Translated from EN; glossary terms untouched
- [ ] App translation stores located (`LanguageContext.tsx`; note `errors.ts` key map)
- [ ] Bold labels verified against LanguageContext for this locale (app code mapping above)
- [ ] `nav_translations` + `BUILD_*` in `mkdocs.yml`
- [ ] `LOCALES` entry in `scripts/build.sh`
- [ ] Header PDF branch
- [ ] Images/videos/PDF links resolve on locale URLs
- [ ] Language switcher + pytest updated
