---
name: primary-market-diligence
description: >-
  Use when Codex needs to run or draft an一级市场 investment research / commercial diligence workflow for a private company, new business direction, industrial project, financing, investment, joint venture, or government-platform cooperation. The skill turns scattered public sources and NDA/internal company materials into industry analysis, company business analysis, company-vs-industry strengths and risks, investment plan, and risk-control measures.
---

# Primary Market Diligence

Use this skill for一级市场新项目研究, not for ordinary public-company equity research. The output must support an investment decision: whether to proceed, how to invest, under what conditions, and how to control downside risk.

## Core Principle

Do not treat company BP or PR as fact. Convert every important claim into a verifiable claim with source, evidence level, missing proof, and impact on investment terms.

Use招股书/年报/公告 as high-quality public references for structure and comparables, but do not mechanically write a prospectus. Private-market targets often lack formal disclosure; internal company materials after NDA are usually the decisive evidence.

For Feishu group delivery, keep execution silent until the result is ready. Do not narrate parser choices, package installs, command failures, OCR attempts, web-search attempts, or internal retries into the group chat. Only send the final useful outcome, the `.docx` attachment, or one concise blocking question.

## Feishu Attachment Recovery

When running inside Hermes/Feishu, do not treat "file is not already in the working directory" as a blocker. The gateway mirrors recent group history and downloads visible group attachments into local cache.

If the prompt contains a `[Local Feishu history mirror]` block:

1. Use any `recent_downloaded_media` local paths directly as the submitted materials.
2. If the referenced file is not obvious from `recent_downloaded_media`, read/search `media_index_jsonl` for the latest matching PDF/PPT/BP/project file.
3. If needed, read/search `messages_jsonl` to understand which file the user meant by "上面/刚才/这些/都做一遍".
4. Do not ask the user to resend and do not reply "本地没有/还没缓存" until these local paths and mirror indexes have been checked.
5. Do not quote cache paths or mirror paths in the Feishu group unless the user explicitly asks for debugging.

## PDF/PPT Visual-First Reading

For PDF, PPT, BP, pitch deck, investment deck,招商材料, and商业计划书 inputs, page-image understanding is the primary reading path. Text extraction is only an auxiliary cross-check.

1. Render pages into images first, then use `vision_analyze` to inspect cover pages,目录, charts, tables, technical routes, customer/order pages, capacity plans, financing/use-of-funds pages, and risk disclosures. Empty text, garbled text, embedded fonts, or scanned/image-only PDFs are not a blocking failure.
2. Page-count rule: for 30 pages or fewer, render and visually inspect all pages when feasible. For longer files, start with cover,目录, first 12 pages, final 2 pages, and pages that appear to contain charts/tables/amounts/capacity/customers/orders/technical routes; then add pages as needed.
3. For each visually inspected page, capture page number, visible title, company/project names, products, technology route, customers/orders, capacity, funding amount/use, costs, construction plan, chart/table claims, obvious risks, and uncertain items.
4. Use text extraction libraries only to cross-check names and numbers. Never ask the user to resend a material merely because `pdftotext`, PyMuPDF, pdfminer, or pypdf produced empty/garbled text.
5. Use public search only after the visual material pass, to supplement company background, registry/legal/policy/industry context. Search is not a substitute for reading the submitted material.
6. In Feishu, do not expose internal tool names, parser failures, package installs, OCR retries, or search attempts. The user-facing output is the Word deliverable or one concise blocking question.

When code execution is available, render PDF pages with:

```bash
python scripts/render_pdf_pages_for_vision.py --pdf <material.pdf> --out <workdir>/page_images --max-pages 30 --dpi 160
```

Then use the generated `manifest.json` image paths as inputs for `vision_analyze`, build an evidence/claim draft, and generate the formal `.docx`.

## Standard Output

For leader-facing prospectus-style project reports, produce four substantive
modules plus a final evidence section:

1. **行业情况**: industry definition, chain, market size, drivers, technical routes, competition, costs, policy/regulation, industry risks.
2. **公司业务情况**: company/project boundary, products, technology, customers, orders, production, supply chain, finance, funding use, internal evidence.
3. **公司在行业环境中的优劣势**: industry fit, real advantages, weak points, unverified assumptions, comparable-company/competitor positioning.
4. **投资方案与风控措施**: investment judgment, staged funding, conditions precedent, transaction terms, veto/stop items.
5. **资料来源与待核验事项**: source list and evidence gaps only; this is not a fifth business-analysis module.

## Workflow

1. **Scope the study**
   - Identify target company/project/new direction.
   - Identify transaction purpose: investment,增资, JV, M&A, government cooperation, or strategic partnership.
   - Build an input map: public sources, internal materials, interviews, third-party evidence, missing items.
   - If the only target-specific material is a BP/PPT/招商材料, run a PPT-only
     evidence pass before writing: page evidence index, visual asset inventory,
     and a gap matrix that separates `PPT事实`, `PPT可推断`, `需外部搜索`, and
     `需项目方补充`. Do not jump from a project deck to a formal investment
     recommendation.

2. **Collect public baseline**
   - Search industry definitions, chain, market size, technical routes, competitors, policy, standards, patents, recruitment, financing, and legal/company records.
   - For comparables, prioritize prospectuses, annual reports, announcements, exchange filings, official policy, industry association data, and reputable third-party reports.
   - Create source/fact cards before writing conclusions.

3. **Ingest internal materials**
   - Parse BP, company intro, financial model, customer list, order/contracts, testing reports, equipment quotes, capex plan, shareholder documents, financing terms, commitments, and interview notes.
   - Assign evidence levels:
     - S: regulatory/official filings, government records, exchange disclosures, official company registry/court systems.
     - A: third-party testing, signed customer/bank documents, formal contracts, invoices, audit reports.
     - B: internal ledgers, ERP exports, board materials, unaudited statements.
     - C: BP, oral explanations, screenshots, PR.
     - D: unsourced estimates or rumors.
   - For BP/PPT claims, keep page numbers next to every major number, product,
     customer/order implication, capacity, investment amount, policy request,
     process image, and market chart. PPT market charts are only clues until
     the original public source is checked.

4. **Build claim table**
   - For each key claim: claim, source, importance, required evidence, public cross-check, current evidence level, investment impact if unverified.
   - Claims with weak evidence must become follow-up questions, risk items, or closing conditions.

5. **Write modules**
   - Industry module mainly from public sources.
   - Company module mainly from internal materials.
   - Strengths/risks module must cite the first two modules; do not invent advantages.
   - Investment/risk modules must translate analysis into terms, not generic warnings.
   - With PPT-only evidence, the investment module must stop at evidence-based
     gating language such as “不得按申报方案直接交割，需补齐客户、检测、主体、财务
     和建设证据”. Do not generate definitive valuation, investment amount,
     performance commitment, or go/no-go language unless the supporting evidence
     exists.

6. **Quality gate**
   - Every major conclusion must have evidence or be explicitly marked unverified.
   - Separate facts, company claims, analyst judgments, and assumptions.
   - Identify manual escalation needs: customer calls, site visit, legal, finance, technical expert, environmental/export-control review.
   - For formal prospectus-style reports, require visual evidence: product or
     process images from project materials, redrawn public-data charts, and
     analyst calculation charts where enough assumptions exist. Each figure or
     table needs a nearby source marker; a source list only at the end is not
     enough.

## BP/PPT To Diligence Checklists

Use this sub-workflow when the input is a company BP, project PPT,招商材料, commercial plan, or early project proposal and the task is to produce商务尽调问题清单,资料准备清单,重点清单, or a report framework.

Do not summarize the BP as facts. Convert BP claims into diligence questions, evidence requests, substitute evidence, report slots, and risk-control conditions.

### PDF/PPT Reading Discipline

Do not assume a PDF is readable text. First classify the input:

- Text-layer PDF: use text extraction as the main evidence source, but still inspect chart/table pages when they contain key numbers.
- Image-only PDF: render pages to images and use visual reading or OCR-backed visual extraction. Plain `pdftotext` is insufficient.
- Mixed PDF: combine text extraction and page-image reading; cross-check key numbers, customer names, product names, financing amounts, capacity plans, revenue forecasts, and policy claims.

When the environment supports visual reading, prefer a page-level evidence pass before writing the checklist. Record page number, visible title, project claims, numbers, tables/charts, customer or partner names, technical terms, and uncertain items. If visual reading is unavailable, state the limitation in the internal brief and do not overclaim completeness.

For robust agent deployments such as Hermes or OpenClaw, split the workflow into two stages:

1. Evidence extraction: `extracted_text.txt`, optional `page_images/`, optional `evidence_pages.jsonl`, and a claim table.
2. Checklist generation: map claims into the 12-category framework and produce the formal five-column checklist.

Use Markdown as the editable intermediate draft, not as the preferred formal deliverable. When the environment has document-generation capability and the user asks for a deliverable or formal checklist, generate a `.docx` version after the Markdown draft.

For `.docx`, do not invent a Word style. Use the bundled generator `scripts/build_diligence_checklist_docx.py` whenever code execution is available. First create the required JSON payload, then call the script. The Word style must match the approved sample:

- A4 landscape page.
- Main title exactly `商务尽调资料准备清单`, centered, black, 楷体, bold, about 17pt.
- No blue title, no project-name hero title, no project overview paragraph unless the user explicitly asks.
- Metadata block under the title with four left-aligned lines: `委托单位：`, `受托尽调机构：`, `尽调对象：`, `适用阶段：`.
- Section headings black, 楷体, bold, e.g. `第一类：企业主体与背景信息`; no blue heading color.
- Tables use white header cells, light gray borders, no dark-blue fill, no colored bands.
- Fixed five columns: `序号 / 需了解的核心问题 / 推荐提供的资料 / 核心目的 / 资料提供状态`.
- Serial-number and status columns are narrow; question/material/purpose columns receive the width.
- Status cells are left blank for the company to fill; do not write `□未提供` unless the user explicitly asks.
- Use readable compact Chinese line spacing; avoid MS Gothic/default Japanese fonts.

The formal checklist should not mention OCR, visual reading, extraction failures, or internal uncertainty notes. Put those in `brief.md`.

### Default Delivery Format

By default, deliver尽调问卷/资料清单 in `.docx` format in the group chat, not as plain markdown text. The markdown is the intermediate draft; the Word file is the formal deliverable.

The `.docx` conversion workflow:
1. Write the Markdown draft first only as an editable intermediate.
2. Create a JSON payload that matches `scripts/build_diligence_checklist_docx.py`'s schema.
3. Generate the formal Word file by calling the bundled script:

```bash
python scripts/build_diligence_checklist_docx.py --input <payload.json> --output <checklist.docx>
```

4. Do not hand-build a `.docx` with custom colors, custom fonts, or a different layout. Do not use any alternate "practical" or "modern" Word style.
5. Save the `.docx` to the active working directory supplied by the runtime.
6. Send the file using a `MEDIA:` attachment directive in the final Feishu response. On Windows, use a native Windows absolute path, for example `MEDIA:C:\Path\To\Workdir\project_diligence_checklist.docx`; do not use Git Bash/MSYS paths such as `/c/Users/...`.
7. Before saying the file was sent, confirm the final response actually contains the `MEDIA:` directive with the existing `.docx` path. If the final answer does not include `MEDIA:...docx`, the file has not been sent.
8. Keep the 12-category structure and five-column table. The script controls fonts, widths, borders, colors, metadata block, and blank status cells.

Final Feishu reply for `.docx` deliverables must be short and must end with the attachment directive on its own line:

```text
已生成 Word 版尽调问题清单，见附件。
MEDIA:C:\Path\To\Workdir\<actual_file_name>.docx
```

Do not paste the full checklist table in the group chat when a Word deliverable was requested. Do not write “Word 已发送到群里 / 可直接下载” unless the same final response includes the `MEDIA:` line.

For Feishu replies, never expose internal terms such as `pdftotext`, `pdfminer`, `PyMuPDF`, `pip`, `OCR environment`, `tool failed`, `I will try another method`, `URL方式不行`, or `我搜索一下`. If a PDF is image-only or uses embedded/encrypted fonts, handle that internally with available parsers, page rendering, public-source supplementation, or a generic diligence framework. The final user-facing wording should be outcome-focused, for example: `已根据材料可识别信息及公开资料生成初稿，见附件。`

### Linear Process

1. **Set standard modules first**
   - Build the generic module map before reading the PPT in detail.
   - Do not mechanically force a two-list output. Treat existing first-round and supplemental checklists as examples of stages in human work, not as a mandatory dual format.

2. **Extract BP/PPT claims**
   - Capture page number, claim, type, numbers, product names, market assertions, policy requests, implied business logic, and visible inconsistencies.
   - Treat all BP/PPT content as company claims unless independently verified.

3. **Map claims to modules**
   - For each claim: identify the module, ask what evidence would make it true, list formal documents and acceptable substitutes, and state why it matters.

4. **Generate the full question list**
   - By default, produce one integrated资料准备清单 that combines broad module coverage with focused risk follow-up.
   - Use the original 12-category checklist framework as the first-level structure. Do not rebuild the first-level framework from supplemental checklist parts, and do not invent loose three-part compound headings.
   - Use these first-level headings exactly unless the user explicitly changes the framework:
     - 第一类：企业主体与背景信息
     - 第二类：项目技术与产品基础
     - 第三类：市场规模与竞争
     - 第四类：项目投资与建设方案
     - 第五类：资金筹措与风险保障
     - 第六类：过往业绩与商誉
     - 第七类：拟派管理团队与组织规划
     - 第八类：财务预测与经营假设
     - 第九类：工商登记与关联方信息
     - 第十类：诉讼、行政处罚与合规记录
     - 第十一类：上市进展与重大资本运作
     - 第十二类：行业政策与竞争动态
   - Supplemental checklist topics are deepening logic, not first-level headings. Attach them to the 12-category framework:
     - 合资方案与合作基础: mainly under 第一类;出资节奏 also under 第五类.
     - 外购转自产战略合理性: product/technology under 第二类; demand and competitors under 第三类; cost and pressure tests under 第八类.
     - 行业市场与产品: under 第二类, 第三类, and 第八类 as appropriate.
     - 供应链与销售管理: under 第八类;关联交易 links to 第九类.
     - 管理团队与人力资源: under 第七类.
     - 项目建设与产能规划: under 第四类;产能爬坡 and output-value assumptions link to 第八类.
   - Table fields must be: `序号 / 需了解的核心问题 / 推荐提供的资料 / 核心目的 / 资料提供状态`.
   - In `推荐提供的资料`, combine formal evidence and acceptable substitute evidence in the same cell. Do not split them into two top-level columns unless the user asks.

5. **Generate a focused supplemental list only when useful**
   - Even for a supplemental list, keep the 12-category framework unless the user explicitly asks for a separate专项清单.
   - Do not use the six supplemental parts as first-level headings for the main deliverable. They are risk-focus lenses to be inserted under the relevant 12 categories.
   - Table fields must remain: `序号 / 需了解的核心问题 / 推荐提供的资料 / 核心目的 / 资料提供状态`.
   - The final report or formal checklist should not contain internal process labels such as blind-test round, version notes, or drafting rationale unless the user explicitly asks for an iteration report.

6. **Quality check**
   - Confirm every material BP/PPT number, product line, customer/order implication, policy request, technology claim, market-size assertion, capex/funding claim, and inconsistency appears in at least one question or資料项.
   - If a project has a special commercial logic such as外购转自产, make it a named section rather than hiding it inside generic supply chain analysis.
   - Confirm the checklist has exactly the 12 standard first-level categories, the fixed five-column table, and no internal process words such as blind test, round, version note, drafting rationale, OCR limitation, or skill instruction.
   - Confirm `brief.md`, if requested, records the project facts extracted from the source material, page/image reading limitations, and a concise quality self-review.

## Templates And Prompts

Use bundled files when useful:

- `../public-prospectus-style-report/`: companion four-module prospectus-style report workflow, including comparable-company selection, prospectus download/search playbooks, evidence grading, report audit, source registry, and DOCX generation.
- `references/diligence-checklist-workflow.md`: operational workflow for BP/PPT/PDF evidence extraction, 12-category checklist generation, blind-test iteration, and Hermes/OpenClaw migration.
- `scripts/build_diligence_checklist_docx.py`: approved Word generator for the formal checklist style. Use it instead of hand-building a differently styled DOCX.
- `templates/investment_memo_structure.md`: final memo skeleton.
- `templates/evidence_fact_card.md`: source and fact card schema.
- `templates/internal_information_request.md`: NDA/internal information request schema.
- `templates/public_source_plan.md`: public research planning schema.
- `checklists/public_source_quality.md`: public source quality gate.
- `checklists/investment_decision_gates.md`: investment readiness and risk-control gate.
- `prompts/01_public_research_agent.md`: public-source research agent prompt.
- `prompts/02_internal_information_agent.md`: internal-material extraction prompt.
- `prompts/03_company_vs_industry_agent.md`: strengths/weaknesses analysis prompt.
- `prompts/04_investment_risk_agent.md`: investment plan and risk-control prompt.

## Output Discipline

- Write in investor-facing Chinese by default.
- Use tables for claims, sources, comparables, risks, and milestones.
- Formal report正文 must be evidence-gated: no `XXX`, `xx`, `待补充`,
  `此处可写`, `可能需要补充资料`, or similar template/placeholder wording.
  If evidence is absent, either omit the unsupported claim or state the exact
  non-adopted conclusion and its investment effect; put the exact document
  request in `资料来源与待核验事项`.
- For formal investment reports or prospectus-style reports, do not put
  `重要提示`, `重要声明`, `报告边界`, `使用说明`, or `附录` as standalone
  chapters. Put `资料来源与待核验事项` at the end of the report.
- When the user asks for a formal prospectus-style report and document
  generation is available, deliver a `.docx` report rather than a Markdown-only
  artifact. Use the `public-prospectus-style-report` four-module DOCX workflow
  for that case.
- Avoid boilerplate risk wording. Each risk must name evidence missing, effect on investment, and control action.
- If evidence is not enough to conclude, do not write a soft conclusion. Convert
  it into a condition precedent, veto item, staged-funding gate, or exact
  follow-up evidence item.
