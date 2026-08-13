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
```

## Adding a new post

1. Copy `posts/first-post.html` to `posts/your-new-post.html` and fill it in.
2. Add a new `<li>` entry to the post list in `index.html` linking to it, with a one-line summary.
3. Commit and push to `main` — GitHub Pages redeploys automatically within a minute or two.

## Local preview

No build step — just open `index.html` directly in a browser, or run a tiny local server:

```
python3 -m http.server 8000
```

then visit http://localhost:8000
