# ankitpremrajka.github.io

Personal website, hosted with GitHub Pages, served at [premrajka.com](https://premrajka.com).

## Structure

```
index.html          Landing page — intro + list of posts
posts/               One static .html file per post
  first-post.html
assets/
  css/style.css      Shared stylesheet for index + posts
  img/                Images used in posts (empty for now)
CNAME                Custom domain config for GitHub Pages
robots.txt            Points crawlers at the sitemap
sitemap.xml            List of indexable pages, kept in sync by hand
```

## Adding a new post

1. Copy `posts/first-post.html` to `posts/your-new-post.html` and fill it in.
2. Add a new `<li>` entry to the post list in `index.html` linking to it, with a one-line summary.
3. Add the post's URL and `<lastmod>` date to `sitemap.xml`.
4. Add matching `<meta name="description">` and Open Graph/Twitter Card tags to the post's `<head>` (see an existing post for the pattern).
5. Commit and push to `main` — GitHub Pages redeploys automatically within a minute or two.

## Local preview

No build step — just open `index.html` directly in a browser, or run a tiny local server:

```
python3 -m http.server 8000
```

then visit http://localhost:8000
