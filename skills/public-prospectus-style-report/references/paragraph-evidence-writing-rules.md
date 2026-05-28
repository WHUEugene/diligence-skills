# Paragraph Evidence Writing Rules

Use this reference when drafting the formal DOCX report. It exists to prevent
template prose, placeholder data, and vague "need more data" paragraphs.

## Core Rule

The report body should be finished analysis in the reference report's style, not
a list of missing materials. Every paragraph must do one of four things:

1. state an evidence-backed fact with a nearby source marker;
2. explain a calculation or assumption with its source and limitation;
3. make an analyst judgment that follows from named evidence;
4. state that a specific conclusion is not adopted because specific evidence is
   absent, but only where that boundary is necessary for investment judgment.

Do not write a paragraph whose only function is "this section should discuss
X" or "the project may need X data." Those belong in the working notes, not the
formal report.

## No Placeholder Policy

The formal report must not contain:

- `XXX`, `xx`, `某某`, `待补充`, `TODO`, `TBD`, `N/A`;
- `[缺资料]`, `[需外部搜索]`, `[需项目方补充]` labels in正文;
- sentences such as `可能需要进一步提供相关数据`, `建议后续补充相关资料`,
  `此处可写行业情况`, `数据待完善`;
- soft request paragraphs such as `可能需要客户数据`, `建议项目方补充订单资料`,
  or `后续可进一步核实`. The formal report can require evidence, but it must
  name the exact evidence and connect it to an investment gate.

Use exact wording instead:

- `截至本报告可核验资料范围，项目方未提供客户测试反馈、第三方检测报告及正式订单；因此，本报告不将客户验证通过或订单放量作为已实现事实。`
- `项目方商业计划书披露达产年收入15.25亿元[B1]；但未提供客户、单价、销量、成本及产能爬坡底稿，故该预测仅作为项目方申报口径列示，不作为本报告投资规模测算基础。`

## When Evidence Exists

Write concrete paragraphs:

```text
项目商业计划书披露，本项目总投资15亿元，其中设备投资9.5亿元、土地及厂房2.5亿元、铺底流动资金3亿元[B1]。该投资强度对应较完整的材料制备、压铸成型、机械加工和检测交付产能；在未取得正式订单及产能消化证据前，上述投资规模不宜直接作为首期出资安排。
```

Requirements:

- include the number;
- include the source marker;
- state the business implication;
- do not add unsupported facts.

## When Evidence Does Not Exist

Do not invent a substitute. Either omit the paragraph or write a bounded
negative/limitation paragraph. Prefer omission when the absent item is merely a
reference-report slot that cannot be supported. Use a limitation paragraph only
when the absent evidence would otherwise make a project-side claim look verified:

```text
截至本报告可核验资料范围，项目方未提供送样客户名单、客户测试反馈、正式小批量订单或框架协议。本报告因此仅将“客户导入”作为待验证事项，而不将其纳入收入实现基础。
```

This is acceptable because it states a verified evidence gap and its analytical
effect. It is not acceptable to write:

```text
客户方面可能需要补充客户名单、订单等资料，后续可进一步核实。
```

The difference is not tone; it is evidentiary function. The acceptable paragraph
defines which conclusion is rejected. The unacceptable paragraph merely leaves a
blank for later.

## Paragraph Patterns By Topic

| Topic | Write if evidence exists | If evidence is absent |
|---|---|---|
| 客户验证 | state customer type, test stage, date, test items, feedback, next milestone, source | say no customer list/test feedback/order was provided; do not claim validation or revenue conversion |
| 订单/协议 | state contract party, product, amount, term, status, source | say no formal order/framework agreement was provided; do not treat forecast as backlog |
| 第三方检测 | state institution, report number/date, sample, method, result, source | say technical indicators remain project-side claims; require report before using as validated performance |
| 项目主体 | state company name, USCC, capital, shareholders, responsibility boundary, source | distinguish group background from project-company facts; do not infer ownership |
| IP权属 | state patent/trade-secret owner, transfer/license, project-company rights, source | say IP ownership cannot be confirmed; do not count group patents as project patents |
| 产线/设备 | state existing vs planned, model, quantity, capacity, price, ownership, source | say equipment images/plan are申报口径; do not infer current production capability |
| 财务预测 | state assumptions, volume, price, cost, margin, ramp, source | list project-side forecast only as申报口径; do not create independent forecast |
| 可服务市场 | state BOM, unit value, customer demand, penetration, source | do not use total industry market as project revenue base |
| 可比公司 | state peer data from annual report/prospectus and limitation | do not substitute peer facts for target facts |

## Final Section Handling

The final `资料来源与待核验事项` section should be precise, not vague:

| 待核验事项 | 需要的证据 | 影响模块 |
|---|---|---|
| 客户验证是否进入小批量 | 送样客户名单、测试反馈、样品编号、正式小批量订单或客户邮件确认 | 财务预测、投资规模、分期出资 |

Do not write `补充相关资料` as the evidence requirement. Name the exact
document, data table, or confirmation needed.

Good final evidence rows use exact nouns:

- `送样客户名单、测试反馈、样品编号、正式小批量订单或客户邮件确认`
- `客户/产品/单价/销量/产能爬坡/成本/毛利率预测底稿`
- `设备供应商报价单、设备型号清单、单台产能、付款节点、交付周期`

Bad rows use generic nouns:

- `相关资料`
- `客户数据`
- `财务数据`
- `进一步说明`
