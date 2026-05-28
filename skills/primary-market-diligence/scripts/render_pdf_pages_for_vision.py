#!/usr/bin/env python3
"""Render PDF pages to images for vision-model reading."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import fitz  # PyMuPDF


def parse_pages(spec: str, total_pages: int) -> list[int]:
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start, end = int(start_s), int(end_s)
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= total_pages)


def default_pages(total_pages: int, max_pages: int) -> list[int]:
    if total_pages <= max_pages:
        return list(range(1, total_pages + 1))
    head_count = max(1, max_pages - 2)
    selected = set(range(1, min(head_count, total_pages) + 1))
    selected.update(range(max(1, total_pages - 1), total_pages + 1))
    return sorted(selected)[:max_pages]


def render_pdf(
    pdf_path: Path,
    out_dir: Path,
    pages: Iterable[int],
    dpi: int,
    fmt: str,
    jpeg_quality: int,
) -> list[dict[str, object]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    manifest: list[dict[str, object]] = []

    with fitz.open(pdf_path) as doc:
        stem = pdf_path.stem
        for page_num in pages:
            page = doc.load_page(page_num - 1)
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            image_path = out_dir / f"{stem}_p{page_num:03d}.{fmt}"
            if fmt.lower() in {"jpg", "jpeg"}:
                pix.save(str(image_path), jpg_quality=jpeg_quality)
            else:
                pix.save(str(image_path))
            manifest.append(
                {
                    "page": page_num,
                    "image_path": str(image_path.resolve()),
                    "width": pix.width,
                    "height": pix.height,
                    "dpi": dpi,
                }
            )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Render PDF pages to images for vision models.")
    parser.add_argument("--pdf", required=True, help="Input PDF path")
    parser.add_argument("--out", required=True, help="Output directory for page images")
    parser.add_argument("--max-pages", type=int, default=30, help="Maximum pages to render by default")
    parser.add_argument("--pages", default="", help="Optional page list, e.g. 1,3,5-9")
    parser.add_argument("--dpi", type=int, default=160, help="Render DPI")
    parser.add_argument("--format", choices=["png", "jpg", "jpeg"], default="jpg")
    parser.add_argument("--jpeg-quality", type=int, default=90)
    args = parser.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    with fitz.open(pdf_path) as doc:
        total_pages = doc.page_count

    pages = parse_pages(args.pages, total_pages) if args.pages else default_pages(total_pages, args.max_pages)
    manifest = render_pdf(pdf_path, out_dir, pages, args.dpi, args.format, args.jpeg_quality)

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "pdf": str(pdf_path),
                "total_pages": total_pages,
                "rendered_pages": pages,
                "images": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"manifest": str(manifest_path), "count": len(manifest)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
