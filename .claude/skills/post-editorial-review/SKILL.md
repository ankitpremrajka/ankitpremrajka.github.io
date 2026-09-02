---
name: post-editorial-review
description: Audits one long-form post under posts/*.html on this site (premrajka.com) for flow, continuity, and cohesiveness — the connective tissue between sections, not grammar or facts. Use this whenever the user asks to review, audit, critique, or improve the flow/structure/organization of a post, asks whether sections "connect well" or "flow logically," mentions a post feeling disjointed or repetitive, or wants a post reorganized or simplified. Also use it proactively after a post has been substantially rewritten or restructured, to catch dangling references before the user notices them. Do not use it for a brand-new post that hasn't been written yet, and do not use it for site-wide changes (CSS, index.html, sitemap.xml) — it only edits the internal content of one post file.
---

# Post editorial review

This skill runs the kind of structural edit a good editor does on a second pass: not "is this sentence well-written," but "does reading this straight through actually make sense, section to section." It was distilled from a real, long editing session on `posts/robot-world-models.html` — the checklist below is every category of problem that turned up in that pass, generalized so it applies to any post on this site.

## Why this matters here specifically

Every long-form post on this site follows one blueprint (documented in `assets/css/style.css` under "Long-form article template"): a hero, a sticky sidebar nav (`.rail`), Parts (`.part-head`) containing numbered sections (`section.s`), and a scattering of `.box`/`.two`/`.three` grids, `.analogy` callouts, `.note` asides, and a `.glossary`. `posts/training-robot-policies.html` is the cleanest example of the blueprint used well — in particular its use of `<p class="bridge">` as the first thing inside most sections, one sentence that says why this section follows the last one. That convention is what makes a 3,000-word technical guide readable start to finish instead of feeling like ten independent Wikipedia stubs. When a post skips it, or uses it inconsistently, the reader has to do the connective work themselves — and usually doesn't.

## Before you start

1. **Confirm the target post.** If the user named one, use it. If not, ask — don't guess, since this is a real edit to a real file.
2. **Read the whole post first**, not just the section someone flagged. Nearly every finding below only shows up by holding the whole structure in your head at once — a taxonomy that's too fine-grained, or a promise made in Part One and never paid off in Part Three, is invisible if you only look at the section where it's mentioned.

## The checklist

Work through all nine. Most posts will only trip a few of these — that's fine, report what you actually find rather than padding the list.

**1. Missing connective tissue.** Every section that isn't the first in its Part should open with a `<p class="bridge">` sentence linking back to whatever came immediately before it (reread `posts/training-robot-policies.html` for the pattern if you need a refresher). Part-heads — the paragraph under each Part's `<h2>` — should do the same job one level up: connect back to the previous Part, not just preview the upcoming one in isolation. Flag every section and part-head missing this, and draft the actual replacement sentence, not a description of what it should do.

**2. Unpaid promises.** Search for language like "comes up again below," "discussed later," or "we'll return to this." For each one, verify the payoff actually exists later in the post. If it doesn't, either cut the forward reference or write the payoff in — don't leave a reader looking for something that isn't there.

**3. Terminology precision.** Watch for a specific term being used as a stand-in for a more general one, or vice versa — the kind of thing a careful reader would stop and question. (The seed example: a post calling a VLA "a robot policy," when policy is the general term and VLA is one particular way of building one.) Check the term is used the same way everywhere it appears, including the glossary — a glossary entry that contradicts how the term was used three sections earlier is worse than no glossary entry at all.

**4. Analogies that don't land.** An analogy is suspect when the two things being compared operate on different timescales, or come from a domain that hasn't been established anywhere else in the post. The fix is almost never a fancier new analogy — it's usually to reuse a domain the post already set up nearby (a worked example two paragraphs earlier, a comparison from the previous section), because that reinforces something the reader already has in mind instead of asking them to hold a third unrelated mental model.

**5. Over-fine-grained taxonomies.** If a section presents N parallel items (a numbered "four ways X helps" list, say) and a meaningful chunk of a later section exists purely to explain which of the N are easy to confuse with which — that disambiguation is a symptom, not a feature. It means the taxonomy is finer than the post's own audience needs. Propose consolidating to fewer categories along a real organizing axis (by timing, by mechanism, by who's responsible — something structural, not a cosmetic relabeling), and check whether the disambiguation section can shrink or disappear once the categories are actually distinct from each other.

**6. Redundant sections.** Flag any section or subsection that substantially re-covers ground another section already covered — the same named model, product, or concept given a full standalone treatment twice. Collapse the smaller or later one into the earlier one rather than keeping both; a reader who just read the first treatment doesn't need the second.

**7. Reference propagation.** This is the step most likely to get missed, and it's the one that actually breaks the post if you skip it. Any time you rename, remove, split, or consolidate a section as part of fixing 1–6, grep the *entire file* for anything that could still point at the old shape: sidebar nav entries (`<a href="#sX">...</a>`), other sections' `.bridge` lines, part-head paragraphs, table cells, glossary entries. A post that says "the four roles above" after you've consolidated four roles into two reads as broken, even though every individual sentence is grammatically fine. Do this grep as a distinct step after applying edits, not just from memory of what you touched.

**8. Visual balance.** Where content sits in parallel side-by-side boxes (`.two`/`.three` grids), a big length mismatch between columns looks like a mistake even when the content is correct. If one is much longer, trim it — don't pad the short one with filler just to match.

**9. Verify by rendering.** HTML source reading isn't enough to catch a broken layout or an orphaned box. After edits, start a local server (`python3 -m http.server` from the repo root — reuse one if it's already running) and use the `claude-in-chrome` skill/tools to actually open the post and scroll through the sections you changed. Confirm bridges render where expected, boxes look balanced, and nothing collapsed oddly.

## Process

1. Read the full target post.
2. Work through the checklist and compile a concrete findings list — for each finding, quote the exact current text and write the specific proposed replacement. "This section feels disconnected" is not a finding; the rewritten bridge sentence is.
3. **Present the findings list to the user and stop.** Don't edit anything yet. This mirrors how the original editing session actually went — every structural change was proposed and approved before being applied, and that back-and-forth is what kept a long series of edits from drifting away from what the user actually wanted.
4. Once approved (the user may approve all of it, some of it, or redirect entirely — treat their reply as real feedback, not a formality), apply the edits.
5. Re-run the reference-propagation grep (checklist item 7) as its own step, even if you're confident you caught everything while editing.
6. Do the visual spot-check (checklist item 9).
7. Summarize what changed, organized by checklist category, so the user can see the shape of the edit at a glance.

## What this skill does not do

Stay inside the one post file. Don't touch `sitemap.xml`, `index.html`, `assets/css/style.css`, or OG images as part of this review — those are separate, deliberate steps the user asks for on their own (new post → homepage entry → sitemap → title card is its own established workflow on this site). Don't run `git commit` or `git push`; this skill's job ends when the file is edited and verified, and committing stays an explicit separate request like it does everywhere else in this repo.
