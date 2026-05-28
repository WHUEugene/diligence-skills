# Prospectus Format Reference

This reference is based on three local A-share IPO prospectuses already stored in
the project:

- 美利信 2023 IPO prospectus: `materials/prospectus_harvest/extracted/PH-001_meilixin_2023_ipo_prospectus.txt`
- 铭利达 2022 IPO prospectus: `materials/prospectus_harvest/extracted/PH-002_minglida_2022_ipo_prospectus.txt`
- 飞荣达 2017 IPO prospectus: `materials/prospectus_harvest/extracted/PH-003_feirongda_2017_ipo_prospectus.txt`

## Common A-share Prospectus Skeleton

| Common Chapter | Typical Contents | Public-Style Replication Notes |
|---|---|---|
| 发行概况 / 本次发行概况 | issuance size, price, listing venue, sponsor, intermediary institutions, dates | Usually not applicable to a private project; omit unless there is a real financing transaction. Do not replace with a meta `报告边界` chapter. |
| 重大事项提示 | key commitments, dilution, profit distribution, special risks, post-reporting events | Do not create a standalone `重大事项提示`/`重要提示` chapter for diligence reports. Put material risks in `项目在行业环境中的优劣势与风险因素` or `投资方案与风险控制措施`. |
| 风险因素 | industry, technology, operation, finance, legal, fundraising, project risks | Use as substantive analysis, not as boilerplate. For the default report, combine with strengths/weaknesses in `项目在行业环境中的优劣势与风险因素`. |
| 释义 | company names, technical terms, abbreviations | Replicable. |
| 概览 | issuer basics, business summary, financial data, fundraising use | Partially replicable; financial data often missing for private targets. |
| 发行人基本情况 | establishment, equity, subsidiaries, major shareholders, actual controller, executives, employees | Public registry can fill some; most requires internal documents. |
| 业务与技术 | main business, products, industry, competition, customers, suppliers, assets, core tech, R&D, environment, quality | Most useful public-data chapter; combine target public facts and comparable prospectuses. |
| 公司治理与独立性 / 同业竞争与关联交易 | governance, internal control, independence, competition, related parties, related transactions | Usually cannot be fully verified from public data. Mark missing. |
| 财务会计信息与管理层分析 | audited statements, accounting policies, ratios, revenue, margin, cash flow, assets, liabilities | Not replicable unless audited/internal financial data exists; public comparable benchmarks only. |
| 募集资金运用与未来发展规划 | use of proceeds, project necessity, feasibility, capex, capacity, expansion, impact | Can draft from BP but must mark as project-side claim; benchmark with comparable prospectuses. |
| 投资者保护 | dividend policy, voting, investor relations, commitments | Mostly not applicable before formal issuance; adapt to stakeholder protection / investor rights. |
| 其他重要事项 | material contracts, lawsuits, guarantees, penalties, related-party undertakings | Public litigation/registry can fill some; legal counsel verification missing. |
| 声明 / 附件 | issuer/sponsor/lawyer/auditor declarations | Do not replicate in a public-source report. |

## Default Four-Module Private-Project Report Order

Use this order for the final DOCX deliverable unless the user explicitly asks
for a full IPO-prospectus chapter simulation. The four substantive modules come
from the leader's diligence requirement; prospectuses provide the writing style
and evidence order inside each module.

1. 行业情况: map to `业务与技术`中的`发行人所处行业基本情况及其竞争情况`
   and `风险因素`中的行业风险.
2. 项目业务情况: map to `业务与技术`中的主营业务、产品、工艺、核心技术,
   plus `募集资金运用` and `财务会计信息与管理层分析`.
3. 项目在行业环境中的优劣势: map to `业务与技术`中的竞争地位、竞争优势,
   plus `风险因素`中的技术、市场、客户、原材料和产能风险.
4. 投资方案与风控措施: adapt `募集资金运用`中的可行性 and `风险因素`中的
   风险揭示 into primary-market investment terms.
5. 资料来源与待核验事项: final evidence section only.

Do not add preface/meta chapters before the first module. Sources belong in the
final section only.

## Business And Technology Substructure

This is the most transferable section:

1. 主营业务、主要产品及变化
2. 所处行业基本情况及竞争情况
3. 销售情况和主要客户
4. 采购情况和主要供应商
5. 主要资产情况
6. 核心技术与研发情况
7. 环境保护情况
8. 境外经营情况
9. 质量控制和安全生产

## Fundraising/Megaproject Substructure

For industrial projects:

1. 募集/拟投入资金概况
2. 项目必要性
3. 项目可行性
4. 项目具体情况: location, land, construction, equipment, capacity, timeline
5. 新增产能消化
6. 对财务状况和经营成果的影响
7. 未来发展规划

## Non-Negotiable Boundary

A public-source prospectus-style report must never include:

- issuer or intermediary declarations;
- audited financial statement claims without audited reports;
- definitive legal conclusions without counsel;
- customer/supplier names that only come from unsourced rumors;
- invented ownership, related-party, or governance facts.
