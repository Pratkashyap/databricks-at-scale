# Episode 02 · Where the data actually lives

**Season 1 · The Problem** — *What are we even measuring?*

> **The learning doc.** The LinkedIn post is the short version; this is the detail.
> No Databricks experience needed — every term is explained where it first appears.

---

## 1. Where we left off

Episode 01 ended with one agreed definition of churn, stored in Unity Catalog. But a definition still needs data underneath it, and **I didn't own a single table I depended on.**

## 2. The situation

The churn project read from tables built and owned by other teams: subscription and billing facts, session summaries, viewing events, and a content catalogue. My job was to turn those into something a model could learn from.

That makes you a **consumer**. You get the data, but you don't get:

- a say in when it arrives
- a warning when its shape changes
- a promise that yesterday's assumptions still hold

Three things went wrong, and all three are normal:

1. **A number arrived as text.** In some markets a numeric column came through as a string, sometimes empty. The moment a job tried to add it up, it failed with a type error.
2. **The month hadn't landed.** Source data arrived monthly. Start the build too early and you don't get an error — you get a half-month of data and a quietly wrong answer.
3. **Nothing announced the change.** Upstream teams ship improvements. They don't know who is downstream.

**The failure that matters is the second one.** A job that dies wakes you up. A job that succeeds with bad data goes into a dashboard.

## 3. The idea: layers, and knowing which one is yours

Databricks organises data in a **medallion architecture** — three layers of increasing trust:

| Layer | What's in it | Who normally owns it |
|---|---|---|
| **Bronze** | Raw data exactly as it arrived, nothing cleaned | Platform / data engineering |
| **Silver** | Cleaned and conformed: types fixed, duplicates gone, joins resolved | Platform / data engineering |
| **Gold** | Business-ready tables people actually query | Whoever owns that business area |

The clarifying question isn't "what is bronze?" — it's **"which layer am I standing on, and which one do I own?"**

For this project the answer was: I **read** other teams' gold, and I **publish** my own gold — the churn label from Episode 01, the feature table, the daily scores. I never touched bronze or silver.

That's a common and healthy position. It just means the risk sits at the boundary: **everything I depend on can change without me.**

## 4. What Delta gives you underneath

All of these tables are **Delta** tables. Delta is the storage format Databricks uses: data files plus a transaction log that records every change.

Four things it gives you, in plain terms:

- **A write either fully happens or doesn't.** No half-written table if a job crashes mid-way.
- **Schema enforcement.** A write that doesn't match the table's columns is rejected rather than silently mangled.
- **Time travel.** You can read the table as it was yesterday, or at a specific version. Priceless when a number changes and nobody knows why.
- **Cheap appends.** Adding a new month doesn't rewrite history.

Time travel is the one to remember. When someone asks *"why did last month's number move?"*, you can compare the table today against the table then, instead of guessing.

## 5. The two habits that stopped the failures

### Habit 1 — never trust a column's declared type

When you read tables you don't own, treat every type as a claim rather than a fact. The defensive version of a cast turns a bad value into an empty one instead of killing the job:

```sql
-- Fragile: one bad row and the whole job fails
SELECT SUM(CAST(time_to_first_play AS BIGINT)) FROM upstream.gold.session_summary;

-- Defensive: bad values become NULL, the job survives, and you can count them
SELECT SUM(TRY_CAST(time_to_first_play AS BIGINT)) AS total,
       SUM(CASE WHEN TRY_CAST(time_to_first_play AS BIGINT) IS NULL
                 AND time_to_first_play IS NOT NULL THEN 1 ELSE 0 END) AS bad_values
FROM   upstream.gold.session_summary;
```

The second column matters as much as the first. **Surviving isn't enough — you want to know how often it happened**, so a slow drift upward gets noticed.

### Habit 2 — check before you run

The build job's first step isn't reading data. It's asking whether the data is there yet:

```python
# Freshness gate: refuse to build on a month that hasn't fully landed
if rows_for(target_month) == 0:
    abort("source month not yet landed — retry later")
```

A job that refuses to run is a good job. It turns a silent wrong answer into an obvious "not yet".

## 6. The decision: what to run it on

Databricks charges for compute by the second, so *how* you run a job is a real cost decision.

| Option | Use it for | Cost shape |
|---|---|---|
| **Job cluster** | Anything scheduled | Created for the run, destroyed after. Cheapest for scheduled work |
| **All-purpose cluster** | Interactive exploration | Stays up until stopped — the most common source of wasted spend |
| **SQL warehouse** | SQL and dashboards | Auto-stops when idle |

This project uses job clusters for everything scheduled, a SQL warehouse for ad-hoc digging, and a local IDE connected to a cluster for development.

Two settings worth knowing:

- **Workers on spot, driver on demand.** Spot capacity is heavily discounted but can be reclaimed at short notice. Lose a worker, the task retries. Lose the driver, the whole run dies — so the driver is never on spot.
- **A long-term-support runtime, not the newest.** You give up new features for a version that doesn't change under a production job.

And one that saves money by *not* being used: **Photon**, the vectorised engine, speeds up SQL and DataFrame work. It does nothing for a Python training loop, so enabling it on an ML cluster is a premium for no gain. It belongs on the SQL feature build instead.

## 7. What it cost

| Decision | What it bought | What it cost |
|---|---|---|
| Read upstream gold instead of raw | Someone else's cleaning and conforming | No control over shape or timing |
| Defensive casting everywhere | Jobs that survive bad data | Slightly slower queries, and code that's less pretty |
| A freshness gate | No silent half-month answers | Some mornings the pipeline simply doesn't run |
| Job clusters over always-on | Much lower spend | A minute or two of start-up per run |

## 8. What you can copy

- [ ] Write down **which layer you own** and which you only read
- [ ] For every table you don't own: **cast defensively and count the failures**
- [ ] Add a **freshness check as the first step** of any scheduled job
- [ ] Use **time travel** to answer "why did this number change?" instead of guessing
- [ ] Put scheduled work on **job clusters**; check nobody left an all-purpose cluster running
- [ ] Ask the upstream team for **one thing only**: tell me before the schema changes

## 9. Key terms

| Term | Plain English |
|---|---|
| **Medallion architecture** | Organising data in three layers: bronze (raw), silver (cleaned), gold (business-ready) |
| **Delta** | The storage format Databricks uses: data files plus a log of every change |
| **Transaction log** | The record that makes writes all-or-nothing and enables time travel |
| **Schema enforcement** | Rejecting writes that don't match the table's columns |
| **Time travel** | Reading a table as it was at an earlier point |
| **Schema drift** | A source table's shape changing underneath you |
| **`TRY_CAST`** | A conversion that returns empty instead of failing on bad input |
| **Freshness gate** | A check at the start of a job that stops it if the data isn't ready |
| **Job cluster** | Compute created for one job run and destroyed afterwards |
| **All-purpose cluster** | Interactive compute that stays running until someone stops it |
| **SQL warehouse** | Compute tuned for SQL and dashboards, auto-stops when idle |
| **Spot instance** | Discounted cloud capacity that can be reclaimed at short notice |
| **Driver / worker** | The driver coordinates a job; workers do the parallel work |
| **Photon** | A faster engine for SQL and DataFrame work; no help for plain Python |

## 10. Check yourself

1. Which medallion layer do you read, and which do you own?
2. Why is a job that silently succeeds worse than one that fails?
3. What does `TRY_CAST` change, and why count the failures?
4. Why is the driver never put on spot capacity?
5. When would Photon give you nothing?

---

## Next episode

The data is landing, it's being read safely, and it's mine from gold onwards. Now the real question: **what do you actually feed a model** — and which signals turn out to matter?

**Episode 03 · Features that don't lie.**

---

**Prateek Kashyap** · Databricks at Scale · LinkedIn: **pratkashyap**
