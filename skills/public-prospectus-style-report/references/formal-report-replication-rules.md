# Formal Report Replication Rules

Use this reference when the user provides a formal report and asks the agent to
make a new report in the same style from weaker evidence such as PPT/BP plus
public sources.

## Goal

Replicate the reference report's form and writing logic. When the target project
is the same project as the reference report, the reference can also be used as
the factual master to calibrate the generated version; when the target differs,
the reference remains a template only and must not supply facts for the new
target.

The new report should feel like the same class of deliverable: same chapter
rhythm, similar paragraph density, similar table/figure density, same front
matter, same table of contents/definition rhythm where applicable, same source
caption discipline, and the same investment-analysis posture. It must not fill
unknown data with `XXX`, invented assumptions, or generic "need data" prose.
The deliverable must read as a finished report prepared by the analyst, not as a
description of how a skill used a reference document.

## Build A Style Blueprint First

Before drafting, create `01_formal_report_style_blueprint.md` with:

1. section list and subsection list;
2. paragraph role map, such as industry definition, market trend, peer
   benchmark, project fact, calculation, risk judgment, control measure;
3. table inventory: title, columns, data type, source type, and whether the new
   target has enough evidence to reproduce it;
4. figure inventory: title, visual type, data source, and whether the new target
   has enough evidence to redraw it;
5. source-marker style: how captions, table notes, and inline data references
   appear;
6. Word style notes: heading levels, table borders, chart caption placement,
   body paragraph length, and numbering.
7. front-matter map: cover, `重要声明`, `重大事项提示`, `目录`, `释义`, and any
   closing source or appendix-like section that the reference places before or
   after the core chapters.

Use this blueprint as the drafting checklist.

## Front Matter And Author Stance

If the reference report includes front matter, keep it in the generated report
in the same order. `重要声明`, `重大事项提示`, `目录`, and `释义` are part of the
formal report form in that case; do not delete them merely because they are not
one of the four analytical modules.

Do not write process language in the report body. Forbidden stance includes:

- "本报告未使用正式报告中的资料";
- "根据参考报告格式";
- "由于只有PPT";
- "此处按照模板";
- "可补充/可能需要补充XXX".

The report may state evidence boundaries only as substantive diligence
judgments, for example "截至本报告出具日，项目尚未形成收入及正式订单" or "设备
报价单、型号清单和产能测算底稿尚需作为出资前置核验资料". It should not expose
the drafting workflow to the reader.

## Fill Or Omit Slots

For each paragraph/table/figure slot in the reference report:

- `fill`: if the new target or public source has enough evidence, write the
  analogous paragraph/table/figure with source markers;
- `narrow`: if only project-side evidence exists, write it as project-side
 口径 and state only the supported implication;
- `omit/merge`: if no evidence exists and omission does not mislead the reader,
  do not write the slot in the body;
- `condition`: if the missing evidence affects investment feasibility, convert
  it into a condition precedent, staged-funding gate, veto item, or final
  verification row.

Do not use the missing slot as a place to write "可能需要补充资料".

## Figure And Table Replication

A formal reference report often uses charts that were redrawn by the analyst.
The new report should do the same when data exists:

- redraw public market data into clean report-style charts;
- redraw project-side investment composition, revenue plan, capacity plan, and
  use-of-funds data from the PPT/BP if the numbers are explicit;
- use project material screenshots only for product/process/site visuals, with
  clear captions and source markers;
- omit charts whose underlying data is unavailable.

Every chart/table needs a title and source marker. Do not paste a chart without
explaining the source.

When the reference report's visual language is known, reuse it: table grid
weight, header shading, caption placement, figure numbering, source-note wording,
page margins, body font, and heading sizes. A visually different DOCX is a
failed replica even if the words are directionally correct.

## Body Writing Standard

The body should be finished prose:

- concrete number plus source marker where data exists;
- sober comparison where comparable-company data exists;
- bounded conclusion where project evidence is weak;
- no placeholders, no unrendered Markdown, no internal labels, no drafting
  notes.

Acceptable:

```text
项目商业计划书披露，本项目总投资15亿元，其中设备及安装投入占比较高[B1]。在尚未取得设备报价单、设备型号清单及产能测算底稿前，本报告不将该投资额直接作为首期出资依据，而建议将设备清单核验作为首期付款前置条件。
```

Not acceptable:

```text
本项目设备投资较大，可能需要补充设备报价、型号、数量等资料。
```

The first paragraph has a project fact, source, analytical consequence, and
investment-control action. The second paragraph is only a placeholder.

## Final Verification Section

The final `资料来源与待核验事项` section is where evidence gaps live. It should
name exact documents and exact impact. It should not be an appendix and should
not contain generic requests such as `补充相关资料`.
