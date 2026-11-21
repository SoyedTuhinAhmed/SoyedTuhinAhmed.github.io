# soyedtuhinahmed.github.io

Personal academic website of Soyed Tuhin Ahmed (static HTML/CSS/JS, served by GitHub Pages).

## Editing
- Page text: edit `_src/index.template.html` and `_src/publications.template.html`.
- Publications: edit the `P` list (and `SELECTED`) in `_src/build.py`; abstracts live in `_src/abstracts.json`; PDFs go in `assets/papers/`.
- Rebuild: `python3 _src/build.py` (regenerates `index.html` and `publications.html`; do not edit those directly).
- Styles: `assets/css/style.css` · Scripts: `assets/js/main.js` · Images: `assets/img/`.

`Docs/` (private drafts, statements, cover letters) is git-ignored and never published.
`_legacy/` holds the previous version of the site.
