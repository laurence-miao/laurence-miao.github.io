# Laurence Miao's website

A static Jekyll portfolio, published with GitHub Pages at https://laurence-miao.github.io.

## Preview

Install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open the local URL printed by Jekyll. Build for production with `bundle exec jekyll build`.

## Edit content

- `index.md` contains the homepage introduction; `_layouts/about.html` contains its sections.
- `_data/projects.yml` selects the work shown on the homepage and work index. Work pages live in `work/` with explicit permalinks.
- `_data/writing.yml` contains publications, language labels, and descriptive links. The homepage follows its curated order; the writing index groups entries by year.
- `writing/` contains original articles with explicit permalinks. Add an entry to `_data/writing.yml` to include an article in the writing index.
- `_posts/` contains technical notes. Keep historical dates and add version context when commands have not been revalidated.
- `_data/cv.yml` is shared by the web CV and the PDF generator. Keep descriptions grounded in documented experience and use verified results when adding metrics.

After changing CV data or the social preview, regenerate the assets:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-assets.txt
.venv/bin/python scripts/build_assets.py
```

Review the PDF's rendered pages before publishing. The generated PDF and preview PNG are checked in; GitHub Pages does not run the Python script. Fonts for the social image use Arial on macOS or DejaVu Sans on Linux, with Pillow's default as a fallback.

Canonical URLs, social metadata, the sitemap, and robots.txt all derive from `url` in `_config.yml`. Existing note URLs are preserved.
