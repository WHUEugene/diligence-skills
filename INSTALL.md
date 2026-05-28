# Install

## Codex

```bash
git clone https://github.com/WHUEugene/diligence-skills.git
cd diligence-skills
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
rsync -a skills/primary-market-diligence "${CODEX_HOME:-$HOME/.codex}/skills/"
rsync -a skills/public-prospectus-style-report "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex or refresh skills after copying.

## Hermes

```bash
git clone https://github.com/WHUEugene/diligence-skills.git
cd diligence-skills
mkdir -p "${HERMES_HOME:-$HOME/.hermes}/skills"
rsync -a skills/primary-market-diligence "${HERMES_HOME:-$HOME/.hermes}/skills/"
rsync -a skills/public-prospectus-style-report "${HERMES_HOME:-$HOME/.hermes}/skills/"
```

Restart or reload the target Hermes profile after copying.

## One-Line Copy From An Existing Checkout

```bash
DEST="${CODEX_HOME:-$HOME/.codex}/skills"; mkdir -p "$DEST"; rsync -a skills/primary-market-diligence skills/public-prospectus-style-report "$DEST/"
```

For Hermes, replace `DEST` with `"${HERMES_HOME:-$HOME/.hermes}/skills"`.

## Python Dependencies For DOCX/PDF Helpers

```bash
python -m pip install -r requirements.txt
```

`pdftotext` from Poppler is optional but improves PDF text extraction when available. Page rendering uses PyMuPDF.
