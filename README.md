# F-SCANT user guide

Public instruction manual for the F-SCANT computer software (macOS and Windows). Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

- **Published site:** https://FedeMatt.github.io/fscant-docs/
- **Sibling app repo (private):** `../fscapp`

## Preview locally

```bash
cd /Users/federicomatteo/Developer/fscant/fscant-docs
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000/

## Deploy

Pushes to `main` that touch `docs/`, `mkdocs.yml`, `requirements.txt`, or the workflow file build and deploy to GitHub Pages. You can also run the **Deploy docs** workflow manually.

In the GitHub repo: **Settings → Pages → Source: GitHub Actions**.

## Media

Screenshots and videos are not all present yet. Drop files into:

- `docs/assets/images/fscant-user-guide/` — see that folder’s README
- `docs/assets/images/connect-the-f-scan-on-mac/` — see that folder’s README
- `docs/assets/videos/` — see that folder’s README
