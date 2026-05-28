# Investment-Decision Commercial Diligence Contracts

Use this reference when the input is a business plan, PPT,招商材料, project PDF,
or when a formal commercial diligence report is used as the reference style.
The central rule is: do not rewrite the source deck in order. Extract every
material project-side claim, test it, narrow it, and reallocate it to the
chapter where it affects investment decisions.

## Fixed Formal Structure

Use this structure in formal commercial diligence mode:

```text
封面
重要声明
重大事项提示
目录
释义
第一章 项目概览
第二章 行业研究
第三章 出资主体与项目主体基本情况
第四章 公司业务与技术
第五章 同业竞争、关联交易与集团协同
第六章 财务分析与财务预测
第七章 募集资金运用与落地匹配度
第八章 风险因素与风险控制
第九章 尽调结论与投资建议
附录/资料来源与待核验事项
```

The visible structure is the formal report form. The hidden logic remains:
industry, project business, project strengths/weaknesses in the industry,
investment plan and risk controls.

## Required Working Matrices

Before writing the report, create these four matrices. If code execution is
available, save them in `00_investment_decision_matrices.json` and export to
`.xlsx` with `scripts/build_investment_decision_workbooks.py`.

### 1. PPT主张清单

Fields:

```text
slide_no
ppt_section
original_claim
claim_type
quantitative_value
report_section
evidence_required
external_verification_needed
risk_level
```

Typical mappings:

| Project-side claim | Formal report destination | Treatment |
|---|---|---|
| 集团概况、全球布局、行业地位 | 第一章、第三章、第五章 | Extract subject background and platform capability; also assess dependence on the group. |
| 项目优势、应用场景、市场分析 | 第二章、第四章 | Define industry boundary first; verify demand and route competition before accepting market space. |
| 产品方案、技术指标 | 第一章、第四章 | Convert into product-system table and judge the span between material capability and manufacturing capability. |
| 建设内容与规模 | 第一章、第六章、第七章 | State the申报 scale, then test whether it matches stage, orders and capacity evidence. |
| 经济效益、达产产值、纳税 | 第六章、第九章 | Treat as project-side forecast; build independent cautious scenarios only if evidence supports them. |
| 政策诉求、贷款、贴息、奖励 | 第七章、第八章、第九章 | Convert into fund-use supervision, milestone payment, and closing conditions. |
| 工艺流程、主要设备 | 第四章、第八章、附录 | Assess industrialization ability; require existing/proposed boundary, equipment models, quantities, quotes and capacity. |
| 社会效益、就业、平台建设 | 第七章 | Use as landing-match supplement, not as core investment return evidence. |

### 2. 尽调问题与资料索取清单

Fields:

```text
question_id
report_section
diligence_question
required_document
owner_or_source
why_it_matters
decision_use
priority
```

Ask for exact documents, not generic data. Examples: customer validation
records, orders or framework agreements, third-party testing reports, project
company and equity structure, technology/IP ownership, existing/proposed
production-line boundary, equipment quotes/models/quantities/capacity,
financial forecast workpapers, serviceable-market calculation, comparable
company/public industry data.

### 3. 证据矩阵

Fields:

```text
ppt_claim
company_evidence
interview_evidence
external_evidence
evidence_strength
conclusion
report_sentence
follow_up_question
```

The `report_sentence` field should already be written in formal report voice.
It must include the fact, source marker, narrowed conclusion, and where
necessary the investment consequence.

### 4. 风险与前置条件清单

Fields:

```text
risk_item
fact_basis
risk_judgment
investment_impact
condition_precedent
control_clause
verification_document
report_section
```

Every major risk should become a control action. Do not stop at "存在风险".

| Risk | Weak writing | Required writing |
|---|---|---|
| 客户验证未完成 | 存在客户验证风险 | Set customer test pass, small-batch order, or first revenue as staged funding conditions. |
| 技术无专利 | 存在知识产权风险 | Require key IP ownership to enter the project company and patent/application milestones after investment. |
| 集团依赖强 | 存在独立性风险 | Require group support commitment and related-party pricing rules. |
| 设备产能不明 | 存在产能风险 | Make equipment list, quote, model, quantity, capacity and ownership review a payment condition. |

## Chapter Contracts

### 重要声明

Function: define report identity and responsibility boundary.

Must cover: use restriction, information base, project-side materials and
interviews, public information limits, forward-looking statements, and the rule
that conclusions should be read as a whole. Do not call it `免责声明`.

### 重大事项提示

Function: place the most decision-relevant facts and risks before the body.

Write 3 to 5 items. Each item must contain:

```text
事实基础 -> 风险判断 -> 投资影响
```

Do not write a project亮点 list. This section is the early version of the final
investment conclusion.

### 释义

Function: make the report feel formal and avoid subject confusion.

Include report terms, target project, project company, group/entity names,
technology/product terms, downstream terms, transaction terms and key financing
terms. A short token list is not enough when the project involves multiple
subjects, products, technologies or investment conditions.

### 第一章 项目概览

Function: let the decision-maker understand what the project is within a few
pages.

Inputs: project material, interview notes, public subject data, source registry.

Must answer: project and subject, industry overview, business/technology
overview, finance/funding overview, and summary investment view.

Do not write a long industry study here.

### 第二章 行业研究

Function: redefine market口径, not prove that the market is large.

Must start with research boundary. If the PPT lists many applications, separate
the product's current application, likely extension, and unsupported broad
market. Do not equate a large industry market with the target's serviceable
market.

Must cover: industry definition, route competition, demand drivers, industry
chain, competitive landscape, comparable-company evidence, and industry risks.

### 第三章 出资主体与项目主体基本情况

Function: decide who invests, who implements, who owns assets, and who bears
obligations.

Must cover:出资主体, project company, equity/governance, related parties,
ultimate controller if available, asset/IP/customer/resource ownership, and
missing subject documents.

If group facts and project company facts differ, write the difference as an
investment前置条件.

### 第四章 公司业务与技术

Function: verify what the project sells, where the technology comes from, what
stage customer validation is in, and whether production can be scaled.

Must cover: product system, technical route, technology source, IP/commercial
secret status, third-party testing, customer samples and feedback, orders or
framework agreements, production line status, equipment, supply chain, and
milestones.

Forbidden: unsupported statements such as `技术领先`, `客户需求旺盛`, `市场前景广阔`.

### 第五章 同业竞争、关联交易与集团协同

Function: treat group resources as both support and risk.

Must write both sides:

```text
集团协同带来的研发/客户/供应链/资金优势
集团依赖导致的独立经营、关联交易、资源持续性和利益冲突风险
```

Convert unresolved group reliance into support commitments, related-party
pricing mechanisms and information-rights clauses.

### 第六章 财务分析与财务预测

Function: test whether project-side forecasts can be used for investment.

Always separate:

```text
项目方自报预测
本报告审慎测算/情景判断
```

If customer, capacity, cost, price, gross margin and capex support are weak, do
not create a false independent forecast. State the project-side forecast, narrow
its use, and convert missing support into conditions or scenario boundaries.

### 第七章 募集资金运用与落地匹配度

Function: evaluate the money requested and policy/funding ask.

Must cover: project-side申报 investment, use of funds, construction schedule,
equipment/factory/working-capital split, local landing fit, government support
requests, and whether current stage supports the requested scale.

If the project asks for a large amount, write it as:

```text
项目方申报金额 -> 对应完整产能/量产假设 -> 当前证据是否支持 -> 分期建议
```

### 第八章 风险因素与风险控制

Function: convert risk into transaction design.

For each major risk, write:

```text
风险事实 -> 投资影响 -> 风控措施/条款
```

Must include where relevant:分期投资, valuation adjustment, repurchase,
conditions precedent, information disclosure, fund-use supervision, governance
rights, veto items and post-investment milestones.

### 第九章 尽调结论与投资建议

Function: make the final investment judgment explicit.

Must include: project stage classification, core support factors, core
unverified matters, investment recommendation, investment amount/scenario
logic if supported, unsupported project-side asks, and transaction条件.

Use conditional support/no-current-support language when the evidence requires
it. Do not end with vague "可进一步关注".

## Formal Voice

Use phrases like:

```text
根据项目方提供资料及访谈口径……
截至本报告出具日，项目方尚未提供……
从尽调视角看……
本报告认为……
该事项仍需进一步核验……
不宜直接等同于……
不应作为当前收入测算和估值基础……
建议作为投资交割或资金拨付的前置条件……
```

Do not write process language such as `按模板`, `根据参考报告`, `由于只有PPT`,
`此处可补充`, `可能需要数据`, or `不使用正式报告中的资料`.

## Quality Checklist

Before DOCX generation, confirm:

1. Fixed formal structure is present when required.
2. Major事项提示 contains facts, risks and investment impact.
3. 释义 is substantial enough for subjects, products, technologies and deal terms.
4. Every chapter contains diligence judgment, not PPT retelling.
5. Project-side statements, provided materials, interviews, public sources and
   report judgment are distinguishable.
6. Unsupported project-side claims are narrowed or converted into conditions.
7. Industry research starts with boundary and does not copy broad market size
   as the target's market.
8. Finance separates project-side forecast from report judgment.
9. Customer, order, production line, team, IP, group reliance and capex are
   assessed where relevant.
10. Investment recommendation includes staged funding, valuation adjustment,
    repurchase, conditions precedent, information rights and fund-use controls
    where relevant.
11. Every data point has a nearby source marker.
12. Tables and figures are sourced; charts are redrawn where public/project data
    supports them.
