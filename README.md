# F-SCANT user guide

Public instruction manual for the F-SCANT computer software (macOS and Windows). Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). PDF export via [mkdocs-to-pdf](https://mkdocs-to-pdf.readthedocs.io/en/stable/).

- **Published site:** https://FedeMatt.github.io/fscant-docs/
- **PDF:** https://FedeMatt.github.io/fscant-docs/pdf/fscant-user-guide.pdf
- **Sibling app repo (private):** `../fscapp`

## Preview locally

Requires [uv](https://docs.astral.sh/uv/). Python **3.12+** (mkdocs-to-pdf needs ≥3.11).

```bash
cd /Users/federicomatteo/Developer/fscant/fscant-docs
uv python install 3.12
uv venv --python 3.12
uv pip install -r requirements.txt
uv run mkdocs serve
```

Open http://127.0.0.1:8000/fscant-docs/ (the path matches the GitHub Pages project URL).

Header chrome: English language selector, light/dark toggle, no GitHub repo chip. Brand primary is `#1F40C8`.

## Build PDF

PDF generation is off during `mkdocs serve`. Enable it for a full build:

```bash
ENABLE_PDF_EXPORT=1 uv run mkdocs build
# → site/pdf/fscant-user-guide.pdf
```

## Deploy

Pushes to `main` that touch `docs/`, `mkdocs.yml`, `requirements.txt`, `templates/`, or the workflow file build (with PDF) and deploy to GitHub Pages. You can also run the **Deploy docs** workflow manually.

In the GitHub repo: **Settings → Pages → Source: GitHub Actions**.

## Media

Screenshots and videos are not all present yet. Drop files into:

- `docs/assets/images/fscant-user-guide/` — see that folder’s README
- `docs/assets/images/connect-the-f-scan-on-mac/` — see that folder’s README
- `docs/assets/videos/` — see that folder’s README
