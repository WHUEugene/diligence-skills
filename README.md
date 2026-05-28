# 实习尽调小D Skill Pack

这是「实习尽调小D」/ 一级市场尽调 skill 包，用于把项目 BP、PPT、PDF、公开资料和内部访谈材料转成可交付的尽调清单、四模块类招股书报告、投资判断和风控条件。

## Included Skills

- `primary-market-diligence`: 一级市场投资研究、商务尽调、BP/PPT 证据拆解、尽调资料准备清单、投资方案与风控措施。
- `public-prospectus-style-report`: 公开资料拟招股书/类招股书报告，包含可比公司选择、招股书资料采集、证据分级、四模块报告审计和 DOCX 生成。

## Install

See [INSTALL.md](INSTALL.md) for copy-paste commands.

Quick Codex install:

```bash
git clone https://github.com/WHUEugene/diligence-skills.git
cd diligence-skills
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
rsync -a skills/primary-market-diligence "${CODEX_HOME:-$HOME/.codex}/skills/"
rsync -a skills/public-prospectus-style-report "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Quick Hermes install:

```bash
git clone https://github.com/WHUEugene/diligence-skills.git
cd diligence-skills
mkdir -p "${HERMES_HOME:-$HOME/.hermes}/skills"
rsync -a skills/primary-market-diligence "${HERMES_HOME:-$HOME/.hermes}/skills/"
rsync -a skills/public-prospectus-style-report "${HERMES_HOME:-$HOME/.hermes}/skills/"
```

## Usage

Use `primary-market-diligence` when the user asks for:

- 一级市场项目研究、商业尽调、投资 memo、投前判断。
- 根据 BP/PPT/项目材料生成商务尽调问题清单或资料准备清单。
- 把公司材料、公开资料、访谈线索转成行业情况、公司业务、优劣势、投资方案与风控措施。

Use `public-prospectus-style-report` when the user asks for:

- 类招股书报告、公开资料拟招股书、按招股书格式写报告。
- 使用可比上市公司招股书/年报搭建正式四模块报告。
- 对 BP/PPT-only 证据做页级证据索引、视觉资产清单和缺口矩阵后再写报告。

## Inputs

Typical inputs are:

- BP, PPT, PDF, project deck, company intro, financial forecast, contracts, test reports, capex plan, customer/order evidence.
- Public sources such as prospectuses, annual reports, exchange filings, government pages, standards, patents, company registry and litigation records.
- Feishu/Hermes group attachments and recent group context mirrored by the runtime.

## Outputs

The skills are designed to produce:

- `brief.md`: internal evidence extraction note when needed.
- `*.json`: structured payload for DOCX generation.
- `商务尽调资料准备清单.docx`: formal five-column diligence checklist.
- `04_prospectus_style_report_draft.md`: editable intermediate report.
- `05_prospectus_style_report.docx`: formal four-module prospectus-style report.
- Source registry, evidence gap matrix, visual asset inventory, and quality audit outputs.

## Feishu Interaction Contract

For Feishu/Hermes group use:

- Do not narrate parser failures, package installs, OCR retries, search attempts, or internal tool choices in the group.
- Use recent downloaded attachments and mirrored group history before asking the user to resend files.
- Ask only one concise blocking question when necessary.
- For DOCX delivery, the final message should be short and include a `MEDIA:` attachment directive with an existing absolute DOCX path supplied by the runtime.
- Do not paste the full checklist/report into the group when a DOCX deliverable was requested.

## DOCX Rules

For diligence checklists, use `skills/primary-market-diligence/scripts/build_diligence_checklist_docx.py`.

Checklist format:

- A4 landscape.
- Title exactly `商务尽调资料准备清单`.
- Fixed five columns: `序号 / 需了解的核心问题 / 推荐提供的资料 / 核心目的 / 资料提供状态`.
- Twelve standard first-level categories.
- Blank status cells for the company to fill.

For prospectus-style reports, use `skills/public-prospectus-style-report/scripts/build_prospectus_style_docx.py` after running `audit_four_module_report.py`.

Report format:

- Four substantive modules plus final `资料来源与待核验事项`.
- No issuer/sponsor/auditor/lawyer declarations.
- No `重要提示`, `免责声明`, `报告边界`, `附录`, or placeholder prose.
- Inline source markers for quantitative claims, tables, and figures.

## What Is Not Included

This package intentionally excludes raw client materials, formal reports, rendered images, downloaded files, caches, `.env` files, local machine paths, and deployment-private records.
