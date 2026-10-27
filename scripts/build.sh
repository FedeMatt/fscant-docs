#!/usr/bin/env bash
# Build the multilingual site and one PDF per locale.
# mkdocs-to-pdf is not locale-aware with mkdocs-static-i18n, so each PDF is
# generated in a single-locale pass, copied into docs/pdf/ as static assets,
# then the full site is rebuilt (MkDocs copies docs/pdf → site/pdf).
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ -x .venv/bin/mkdocs ]]; then
  MKDOCS=(.venv/bin/mkdocs)
elif command -v uv >/dev/null 2>&1; then
  MKDOCS=(uv run mkdocs)
else
  MKDOCS=(mkdocs)
fi

run_mkdocs() {
  "${MKDOCS[@]}" "$@"
}

PDF_STAGING="$(mktemp -d)"
trap 'rm -rf "$PDF_STAGING"' EXIT
mkdir -p docs/pdf

echo "Building English PDF…"
EN_DEFAULT=true IT_DEFAULT=false \
  BUILD_EN=true BUILD_IT=false \
  ENABLE_PDF_EXPORT=1 \
  PDF_OUTPUT_PATH=pdf/fscant-user-guide.pdf \
  PDF_COVER_SUBTITLE="Instruction manual" \
  run_mkdocs build
cp -f site/pdf/fscant-user-guide.pdf "$PDF_STAGING/fscant-user-guide.pdf"

echo "Building Italian PDF…"
# i18n requires the default locale to build; promote IT to default for this pass only.
EN_DEFAULT=false IT_DEFAULT=true \
  BUILD_EN=false BUILD_IT=true \
  ENABLE_PDF_EXPORT=1 \
  PDF_OUTPUT_PATH=pdf/fscant-user-guide.it.pdf \
  PDF_COVER_SUBTITLE="Manuale di istruzioni" \
  run_mkdocs build
cp -f site/pdf/fscant-user-guide.it.pdf "$PDF_STAGING/fscant-user-guide.it.pdf"

echo "Installing PDFs into docs/pdf/ (static assets for site + serve)…"
cp -f "$PDF_STAGING/fscant-user-guide.pdf" docs/pdf/fscant-user-guide.pdf
cp -f "$PDF_STAGING/fscant-user-guide.it.pdf" docs/pdf/fscant-user-guide.it.pdf

echo "Building EN + IT site…"
EN_DEFAULT=true IT_DEFAULT=false \
  BUILD_EN=true BUILD_IT=true \
  run_mkdocs build

echo "Done → site/ (PDFs at docs/pdf/ and site/pdf/)"
