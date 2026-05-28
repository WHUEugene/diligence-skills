# Figure And Table Source Rules

Formal prospectus-style diligence reports need local evidence near the data.
The final source list is not enough.

## Figure Classes

Use these classes deliberately:

| Class | Examples | Source rule |
|---|---|---|
| Public data chart | market size, growth rate, shipment, listed-company revenue, capex benchmark | Redraw from verified public data. Caption must include source marker such as `资料来源：[A1][M2]`. |
| Analyst logic diagram | industry chain, material route hierarchy, product position, customer validation path, milestone timeline | Draw from public sources plus project evidence. Caption must say `根据...整理` with markers. |
| Project material image | product photo, sample, equipment, process photo from BP/PPT | Re-layout rather than paste raw slide. Caption must say `资料来源：项目商业计划书[B1]` or equivalent. |
| Analyst calculation chart | project-side forecast vs serviceable market, investment ask vs recommended range, scenario revenue forecast | State formula/basis in text or table and cite the sources used. If assumptions are weak, mark `测算，待核验`. |

Do not use screenshots of PPT market charts as final evidence unless the original
public source has been checked. Use the PPT chart as a clue, then find the
source data and redraw.

## Minimum Figure Set For Industrial Project Reports

When the task is a formal report rather than a quick memo, attempt these
figures. If a figure cannot be supported, list it in `待核验事项` or the internal
gap matrix.

1. industry route / substitute technology map;
2. industry chain and project position map;
3. downstream demand or market-size chart;
4. comparable-company or peer revenue/business-position chart;
5. product form or product-position image;
6. process flow chart;
7. main equipment or production stage image;
8. project-side forecast vs serviceable market / capacity absorption chart;
9. investment ask vs staged recommendation chart;
10. revenue/gross-margin scenario chart if enough assumptions exist.

For PPT-only runs, figures 5-7 are usually easiest; figures 3-4 need public
search; figures 8-10 need analyst measurement plus project-side evidence.

## Minimum Tables

Use tables for:

- source registry;
- evidence/gap matrix;
- product system and target applications;
- market boundary and serviceable-market口径;
- comparable companies and relevance/limitations;
- construction/investment composition;
- finance assumptions and scenario outputs;
- risk-control conditions and veto items;
- final pending evidence list.

## Caption Rules

Every figure caption should include:

```markdown
![图X 标题（资料来源：[B1]；根据项目材料整理）](figures/x.png)
```

or:

```markdown
![图X 标题（资料来源：[A1][M2]；作者重绘）](figures/x.png)
```

Every table with shared data source should put the source in the table title or
the line immediately before/after the table. If rows have different sources,
put the marker in the relevant row/cell.

## Formatting Rules

- Use clean report charts: white background, muted blue/gray palette, simple
  bars/lines, readable labels, no decorative gradients.
- Recreate PPT process diagrams in a consistent style instead of embedding
  raw slide screenshots.
- For images from project materials, crop and align them into a figure panel;
  do not include surrounding slide chrome.
- Never leave Markdown syntax such as `**合计**`, leading `-`, or raw image links
  visible in DOCX tables or captions.
