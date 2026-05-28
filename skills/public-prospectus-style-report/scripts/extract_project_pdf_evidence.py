#!/usr/bin/env python3
"""Create a page-level evidence index and rendered page images for a project PDF."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import fitz  # PyMuPDF


NUMBER_RE = re.compile(
    r"\d[\d,.]*\s*(?:亿元|万元|万平方米|平方米|亩|吨|GWh|MWh|Wh/kg|μm|um|nm|%|年|个月|条|台|套)"
)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def page_title(text: str, page_no: int) -> str:
    lines = [clean(line) for line in text.splitlines() if clean(line)]
    if not lines:
        return f"第{page_no}页"
    for line in lines[:8]:
        if 4 <= len(line) <= 45 and not NUMBER_RE.search(line):
            return line
    return lines[0][:45]


def classify_page(text: str) -> list[str]:
    compact = text.replace(" ", "")
    labels: list[str] = []
    rules = [
        ("项目概况", ("项目", "公司", "主体", "建设")),
        ("产品技术", ("产品", "技术", "工艺", "专利", "指标", "复合铜箔")),
        ("市场行业", ("市场", "行业", "需求", "客户", "竞争")),
        ("产能设备", ("产线", "设备", "产能", "厂房", "建设")),
        ("财务投资", ("投资", "收入", "利润", "成本", "毛利")),
        ("融资交易", ("融资", "估值", "股权", "出资")),
        ("风险待核验", ("风险", "问题", "待", "不确定")),
    ]
    for label, terms in rules:
        if any(term in compact for term in terms):
            labels.append(label)
    return labels or ["项目材料"]


def evidence_items(text: str) -> list[str]:
    nums = NUMBER_RE.findall(text)
    snippets: list[str] = []
    sentences = re.split(r"(?<=[。；;])", clean(text))
    for sentence in sentences:
        if NUMBER_RE.search(sentence) or any(term in sentence for term in ("客户", "订单", "专利", "产能", "投资", "融资", "收入", "复合铜箔")):
            snippets.append(sentence[:180])
    result = snippets[:8]
    if nums and not result:
        result.append("可见数字：" + "、".join(nums[:12]))
    return result


def write_markdown(out: Path, source_id: str, pdf: Path, pages: list[dict]) -> None:
    lines = [
        "# 输入材料逐页证据索引",
        "",
        f"- 来源编号：{source_id}",
        f"- 文件：{pdf}",
        f"- 页数：{len(pages)}",
        "- 证据属性：项目方材料，未独立验证；可作为项目方口径，不直接证明客户、订单、收入、技术达标或估值。",
        "",
        "| 页码 | 标题/主题 | 证据标签 | 可见事实/数字 | 页面图 |",
        "|---:|---|---|---|---|",
    ]
    for page in pages:
        facts = "<br>".join(page["items"]) if page["items"] else "未抽取到可直接引用事实，需视觉复核"
        labels = "、".join(page["labels"])
        lines.append(f"| {page['page_no']} | {page['title']} | {labels} | {facts} | {page['image']} |")
    (out / "00_input_evidence_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_visual_inventory(out: Path, source_id: str, pages: list[dict]) -> None:
    lines = [
        "# 视觉资产清单",
        "",
        f"- 来源编号：{source_id}",
        "- 页面截图均可作为视觉复核材料；正式报告中只使用产品、工艺、产线、项目图示等与正文判断直接相关的页面。",
        "",
        "| 页码 | 图片路径 | 初步用途 | 报告引用规则 |",
        "|---:|---|---|---|",
    ]
    for page in pages:
        use = "可作为报告图示候选" if any(label in page["labels"] for label in ("产品技术", "产能设备", "市场行业")) else "仅作证据复核"
        lines.append(f"| {page['page_no']} | {page['image']} | {use} | 资料来源：项目材料[{source_id}] |")
    (out / "00_visual_assets_inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_gap_matrix(out: Path, source_id: str, pages: list[dict]) -> None:
    page_labels = {label for page in pages for label in page["labels"]}
    slots = [
        ("重大事项提示", "可部分复刻", "根据项目阶段、投资规模、客户/订单证据缺口形成重大事项。"),
        ("项目概览", "可部分复刻" if "项目概况" in page_labels else "需项目方补充", "项目名称、主体、产品、投资计划可来自项目材料；主体工商、股权、授权需外部/项目方核验。"),
        ("行业研究", "需外部公开搜索", "复合铜箔行业边界、技术路线、市场空间、竞争格局需用招股书、年报、行业报告、公告交叉验证。"),
        ("主体与股权", "需项目方补充", "需要营业执照、股权结构、实控人、历史沿革、项目公司设立文件。"),
        ("业务与技术", "可部分复刻" if "产品技术" in page_labels else "需项目方补充", "PPT可写产品/工艺口径；客户测试、检测报告、专利权属、批量稳定性需补证据。"),
        ("生产与募投", "可部分复刻" if "产能设备" in page_labels or "财务投资" in page_labels else "需项目方补充", "建设计划和投资额可列示为项目方口径；设备清单、报价、产能测算、环评能评需核验。"),
        ("财务预测", "可部分复刻" if "财务投资" in page_labels else "需项目方补充", "PPT预测只能作为项目方口径；需财务模型、成本、售价、良率、产能利用率底稿。"),
        ("风险因素", "可直接复刻", "围绕客户验证、量产良率、技术路线替代、资金需求、证据不足形成风险。"),
        ("结论与投资建议", "可部分复刻", "只能给证据约束下的阶段性判断和风控条件，不能直接给确定估值/投资结论。"),
    ]
    lines = [
        "# 母版复刻缺口矩阵",
        "",
        f"- 项目材料来源：{source_id}",
        f"- 项目方材料可转写比例估计：{sum(bool(p['items']) for p in pages)}/{len(pages)} 页有可抽取事实。",
        "- 正式尽调正文可支持比例估计：约 35%-45%，取决于公开资料和招股书可补充的行业/可比部分。",
        "- 独立投资判断可支持比例估计：约 15%-25%，客户、订单、检测、设备、财务底稿缺失时不得写成确定结论。",
        "",
        "| 母版槽位 | 当前状态 | 处理规则 |",
        "|---|---|---|",
    ]
    for slot, status, rule in slots:
        lines.append(f"| {slot} | {status} | {rule} |")
    (out / "00_replication_gap_matrix.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--source-id", default="B1")
    parser.add_argument("--dpi", type=int, default=160)
    args = parser.parse_args()

    pdf = Path(args.pdf).expanduser().resolve()
    out = Path(args.output_dir).expanduser().resolve()
    image_dir = out / "page_images"
    out.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf))
    pages: list[dict] = []
    full_text_parts: list[str] = []
    zoom = args.dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    for idx, page in enumerate(doc, 1):
        text = page.get_text("text")
        full_text_parts.append(f"\n\n--- page {idx} ---\n{text}")
        img = image_dir / f"page_{idx:02d}.png"
        page.get_pixmap(matrix=matrix, alpha=False).save(str(img))
        pages.append(
            {
                "page_no": idx,
                "title": page_title(text, idx),
                "labels": classify_page(text),
                "items": evidence_items(text),
                "image": str(img),
                "text_chars": len(text),
            }
        )

    (out / "source_text.txt").write_text("\n".join(full_text_parts), encoding="utf-8")
    (out / "project_pdf_evidence.json").write_text(json.dumps({"pdf": str(pdf), "source_id": args.source_id, "pages": pages}, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(out, args.source_id, pdf, pages)
    write_visual_inventory(out, args.source_id, pages)
    write_gap_matrix(out, args.source_id, pages)
    print(json.dumps({"ok": True, "pages": len(pages), "output_dir": str(out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
