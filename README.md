# F-SCANT user guide

Public instruction manual for the F-SCANT computer software (macOS and Windows). Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/). PDF export via [mkdocs-to-pdf](https://mkdocs-to-pdf.readthedocs.io/en/stable/).

- **Published site (EN):** https://fscant-docs.fscan.com/
- **IT:** https://fscant-docs.fscan.com/it/
- **DE:** https://fscant-docs.fscan.com/de/
- **PL:** https://fscant-docs.fscan.com/pl/
- **CS:** https://fscant-docs.fscan.com/cs/
- **PDF (EN):** https://fscant-docs.fscan.com/pdf/fscant-user-guide.pdf
- **PDF (IT):** https://fscant-docs.fscan.com/pdf/fscant-user-guide.it.pdf
- **PDF (DE):** https://fscant-docs.fscan.com/pdf/fscant-user-guide.de.pdf
- **PDF (PL):** https://fscant-docs.fscan.com/pdf/fscant-user-guide.pl.pdf
- **PDF (CS):** https://fscant-docs.fscan.com/pdf/fscant-user-guide.cs.pdf
- **Sibling app repo (private):** `../fscapp`

## Languages

Pages live under language folders; shared media stays outside those folders:

```
docs/
  assets/       # shared images, videos, logo
  pdf/          # generated PDFs (gitignored binaries; run build.sh)
  stylesheets/
  en/           # English (default, site root)
  it/           # Italian (/it/)
  de/           # Deutsch (/de/)
  pl/           # Polski (/pl/)
  cs/           # Čeština (/cs/; app code CZ)
```

English is the default at `/`. Further locales: `/it/`, `/de/`, `/pl/`, `/cs/`. See `.cursor/skills/fscant-docs-i18n/`. Always translate from `docs/en/`.

## Preview locally

Requires [uv](https://docs.astral.sh/uv/). Python **3.12+** (mkdocs-to-pdf needs ≥3.11).

```bash
cd /Users/federicomatteo/Developer/fscant/fscant-docs
uv python install 3.12
uv venv --python 3.12
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt
./scripts/build.sh                       # generate docs/pdf/*.pdf (all locales)
uv run mkdocs serve
```

Open http://127.0.0.1:8000/ (and `/it/`, `/de/`, `/pl/`, `/cs/`). PDF downloads need `docs/pdf/*.pdf` — run `./scripts/build.sh` first.

## Build site + PDF

```bash
./scripts/build.sh
# → docs/pdf/fscant-user-guide.pdf (+ .it / .de / .pl / .cs)
# → site/ …
```

The script loops single-locale PDF passes, installs files under `docs/pdf/`, then rebuilds the full multilingual site. Do not run `ENABLE_PDF_EXPORT=1 mkdocs build` with all languages enabled in one pass.

## Tests

```bash
uv run pytest tests/test_pdf_links.py -q
uv run pytest tests/test_pdf_artifacts.py -q   # after ./scripts/build.sh
```

## Deploy

Pushes to `main` that touch docs/config/scripts/tests build (with PDF) and deploy to GitHub Pages.

## Media

**Originals:** `videos-images/` (gitignored). **Published:** `docs/assets/`. Generated PDFs under `docs/pdf/` are gitignored.

Video `src` paths: `/assets/videos/...`. Images from locale pages: `../assets/images/...`.
