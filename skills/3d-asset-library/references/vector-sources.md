# SVG and DXF sources

Use the source that best matches the motif. Record the individual asset page, not merely the search page.

| Source | Best use | Access | License rule |
| --- | --- | --- | --- |
| Wikimedia Commons | Public-domain and Creative Commons illustrations, symbols, historical art | MediaWiki API or direct file page; no login | Read the file page: licenses vary by file. Prefer PD, CC0, CC-BY, or CC-BY-SA as the project allows. |
| Openverse | Cross-source discovery for openly licensed images and SVGs | Website or API; API may require credentials/rate limits | Follow the originating work's license and preserve attribution metadata. |
| Iconify | Open-source icon sets and simple functional motifs | Public API, npm packages, or GitHub; no login | Inspect the icon set metadata, which carries its author and SPDX license. Do not assume one set's license applies to another. |
| SVG Repo | Generic icons, silhouettes, and decorative symbols | Website/direct SVG; no login normally | Verify the individual SVG's displayed license; the site hosts several license families. |
| GitHub | Author-maintained SVG/DXF, OpenSCAD and project-native source | `gh` CLI or HTTPS; public repositories work without login | Read `LICENSE` and the asset's provenance; an open-source code license does not grant a third party's trademark rights. |

## Search and import priorities

1. For decorative production work, prefer one-color, closed-path SVG with a clear license.
2. Favor art with minimum line/gap widths at least 0.8 mm after scaling for FDM. Remove invisible layers, text, clipping masks, and unnecessary detail before import.
3. SVG is generally the better acquisition format. Use Inkscape to create a derived DXF only when a downstream FreeCAD operation specifically prefers DXF.
4. For well-known characters and logos, a permissive vector-file license is not a license to use the underlying trademark. Mark the manifest `ip_status` as `private-use-pending` unless the rights holder expressly permits the intended use.

## Not recommended as library defaults

Do not make Vecteezy, Freepik, random Pinterest/Google Image links, or unverified "free SVG bundle" websites default sources. They may be useful only after checking the individual file's terms, creator, and direct-download legitimacy.

Useful official references:

- Wikimedia Commons SVG help: https://commons.wikimedia.org/wiki/Help:SVG/en
- Openverse API: https://docs.openverse.org/api/reference/index.html
- Iconify icon data: https://iconify.design/docs/icons/icon-data.html
- SVG Repo licensing: https://www.svgrepo.com/page/licensing
