---
name: post-to-x-thread
description: Turns one long-form post under posts/*.html on premrajka.com into an X (Twitter) thread of up to 9 posts that opens and closes on a hook grounded in real, verified news. Use this whenever the user asks to share, promote, spin, summarize or "turn into a thread" a post for X/Twitter, or asks for tweets or social copy about a post. Also use it when the user wants an existing thread revised (new ending, added facts, hashtags, images). It drafts the thread text and its images (re-rendered post figures, Claude Design prompts), but never posts to X or edits site files.
---

# Post → X thread

The user uses X as the media channel for premrajka.com: short threads that pull readers into the long-form posts. This skill was distilled from the session that produced the thread for `posts/spectrum-satellites.html`. Every rule below exists because something in that session went wrong or got corrected.

## The shape (fixed)

**Up to 9 posts** (aim for 7–9; use the extra room only when the post has that many ideas worth a post each), each **≤280 characters**, always as a **thread** (the user tried a single long post and went back to threads). Below, N is the last post.

| Post | Job |
|---|---|
| **1. News hook** | A specific, recent, verified news event tied to the post's topic, with a hard number. Then the question the post answers ("Why would X move Y that much?") and 🧵. Ends with 1–2 hashtags. |
| **2 to N−2. The explainer** | One idea per post, taken from the long-form post in its order. Plain English, concrete numbers, no jargon the post itself didn't define. Reuse the post's own analogies (e.g. the spectrum "highway and lanes") rather than inventing new ones. |
| **N−1. The stakes** | Who's winning and why: the players, the money, the moves, mapped back to the explainer. |
| **N. News hook, second angle** | Return to the news from a different angle (e.g. post 1 was the company that lost; the last post is the wider industry fallout). End on a **thought-provoking open question** about what happens next, then the post link, then one niche hashtag. |

**Both the first and the last post must be grounded in real news.** The last post is not a summary or a "what's available today" roundup. The user cut that ending as boring. It's the bigger implication of the news, posed as a question.

## Process

1. **Confirm the post.** Use the one the user names; if none, ask.
2. **Read the whole post.** Pull out the 4–5 ideas that carry the argument, plus the concrete numbers that make them land.
3. **Find the news.** Search for events from roughly the last two weeks tied to the post's subject (deals, launches, rulings, stock moves). Prefer an event with a measurable consequence. Pick a second angle on the same event for the last post.
4. **Verify every number against raw sources, not headlines.** Headlines disagree. For the spectrum thread, outlets quoted 6%, 10%, 14% and 16% for the same move.
   - **Stock moves:** pull daily closes yourself:
     ```bash
     curl -s -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v8/finance/chart/TICKER?period1=$(date -j -f %Y-%m-%d START +%s)&period2=$(date -j -f %Y-%m-%d END +%s)&interval=1d"
     ```
     Also pull `SPY` for the same days to show the move wasn't market-wide.
   - **Check when the news broke before choosing the window.** The SpaceX deal was announced *after the close* on Oct 8. A "two-day" drop from the Oct 7 close wrongly included a day when nobody knew about the deal. The honest figure was the first full session after the news (−10.5%, −16% intraday). Find the announcement time (article timestamps, "after-hours" reporting) and measure from the last close before it.
   - **Deals:** say "agreed to buy" or "pending FCC approval" until they close.
   - **Claims about a company's intentions** ("SpaceX wants their customers"): tie them to something on record (an exec's earnings-call comment) and tell the user which.
   - **Contested or thinly sourced claims** (e.g. "AST bid for the same spectrum"): soften to what's reported ("had been chasing") and flag the source in chat.
5. **Draft**, then **count characters with the script** (step 6) before showing anything. Never eyeball the 280 limit.
6. **Count:** save the thread to a scratch file with posts separated by a line containing only `---`, then run:
   ```bash
   python3 -I .claude/skills/post-to-x-thread/count.py path/to/thread.txt
   ```
   It applies X's rules: every URL counts as 23, emoji count as 2. Fix any post over 280 and re-run.
7. **Plan images** for at least two posts (see "Images" below). Mark them in the thread with 📷 and the file they'll use.
8. **Present** the full thread in chat with each post's count. Put each post's text in its own plain fenced code block (```` ```text ````), never in a `>` blockquote: blockquote markers come along when the user copies the post into X. After the thread, add short notes covering:
   - how each hook number was verified (data source and window),
   - anything softened or uncertain,
   - the image plan: which post gets which image, the file path, and alt text for each,
   - a sources list for the user.
   
   Sources go in chat only, never in the thread.

## Images

Aim for images on **two or three of the middle posts**, usually the post that defines the core idea and the post with the key numbers. Skip post 1, so the hook text leads, and the last post, where the link's preview card already shows.

**Where images come from, in order of preference:**

1. **Existing site assets.** The post's own preview card (`assets/img/og-<slug>.png`, 1200×630) often illustrates the core idea; the world models film strip ("seen" vs "imagined") worked well on post 2. Use it as is.
2. **A post figure or table, re-rendered as a feed card.** Don't screenshot the page: tables render small and figures sit in a narrow column. Rebuild the content as a 1600×900 card with `card-template.html` in this folder (edit the title, subtitle and table/body), then render it with headless Chrome:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
     --window-size=1600,900 --virtual-time-budget=8000 \
     --screenshot="$HOME/Downloads/x-thread-<slug>/post-N-<name>.png" "file:///path/to/edited-card.html"
   ```
   Read the PNG back and look at it before handing it over. The post's animations can't play on X; use a still of a key frame, or suggest the user screen-record one.
3. **A new diagram via Claude Design.** When the post describes something visual but has no figure (e.g. the data pyramid), write a prompt for the user to run in the Claude Design thread. Always include: 1600×900 for in-feed images, the exact site palette below, Bricolage Grotesque for headings and IBM Plex Mono for labels, an 80px safe margin, legibility at feed size, and "not to scale" for extreme ratios. Then review each export the user drops in Downloads.

**Site palette** (from `assets/css/style.css`; the cards' background is exactly `--paper`):

| Role | Hex |
|---|---|
| Background | `#EFF1EC` |
| Ink (text, lines) | `#1C2620` |
| Secondary text | `#41504A` |
| Muted text | `#6E7C75` |
| Rules / thin lines | `#CBD2C7` |
| Cobalt accent | `#2F5DD1` |
| Clay labels | `#A8503C` |
| Mustard (sparingly) | `#C98A16` |

Cobalt should be the one strong colour in an image. Teal and purple belong only to the spectrum post's figures.

**Review every image for accuracy, not just looks.** The first data pyramid pointed "~61K hours with actions" at the robot-data tip, implying robots produced all of it, when robot data was only ~5K hours. Check that every callout covers exactly what its number describes. Check that the same kind of callout is drawn the same way: same bracket, same number style. Use one colour for one meaning.

**Deliver:** collect every image in `~/Downloads/x-thread-<slug>/`, named `post-N-<short-name>.png`, and keep the originals where they were. Give alt text for each, describing what the image shows, numbers included.

## Style rules

- **Tickers over hashtags for public companies:** `$ASTS`, `$TMUS`, `$T`, `$VZ`. They link to the stock's feed, and they replace the company name, so they cost no extra characters.
- **Hashtags only on the first and last posts, 1–2 each.** Use one broad audience tag (e.g. #SpaceX, #Starlink, #AI) and one niche industry term (e.g. #DirectToCell). Tags on every post look spammy and hurt reach.
- **Tag companies' X accounts** where they're the subject of a post (e.g. `@physical_int`), to earn impressions from their followers. Verify every handle against the company's own website or X profile before using it. A wrong or look-alike handle sends attention to someone else. One tag per company, at its first mention, and never more than about three tags in one post. A handle counts toward the 280 characters like any other text.
- **No post numbering by default** ("1/9"); offer it if there's room.
- **Approximate with "~"** for rounded figures (~10,000x, ~$8B). Keep exact figures exact (16%, 65 MHz).
- **After any edit, re-read the neighbouring sentence for ambiguity.** Adding "Ligado" to post 6 made "these same airwaves" point at the wrong band, so it had to name "that 800 MHz".
- **Link:** the last post links to `https://premrajka.com/posts/<slug>.html`. X shows the post's preview card, so no image is needed on the last post.

## Revisions

Keep the thread stable. When the user asks for a change, rewrite only the affected posts, re-run the count, and show the full thread again when asked. If a revision forces a new fact, verify it the same way as in step 4.

## What this skill does not do

It doesn't post to X, schedule anything, or change the user's profile. It drafts the text and prepares the images; the user posts them. It doesn't edit site files; if the thread exposes a mistake in the long-form post, tell the user rather than fixing it here.
