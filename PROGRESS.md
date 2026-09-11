# Progress

**Last updated:** 2026-09-11
**Where we are:** Trailer is live on LinkedIn. Episode 01 is drafted and waiting for Prateek's review.

---

## Next steps

In order:

1. **Review Episode 01**: [`learn.md`](episodes/01-nobody-agreed-what-churn-meant/learn.md), [`post.md`](episodes/01-nobody-agreed-what-churn-meant/post.md) and [`poster.png`](episodes/01-nobody-agreed-what-churn-meant/poster.png). Mark anything that didn't happen the way it's described.
2. **Truth check before posting.** Confirm the markets really did define churn differently (renewal window, reconnects, payment failures), and whether payment-failure cycles were dropped or kept as "not churned".
3. **Decide repo visibility.** The repo is **private** for now. Make it public before Episode 01 goes out if the post will point to it. Check `design/design-log.md` and this file first, because they contain working notes.
4. **Post Episode 01** next week. Copy the files from `LinkedIn Posters/01-nobody-agreed-what-churn-meant/`.
5. **After posting:** add the repo link as the first comment, and reply to every comment in the first hour.
6. **Confirm the certification target** against 2–3 real job descriptions.
7. **Start Episode 02.** Reuse the compute material in `../_archive/ep01-compute-draft/`.

---

## Log

| Date | What happened |
|---|---|
| 2026-09-03 | First plan: 8-week sprint, 7 platform layers, 16 posts |
| 2026-09-07 | Reframed as seasons and episodes. Repo scaffolded |
| 2026-09-08 | Discovery questionnaire answered (kept private). Curriculum rebuilt as a **9-episode narrative**. Design log started |
| 2026-09-11 | Databricks logo adopted. Trailer poster built in three styles. **Trailer posted on LinkedIn** (Option B text, Netflix-style v2 poster) |
| 2026-09-11 | Episode 01 drafted: learning doc, post, poster and cert prep. Files reorganised. `PROGRESS.md` and the project skill created. Repo pushed to GitHub (private) |

---

## Status

| Ep | Title | Learn | Post | Poster | Cert | Posted |
|---|---|---|---|---|---|---|
| 00 | Trailer | — | ✅ | ✅ | — | ✅ 2026-09-11 |
| 01 | Nobody agreed what churn meant | 🔍 review | 🔍 review | 🔍 review | ✅ | ⬜ |
| 02 | Where the data actually lives | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 03 | Features that don't lie | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 04 | Why the boring model won | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 05 | My metric was lying to me ⭐ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 06 | A model that runs itself | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 07 | Making it explain itself | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 08 | What breaks when you go global ⭐ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| 09 | What it cost, and what you can copy | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

---

## Open decisions

| # | Decision | Status |
|---|---|---|
| 1 | **Truth check**: some early story beats started as teaching examples. Anything not confirmed is framed as "what happens if you don't", never "I did this" | ⏳ Prateek |
| 2 | **Repo visibility**: private now; public before it's linked from a post? | ⏳ Prateek |
| 3 | **Certification target**: ML Professional is the working assumption | ⏳ Prateek |
| 4 | **Public framing**: visible episode numbers or named arc only? | 🗓 After Ep 02, using engagement data |

---

## Episode checklist

Every episode ships five files in `episodes/NN-name/`:

| File | What it is |
|---|---|
| `learn.md` | The detailed learning doc. The post summarises this |
| `post.md` | The LinkedIn post, in Unicode bold, ready to paste |
| `poster.html` → `poster.png` | The visual. Export with `python design/export_png.py episodes/NN-name/poster.html` |
| `cert-prep.md` | About 15 minutes of recall. Never mentioned in posts |
| `README.md` | Short index page for GitHub |

After exporting, copy `poster.png` and the post text into `../LinkedIn Posters/NN-name/`.

---

## Scorecard

| Check | Test |
|---|---|
| **Answer** | Can you answer the episode's question out loud, unaided, in 90 seconds? |
| **Ship** | Did the commit land? |
| **Signal** | Did a practitioner (data engineer, solutions architect, analytics lead) comment or DM? Record names, not counts |

| Ep | Answer | Ship | Signal | Notes |
|---|---|---|---|---|
| 00 | — | ✅ | · | Posted 2026-09-11 |
| 01 | · | · | · | |

**Health rule:** if two episodes in a row fail *Ship*, the plan is too heavy. Cut scope.
