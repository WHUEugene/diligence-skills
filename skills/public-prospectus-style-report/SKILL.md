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

Use this skill to build a **prospectus-style public information report**. It
borrows the structure and disclosure logic of real IPO prospectuses, but it is
not a legal prospectus and must not pretend to have issuer, sponsor, auditor, or
lawyer verification.

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

0a. **If a formal reference report is available, build its style blueprint**
   - Extract the reference report's chapter order, paragraph roles, table/figure
     inventory, caption style, source-marker style, and risk/control wording.
   - Replicate the form: section rhythm, table density, figure density, formal
     Chinese disclosure tone, source captions, and Word layout.
   - Do not copy confidential facts from the reference as facts about the new
     target. Fill each analogous slot only with evidence from the new target or
     public sources. If a slot has no evidence, omit or merge it instead of
     writing a blank, `XXX`, or "可能需要..." paragraph.
   - See [formal-report-replication-rules.md](references/formal-report-replication-rules.md).

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

3. **Map reference chapters to the four-module output**
   - Extract the table of contents and section-level structure.
   - Record which chapters are common and which are sector-specific.
   - See [prospectus-format.md](references/prospectus-format.md) and
     [module-to-prospectus-map.md](references/module-to-prospectus-map.md).

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
   - Use prospectus-style section names, but do **not** add standalone preface
     chapters such as `重要提示`, `重要声明`, `报告边界`, `使用说明`, or `附录`.
     They are not useful for this diligence deliverable.
   - Preserve the prospectus disclosure logic inside the leader's four modules.
     Do not expand the output into a full IPO prospectus chapter list unless the
     user explicitly asks for a full-chapter simulation.
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
   - Use `scripts/build_prospectus_style_docx.py` whenever code execution is
     available. Do not deliver the Markdown draft as the final report unless
     DOCX generation is impossible.
   - If DOCX generation is impossible, say so and provide the Markdown only as a
     fallback.

8. **Quality gate**
   - Do not include issuer/director/sponsor/auditor/lawyer declarations.
   - Do not include `重要提示`, `重大事项提示`, `重要声明`, `报告边界`, `使用说明`,
     `附录`, or similar meta/preface sections in the formal report.
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
   - Before DOCX generation, check that Markdown syntax does not remain visible
     in rendered tables, bullets, captions, or paragraphs.
   - Before DOCX generation, run `scripts/audit_four_module_report.py` on the
     Markdown draft to catch drift into a full IPO prospectus structure.
     Use `--strict` for formal deliverables so placeholders, vague unsupported
     language, unreferenced data, and figure source omissions fail the build.
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
- Main headings use the leader's module numbering such as `一、行业情况`.
- Use compact, formal body text; avoid marketing-style hero pages, disclaimers,
  process notes, and appendix labels.
- Tables use black or light-gray borders, white header cells, and no dark color
  fills.
- Source markers in tables/figure captions are acceptable when all rows share
  the same source; otherwise mark the individual row or data cell.
- The final section must contain two tables: `资料来源清单` and `待核验事项清单`.
  Do not place source tables at the beginning.

## Useful With Existing Skills

- Use `aiotcap-deep-research` first when the industry baseline is weak.
- Use `primary-market-diligence` after this report when the task moves from
  public disclosure-style writing to investment decision, valuation, terms, and
  risk control.
