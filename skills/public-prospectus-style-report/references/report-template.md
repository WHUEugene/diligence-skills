# Prospectus-Style Four-Module DOCX Report Template

```markdown
# <目标名称>类招股书投资研究报告

## 一、行业情况

### （一）行业定义
### （二）产业链
### （三）下游需求
### （四）竞争格局
### （五）行业风险

写法参考招股书`业务与技术`章节中的`发行人所处行业基本情况及其竞争情况`，
并吸收`风险因素`章节中的行业风险表达。先说明行业边界，再说明上下游，
再说明需求驱动、竞争格局和行业风险。

凡出现市场规模、产量、收入、增长率、客户集中度、技术参数等数据，必须在同句
或相邻表题/图题处加来源角标，例如`[A1]`、`[P2]`。如果用图表示，应写成
`![图1 标题（数据来源：[A1]）](figure.png)`，并在资料来源清单中解释来源。

## 二、项目业务情况

### （一）项目基本情况
### （二）产品方案
### （三）技术工艺
### （四）投资规模
### （五）财务预测

写法参考招股书`业务与技术`章节中的主营业务、主要产品、工艺流程、核心技术，
参考`募集资金运用`章节中的项目建设内容、投资规模、建设周期和项目效益测算，
参考`财务会计信息与管理层分析`章节中的收入、成本、毛利率和盈利能力分析。

项目方商业计划书、PPT、访谈纪要等项目方口径统一编号为`[B1]`、`[B2]`等；
对这类数据可以使用，但必须标出来源，并在待核验事项中列出需要第三方验证的
财务、客户、订单、技术和环评证据。

## 三、项目在行业环境中的优劣势

### （一）潜在优势
### （二）主要短板
### （三）可比公司对标

写法参考招股书`业务与技术`章节中的竞争地位、竞争优势和可比公司描述，
并结合`风险因素`章节披露技术、市场、客户、原材料、产能消化和财务风险。
不要写成泛泛SWOT；优势和短板必须落到项目证据和可比公司差距。

## 四、投资方案与风控措施

### （一）投资判断
### （二）分期出资
### （三）先决条件
### （四）交易条款
### （五）否决项

写法参考招股书`募集资金运用`中的资金安排和项目可行性论证，
以及`风险因素`中的风险揭示方式，但内容必须转换为一级市场投资语言：
是否投、怎么分期投、达到什么条件才投、交易文件如何保护投资人、哪些事项一票否决。

## 资料来源与待核验事项

### （一）资料来源清单

| 编号 | 来源名称 | 类型 | 路径/URL | 使用模块 | 证据等级 |
|---|---|---|---|---|---|

### （二）待核验事项清单

| 待核验事项 | 需要的证据 | 影响模块 |
|---|---|---|
```

Rules:

- If a formal reference report is available, first create a style blueprint and
  imitate its section rhythm, paragraph roles, table/figure density, captions,
  and source-marker placement. Replicate the form, not unsupported facts.
- If the task is a formal commercial diligence report, do not use this
  four-module template as the visible structure. Use
  `investment-decision-report-contracts.md`: create the four working matrices,
  then generate the fixed front matter and nine正文 chapters. The four modules
  remain the underlying analysis logic, not the visible report目录.
- Do not add standalone sections titled `重要提示`, `重大事项提示`, `重要声明`,
  `报告边界`, `使用说明`, or `附录`.
- Do not add a `免责声明`. Public-data limits belong in `待核验事项清单`.
- Do not expand the report into a full IPO prospectus table of contents unless
  the user explicitly asks for it.
- Every quantitative statement should carry an inline source marker such as
  `[A1]` or `[B1]`; a source table only at the end is insufficient.
- Do not leave placeholders, missing-evidence labels, or template prose in the
  formal report. If the evidence is absent, either omit the unsupported claim or
  write a bounded limitation sentence and place the exact required document in
  `待核验事项清单`.
- Do not write generic future-work sentences such as `可能需要客户数据`,
  `建议后续补充订单资料`, or `后续可进一步核实`. Formal正文 should either state a
  sourced fact, state why a conclusion is not adopted, or convert the item into
  a specific investment gate.
- Do not overuse evidence-gap prose in正文. If a reference-report paragraph slot
  cannot be supported and omitting it will not mislead the reader, omit or merge
  it instead of writing a negative placeholder.
- Use charts/figures when the source data supports them, especially for product
  revenue composition, investment composition, market demand, or peer comparison.
  For industrial projects, also attempt route/alternative-material maps,
  industry-chain/project-position diagrams, product image panels, process flow
  charts, equipment panels, serviceable-market comparison charts, and
  investment-scale comparison charts. See `figure-table-source-rules.md` for
  caption/source rules.
- Place sources and evidence gaps only in the final section.
- The formal deliverable should be generated as `.docx`; this Markdown is only
  the editable intermediate.
