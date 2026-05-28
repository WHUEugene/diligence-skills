# Prospectus Download Playbook

## Source Priority

1. Exchange disclosure pages, CNINFO, CSRC, and company announcement pages.
2. Company official investor-relations pages.
3. Securities newspaper PDFs when they reproduce official announcements.
4. Financial portals only as discovery clues.
5. Third-party report mirrors only as fallback; mark evidence grade lower.

## Search Pattern

Use exact company and document names before broad industry terms:

```text
<公司名> 首次公开发行股票 招股说明书 PDF
<公司名> 招股说明书 巨潮资讯
<股票代码> 招股说明书 static.cninfo
<产品关键词> 招股说明书
铝合金精密压铸 招股说明书
新能源汽车 铝合金压铸 募集资金项目
通信结构件 铝合金压铸 招股说明书
```

## Local Filing Rule

Store source files under a run or project raw directory and preserve stable IDs:

```text
materials/prospectus_harvest/raw/PH-001_<company>_<year>_ipo_prospectus.pdf
materials/prospectus_harvest/raw/PH-002_<company>_<year>_annual_report.pdf
prospectus_style_runs/<target_slug>/03_source_registry.jsonl
```

Every downloaded or scanned file must have a registry record with:

- source id;
- name;
- URL or local origin;
- local raw path;
- extracted text path;
- source type;
- evidence grade;
- download/scan timestamp;
- notes about relevance and limitations.

## Script

Use `scripts/harvest_prospectus.py`:

```bash
python scripts/harvest_prospectus.py add-url \
  --id PH-001 \
  --name 美利信招股说明书 \
  --url https://example.com/prospectus.pdf \
  --raw-dir materials/prospectus_harvest/raw \
  --extracted-dir materials/prospectus_harvest/extracted \
  --registry prospectus_style_runs/<target_slug>/03_source_registry.jsonl

python scripts/harvest_prospectus.py scan-local \
  --raw-dir materials/prospectus_harvest/raw \
  --extracted-dir materials/prospectus_harvest/extracted \
  --registry prospectus_style_runs/<target_slug>/03_source_registry.jsonl
```

If the source is already local, `file:///absolute/path/to/file.pdf` is valid for
repeatable smoke tests.

## Visual/OCR Fallback

The harvester's text extraction is an evidence-indexing aid, not the final
reader for all PDFs. If the registry quality output contains
`needs_visual_fallback: true`, or if a PDF is scanned/image-only/garbled:

1. Render pages to images.
2. Use OCR or the available vision model to read cover, table of contents,
   business/technology, risk, fundraising, financial-analysis, and project pages.
3. Record the rendered image paths and the visual/OCR notes in the source
   registry or working directory.
4. Do not treat `pdftotext`/PDFMiner failure as a reason to abandon the source.

For Hermes 小D deployments, prefer the configured Mimo vision provider for this
fallback, with text extraction only as an auxiliary cross-check.
