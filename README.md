# Your personal website

A single-page academic site: Bio, Research interests, Publications, Teaching, Education,
and Other activities (with a photo gallery). Plain HTML/CSS — no build step, so it works
directly on GitHub Pages.

## Files

```
site/
├── index.html      ← all your content lives here
├── style.css        ← all styling
├── images/          ← your photos (profile + activity photos)
├── cv.pdf            ← add your CV here (linked from the sidebar)
└── README.md
```

## 1. Edit your content

Open `index.html` in any text editor and replace every `&lt;placeholder&gt;`-style bracket
and generic sentence with your own text:

- **Sidebar**: name, title/department, university, location, email, CV link, and social links.
- **Bio** (`#bio`): 2–3 sentences about who you are and what you work on.
- **Research interests** (`#research`): a short framing paragraph + a list of areas
  (edit the `<li>` items inside `.tag-list`).
- **Publications** (`#publications`): duplicate the `<article class="pub">...</article>`
  block for each paper — title, authors, venue/year, and links (PDF/code/bibtex).
- **Teaching** (`#teaching`) and **Education** (`#education`): duplicate the
  `<div class="timeline-item">...</div>` block for each entry.
- **Other activities** (`#activities`): duplicate `<figure class="gallery-item">...</figure>`
  for each photo. Add `class="gallery-item span-2"` to make a photo wider (good for one
  standout photo per row of three).

## 2. Add your photos

Replace the placeholder files in `images/` with your own photos, keeping the same file names
(or update the `src=` paths in `index.html` to match new file names):

- `images/profile.jpg` — your headshot, ideally square (e.g. 400×400px).
- `images/activity1.jpg`, `activity2.jpg`, `activity3.jpg`, `activity4.jpg` — photos of
  hobbies/activities you love. Add as many `<figure class="gallery-item">` blocks and image
  files as you like — the gallery grid wraps automatically.

Keep individual photos under ~1–2MB (resize/compress first) so the page loads quickly.
Free tools: [squoosh.app](https://squoosh.app) or `sips`/Preview on Mac.

## 3. Add your CV (optional)

Drop a `cv.pdf` file into the site folder — the sidebar "CV" link already points to it.

## 4. Preview locally

Just double-click `index.html` to open it in a browser, or run a tiny local server so
relative paths behave exactly like they will online:

```bash
cd site
python3 -m http.server 8000
# then open http://localhost:8000 in your browser
```

## 5. Put it on GitHub and make it live (GitHub Pages)

1. **Create a GitHub account** if you don't have one: https://github.com/join

2. **Create a new repository** named exactly:
   ```
   <your-github-username>.github.io
   ```
   (This exact naming pattern is what makes GitHub Pages auto-publish it as your personal
   site at `https://<your-github-username>.github.io`.) Leave it public, and don't
   initialize it with a README (you already have one).

3. **Upload your files.** Easiest way (no command line needed):
   - Open your new repo on GitHub → click **"Add file" → "Upload files"**.
   - Drag in `index.html`, `style.css`, `README.md`, `cv.pdf`, and the whole `images/`
     folder (drag the folder in directly; GitHub preserves the folder structure).
   - Scroll down, add a commit message like "Initial site", click **"Commit changes"**.

   Or, if you're comfortable with the command line:
   ```bash
   cd site
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-username>.github.io.git
   git push -u origin main
   ```

4. **Turn on GitHub Pages** (usually automatic for `username.github.io` repos, but check):
   - In your repo, go to **Settings → Pages**.
   - Under "Build and deployment" → **Source**, choose **Deploy from a branch**.
   - Branch: `main`, folder: `/ (root)` → **Save**.

5. **Wait ~1–2 minutes**, then visit `https://<your-username>.github.io`. Your site is live.

6. **Making future updates**: edit files directly on GitHub (pencil icon on any file) or
   push new commits from your machine — the live site updates automatically within a minute
   or two of each commit.

## Notes

- If you'd rather host it at a repo like `myportfolio` instead of `username.github.io`,
  you can — just enable Pages the same way in Settings, and your site will live at
  `https://<username>.github.io/myportfolio/` instead.
- Want a custom domain (e.g. `yourname.com`)? GitHub Pages supports this under
  **Settings → Pages → Custom domain** — you'll need to buy the domain separately and
  point its DNS at GitHub.
