#!/usr/bin/env python3
"""Trace a simple raster reference into an SVG using the local VTracer CLI."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="PNG, JPEG, WebP, or other VTracer-supported raster")
    parser.add_argument("output", type=Path, help="output SVG path")
    parser.add_argument("--preset", choices=("bw", "poster", "photo"), default="bw")
    parser.add_argument("--simplify", type=float, default=1.5, help="curve simplification in px")
    parser.add_argument("--filter-speckle", type=int, default=8, help="discard regions smaller than this px")
    parser.add_argument("--adaptive", action="store_true", help="adaptive threshold for uneven scans")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"input is not a file: {args.input}")
    if not 0 <= args.filter_speckle <= 128:
        parser.error("--filter-speckle must be between 0 and 128")
    if args.simplify < 0:
        parser.error("--simplify must be non-negative")
    executable = shutil.which("vtracer")
    if executable is None:
        print("VTracer is not installed or not on PATH. Install a verified release from https://github.com/visioncortex/vtracer/releases, then retry.", file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        executable, str(args.input), str(args.output), "--preset", args.preset,
        "--mode", "spline", "--filter-speckle", str(args.filter_speckle),
        "--simplify", str(args.simplify),
    ]
    if args.adaptive:
        command.extend(["--clustering", "bw", "--adaptive"])
    completed = subprocess.run(command, text=True, capture_output=True)
    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr)
    if completed.returncode or not args.output.is_file():
        return completed.returncode or 1
    print(f"Created {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
