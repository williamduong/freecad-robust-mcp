#!/usr/bin/env python3
"""Download an authorized 3D asset and record compact provenance metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def safe_filename(value: str) -> str:
    candidate = Path(value).name
    if not candidate or candidate in {".", ".."}:
        raise ValueError("Supply --filename when the download URL has no file name.")
    return candidate


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"schema_version": 1, "downloads": []}
    with path.open(encoding="utf-8") as handle:
        content = json.load(handle)
    if not isinstance(content.get("downloads"), list):
        raise ValueError(f"Invalid manifest: {path}")
    return content


def fetch(args: argparse.Namespace) -> None:
    parsed = urllib.parse.urlparse(args.url)
    if parsed.scheme not in {"https", "http"} or not parsed.netloc:
        raise ValueError("--url must be an absolute http(s) URL.")
    asset_dir = Path(args.asset_dir).resolve()
    raw_dir = asset_dir / "raw"
    derived_dir = asset_dir / "derived"
    raw_dir.mkdir(parents=True, exist_ok=True)
    derived_dir.mkdir(exist_ok=True)
    filename = safe_filename(args.filename or urllib.parse.unquote(Path(parsed.path).name))
    destination = raw_dir / filename
    if destination.exists() and not args.force:
        raise FileExistsError(f"Refusing to overwrite {destination}; use --force after verifying the target.")

    request = urllib.request.Request(args.url, headers={"User-Agent": "Codex-3d-asset-library/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        with tempfile.NamedTemporaryFile(dir=raw_dir, delete=False) as temp_handle:
            shutil.copyfileobj(response, temp_handle)
            temporary = Path(temp_handle.name)
    temporary.replace(destination)
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()

    manifest_path = asset_dir / "manifest.json"
    manifest = load_manifest(manifest_path)
    manifest["downloads"].append(
        {
            "file": str(destination.relative_to(asset_dir)).replace("\\", "/"),
            "source_url": args.url,
            "source_page": args.source_page,
            "creator": args.creator,
            "license": args.license,
            "downloaded_at": datetime.now(timezone.utc).isoformat(),
            "sha256": digest,
            "notes": args.notes or "",
        }
    )
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"downloaded": str(destination), "sha256": digest, "manifest": str(manifest_path)}, indent=2))


def inspect(args: argparse.Namespace) -> None:
    asset_dir = Path(args.asset_dir).resolve()
    manifest_path = asset_dir / "manifest.json"
    manifest = load_manifest(manifest_path)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    fetch_parser = subparsers.add_parser("fetch", help="download an authorized direct asset URL")
    fetch_parser.add_argument("--url", required=True)
    fetch_parser.add_argument("--asset-dir", required=True)
    fetch_parser.add_argument("--creator", required=True)
    fetch_parser.add_argument("--license", required=True)
    fetch_parser.add_argument("--source-page", required=True)
    fetch_parser.add_argument("--filename")
    fetch_parser.add_argument("--notes")
    fetch_parser.add_argument("--force", action="store_true")
    fetch_parser.set_defaults(handler=fetch)
    inspect_parser = subparsers.add_parser("inspect", help="print an asset manifest")
    inspect_parser.add_argument("--asset-dir", required=True)
    inspect_parser.set_defaults(handler=inspect)
    try:
        args = parser.parse_args()
        args.handler(args)
        return 0
    except (OSError, ValueError, urllib.error.URLError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
