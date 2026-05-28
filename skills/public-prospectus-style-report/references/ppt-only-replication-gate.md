# PPT-Only Replication Gate

Use this gate when the only target-specific material is a BP/PPT/招商材料/project
deck. The goal is to avoid turning project-side assertions into a fake formal
diligence report.

## Required Working Files

Create these before drafting the report:

1. `00_input_evidence_index.md`
   - Page number, title, visible facts, numbers, product names, charts/tables,
     images, and uncertain items.
   - Label every item as `PPT事实`, `PPT可推断`, or `缺资料`.
2. `00_visual_assets_inventory.md`
   - List extracted screenshots/images/tables.
   - Mark each asset as `可直接用于报告`, `需重画`, `仅作参考`, or `不能引用`.
   - For each usable image, state the needed caption source, e.g.
     `资料来源：项目商业计划书[B1]`.
3. `00_replication_gap_matrix.md`
   - Compare the intended prospectus-style report against the available PPT
     evidence.
   - For each chapter, table, and figure, mark:
     `可直接复刻`, `可部分复刻`, `需外部公开搜索`, `需项目方补充`, or `不能复刻`.

## Evidence Boundary

Treat all BP/PPT contents as `项目方口径` unless independently verified.

Allowed from PPT-only:

- project name, group self-description, products as申报, construction plan as申报;
- project-side revenue/capex forecasts as申报口径;
- product/process/equipment images as project-side visual materials;
- claims that become diligence questions or verification gaps.

Not allowed from PPT-only:

- definitive customer validation, orders, market share, valuation, investment
  amount, go/no-go conclusion, or independent revenue forecast;
- audited financial language;
- project company ownership, IP ownership, related-party, or legal conclusions;
- market-size numbers copied from PPT charts without source verification.

## Minimum Gap Matrix

For an industrial project, explicitly test these slots:

| Slot | PPT-only rule |
|---|---|
| Industry definition and boundary | If the PPT lists many applications, separate main line from optional/unsupported extensions. |
| Industry market data | PPT charts are discovery clues; use external public sources before formal citation. |
| Technical route competition | If the PPT mentions copper, tungsten-copper, VC, liquid cooling, or other routes, map them as alternatives, not proof of the target route. |
| Project subject | Group facts do not prove project-company facts. Mark project company, equity, governance, and authorization as missing unless disclosed. |
| Products | Product table can be transcribed, but customer, price, quantity, and BOM basis remain missing unless supported. |
| Technical indicators | Parameters need third-party tests, batch data, method, and customer acceptance before becoming validated facts. |
| Production and equipment | Equipment photos need现有/拟购, model, quantity, price, capacity, and ownership. |
| Customers/orders | If no customer list, sampling record, test feedback, or order exists, do not infer demand realization. |
| Finance | BP forecasts are project-side claims; do not create independent scenarios without customer, cost, capacity, and margin evidence. |
| Investment conclusion | With PPT-only evidence, the strongest conclusion is usually “do not close on the申报方案 before evidence is supplied.” |

## Quantitative Output

At the top of `00_replication_gap_matrix.md`, include:

- estimated percentage of project-side facts that can be transcribed;
- estimated percentage of formal diligence正文 that can be supported;
- estimated percentage of independent investment judgment that can be supported;
- number of intended figures/tables that are direct, partial, externally sourced,
  project-side missing, or impossible from current evidence.

## Drafting Rule

In the draft, use these labels when evidence is weak:

- `[PPT事实]`: directly visible in the deck.
- `[PPT可推断]`: a conservative inference from visible deck content.
- `[缺资料]`: required for a formal diligence conclusion but absent.
- `[需外部搜索]`: industry, peer, policy, market, or public-company information.
- `[需项目方补充]`: customer, order, testing, IP, finance, subject, capex, or legal
  proof that only the project side can provide.

Do not hide these labels only in the final source table. Put them near the
paragraph, table, or figure that depends on the evidence.
