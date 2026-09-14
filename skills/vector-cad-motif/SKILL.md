---
name: vector-cad-motif
description: Turn a reference image into a clean SVG motif for engraving, cut-through patterns, or shallow relief in FreeCAD and FDM-printed parts. Use for vectorizing a simple image or drawing a print-safe motif; not for photorealistic illustration.
---

# Vector CAD Motif

Create editable, fabrication-safe vector motifs. The source image is a visual reference; the output must be genuine SVG paths, not a raster embedded in SVG.

## Choose the approach

- For a bold logo, stencil, icon, or one-color line art, use VTracer and simplify the resulting paths.
- For flat artwork with anti-aliased colours, compare a `bw` trace with a colour trace. Prefer the monochrome result when it preserves the recognisable silhouette with materially fewer paths; it is usually cleaner and more reliable for a small FDM motif.
- For a small lid motif with recognisable features, manually redraw the few essential shapes after tracing. Automatic tracing is a starting point, not proof of printability.
- When a character depends on facial features, preserve the hood/head, face field, eyes, nose/mouth, and emblem as separate closed regions (or documented SVG layers). Do not fuse every imported path into one relief merely because it forms a valid solid.
- For photos, gradients, or detailed illustrations, do not force them into a CAD motif. Ask the user whether to use a simplified silhouette instead.

## Reference and rights

Keep the reference source beside the output and record its source URL or user provenance. Do not claim authorship of a traced copyrighted image. For branded characters, use the work only within the user's authorized/private scope and label the source accordingly.

## Fabrication constraints

- Default to a single-color, closed-path SVG with no masks, clip paths, text objects, or embedded images.
- At final physical scale, use at least 0.8 mm for isolated strokes and gaps on a 0.4 mm FDM nozzle; use 1.0 mm when the motif will be a through-cut.
- Avoid disconnected islands for through-cuts unless bridges deliberately retain them. Prefer engraving, relief, or a separate inlay for eyes, skull marks, and tiny face details.
- For an A7 card-box lid, begin with a 35–45 mm motif and validate it in a lid preview before cutting the production part.

## VTracer workflow

Read [references/vtracer.md](references/vtracer.md) before tracing. Do not install VTracer silently. If `vtracer` is unavailable, tell the user to install a verified VTracer release or run the documented installation command.

```powershell
python scripts/trace_motif.py reference.png motif.svg --preset bw
python scripts/svg_audit.py motif.svg
```

Retain the reference and the raw trace. Put cleaned SVGs in `derived`, with a small manifest noting scale, intended operation, and source provenance.
Ensure the final root SVG has a `viewBox`; add one from its width and height when the tracer omits it, so CAD import has a stable coordinate system.

## FreeCAD handoff

Import the audited SVG as geometry, set the physical scale explicitly, and inspect the outline before extrusion. Treat a colour trace as a useful layer map when it separates facial regions cleanly; a monochrome trace can still be the cleaner contour source.

For a recognisable character relief, assign deliberate Z hierarchy rather than one uniform pad: for example a low hood/head field, a distinct face field, recessed eyes and mouth, and a higher small emblem. Keep each printed step at least two layers high (normally 0.3–0.5 mm) and keep small face marks at least 0.8 mm wide or engrave them. Preserve holes and nested contours when converting SVG wires to faces; test the resulting boolean, rather than making each wire an independent filled face.

Use a shallow 0.6–1.2 mm pad or pocket for decorative relief; use a full cut only after confirming every enclosed region has a structural bridge. Before fusion, name or document each semantic region and its intended height/pocket. A single valid fused solid does not prove the character survived conversion.

Export a top orthographic preview as well as the isometric visual QA. At final motif scale, visually confirm that each requested distinguishing feature—at minimum eyes, nose/mouth, and emblem when present—is separately readable through contour, height, or shadow. If a feature disappears, is merged into a background field, or is only visible due to render colour, revise the vector/layer mapping before final STL export.
