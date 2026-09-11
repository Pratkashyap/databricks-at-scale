# Design log

**Purpose:** a running record of visual formats Prateek has shared as references, what we built from them, and his verdict on each. So we stop re-litigating settled decisions and stop repeating rejected ones.

**Update this file every time** a new reference is shared or a build is accepted/rejected. Newest at the top of each section.

**Last updated:** 2026-09-11

---

## 1. Reference formats shared

### Ref 03 · "Building a Trusted Data Foundation for Responsible AI" — Bajal Mohamed
📎 *Shared 2026-09-08. Image pasted in chat (not on disk). Source article: [LinkedIn Pulse](https://www.linkedin.com/pulse/lake-strategy-how-databricks-data-products-build-ai-bajal-mohamed-qgbzc/)*

**Verdict: this is the target.** Prateek: *"it looks so professional."*

Structure — a **horizontal architecture narrative**, left to right:

```
DATA SOURCES → INGESTION & STORAGE → [governance layer floating above]
             → AZURE DATABRICKS (bronze/silver/gold) → BUSINESS & AI CONSUMPTION
                            ↓
                   EXECUTIVE TAKEAWAYS band
                            ↓
                   personal signature
```

What makes it work:

| Element | Detail |
|---|---|
| **Title** | Centred, heavy, uppercase, navy. Very large. |
| **Subtitle** | One grey sentence explaining the whole diagram |
| **Columns** | Bordered cards, each with a coloured uppercase header label |
| **Icons** | **Colourful, filled, detailed** — not thin line icons. Blue buildings, green IoT, purple robot, red target |
| **Core** | The Databricks box is red-bordered and visually dominant — it's the subject |
| **Medallion** | Bronze / Silver / Gold with metal-coloured icons — instantly legible |
| **Flow** | Real arrows. Dotted lines drop the governance layer onto the platform |
| **Bottom band** | "Executive takeaways" — 5 icon+text items on a light blue field, thin vertical rules |
| **Signature** | *"Sharing my experiences — BAJAL MOHAMED"*, italic + bold, bottom right |
| **Spacing** | Generous. White space between zones does the separating, not boxes-inside-boxes |

**Rules to carry forward:** filled colour icons · a real left-to-right flow with arrows · one visually dominant subject · bordered cards with coloured headers · takeaways band at the bottom · personal italic signature.

---

### Ref 02 · Databricks "Auto Loader" product infographic
📎 *Shared 2026-09-08. Image pasted in chat (not on disk).*

Structure, top to bottom:

1. Logo + huge title + red one-line subtitle + **definition paragraph**
2. Mini architecture diagram (sources → product → destination)
3. **Key Benefits** — 5 icons in a row, thin vertical rules
4. Two columns: **How it works** (numbered 1–5) | **Simple to use** (dark code block)
5. **Common use cases** — 5 icons in a row
6. Dark CTA band with tagline

**What to take:** the definition-first opening · the mini diagram · **the real code block** (highest-value element — the only thing a reader can use tomorrow) · numbered steps · icon rows.

**What to reject:** the tone. It's vendor marketing — everything is "scalable, reliable, cost effective." No tradeoff, no failure mode, no opinion. Our version replaces the sales band with **the tradeoff**, and inverts "Common use cases" into **"Where the money actually leaks."**

---

### Ref 01 · "Power BI storage modes over Fabric and Azure Databricks"
📎 *On disk: [`design-refs/ref-01-powerbi-storage-modes.jpg`](design-refs/ref-01-powerbi-storage-modes.jpg). Shared 2026-09-07.*

Numbered, colour-banded horizontal lanes. Each row: a number badge, a left label, then a left-to-right icon flow. Soft pastel row fills, white background, clean sans.

**What to take:** numbered colour-banded lanes for comparing 3–5 alternatives · left label + flow right · pastel fills rather than hard borders.

---

### Ref 04 · The Pulse article itself (written structure, not visual)
📎 *Shared 2026-09-08.*

1. **Hook** — one short provocative line
2. **Thesis paragraph** — why the obvious approach fails
3. **Numbered sections** (8), prose plus nested bullets
4. A **case study** broken into *Situation · Constraints · Decision*
5. A **layered diagram** with a heading per layer
6. A shift to **leadership framing** partway through
7. **Prioritised recommendations** — numbered, each with a subheading
8. **"Final thought"** synthesis, then hashtags

Voice: *"From my experience…"*, *"I learned…"* — personal narrative carrying professional authority.

**What to take:** hook → thesis → numbered sections → Situation/Constraints/Decision for the worked example → **"Final thought"** close → first-person experience woven in, not appended.

---

## 2. What we built, and the verdicts

### Episode 01 poster v1 · Netflix style, first content episode — ⏳ AWAITING VERDICT
*2026-09-11. `episodes/01-nobody-agreed-what-churn-meant/poster.html` → `poster.png`.*

The first content episode in the series style: an episode and season badge, the logo on the title line, the voluntary/involuntary split as two cards, the six-field contract as a numbered grid, "the trap" (averaging rates) next to "where it lives" (Unity Catalog), and the takeaway in white and red.

**Lessons from building it:**
- A 236px empty band above the footer made the poster look unfinished. **Fill the frame.** The export script checks overflow, but not empty space, so measure the gap too.
- Enlarging the title from 76px to 84px pushed it onto **three lines**. Check the title's line count, not just the overflow.
- Put the red half of the takeaway on **its own line** so it never splits mid-phrase.

---

### Netflix-style poster v2 · dark navy, logo on the title line — ✅ POSTED 2026-09-11 (with Option B text)
*2026-09-11. `episodes/00-trailer/poster.html` → `poster.png`.*

Prateek came back to the Netflix page: *"I liked the previous netflix style."* He kept three things from it (the **title style**, the **overall Netflix look** and the **keyword chips**) and asked for two changes: **the logo beside "Databricks" on the same line** to remove the empty space at the top, and **the season one-liners from the light poster**.

**What changed from the v1 page to make it a LinkedIn poster:**
- Fixed 1080×1350 and exported to PNG. The v1 page was a long web page that couldn't be posted.
- **Deep Databricks navy gradient, not pure black.** Keeps the cinematic feel and addresses the earlier "all black not needed" note.
- Episode cards show **titles only**. The sentence under each episode is gone.
- 16 keyword chips instead of 33. The synopsis paragraph, the CTA buttons and the four audience columns are dropped.

### Trailer poster v1 · light, minimal, logo — ⏸ NOT USED (Netflix v2 chosen)
*2026-09-11. `versions/trailer/light-v1-poster.html` → `.png`.*

Built in response to the series-page rejection below. Light warm ground, Databricks logo top and bottom, centred heavy title, **episode titles only — no descriptions**, three season cards joined by red flow arrows, two red pills marking the turn (Ep 05) and the climax (Ep 08). Exported to PNG because LinkedIn cannot show HTML.

### Series page v1 · dark "Netflix" main screen — ❌ REJECTED
*2026-09-08. Restored intact on 2026-09-11 at `versions/trailer/netflix-style-v1-page.html`. Prateek later said he liked this style (see v2 above), so the verdict is now partly reversed: the **look, title style and keywords are kept**, and the **amount of text and the pure black background are not**.*

Prateek: *"too much text. hard to read. all black not needed."*

**Diagnosis:** it was built as a web page, not a LinkedIn image — synopsis paragraph, a sentence under every episode, 33 term chips, four audience columns. Every block was individually reasonable; together they made a page nobody reads in a feed. The dark ground added mood but cost legibility.

**Rules added:** no all-black grounds · titles only on posters, never a sentence per item · if it can't be read in 5 seconds on a phone, it's too much · **everything built for LinkedIn must end as a PNG.**

---

### Structure v2 -> v3 · Curriculum rebuilt as narrative — ✅ ACCEPTED
*2026-09-08.*

Prateek rejected the 12-episode platform curriculum: *"it feels like we are starting from somewhere in the middle and I have no sense of what's going on."* Episode 1 opened on compute config — a question nobody has until they are already deep in.

**Root cause:** we built a syllabus (compute → storage → governance → …). A syllabus has students, not an audience. He asked for a **series** — his real churn project told as a story, with Databricks knowledge emerging because the story needs it.

**Fix:** 12 platform layers → **9 story beats, 3 seasons of 3.**

| Season | Beat |
|---|---|
| 1 · The Problem | Setup — nobody agreed what churn meant |
| 2 · The Build | Rising action, with the **reversal** at Ep 05 (the metric was lying) |
| 3 · The Scale | **Climax** at Ep 08 (governance breaks, not volume), resolution at Ep 09 |

**Rules added:** lead every episode with a decision or a mistake, never a feature · each episode ends on a question · plant early, pay off late · keep the technical depth in the long post, not the poster · the series is *his project*, not a platform tour.

---

### Poster v3 · Auto Loader format applied — ❌ REJECTED
*2026-09-08. Archived at `versions/ep01-compute-draft-posters/v3-autoloader-format.html`.*

Prateek: *"too AI like."* Wants Ref 03's gapping, fonts, Databricks colours, image style, and bolding.

**Diagnosis — what makes it read as machine-generated:**

| Tell | Fix |
|---|---|
| Uniform thin monochrome line icons, all identical stroke weight | **Filled, colourful, varied icons** |
| Stacked text panels, no actual diagram | A **real left-to-right flow** with arrows |
| Evenly-weighted grey text everywhere | Strong **bold/regular contrast**; let headings dominate |
| Perfectly symmetric grids in every section | Vary block sizes — the subject should be visually biggest |
| Brand colour used as decoration | Anchor with **Databricks red** as the identity of the core |
| Left-aligned generic sans title | **Centred, heavy, uppercase** title |

### Poster v2 · Simplified, one idea — ❌ REJECTED
*2026-09-08.* Passed the newcomer test but **too thin** — no code, nothing to take away, no depth for a practitioner.

### Poster v1 · Dense reference-card — ❌ REJECTED
*2026-09-07.* **22 undefined terms.** Three ideas on one page. Jargon-first. The best line (the tradeoff) buried in 20px grey at the bottom.

---

## 3. Settled rules

Derived from the above. Apply to every episode without re-asking.

**Always**
- Define every term in plain English at first use — assume the reader has never opened Databricks
- One visually dominant subject per poster
- Real, annotated code — the single highest-value block
- End on the **tradeoff**, never a summary or a call to action
- **Databricks logo** on every poster — `brand/databricks-logo.svg`. Prateek's call (2026-09-11), overriding the earlier trademark caution
- Signature: Prateek Kashyap · **LinkedIn · pratkashyap** — the username as text, never a URL
- Light, or deep navy for the Netflix style. Every LinkedIn visual exported to a 1080×1350 PNG
- **Post text uses Unicode bold**, but only for what a skimmer should take away: the hook, the scale, the key lessons, the series name and the promise. Keep searchable words ("Databricks", product names) plain in the body, because LinkedIn search does not match Unicode bold
- Netflix title style: huge uppercase heavy type, "DATABRICKS" in white and "AT SCALE" in red, with the logo on the same line
- Filled, colourful icons; visible bold/regular contrast; generous white space

**Never**
- Thin uniform line icons
- Vendor-marketing tone ("scalable, reliable, cost effective")
- Three ideas competing on one image
- The insight in the smallest type
- Pure black backgrounds. Dark is fine in the Netflix style, but use deep Databricks navy
- A sentence under every item — posters carry titles, the post carries the explanation
- HTML as the deliverable for LinkedIn — it's the source, the PNG is the output

**Open**
- Whether the series is publicly framed as episodes, or just as a named arc — decision deferred to after Episode 2, with real engagement data

---

## 4. Notes for future turns

- Ref 02 and Ref 03 images live **only in chat history**, not on disk. If they're needed again, ask Prateek to re-attach, or work from the written descriptions above.
- Prateek's feedback pattern so far: **he rejects thin before he rejects dense.** Density is fine when it's structured and visually varied. The failure mode to avoid is uniformity, not information.
- He is a Power BI native. Visual idioms from that world (banded rows, KPI cards, clean corporate sans) land well.
- **LinkedIn cannot display HTML.** It accepts images (single or multi), PDFs (shown as swipeable document carousels), video and text. Posters → PNG. Anything multi-page → PDF carousel.
- **PNG export:** run `python design/export_png.py <poster.html>` from the repo root. It writes a 2160×2700 PNG next to the HTML and **warns if content overflows the 1080×1350 frame**. Chrome lays out text a few pixels taller than the preview pane, so always export before calling a poster done. Add `--full` for long web pages. It uses Playwright with the installed Chrome.
- **Don't use headless Edge from the command line.** Edge's startup-boost background process takes over each launch: the command exits instantly and the PNG appears seconds later, or not at all. That caused two false "export failed" results on 2026-09-11.
- **Honesty rule:** several early story beats (the 4.2/3.8/5.1 meeting, the discount sent to non-leavers) started life as teaching examples. Nothing goes public framed as "I did this" unless Prateek confirms it happened.
