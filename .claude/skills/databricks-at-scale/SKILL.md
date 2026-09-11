---
name: databricks-at-scale
description: Build and maintain Prateek Kashyap's "Databricks at Scale" LinkedIn series and its GitHub repo. Use when creating or updating an episode (learning doc, LinkedIn post, poster, cert prep), exporting a poster to PNG, updating PROGRESS.md or the design log, reorganising project files, or committing and pushing the repo.
---

# Databricks at Scale: project skill

**Update this file whenever the workflow, structure or rules change.** Add a line to the changelog at the bottom every time.

## What this is

Prateek's real, end-to-end churn prediction project on Databricks (8 markets, scored daily, deployed as config, monitored for drift, with a GenAI layer), told as a **9-episode LinkedIn series in 3 seasons**. It has four goals: show his experience, learn the rest of the platform in the open, help others, and prepare for a Databricks certification. The certification is **never mentioned in posts**.

Audience: newcomers to Databricks and senior practitioners. Plain English, every term defined, with decisions and trade-offs up front rather than tutorials.

## Where things live

| Path | Purpose |
|---|---|
| `README.md` | High-level front door with the trailer poster image |
| `PROGRESS.md` | Status, log, next steps, open decisions, scorecard. **Update after every piece of work** |
| `PROJECT.md` | The project on one page |
| `episodes/NN-name/` | `learn.md`, `post.md`, `poster.html` + `poster.png`, `cert-prep.md`, `README.md` |
| `design/design-log.md` | Every visual reference, version and verdict, plus the settled design rules. **Read before designing** |
| `design/export_png.py` | Converts an HTML poster to a LinkedIn PNG |
| `design/versions/` | Old and unused drafts, kept for history |
| `design/brand/databricks-logo.svg` | The logo, used on every poster |
| `docs/discovery.md` | The discovery questions |
| `docs/private/` | **Gitignored.** Prateek's real project answers. Source material only, never published |
| `../LinkedIn/NN-name/` | Ready-to-publish copies (post, poster, article), outside the repo. Guide: `../LinkedIn/README.txt` |
| `../_archive/` | Superseded plans and drafts, outside the repo |

## The series

Trailer 00 (posted 2026-09-11) · **S1 The Problem:** 01 Nobody agreed what churn meant · 02 Where the data actually lives · 03 Features that don't lie · **S2 The Build:** 04 Why the boring model won · 05 My metric was lying to me ⭐ (the turn) · 06 A model that runs itself · **S3 The Scale:** 07 Making it explain itself · 08 What breaks when you go global ⭐ (the climax) · 09 What it cost, and what you can copy.

## Building an episode

1. Read `PROGRESS.md`, `design/design-log.md` §3 (settled rules) and `docs/private/discovery_answers.md` for the facts.
2. **`learn.md`**: situation → why it matters → the concepts → the decision in the project → the Databricks part (with illustrative SQL or code using generic names) → what it cost → what you can copy → key terms → check yourself → next episode.
3. **`post.md`**: summarise `learn.md` in the series voice. Bold with Unicode (convert `**x**` markers with the bold map; see `design-log.md`). Keep product names and "Databricks" in plain text in the body so search can find them. Aim for 1,500–2,200 of LinkedIn's 3,000 characters, and make sure the first 210 characters carry the hook.
4. **`poster.html`**: Netflix style with a dark Databricks-navy gradient, the logo on the title line, 1080×1350 and minimal text. Export with `python design/export_png.py episodes/NN-name/poster.html`, fix any overflow warning, then **look at the PNG**.
5. **`cert-prep.md`**: a recall table, 2–3 applied questions and a spaced-repetition note.
6. Copy into `../LinkedIn/NN-name/` as `READY - post.txt`, `READY - poster.png` and `READY - article.md` (a copy of learn.md). After Prateek posts, rename `READY -` to `POSTED -`.
7. Update `PROGRESS.md` (status, log, next steps) and this skill's changelog. Commit and push.

## Non-negotiable rules

- **Truth:** nothing goes public framed as "I did this" unless the discovery answers or Prateek confirm it. Unconfirmed stories are framed as "here's what happens if you don't".
- **Never name the employer or any of its brands or products**, in any file, commit message or image. Always write "a subscription streaming business". Before every push, scan the repo, the git history and `../LinkedIn/`.
- **Confidentiality:** describe methods and patterns only. No figures, no market names, no internal table, tool or catalog names, no employer-specific details. Illustrative numbers are labelled as made up.
- **Feature names:** Databricks renames and ships features quickly. Flag anything recent (metric views, Genie and similar) to be checked against the current docs.
- **Signature:** Prateek Kashyap · LinkedIn · **pratkashyap** (username as text, never a URL).

## Git

- Repo: `github.com/Pratkashyap/databricks-at-scale`, branch `main`, **public** since 2026-09-11. Anyone can see everything that's pushed, so the brand-name and confidentiality checks before each push are essential.
- **Commit identity is set per repo** to Prateek's GitHub no-reply address. The machine's global git identity is his *work* email, and it must never appear in this repo. Check with `git config user.email` before committing.
- Before every push, confirm `docs/private/` and `design/refs/` are ignored: `git check-ignore -v docs/private/discovery_answers.md`.
- End commit messages with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Changelog

- **2026-09-11**: Skill created. Trailer posted. Episode 01 drafted. Repo pushed to GitHub (private). Structure: `learn.md` is the detailed doc and `post.md` is the summary. PNG export moved to a Playwright script, because headless Edge was unreliable.
- **2026-09-11**: Full brand-name scan (all files, git history, GitHub metadata): clean. "No employer or brand names" made an explicit rule. `LinkedIn Posters/` renamed to `LinkedIn/`, and each episode folder now holds post, poster and article.
- **2026-09-11**: Repo made public at Prateek's request.
