---
name: 3d-asset-library
description: Find, download, catalogue, and prepare freely licensed 3D character or prop assets for CAD and fabrication work. Use when sourcing an external 3D asset, not when designing precise mechanical geometry from scratch.
---

# 3D Asset Library

Build a traceable local asset library without confusing an artist mesh with editable CAD.

## Choose an asset type deliberately

- For a logo, stencil, outline, cut-through pattern, or shallow engraving, prefer SVG or DXF. Keep the original vector, then import it into FreeCAD as sketches or wires.
- For mechanical components that must be dimensionally edited, prefer FCStd, STEP, IGES, or a documented parametric source such as SCAD.
- For a sculpted character, prefer original `.blend` when available; GLB/glTF is the next best exchange format. Treat STL, OBJ, and 3MF as mesh assets, not editable CAD.
- Do not convert a dense character mesh to STEP merely to make it look like CAD. That generally makes FreeCAD booleans slow and less reliable.

## Source and licensing rules

Search and inspect before downloading. Keep the source page URL, creator, license, download date, source format, and SHA-256 in the asset manifest.

- Prefer CC0, CC-BY, or an explicit permissive creator license. Respect attribution and share-alike requirements.
- "Free download" and "personal use" are not commercial-use permissions. Preserve those restrictions in the manifest.
- Do not collect or redistribute trademarked/copyrighted characters merely because an upload is marked free. For a private one-off, flag the character owner and the asset page terms; for anything public or commercial, require permission or choose an original character.
- Never bypass a login, paywall, CAPTCHA, Cloudflare challenge, or download restriction. If authentication is required, open the official login page and ask the user to complete it.

## Library layout

For 3D work, keep the library under `D:\3D\asset-library` unless the user specifies a different location. Use one folder per acquired asset:

```text
D:\3D\asset-library\
  character-name\source-slug\
    raw\              # unmodified source download
    derived\          # conversions and print-ready copies
    manifest.json      # provenance, license, geometry notes
    preview.png
```

Keep each project under its own `D:\3D\<project-name>` directory and reference the library asset in that project's manifest. Do not silently copy a derived asset without recording its origin.

## CLI helper

Use `scripts/asset_library.py` for predictable download and provenance capture:

```powershell
python scripts/asset_library.py fetch --url <official-download-url> --asset-dir D:\3D\asset-library\character\source-slug --creator <name> --license <license> --source-page <page-url>
python scripts/asset_library.py inspect --asset-dir D:\3D\asset-library\character\source-slug
```

The helper accepts only a direct URL that the user is authorized to download. It does not search or circumvent host access controls.

## Vector catalogues

For SVG or DXF motifs, read [references/vector-sources.md](references/vector-sources.md) before sourcing. It routes to Wikimedia Commons, Openverse, Iconify, SVG Repo, and GitHub, with the license check appropriate to each source.

Do not treat an HTML canvas, preview image, or a raster PNG as vector source. Obtain the original SVG/DXF where available; otherwise keep the raster only as a visual reference and ask whether vectorization is authorized. When a source supplies SVG only, derive DXF locally with Inkscape if the FreeCAD workflow needs DXF, and retain both the raw SVG and derived DXF in the asset folder.

## Sketchfab

Sketchfab is the preferred searchable character catalogue when its individual model license is acceptable. Its Download API requires a user-authenticated Sketchfab account and returns GLB/glTF/USDZ, not the creator's original FBX/OBJ source. Read [references/sketchfab.md](references/sketchfab.md) before using it. If no token is available, ask the user to sign in through the official browser page or to provide a user-created API token through their normal secret mechanism; never request that it be pasted into chat.

## CAD handoff

Before joining an acquired asset to a product, check scale, orientation, manifoldness, facet count, and minimum printable feature size. For an intricate character decoration, use Blender for mesh repair/placement and FreeCAD for the parametric enclosure. For a vector motif, use FreeCAD directly. Record whether the final result is a through-cut, embossed relief, separate inlay, or merely a render asset.
