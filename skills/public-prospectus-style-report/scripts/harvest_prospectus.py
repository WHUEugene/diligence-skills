#!/usr/bin/env python3
"""Download, scan, extract, and audit prospectus-style source files."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path


DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 prospectus-harvester/1.0"}


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def slug(text: str, limit: int = 80) -> str:
    text = re.sub(r"[\\/:*?\"<>|\s]+", "_", text.strip())
    text = re.sub(r"_+", "_", text).strip("_")
    return (text or "source")[:limit]


def infer_doc_type(path_or_name: str) -> str:
    name = path_or_name.lower()
    if "annual" in name or "年报" in name or "年度报告" in name:
        return "annual_report"
    if "招股" in path_or_name or "prospectus" in name or "ipo" in name:
        return "prospectus"
    if name.endswith((".html", ".htm")):
        return "web_snapshot"
    return "source"


def read_registry(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def write_registry(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n", encoding="utf-8")


def upsert_record(path: Path, record: dict) -> None:
    records = read_registry(path)
    key = record["id"]
    replaced = False
    for idx, existing in enumerate(records):
        if existing.get("id") == key:
            records[idx] = {**existing, **record}
            replaced = True
            break
    if not replaced:
        records.append(record)
    write_registry(path, records)


def suffix_from_url(url: str, fallback: str = ".pdf") -> str:
    parsed = urllib.parse.urlparse(url)
    suffix = Path(parsed.path).suffix
    if suffix and len(suffix) <= 8:
        return suffix
    return fallback


def fetch_url(url: str, dest: Path) -> None:
    parsed = urllib.parse.urlparse(url)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if parsed.scheme == "file":
        src = Path(urllib.request.url2pathname(parsed.path))
        shutil.copy2(src, dest)
        return
    if parsed.scheme in ("", None):
        src = Path(url)
        if src.exists():
            shutil.copy2(src, dest)
            return
    request = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    with urllib.request.urlopen(request, timeout=45) as response:
        dest.write_bytes(response.read())


def extract_pdf(pdf: Path, out: Path, force: bool = False) -> dict:
    if out.exists() and out.stat().st_size > 1000 and not force:
        text = out.read_text(encoding="utf-8", errors="ignore")
        return {"method": "existing", "chars": len(text), "path": str(out)}
    out.parent.mkdir(parents=True, exist_ok=True)
    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        result = subprocess.run([pdftotext, "-layout", str(pdf), str(out)], text=True, capture_output=True)
        if result.returncode == 0:
            text = out.read_text(encoding="utf-8", errors="ignore")
            return {"method": "pdftotext", "chars": len(text), "path": str(out)}

    errors = []
    if pdftotext:
        errors.append(f"pdftotext failed: {result.stderr.strip()}")
    else:
        errors.append("pdftotext not found")

    try:
        import fitz  # type: ignore

        doc = fitz.open(str(pdf))
        text_parts = []
        for page in doc:
            text_parts.append(page.get_text("text"))
        text = "\n".join(text_parts)
        out.write_text(text, encoding="utf-8")
        return {"method": "pymupdf", "chars": len(text), "path": str(out), "fallback_errors": errors}
    except Exception as exc:  # pragma: no cover - depends on optional package
        errors.append(f"pymupdf failed: {exc}")

    try:
        from pdfminer.high_level import extract_text  # type: ignore

        text = extract_text(str(pdf))
        out.write_text(text, encoding="utf-8")
        return {"method": "pdfminer", "chars": len(text), "path": str(out), "fallback_errors": errors}
    except Exception as exc:  # pragma: no cover - depends on optional package
        errors.append(f"pdfminer failed: {exc}")

    out.write_text("", encoding="utf-8")
    return {"method": "none", "chars": 0, "path": str(out), "error": "; ".join(errors)}


def extract_html(src: Path, out: Path, force: bool = False) -> dict:
    if out.exists() and out.stat().st_size > 1000 and not force:
        text = out.read_text(encoding="utf-8", errors="ignore")
        return {"method": "existing", "chars": len(text), "path": str(out)}
    raw = src.read_text(encoding="utf-8", errors="ignore")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    text = html.unescape(re.sub(r"\s+", " ", raw)).strip()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return {"method": "html-strip", "chars": len(text), "path": str(out)}


def extract_file(raw: Path, extracted_dir: Path, force: bool = False) -> dict:
    out = extracted_dir / f"{raw.stem}.txt"
    suffix = raw.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(raw, out, force=force)
    if suffix in (".html", ".htm", ".php", ".phtml"):
        return extract_html(raw, out, force=force)
    return {"method": "unsupported", "chars": 0, "path": str(out), "error": f"Unsupported suffix {raw.suffix}"}


def inspect_text(text_path: Path, doc_type: str) -> dict:
    if not text_path.exists():
        return {
            "chars": 0,
            "contains": {},
            "score": 0,
            "needs_visual_fallback": doc_type in ("prospectus", "annual_report"),
        }
    text = text_path.read_text(encoding="utf-8", errors="ignore")
    term_groups = [
        ("招股说明书", ["招股说明书"]),
        ("风险因素", ["风险因素"]),
        ("业务与/和技术", ["业务与技术", "业务和技术"]),
        ("募集资金", ["募集资金"]),
        ("财务会计", ["财务会计"]),
        ("管理层", ["管理层"]),
    ]
    if doc_type == "annual_report":
        term_groups = [
            ("年度报告", ["年度报告"]),
            ("主营业务", ["主营业务"]),
            ("风险", ["风险"]),
            ("财务", ["财务"]),
            ("管理层", ["管理层"]),
        ]
    contains = {label: any(term in text for term in terms) for label, terms in term_groups}
    score = sum(1 for ok in contains.values() if ok)
    needs_visual_fallback = doc_type in ("prospectus", "annual_report") and (len(text) < 10000 or score < 3)
    return {"chars": len(text), "contains": contains, "score": score, "needs_visual_fallback": needs_visual_fallback}


def add_url(args: argparse.Namespace) -> dict:
    raw_dir = Path(args.raw_dir)
    extracted_dir = Path(args.extracted_dir)
    suffix = suffix_from_url(args.url)
    raw_path = raw_dir / f"{args.id}_{slug(args.name)}{suffix}"
    fetch_url(args.url, raw_path)
    doc_type = args.doc_type or infer_doc_type(args.name + raw_path.name)
    extraction = extract_file(raw_path, extracted_dir, force=args.force)
    quality = inspect_text(Path(extraction["path"]), doc_type)
    record = {
        "id": args.id,
        "name": args.name,
        "source_type": doc_type,
        "url": args.url,
        "raw_path": str(raw_path),
        "extracted_text_path": extraction.get("path"),
        "downloaded_at": now_iso(),
        "evidence_grade": args.evidence_grade,
        "relevance": args.relevance or "",
        "extraction": extraction,
        "quality": quality,
    }
    upsert_record(Path(args.registry), record)
    return record


def scan_local(args: argparse.Namespace) -> dict:
    raw_dir = Path(args.raw_dir)
    extracted_dir = Path(args.extracted_dir)
    registry = Path(args.registry)
    files = sorted(p for p in raw_dir.iterdir() if p.suffix.lower() in (".pdf", ".html", ".htm", ".php", ".phtml"))
    records = []
    for raw_path in files:
        source_id = raw_path.stem.split("_", 1)[0]
        doc_type = infer_doc_type(raw_path.name)
        extraction = extract_file(raw_path, extracted_dir, force=args.force)
        quality = inspect_text(Path(extraction["path"]), doc_type)
        record = {
            "id": source_id,
            "name": raw_path.stem,
            "source_type": doc_type,
            "url": "",
            "raw_path": str(raw_path),
            "extracted_text_path": extraction.get("path"),
            "scanned_at": now_iso(),
            "evidence_grade": "A" if doc_type in ("prospectus", "annual_report") else "B",
            "relevance": "",
            "extraction": extraction,
            "quality": quality,
        }
        upsert_record(registry, record)
        records.append(record)
    return {"count": len(records), "registry": str(registry), "records": records}


def audit(args: argparse.Namespace) -> dict:
    registry = Path(args.registry)
    records = read_registry(registry)
    failures = []
    warnings = []
    by_type: dict[str, int] = {}
    for record in records:
        by_type[record.get("source_type", "unknown")] = by_type.get(record.get("source_type", "unknown"), 0) + 1
        raw = Path(record.get("raw_path", ""))
        text = Path(record.get("extracted_text_path", ""))
        quality = record.get("quality") or inspect_text(text, record.get("source_type", "source"))
        if not raw.exists():
            failures.append({"id": record.get("id"), "reason": "raw_missing", "path": str(raw)})
        if record.get("source_type") == "prospectus" and quality.get("score", 0) < 3:
            item = {"id": record.get("id"), "reason": "low_prospectus_text_score", "quality": quality}
            (failures if args.require_text else warnings).append(item)
        if quality.get("chars", 0) < 1000 and raw.suffix.lower() == ".pdf":
            item = {"id": record.get("id"), "reason": "short_extracted_text", "quality": quality}
            (failures if args.require_text else warnings).append(item)
    result = {
        "registry": str(registry),
        "ok": not failures,
        "count": len(records),
        "by_type": by_type,
        "failures": failures,
        "warnings": warnings,
    }
    if args.output_json:
        Path(args.output_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output_json).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--raw-dir", required=True)
        p.add_argument("--extracted-dir", required=True)
        p.add_argument("--registry", required=True)
        p.add_argument("--force", action="store_true")

    p_add = sub.add_parser("add-url")
    add_common(p_add)
    p_add.add_argument("--id", required=True)
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--url", required=True)
    p_add.add_argument("--doc-type", default="")
    p_add.add_argument("--evidence-grade", default="A")
    p_add.add_argument("--relevance", default="")

    p_scan = sub.add_parser("scan-local")
    add_common(p_scan)

    p_audit = sub.add_parser("audit")
    p_audit.add_argument("--registry", required=True)
    p_audit.add_argument("--output-json", default="")
    p_audit.add_argument(
        "--require-text",
        action="store_true",
        help="Treat short/low-quality text extraction as failure instead of visual-fallback warning.",
    )

    args = parser.parse_args()
    try:
        if args.cmd == "add-url":
            result = add_url(args)
        elif args.cmd == "scan-local":
            result = scan_local(args)
        else:
            result = audit(args)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if isinstance(result, dict) and result.get("ok") is False:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
