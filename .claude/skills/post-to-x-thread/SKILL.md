---
name: post-to-x-thread
description: Turns one long-form post under posts/*.html on premrajka.com into a 7-post X (Twitter) thread that opens and closes on a hook grounded in real, verified news. Use this whenever the user asks to share, promote, spin, summarize or "turn into a thread" a post for X/Twitter, or asks for tweets or social copy about a post. Also use it when the user wants an existing thread revised (new ending, added facts, hashtags). It only drafts text in chat; it never posts to X or edits site files.
---

# Post → X thread

The user uses X as the media channel for premrajka.com: short threads that pull readers into the long-form posts. This skill was distilled from the session that produced the thread for `posts/spectrum-satellites.html`. Every rule below exists because something in that session went wrong or got corrected.

## The shape (fixed)

Exactly **7 posts**, each **≤280 characters**, always as a **thread** (the user tried a single long post and went back to threads).

| Post | Job |
|---|---|
| **1. News hook** | A specific, recent, verified news event tied to the post's topic, with a hard number. Then the question the post answers ("Why would X move Y that much?") and 🧵. Ends with 1–2 hashtags. |
| **2–5. The explainer** | One idea per post, taken from the long-form post in its order. Plain English, concrete numbers, no jargon the post itself didn't define. Reuse the post's own analogies (e.g. the spectrum "highway and lanes") rather than inventing new ones. |
| **6. The stakes** | Who's winning and why: the players, the money, the moves, mapped back to the explainer. |
| **7. News hook, second angle** | Return to the news from a different angle (e.g. post 1 was the company that lost; post 7 is the wider industry fallout). End on a **thought-provoking open question** about what happens next, then the post link, then one niche hashtag. |

**Both the first and the last post must be grounded in real news.** Post 7 is not a summary or a "what's available today" roundup. The user cut that ending as boring. It's the bigger implication of the news, posed as a question.

## Process

1. **Confirm the post.** Use the one the user names; if none, ask.
2. **Read the whole post.** Pull out the 4–5 ideas that carry the argument, plus the concrete numbers that make them land.
3. **Find the news.** Search for events from roughly the last two weeks tied to the post's subject (deals, launches, rulings, stock moves). Prefer an event with a measurable consequence. Pick a second angle on the same event for post 7.
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
7. **Present** the full thread in chat with each post's count, then short notes covering:
   - how each hook number was verified (data source and window),
   - anything softened or uncertain,
   - suggested images (a still or screen recording of a post figure works better than nothing; X can't play the animations),
   - a sources list for the user.
   
   Sources go in chat only, never in the thread.

## Style rules

- **Tickers over hashtags for public companies:** `$ASTS`, `$TMUS`, `$T`, `$VZ`. They link to the stock's feed, and they replace the company name, so they cost no extra characters.
- **Hashtags only on posts 1 and 7, 1–2 each.** Use one broad audience tag (e.g. #SpaceX, #Starlink, #AI) and one niche industry term (e.g. #DirectToCell). Tags on every post look spammy and hurt reach.
- **No post numbering by default** ("1/7"); offer it if there's room.
- **Approximate with "~"** for rounded figures (~10,000x, ~$8B). Keep exact figures exact (16%, 65 MHz).
- **After any edit, re-read the neighbouring sentence for ambiguity.** Adding "Ligado" to post 6 made "these same airwaves" point at the wrong band, so it had to name "that 800 MHz".
- **Link:** the last post links to `https://premrajka.com/posts/<slug>.html`. X shows the post's preview card, so no image is needed on post 7.

## Revisions

Keep the thread stable. When the user asks for a change, rewrite only the affected posts, re-run the count, and show the full thread again when asked. If a revision forces a new fact, verify it the same way as in step 4.

## What this skill does not do

It doesn't post to X, schedule anything, or change the user's profile. It drafts text for the user to post. It doesn't edit site files; if the thread exposes a mistake in the long-form post, tell the user rather than fixing it here.
