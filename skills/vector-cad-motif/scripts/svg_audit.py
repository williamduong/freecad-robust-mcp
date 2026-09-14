#!/usr/bin/env python3
"""Report basic CAD-readiness checks for an SVG file."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


DISALLOWED = {"image", "mask", "clippath", "text", "filter"}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()
    try:
        root = ET.parse(args.svg).getroot()
    except (OSError, ET.ParseError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    tags = [local_name(element.tag) for element in root.iter()]
    paths = [element for element in root.iter() if local_name(element.tag) == "path"]
    commands = sum(len(re.findall(r"[AaCcHhLlMmQqSsTtVvZz]", path.get("d", ""))) for path in paths)
    unsupported = sorted(set(tags) & DISALLOWED)
    print(f"viewBox: {root.get('viewBox', 'missing')}")
    print(f"paths: {len(paths)}")
    print(f"path commands: {commands}")
    print(f"embedded/risky elements: {', '.join(unsupported) if unsupported else 'none'}")
    if not paths:
        print("FAIL: no path geometry found", file=sys.stderr)
        return 1
    if unsupported:
        print("WARN: remove or convert risky elements before FreeCAD import", file=sys.stderr)
    if commands > 2000:
        print("WARN: dense SVG; simplify paths before FreeCAD import", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
