#!/usr/bin/env python3
"""Audit a prospectus-style report draft for the leader's four-module structure."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


EXPECTED = [
    "一、行业情况",
    "二、项目业务情况",
    "三、项目在行业环境中的优劣势",
    "四、投资方案与风控措施",
    "资料来源与待核验事项",
]

FORBIDDEN_HEADINGS = [
    "重要提示",
    "重大事项提示",
    "重要声明",
    "报告边界",
    "使用说明",
    "附录",
    "第一章 释义",
    "第二章 概览",
    "发行人基本情况",
    "公司治理",
    "投资者保护",
    "有关声明",
    "备查文件",
]

STRICT_SUBHEADINGS = {
    "一、行业情况": ["行业定义", "产业链", "下游需求", "竞争格局", "行业风险"],
    "二、项目业务情况": ["项目基本情况", "产品方案", "技术工艺", "投资规模", "财务预测"],
    "三、项目在行业环境中的优劣势": ["潜在优势", "主要短板", "可比公司对标"],
    "四、投资方案与风控措施": ["投资判断", "分期出资", "先决条件", "交易条款", "否决项"],
}

CITATION_RE = re.compile(r"\[[A-Z]{1,5}\d+\]")
IMAGE_RE = re.compile(r"^!\[(?P<alt>.*)\]\((?P<path>[^)]+)\)\s*$")
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
DATA_RE = re.compile(
    r"\d[\d,.]*\s*(?:亿元|万元|万套|万台|万个|吨|亩|平方米|%|MPa|W/\(m[·.。]?K\)|W/m[·.。]?K|W/mK|年|个月)"
)
FORBIDDEN_BODY_TERMS = [
    "免责声明",
]
FIGURE_SOURCE_TERMS = ("资料来源", "数据来源", "来源")
BODY_GAP_RE = re.compile(r"未提供|尚未提供|未取得|尚未取得|无法确认|不能确认|待验证事项|不将其纳入")
STRICT_FORBIDDEN_PATTERNS = [
    (re.compile(r"\b(?:XXX|TBD|TODO|N/A)\b", re.I), "placeholder token", False),
    (re.compile(r"(?<![A-Za-z])xx(?![A-Za-z])", re.I), "placeholder xx", False),
    (re.compile(r"某某|待补充|数据待完善|此处可写|模板|占位"), "template/placeholder wording", False),
    (re.compile(r"\[(?:缺资料|需外部搜索|需项目方补充|PPT事实|PPT可推断|PPT-only结论)\]"), "working evidence label left in formal report", False),
    (
        re.compile(
            r"可能需要(?:进一步)?(?:补充|提供|核实)?[^，。；;\n]{0,40}(?:数据|资料|文件|底稿|证明|报告|合同|清单)"
            r"|可能需要(?:进一步)?(?:补充|提供|核实)"
            r"|建议(?:后续)?(?:进一步)?(?:补充|提供|核实)"
            r"|后续可(?:进一步)?(?:补充|核实)"
        ),
        "vague future-data wording",
        True,
    ),
]


def collect_headings(text: str) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            headings.append((lineno, len(match.group(1)), match.group(2).strip()))
    return headings


def audit(path: Path, strict: bool = False) -> dict:
    text = path.read_text(encoding="utf-8")
    headings = collect_headings(text)
    errors: list[str] = []
    warnings: list[str] = []

    h2 = [(line, title) for line, level, title in headings if level == 2]
    actual = [title for _, title in h2]
    if actual[: len(EXPECTED)] != EXPECTED:
        errors.append(f"Top-level H2 headings must start exactly as {EXPECTED}; got {actual}")
    if len(actual) != len(EXPECTED):
        errors.append(f"Expected exactly {len(EXPECTED)} top-level H2 headings; got {len(actual)}")

    for lineno, _level, title in headings:
        for forbidden in FORBIDDEN_HEADINGS:
            if forbidden in title:
                errors.append(f"Forbidden heading at line {lineno}: {title}")

    for lineno, line in enumerate(text.splitlines(), 1):
        for forbidden in FORBIDDEN_BODY_TERMS:
            if forbidden in line:
                errors.append(f"Forbidden report body term at line {lineno}: {forbidden}")

    final_start = None
    for lineno, title in h2:
        if title == "资料来源与待核验事项":
            final_start = lineno
            break
    if final_start is None:
        errors.append("Missing final section: 资料来源与待核验事项")
    else:
        for lineno, level, title in headings:
            if lineno < final_start and level <= 3 and ("资料来源" in title or "待核验" in title):
                errors.append(f"Source/gap heading appears before final section at line {lineno}: {title}")

    if strict:
        for lineno, raw in enumerate(text.splitlines(), 1):
            in_final_section = final_start is not None and lineno >= final_start
            for pattern, label, allow_final_section in STRICT_FORBIDDEN_PATTERNS:
                if allow_final_section and in_final_section:
                    continue
                if pattern.search(raw):
                    errors.append(f"Forbidden {label} at line {lineno}: {raw.strip()[:90]}")

        by_section: dict[str, list[str]] = {key: [] for key in STRICT_SUBHEADINGS}
        current = None
        for _lineno, level, title in headings:
            if level == 2 and title in by_section:
                current = title
            elif level == 3 and current:
                by_section[current].append(title)
        for section, required in STRICT_SUBHEADINGS.items():
            joined = " ".join(by_section.get(section, []))
            for item in required:
                if item not in joined:
                    errors.append(f"Missing subheading containing `{item}` under `{section}`")

        citation_count = len(CITATION_RE.findall(text))
        if citation_count < 18:
            errors.append(f"Expected at least 18 inline source markers in strict mode; got {citation_count}")

        figure_count = 0
        for lineno, raw in enumerate(text.splitlines(), 1):
            image = IMAGE_RE.match(raw.strip())
            if not image:
                continue
            figure_count += 1
            alt = image.group("alt")
            if not any(term in alt for term in FIGURE_SOURCE_TERMS):
                errors.append(f"Figure caption missing source wording at line {lineno}: {alt[:90]}")
            if not CITATION_RE.search(alt):
                errors.append(f"Figure caption missing source marker at line {lineno}: {alt[:90]}")
        if figure_count < 4:
            warnings.append(f"Strict report has only {figure_count} figures; industrial reports usually need more visual evidence.")

        table_count = 0
        in_table = False
        for raw in text.splitlines():
            is_row = bool(TABLE_ROW_RE.match(raw.strip()))
            if is_row and not in_table:
                table_count += 1
            in_table = is_row
        if table_count < 6:
            warnings.append(f"Strict report has only {table_count} tables; check whether product, finance, peers, risks, and source/gap tables are covered.")

        source_section = False
        body_gap_lines = 0
        for lineno, raw in enumerate(text.splitlines(), 1):
            line = raw.strip()
            if line.startswith("## 资料来源与待核验事项"):
                source_section = True
            if source_section or not line or line.startswith("#") or line.startswith("|") or line.startswith("!["):
                continue
            if BODY_GAP_RE.search(line):
                body_gap_lines += 1
            if DATA_RE.search(line) and not CITATION_RE.search(line):
                errors.append(f"Quantitative claim missing inline source marker at line {lineno}: {line[:90]}")
        if body_gap_lines > 8:
            warnings.append(
                "正文 contains many missing-evidence/boundary paragraphs; "
                "formal reports should usually omit unsupported slots and keep evidence gaps in the final section."
            )

    if not text.strip().startswith("# "):
        warnings.append("Draft should start with a single H1 report title.")

    return {
        "path": str(path),
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "h2_headings": actual,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("draft", help="Markdown report draft")
    parser.add_argument("--strict", action="store_true", help="Require expected subheadings")
    parser.add_argument("--json", action="store_true", help="Print JSON result")
    args = parser.parse_args()

    result = audit(Path(args.draft), strict=args.strict)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PASS" if result["ok"] else "FAIL")
        for key in ("errors", "warnings"):
            for item in result[key]:
                print(f"{key[:-1].upper()}: {item}")
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
