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

# locale|pdf_basename|cover_subtitle
# Default language (en) keeps unsuffixed PDF name.
LOCALES=(
  "en|fscant-user-guide.pdf|Instruction manual"
  "it|fscant-user-guide.it.pdf|Manuale di istruzioni"
  "de|fscant-user-guide.de.pdf|Bedienungsanleitung"
  "pl|fscant-user-guide.pl.pdf|Instrukcja obsługi"
  "cs|fscant-user-guide.cs.pdf|Návod k použití"
)

ALL_CODES=(en it de pl cs)

unset_locale_env() {
  local code
  for code in "${ALL_CODES[@]}"; do
    local upper
    upper=$(echo "$code" | tr '[:lower:]' '[:upper:]')
    unset "BUILD_${upper}" || true
    unset "${upper}_DEFAULT" || true
  done
}

# Export BUILD_*=false for all, BUILD_$1=true; *_DEFAULT=false except $1=true
activate_only() {
  local only=$1
  local code upper
  for code in "${ALL_CODES[@]}"; do
    upper=$(echo "$code" | tr '[:lower:]' '[:upper:]')
    if [[ "$code" == "$only" ]]; then
      export "BUILD_${upper}=true"
      export "${upper}_DEFAULT=true"
    else
      export "BUILD_${upper}=false"
      export "${upper}_DEFAULT=false"
    fi
  done
}

activate_all_en_default() {
  local code upper
  for code in "${ALL_CODES[@]}"; do
    upper=$(echo "$code" | tr '[:lower:]' '[:upper:]')
    export "BUILD_${upper}=true"
    if [[ "$code" == "en" ]]; then
      export "${upper}_DEFAULT=true"
    else
      export "${upper}_DEFAULT=false"
    fi
  done
}

PDF_STAGING="$(mktemp -d)"
trap 'rm -rf "$PDF_STAGING"' EXIT
mkdir -p docs/pdf

for entry in "${LOCALES[@]}"; do
  IFS='|' read -r code pdf_name subtitle <<<"$entry"
  echo "Building PDF for ${code} → ${pdf_name}…"
  activate_only "$code"
  export ENABLE_PDF_EXPORT=1
  export PDF_OUTPUT_PATH="pdf/${pdf_name}"
  export PDF_COVER_SUBTITLE="$subtitle"
  run_mkdocs build
  cp -f "site/pdf/${pdf_name}" "$PDF_STAGING/${pdf_name}"
done

echo "Installing PDFs into docs/pdf/…"
for entry in "${LOCALES[@]}"; do
  IFS='|' read -r _ pdf_name _ <<<"$entry"
  cp -f "$PDF_STAGING/${pdf_name}" "docs/pdf/${pdf_name}"
done

echo "Building full multilingual site…"
unset ENABLE_PDF_EXPORT || true
unset PDF_OUTPUT_PATH || true
unset PDF_COVER_SUBTITLE || true
activate_all_en_default
run_mkdocs build

echo "Done → site/ (PDFs at docs/pdf/ and site/pdf/)"
