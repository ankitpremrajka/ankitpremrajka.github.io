# AGENTS.md

Conventions for any coding agent working on premrajka.com. This is the canonical file; `CLAUDE.md` points here.

## The site

- Static site on GitHub Pages, served at https://premrajka.com from the `main` branch. No build step.
- `index.html` — intro, Products (Current), and the Posts list with topic filter chips.
- `posts/*.html` — one file per long-form post.
- `current.html` — landing page for Current, the WhatsApp daily tech digest.
- `current-archive.html` + `current-archive/data/*.json` — archive of past Currents (`index.json` lists months; one JSON file per month).
- `terms.html` — Terms & Conditions and Privacy Policy, including the WhatsApp messaging-program terms.
- `assets/css/style.css` — the one shared stylesheet. `assets/img/` — images, OG cards, favicons.
- `sitemap.xml` — kept in sync by hand. `404.html` lowercases mixed-case paths.

## Workflow

1. Make the change, then preview it locally: `python3 -m http.server 8123` from the repo root.
2. Check it in a real browser: desktop, ~375px phone width (no horizontal scroll), and dark mode.
3. Let the owner review. Don't commit or push until explicitly told to (usually "kill the server, commit and push it").
4. Stop the local server before committing. Commit only the files that belong to the change; leave unrelated work-in-progress (for example an unpublished post) out of the commit.

## Rules that are easy to miss

- **Cache-busting:** whenever `assets/css/style.css` changes, bump `style.css?v=YYYY-MM-DD` on every HTML page, not only the pages you touched. Use the same value everywhere.
- **Sitemap:** when a page is added or its content changes, add it to `sitemap.xml` or update its `<lastmod>`.
- **Terms must match the product:** anything the Current pages promise (question limits, delivery times, countries, how to stop) must agree with the messaging-program section of `terms.html`. When the Terms change, update their effective date.
- **Product name:** the product is "Current". "A Premrajka LLC product" identifies the company; Premrajka LLC also appears in footers and the Terms.
- **Archive data:** never modify `current-archive/data/*.json`. Copy the files in exactly as provided, byte for byte. Query strings on source URLs (NYT `unlocked_article_code`, Bloomberg `accessToken`, WSJ `st`, The Verge `view_token`) are deliberate gift/share codes that let readers open paywalled articles free, so don't strip them.

## Writing posts

- Every post follows the long-form template (see `posts/training-robot-policies.html`): hero with a topic kicker, a sticky contents rail, Parts (`.part-head`) containing sections (`section.s`), and a glossary at the end.
- Every section that isn't the first in its Part opens with a `<p class="bridge">` sentence linking it to the one before. Part intros connect back to the previous Part. Exception: the closing "Bottom line" section has no bridge.
- Posts end with the glossary. Don't add a "Sources" or references section ("This isn't an academic paper"). Facts must still be verified before they're written.
- Plain English first. Reuse an analogy the post already set up rather than inventing a new one.
- Cross-link related posts with a short parenthetical, e.g. `(<a href="other-post.html#s3">Post title</a> covers this)`.
- Time-sensitive claims (funding, launches, approvals, benchmark numbers) need a dated, checked source. Say "reported" or "the company says" when a claim isn't independently confirmed.

### Adding a new post

1. Write `posts/<slug>.html` from the template.
2. Add an entry at the top of the `.post-list` in `index.html`: `data-topics` (any of `ai`, `robotics`, `startup-finance`, `space-tech`), a `post-meta` date and `post-tags` links.
3. Add it to `sitemap.xml`.
4. Create a 1200×630 OG card (`assets/img/og-<slug>.png`) and point the post's `og:image` and `twitter:image` at it.
5. Add cross-links from and to related posts.

## Design

- Palette (CSS custom properties in `style.css`): paper `#EFF1EC`, ink `#1C2620`, ink-2 `#41504A`, ink-3 `#6E7C75`, rule `#CBD2C7`, cobalt `#2F5DD1` (dark mode `#5B8CFF`), clay `#A8503C`, mustard `#C98A16`. Cobalt is the one strong accent.
- Fonts: Bricolage Grotesque (headings), Source Serif 4 (body), IBM Plex Mono (labels).
- Homepage section headings stay mono and clay-coloured.
- Keep page-specific styles scoped (e.g. `.ca-*` for the archive, `.dlm` for the diffusion post's figures).

## Social and skills

- Reusable workflows live in `.claude/skills/` (the canonical copy):
  - `post-editorial-review` — structural review of one post's flow and continuity.
  - `post-to-x-thread` — turns a post into an X thread (up to 9 posts, ≤280 characters each, counted with `count.py`), opening and closing on verified recent news, tagging verified company accounts, with 1600×900 image cards in the site palette.
- `.agents/skills/` is a copy for other agents. Edit `.claude/skills/` first, then re-copy it there. The copy differs in only two places: its `count.py` path points at `.agents/skills/…`, and the editorial review's browser step names any browser tool instead of only `claude-in-chrome`. Don't find-and-replace "Claude" in the copy: "Claude Design" is the real tool used for image prompts.
- The X account is @ankitp. Never post to X or LinkedIn on the owner's behalf; draft only.
