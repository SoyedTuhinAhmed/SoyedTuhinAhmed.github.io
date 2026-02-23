# Soyed Tuhin Ahmed — Academic CV Website

Personal academic portfolio website for [soyedtuhinahmed.github.io](https://soyedtuhinahmed.github.io).

Built with pure HTML5, CSS3, and minimal JavaScript — no build tools, no frameworks.

---

## Folder Structure

```
.
├── index.html          # Main (and only) page — all sections
├── style.css           # All styles, including dark mode & responsive
├── script.js           # Dark mode toggle, mobile nav, pub collapsing
├── .nojekyll           # Tells GitHub Pages to skip Jekyll processing
├── assets/
│   ├── cv.pdf          # Your CV — replace with actual PDF
│   └── img/
│       └── profile.jpg # Your photo — replace with actual image
└── README.md           # This file
```

---

## Deploying on GitHub Pages

1. Push this repository to `https://github.com/SoyedTuhinAhmed/SoyedTuhinAhmed.github.io`
2. Go to **Settings → Pages**
3. Set **Source** to `Deploy from a branch`
4. Choose branch `main` (or `master`), folder `/ (root)`
5. Click **Save** — the site will be live at `https://soyedtuhinahmed.github.io` within a minute

> The `.nojekyll` file ensures GitHub Pages serves the raw HTML without Jekyll processing.

---

## How to Update Your CV

Replace `assets/cv.pdf` with your latest CV file (keep the same filename):

```bash
cp /path/to/your/CV.pdf assets/cv.pdf
git add assets/cv.pdf
git commit -m "Update CV"
git push
```

---

## How to Update Your Profile Photo

Replace `assets/img/profile.jpg` with a square headshot (recommended 400×400px or larger):

```bash
cp /path/to/your/photo.jpg assets/img/profile.jpg
git add assets/img/profile.jpg
git commit -m "Update profile photo"
git push
```

---

## How to Update Publications

All publications are in `index.html` inside the `#publications` section.

Each entry follows this pattern:

```html
<li class="pub-item">
  <div class="pub-meta">
    <span class="pub-id">J12</span>
    <span class="pub-year">2025</span>
    <!-- Optional: -->
    <span class="pub-award">Best Paper Award</span>
  </div>
  <div class="pub-body">
    <p class="pub-title">Your Paper Title Here</p>
    <p class="pub-authors"><strong>S. T. Ahmed</strong>, Co-Author, et al.</p>
    <p class="pub-venue"><em>Journal/Conference Name</em>, Year</p>
  </div>
</li>
```

Add new journals under `#journals-list` and conferences under `#conferences-list`.
Update the `pub-count` span on the `.pub-toggle` button to reflect the new count.

---

## How to Update Links

Open `index.html` and search for `PLACEHOLDER` — replace with your actual Google Scholar and LinkedIn URLs:

- **Google Scholar**: search for `scholar.google.com/citations?user=PLACEHOLDER`
- **LinkedIn**: search for `linkedin.com/in/soyedtuhinahmed`

---

## Dark Mode

Dark mode is automatically detected from the user's system preference and can be toggled via the moon/sun icon in the top-right corner. The preference is saved in `localStorage`.

---

## Local Preview

No build step required. Simply open `index.html` in your browser:

```bash
# Option 1: direct open
open index.html

# Option 2: local server (avoids any CORS issues with fonts)
python3 -m http.server 8000
# then visit http://localhost:8000
```
