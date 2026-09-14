# Sketchfab access

Use only the official Data and Download APIs.

- Public search can filter downloadable models, face count, and source format.
- Download calls require the user's authenticated account. The API returns a short-lived download URL.
- Returned formats are GLB/glTF/USDZ. Preserve the downloaded archive in `raw`; do not represent it as a parametric source.
- Before downloading, capture the model URL, author, license, triangle count, and whether attribution is required.
- For a trademarked character, the uploader's Creative Commons setting does not grant character-IP rights. Mark the asset as private-use pending user confirmation.

Official docs: https://sketchfab.com/developers/download-api
