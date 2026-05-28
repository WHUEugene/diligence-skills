# Diligence Checklist Workflow

This reference defines the operational workflow for converting BP/PPT/PDF project materials into a commercial diligence information request checklist.

## 1. Purpose

The checklist is not a summary of the BP. It is a formal request list that asks the company to provide evidence for key claims.

Default output:

- `checklist.md`: editable intermediate checklist draft used for review, diffing, and automated structure checks.
- `商务尽调资料准备清单.docx`: formal checklist deliverable when document-generation capability is available.
- `brief.md`: internal note containing extracted project facts, reading limitations, and quality self-review.

Optional output:

- `claims_table.md`
- `extracted_text.txt`
- `evidence_pages.jsonl`
- `page_images/`
- Word render preview for visual QA.

## 2. Fixed Checklist Structure

Use exactly these 12 first-level categories unless the user explicitly changes them:

1. 企业主体与背景信息
2. 项目技术与产品基础
3. 市场规模与竞争
4. 项目投资与建设方案
5. 资金筹措与风险保障
6. 过往业绩与商誉
7. 拟派管理团队与组织规划
8. 财务预测与经营假设
9. 工商登记与关联方信息
10. 诉讼、行政处罚与合规记录
11. 上市进展与重大资本运作
12. 行业政策与竞争动态

Use exactly these five columns:

| 序号 | 需了解的核心问题 | 推荐提供的资料 | 核心目的 | 资料提供状态 |
|---|---|---|---|---|

In `推荐提供的资料`, combine formal evidence and substitute evidence:

`正式资料：...；替代资料：...。`

Do not split formal evidence and substitute evidence into two top-level columns unless the user asks.

## 3. Supplemental Topics Are Deepening Lenses

Do not rebuild the first-level structure from supplemental lists.

Map supplemental topics into the 12-category framework:

| Topic | Mapping |
|---|---|
| 合资方案与合作基础 | Mainly category 1; contribution schedule also category 5 |
| 外购转自产战略合理性 | Product/technology category 2; demand and competitors category 3; cost and stress test category 8 |
| 行业市场与产品 | Categories 2, 3, and 8 |
| 供应链与销售管理 | Category 8; related-party issues link to category 9 |
| 管理团队与人力资源 | Category 7 |
| 项目建设与产能规划 | Category 4; ramp-up and output assumptions link to category 8 |

## 4. PDF/PPT Reading

First classify the file:

- Text-layer PDF: `pdftotext` or equivalent text extraction is useful.
- Image-only PDF: render pages to images and use visual reading or OCR-backed visual extraction.
- Mixed PDF: combine both.

Recommended evidence extraction:

1. Run basic file checks: page count, encryption, text extraction availability.
2. Extract text where possible.
3. Render key pages or all pages to images when the material is image-heavy.
4. For each page, capture page number, title, project claims, numbers, customer/partner names, tables/charts, technical terms, and uncertain items.
5. Keep uncertainty in the internal brief, not in the formal checklist.

Page evidence schema:

```json
{
  "page": 1,
  "visible_title": "",
  "project_claims": [],
  "numbers": [],
  "tables": [],
  "charts": [],
  "customer_or_partner_names": [],
  "technical_terms": [],
  "uncertain_items": []
}
```

## 5. Claim Extraction

Treat BP/PPT content as company claims until verified.

For each material claim, capture:

- Page number.
- Original claim.
- Claim type: entity, product, technology, customer, order, market, capacity, finance, funding, policy, team, compliance.
- Key numbers.
- Evidence currently available.
- Evidence still required.
- Investment impact if unverified.

## 6. Mapping Claims To Questions

A good question asks what must be verified, not merely what file is wanted.

Weak:

`请提供销售资料。`

Better:

`公司声称 2026 年可实现收入目标，该目标对应的客户、订单、价格、产能、良率和交付节奏是否已有证据支持？`

Each question needs:

- A precise claim or uncertainty.
- Formal evidence request.
- Substitute evidence request.
- Purpose tied to investment judgment.
- Status, usually `待提供`.

## 7. Quality Gate

Before finalizing, check:

- There are exactly 12 first-level categories.
- The first-level category names match the standard wording.
- Each category uses the fixed five-column table.
- Formal and substitute evidence are in the same column.
- No internal process words appear in `checklist.md`.
- Every material number, product line, customer/order implication, policy request, technology claim, market-size assertion, capex/funding claim, and inconsistency is covered.
- Project-specific logic is not lost inside generic template wording.
- `brief.md` records reading limitations and quality self-review.

## 8. Hermes/OpenClaw Deployment Pattern

For production agents, split the work:

```text
Input PDF/PPT
  -> file permission check
  -> PDF type classification
  -> text extraction and/or page rendering
  -> page-level evidence extraction
  -> claim table
  -> 12-category checklist
  -> brief
  -> optional Word render and visual QA
```

This keeps evidence extraction separate from checklist writing, making failures easier to diagnose and making the workflow portable across agent runtimes.

## 9. Formal Output Restrictions

The formal checklist must not contain:

- Blind-test round labels.
- Version notes.
- Drafting rationale.
- Agent self-review.
- OCR or visual-reading caveats.
- References to this skill.

Use `brief.md` for internal caveats and review notes.

## 10. Word Deliverable

Markdown is the working draft. For formal delivery, generate a `.docx` from the same checklist content.

Word formatting requirements:

- Title: `商务尽调资料准备清单`.
- Keep the 12 standard section headings.
- Use the same five columns: `序号 / 需了解的核心问题 / 推荐提供的资料 / 核心目的 / 资料提供状态`.
- Make the serial-number and status columns narrow.
- Allocate most table width to the core-question, material-request, and purpose columns.
- Keep formal evidence and substitute evidence in the same material-request cell.
- Use 楷体 for Chinese text where possible; do not fall back to MS Gothic/Japanese default styling.
- Use black section headings and white table headers with light gray borders.
- Do not use blue titles, blue headings, dark-blue header fills, decorative project summary blocks, or card-like formatting.
- Put the four-line metadata block below the title: `委托单位：`, `受托尽调机构：`, `尽调对象：`, `适用阶段：`.
- Leave status cells blank for the company to fill; do not write `□未提供` unless the user explicitly asks for checkbox status.
- Do not include version notes, internal process labels, extraction caveats, or agent self-review in the `.docx`.

Use `scripts/build_diligence_checklist_docx.py` when code execution is available. If the runtime cannot generate `.docx`, state that limitation in the response and still produce `checklist.md` as the fallback.
