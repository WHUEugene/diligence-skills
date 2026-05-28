# 实习尽调小D Skill Pack

这是「实习尽调小D」/ 一级市场尽调 skill 包。它不是把项目 BP、PPT、PDF、公开资料和访谈材料直接改写成一篇“AI 尽调报告”，而是把材料先转成可追溯的证据管理系统：主张拆解、证据分级、自动追问、风险红旗、四模块类招股书报告、投资判断和风控条件。

## Core Differentiation

普通 AI 工具通常会总结文档、回答问题、生成报告。这个 skill 包的定位更垂直：尽调不是文学写作，尽调的本质是证据管理。

1. **主张-证据-结论三元组**
   - 每一个重要报告结论都必须能回到原始 PPT/BP 主张、企业材料、外部资料和证据强度。
   - 报告正文只写证据支持到的程度；没有证据支撑的内容进入待核验事项、追问清单、分期出资条件或否决项。
   - 输出不只是一篇报告，而是一套 claim -> evidence -> conclusion 的可追溯链条。

2. **自动生成追问**
   - 项目方补材料后，AI 不只是总结新增材料，而是判断哪些材料缺失、哪些材料互相矛盾、哪些结论只有企业单方证据、哪些数据口径不一致、哪些问题需要二轮追问。
   - 追问必须映射到“要证明什么、要什么材料、缺口影响什么投资判断”。
   - 红旗清单优先服务投资经理和领导快速决策，完整报告排在后面。

3. **机构自己的垂直尽调记忆库**
   - 不把“有记忆”当作卖点本身。通用 agent 也能记住代码库、工作流和用户偏好；本包强调的是机构尽调记忆。
   - 可沉淀的信息包括：机构过去做过哪些项目、哪些行业报告常用、哪些数据源可信、某类项目常见造假点、领导喜欢的报告结构、每次必问问题、红旗出现后的处理规则。
   - 当运行环境支持长期记忆时，skill 应优先复用机构偏好、历史问题模板和行业红旗；当没有长期记忆时，也应在本次工作目录中保留可复用的机构记忆笔记。

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
- `claim_evidence_conclusion_matrix.md`: traceable claim -> evidence -> conclusion matrix.
- `followup_questions.md`: missing, contradictory, single-sided, inconsistent, and second-round follow-up questions.
- `institution_memory_notes.md`: reusable vertical diligence lessons when durable memory is unavailable.
- `*.json`: structured payload for DOCX generation.
- `商务尽调资料准备清单.docx`: formal five-column diligence checklist.
- `04_prospectus_style_report_draft.md`: editable intermediate report.
- `05_prospectus_style_report.docx`: formal four-module prospectus-style report.
- Source registry, evidence gap matrix, visual asset inventory, red-flag list, and quality audit outputs.

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
