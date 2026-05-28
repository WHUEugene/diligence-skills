---
name: public-prospectus-style-report
description: >-
  Use when Codex needs to generate a prospectus-style public-source report for
  a private company, new project, industry target, or comparable-company study,
  based on public data and reference prospectus formats. Trigger on requests
  such as 类招股书报告, 按招股书格式写报告, 公开资料拟招股书, 拆解招股书格式,
  prospectus-style report, or using prospectuses to structure diligence output.
---

# Public Prospectus-Style Report

Use this skill to build a **commercial diligence report in a prospectus-like
formal style**. The core task is not to rewrite a BP/PPT into Word. The task is
to extract the project-side claims, verify or narrow them with evidence, and
reorganize them into an investment-decision narrative.

## Core Principle

Separate three layers:

1. `公开事实`: official filings, annual reports, prospectuses, government pages,
   company registry/court records, patents, standards, official websites.
2. `项目方口径`: BP, interview, PR, screenshots, management statements.
3. `缺失/需核验`: facts that a real prospectus would need but public data cannot
   prove.

Never fill private-company facts by copying comparable-company facts. Comparable
prospectuses are templates and benchmarks, not evidence for the target company.

The finished report should look and read like the reference formal report, not
like a data-request memo. Evidence gaps control what facts can be stated; they
do not justify `XXX`, filler paragraphs, or repeated "need more data" prose in
the body.

## Investment-Decision Narrative

Every BP/PPT claim must pass through this chain before it appears in the
report:

```text
项目方主张 -> 证据验证 -> 口径压缩 -> 风险判断 -> 投资建议/交易条款
```

For example, a PPT claim such as `总投资15亿元、达产产值15.25亿元` should not
be copied as the report's own conclusion. The report should identify it as
`项目方自报预测`, test it against order, customer, capacity, capex, equipment and
financial evidence, then decide whether it supports a staged investment,
condition precedent, veto item, or no-current-support conclusion.

When the user provides a formal reference report and asks to imitate it, the
reference report becomes the structural and visual master. Preserve its front
matter, table of contents, definition section, chapter hierarchy, page rhythm,
font/table style, caption conventions, and investment-analysis posture unless
the user explicitly asks to simplify. The report body must be written from the
report preparer's point of view; never mention the prompt, the skill, the act of
copying a reference report, or phrases such as "不使用正式报告中的资料" inside the
deliverable.

## Formal Master-Template Mode

For recurring project reports, first convert a good formal report into a master
template package. The package is not a frozen text file; it is a reusable
report skeleton made of:

- front-matter order;
- table of contents rhythm;
- chapter and subsection slots;
- table/figure slots and source-note rules;
- Word style master DOCX;
- evidence requirements for each slot.

Use `scripts/extract_reference_report_template.py` to create the package:

```bash
python scripts/extract_reference_report_template.py \
  /path/to/reference_report.docx \
  --output-dir prospectus_style_runs/<target_slug>/master_template
```

Then process each new PPT/PDF/BP with
`scripts/extract_project_pdf_evidence.py` or the equivalent PPT page-index
workflow before writing. The new project's report fills the template slots with
new-project evidence, public sources, and comparable-company filings. It must
not carry over facts from the old report unless the old report is about the
same project and is explicitly being used as the factual master.

When the reference is a commercial diligence report, also read
[investment-decision-report-contracts.md](references/investment-decision-report-contracts.md).
That reference defines the required fixed structure, chapter contracts, PPT
claim mapping, evidence matrix, cautious writing patterns, and quality checks.

## Workflow

0. **Classify the input evidence first**
   - If the user provides only a BP/PPT/招商材料/project deck, treat it as
     `项目方口径`, not a report-ready diligence base.
   - Before writing the formal report, create a page-level evidence index,
     visual asset inventory, and replication gap matrix. See
     [ppt-only-replication-gate.md](references/ppt-only-replication-gate.md).
   - With only BP/PPT evidence, do not give a definitive investment amount,
     valuation, go/no-go conclusion, customer validation conclusion, or
     independent revenue forecast. Convert those items into missing evidence,
     follow-up requests, or conditions precedent.

0c. **Build investment-decision working matrices**
   - Before drafting the body, create four working matrices:
     1. `PPT主张清单`;
     2. `尽调问题与资料索取清单`;
     3. `证据矩阵`;
     4. `风险与前置条件清单`.
   - These are not optional when the input is a BP/PPT/project PDF or when the
     user asks for a formal diligence report. Use the fields and rules in
     [investment-decision-report-contracts.md](references/investment-decision-report-contracts.md).
   - If code execution is available, write the matrices as
     `00_investment_decision_matrices.json` and run
     `scripts/build_investment_decision_workbooks.py` to create the `.xlsx`
     files. These workbooks are the guardrail that prevents PPT claims from
     being copied directly into the report.

0a. **If a formal reference report is available, build its style blueprint**
   - Extract the reference report's chapter order, paragraph roles, table/figure
     inventory, caption style, source-marker style, and risk/control wording.
   - Replicate the form: front matter, table of contents, definition section,
     chapter rhythm, table density, figure density, formal Chinese disclosure
     tone, source captions, font choices, table borders, and Word layout.
   - If the reference report includes `重要声明`, `重大事项提示`, `目录`, `释义`,
     or a source/appendix-style closing section, keep analogous sections in the
     same order. These sections are not optional in reference-replica mode.
   - Do not copy confidential facts from the reference as facts about the new
     target. Fill each analogous slot only with evidence from the new target or
     public sources. If a slot has no evidence, omit or merge it instead of
     writing a blank, `XXX`, or "可能需要..." paragraph.
   - See [formal-report-replication-rules.md](references/formal-report-replication-rules.md).

0b. **If a reusable mother template is needed**
   - Run `scripts/extract_reference_report_template.py` on the reference DOCX.
   - Use the generated `formal_report_master_template.json`,
     `formal_report_master_template.md`, and `formal_report_style_master.docx`
     as the template package for future projects.
   - For each new project PDF/PPT, create the required page-level evidence
     index, visual asset inventory, and replication gap matrix before drafting.
     For PDFs, run `scripts/extract_project_pdf_evidence.py`.

1. **Select comparable companies**
   - Build the peer list by product, process, downstream customers, and
     fundraising/project similarity.
   - See [comparable-company-selection.md](references/comparable-company-selection.md).

2. **Harvest reference prospectuses and public sources**
   - Pick 3 to 5 prospectuses from comparable listed or IPO companies.
   - Prefer exchange, CNINFO, CSRC, company announcements, and official sources.
   - Use [prospectus-download-playbook.md](references/prospectus-download-playbook.md)
     and [web-search-playbook.md](references/web-search-playbook.md).
   - When a PDF/HTML file or URL is available, use
     `scripts/harvest_prospectus.py` to download or scan it, extract text, and
     update the source registry.

3. **Map reference chapters to the output structure**
   - Extract the table of contents and section-level structure.
   - Record which chapters are common and which are sector-specific.
   - See [prospectus-format.md](references/prospectus-format.md) and
     [module-to-prospectus-map.md](references/module-to-prospectus-map.md).
   - If a formal commercial diligence report is being replicated, use its
     nine-chapter investment-decision structure rather than the four-module
     visible structure. The leader's four modules remain the hidden analytical
     logic: industry situation, project business, project advantages/risks in
     the industry, investment plan and risk control.

4. **Map data availability and evidence grade**
   - For every prospectus-style chapter, mark what can be filled from public
     sources, what can only be filled from the target's BP, and what must remain
     missing.
   - Use [public-data-fit.md](references/public-data-fit.md) and
     [evidence-grading.md](references/evidence-grading.md).

5. **Build a source registry**
   - Number sources as `P1`, `P2`, `A1`, `G1`, etc.
   - `P`: prospectus, `A`: annual report, `G`: government/official, `C`: company
     official, `B`: BP or project-side material, `M`: market/media.
   - Include local path/URL, date, source type, grade, and use.
   - Keep the numbering stable from draft through DOCX. Use inline markers such
     as `[P1]` and `[A2]` in the body; the DOCX generator renders them as
     superscript source markers, and the final section maps them to full source
     names.

6. **Write the report**
   - If no formal reference report is provided, use prospectus-style section
     names without adding decorative or empty preface chapters.
   - If a formal reference report is provided and the user asks to imitate it,
     follow the reference report's actual structure first, including front
     matter and full chapter list. The leader's four modules are then the
     analytical logic behind the chapters, not necessarily the visible headings.
   - For ordinary primary-market reports, preserve the prospectus disclosure
     logic inside the leader's four modules. Do not expand the output into a
     full IPO prospectus chapter list unless the user explicitly asks for a
     full-chapter simulation or provides a formal report to replicate.
   - In formal commercial diligence mode, use the fixed structure:
     `封面`, `重要声明`, `重大事项提示`, `目录`, `释义`, `第一章 项目概览`,
     `第二章 行业研究`, `第三章 出资主体与项目主体基本情况`,
     `第四章 公司业务与技术`, `第五章 同业竞争、关联交易与集团协同`,
     `第六章 财务分析与财务预测`, `第七章 募集资金运用与落地匹配度`,
     `第八章 风险因素与风险控制`, `第九章 尽调结论与投资建议`, and
     source/appendix material if the reference report uses it.
   - Each formal chapter must follow a chapter contract: function, inputs,
     questions answered, required table/figure, and forbidden overclaiming.
     Do not treat the heading list as enough.
   - Mark every target-specific claim with source type and confidence.
   - Put a source marker next to every quantitative claim, technical parameter,
     market size, growth rate, customer concentration, investment amount, or
     financial assumption. A final source list alone is not enough; data must
     carry local references near the relevant sentence/table/figure.
   - Write only evidence-supported paragraphs. Do not use placeholders such as
     `XXX`, `xx`, `待补充`, or template paragraphs that merely say a type of
     data "may be needed." If a fact is not known, omit the unsupported
     conclusion and move the exact missing evidence to the final
     `待核验事项清单` or to transaction conditions.
   - Do not make the body a catalogue of absent data. Use a limitation sentence
     only when necessary to prevent misuse of a project-side forecast or claim;
     otherwise let the report read as a completed, evidence-bounded analysis.
   - Use [paragraph-evidence-writing-rules.md](references/paragraph-evidence-writing-rules.md)
     for paragraph-level writing rules. The formal report should read like a
     completed diligence judgment, not a questionnaire with blanks.
   - Use prospectus-style tables and figures where the source has structured
     data. For project finance reports, include tables for product revenue,
     investment composition, comparable companies, and risk controls; add charts
     for the most important revenue/investment or market data when feasible.
     Follow [figure-table-source-rules.md](references/figure-table-source-rules.md):
     figure captions need local source markers, project-side images need
     `资料来源：项目商业计划书/访谈/项目材料`, and public data charts should be
     redrawn into a consistent report style rather than pasted as screenshots.
   - Put `资料来源与待核验事项` as the final section, not at the front.
   - See [report-template.md](references/report-template.md).

7. **Generate DOCX**
   - Markdown is only the editable intermediate draft.
   - The formal deliverable must be a `.docx` that visually follows a China
     A-share prospectus-like report structure: cover title, numbered chapters,
     compact black headings, formal Chinese body text, and bordered tables.
   - In reference-replica mode, use the reference DOCX itself as the style
     master when possible. Preserve page setup, heading styles, body font,
     paragraph spacing, table borders, table shading, figure captions, and table
     captions. Do not invent a new visual system.
   - Use `scripts/build_prospectus_style_docx.py` whenever code execution is
     available. Do not deliver the Markdown draft as the final report unless
     DOCX generation is impossible.
   - If DOCX generation is impossible, say so and provide the Markdown only as a
     fallback.

8. **Quality gate**
   - Do not include issuer/director/sponsor/auditor/lawyer declarations.
   - Do not include decorative `重要提示`, `重大事项提示`, `重要声明`, `报告边界`,
     `使用说明`, `附录`, or similar meta/preface sections when no formal
     reference report contains them. In reference-replica mode, preserve the
     reference front matter and closing sections instead of deleting them.
   - Do not state audited financials unless the target has audited statements.
   - Do not invent shareholders, related parties, customers, suppliers, patents,
     or financial tables.
   - Missing evidence should normally be written only in the final
     `资料来源与待核验事项` chapter or converted into transaction conditions. Put
     it in a substantive chapter only when it changes the interpretation of a
     stated project-side forecast, customer claim, technology claim, or
     investment judgment.
   - Never include a `免责声明` paragraph. If the report has public-data limits,
     express them as `待核验事项` tied to the relevant evidence gap.
   - In formal commercial diligence mode, verify that the report has converted
     project-side promotion into investment-decision language: material claims
     appear in the relevant chapter, have evidence strength, have a narrowed
     conclusion, and where needed become a condition precedent, staged-payment
     trigger, repurchase/valuation-adjustment item, information-rights item, or
     veto item.
   - Before DOCX generation, check that Markdown syntax does not remain visible
     in rendered tables, bullets, captions, or paragraphs.
   - Before DOCX generation in four-module mode, run
     `scripts/audit_four_module_report.py` on the Markdown draft to catch drift
     into a full IPO prospectus structure. Use `--strict` for formal
     deliverables so placeholders, vague unsupported language, unreferenced
     data, and figure source omissions fail the build. In reference-replica
     mode, run the audit with `--reference-replica` or use a separate structural
     comparison against the reference report.
   - In strict mode, also audit figures and tables. A formal industrial project
     report should normally contain figures/tables that cover industry route,
     industry chain, product form, process, investment, finance, comparables,
     and evidence gaps. If the source set cannot support them, state which
     figures/tables are missing and why.

## Standard Output

Create or return a formal DOCX report. Working files are allowed, but only the
DOCX is the formal user-facing deliverable:

```text
prospectus_style_runs/<target_slug>/
  00_input_evidence_index.md
  00_visual_assets_inventory.md
  00_replication_gap_matrix.md
  00_investment_decision_matrices.json
  01_PPT主张清单.xlsx
  02_尽调问题与资料索取清单.xlsx
  03_证据矩阵.xlsx
  04_风险与前置条件清单.xlsx
  01_formal_report_style_blueprint.md
  01_reference_prospectus_format.md
  02_public_data_fit_map.md
  03_source_registry.md
  04_prospectus_style_report_draft.md
  05_prospectus_style_report.docx
```

The `00_*` files are required when the initial evidence is only BP/PPT/project
materials. For a fully sourced formal report, put source registry summaries and
evidence gaps in the final chapter of the report. Do not create a separate
`gap_list` deliverable for the user unless they explicitly ask; the internal
replication gap matrix is an evidence-control artifact.

## Default Four-Module Structure

Use this only when the user asks for the leader's four-module deliverable or
does not provide a formal report to replicate. If the user provides a formal
report and asks to copy its structure/style, the reference report structure
overrides this section.

Use this default order for primary-market project reports. The report should be
organized around the leader's four modules, while each module borrows the
writing style, evidence order, and tables from the corresponding prospectus
chapters.

1. 行业情况
   - 行业定义
   - 产业链
   - 下游需求
   - 竞争格局
   - 行业风险
   - Reference prospectus chapters: `业务与技术`中的`发行人所处行业基本情况`
     and `风险因素`中的行业风险.
2. 项目业务情况
   - 项目基本情况
   - 产品方案
   - 技术工艺
   - 投资规模
   - 财务预测
   - Reference prospectus chapters: `业务与技术`中的主营业务、主要产品、
     工艺流程、核心技术, plus `募集资金运用` and `财务会计信息与管理层分析`.
3. 项目在行业环境中的优劣势
   - 潜在优势
   - 主要短板
   - 可比公司对标
   - Reference prospectus chapters: `业务与技术`中的竞争地位、竞争优势,
     and `风险因素`中的技术、市场、客户、原材料、产能消化等风险.
4. 投资方案与风控措施
   - 投资判断
   - 分期出资
   - 先决条件
   - 交易条款
   - 否决项
   - Reference prospectus chapters: `募集资金运用`中的项目可行性 and
     `风险因素`中的风险揭示, adapted into primary-market investment terms.
5. 资料来源与待核验事项
   - Sources and evidence gaps only. This is not a fifth business module.

If the target is a project rather than a company, rename `发行人` to `目标项目`
or `项目公司（拟设）`, and clearly mark that there is no formal issuer.

## DOCX Style Requirements

- A4 portrait unless the tables require landscape.
- Cover title centered in black, Chinese font, bold, no decorative color blocks.
- In reference-replica mode, main headings use the reference report's exact
  heading hierarchy and numbering.
- In default four-module mode, main headings use the leader's module numbering
  such as `一、行业情况`.
- Use compact, formal body text; avoid marketing-style hero pages, disclaimers,
  process notes, and tool/self-reference language.
- Tables use black or light-gray borders, white header cells, and no dark color
  fills unless the reference report uses a different formal table style.
- Source markers in tables/figure captions are acceptable when all rows share
  the same source; otherwise mark the individual row or data cell.
- The final section must contain two tables: `资料来源清单` and `待核验事项清单`.
  Do not place source tables at the beginning.

## Useful With Existing Skills

- Use `aiotcap-deep-research` first when the industry baseline is weak.
- Use `primary-market-diligence` after this report when the task moves from
  public disclosure-style writing to investment decision, valuation, terms, and
  risk control.
