# VTracer reference

VTracer is the default automatic tracer because it is a maintained MIT-licensed raster-to-SVG engine with a CLI, Python package, and Node package.

Use the official repository and releases: https://github.com/visioncortex/vtracer

For binary/stencil art, begin with:

```powershell
vtracer input.png output.svg --preset bw --mode spline --filter-speckle 8 --simplify 1.5
```

For a scanned drawing with uneven lighting, use `--clustering bw --adaptive`. Increase `--filter-speckle` to remove noise; increase `--simplify` gradually to reduce nodes, then check that ears, eyes, and bridge details remain intact.

Do not use a colour-photo trace directly in a small FDM motif. Prepare a high-contrast reference or simplify the illustration first.

The Windows application/release is preferable to compiling from source. If the user explicitly chooses source installation and Rust is available, the upstream command is `cargo install vtracer-cli`.
