# Episode 03 · Features that don't lie

**Season 1 · The Problem** — *What are we even measuring?*

> **The learning doc.** The LinkedIn post is the short version; this is the detail.
> No Databricks experience needed — every term is explained where it first appears.

---

## 1. Where we left off

Episode 01 settled what churn means. Episode 02 made the data underneath safe to read. Now the question that decides whether any of it works: **what do you actually feed the model?**

## 2. What a "feature" is

A **feature** is one number describing a subscriber at the moment you make a prediction. "Sessions in the last 30 days" is a feature. "Lives in a city" is a feature. The model sees nothing but features, so **the features are the model's entire view of the world.**

Pick them badly and no algorithm can rescue you. That's why this episode sits before the modelling one.

## 3. What went in — and what didn't

Four families, deliberately behaviour-heavy:

| Family | Examples |
|---|---|
| **Tenure** | Which paid month they're in, whether they're a returning subscriber |
| **Engagement** | Session counts, active days, streaming duration, time to first play, weekend and evening ratios |
| **Content** | Distinct genres and titles watched, variety of viewing, weekly trend, qualified streams per week |
| **Plan and device** | Price tier, primary device bucketed to mobile / TV / other |

**No demographic personal data.** Partly for privacy, but mostly because it didn't help: *what someone does* predicted leaving far better than *who they are*. That holds across most subscription businesses, and it is worth checking before anyone spends months enriching demographics.

## 4. Trap 1 — a total hides the trend

This is the mistake that costs most teams their first model.

Take two subscribers, both with 20 hours of viewing in a 30-day window:

| | First half of the window | Second half |
|---|---|---|
| **Subscriber A** | 4 hours | 16 hours |
| **Subscriber B** | 18 hours | 2 hours |

Identical totals. **Completely different futures.** B has already left in every way except the paperwork.

A single 30-day total cannot tell them apart. The fix is to stop summarising the whole window at once:

- Split the observation window into **early and late sub-windows** and compute engagement in each.
- Add a **weekly trend** — is activity rising or falling?
- Keep **recency** features: days since last session, time to first play.

**The strongest signal in the model was late-window engagement** — what someone did in the final days before the prediction point mattered more than everything before it. That matches intuition, and it only becomes visible once you split the window.

### How it's built on Databricks

The raw material is an event table: one row per session or stream. Turning that into one row per subscriber per cycle is a SQL aggregation, and the early/late split is just a conditional inside it:

```sql
-- One row per subscriber per billing cycle, with the window split in two
SELECT
  subscription_id,
  billing_cycle_start,
  SUM(CASE WHEN event_date >= cutoff - INTERVAL 7 DAYS
           THEN watch_minutes ELSE 0 END)              AS watch_last_7d,
  SUM(CASE WHEN event_date <  cutoff - INTERVAL 7 DAYS
           THEN watch_minutes ELSE 0 END)              AS watch_earlier,
  COUNT(DISTINCT event_date)                           AS active_days,
  COUNT(DISTINCT genre)                                AS genres_watched
FROM   analytics.silver.viewing_events
WHERE  event_date < cutoff          -- nothing after the prediction point
GROUP BY subscription_id, billing_cycle_start;
```

Two things to notice: the **cut-off appears in the `WHERE` clause** (see trap 2), and the output has exactly the grain of the label from Episode 01 — one row per billing cycle — so the two join cleanly.

## 5. Trap 2 — using something the model won't have

This is the one that produces a brilliant model that fails the moment it goes live. It's called **leakage**.

If any feature contains information from *after* the moment you'd actually predict, the model learns from the future. In a churn model the classic version is including activity from the cancellation week itself: of course somebody who stopped watching entirely is about to cancel — but on the day you need the prediction, that week hasn't happened yet.

Three rules that prevent it:

1. **Fix the grain.** One row per paid billing cycle — the same grain as the label.
2. **Fix the cut-off.** Every feature is built only from data dated before the prediction point.
3. **Fix the label timing.** The outcome is only known once the renewal window closes, so you label later than you predict. Those two clocks are different, and keeping them straight is most of the work.

This is **point-in-time correctness**: every row answers "what did we know at the moment we'd have had to decide?" Get it wrong and every number downstream — the metric in Episode 05, the business case in Episode 09 — is inflated.

The thing that made this reliable rather than careful was **putting the period into the key**. The feature table is keyed on subscriber *and* billing cycle, so looking up features for a row returns what was true for that cycle. Correctness comes from the structure rather than from remembering to filter dates in every new query — which is the kind of discipline that survives other people joining the project.

## 6. Trap 3 — features built twice drift apart

In this project the features are built in SQL and published as a **gold feature table**, then the training notebook does the last mile: one-hot encoding the categories, log-scaling the skewed counts, filling the gaps.

That last mile is a risk. If the scoring job later fills a gap differently, or encodes a category in another order, the model sees inputs that don't match what it learned from. The model is fine; the inputs moved. This is **training/serving skew**, and it is quiet — no error, just slowly worse predictions.

Two defences:

- **One governed table** that both training and scoring read, rather than two notebooks each building their own. It lives in Unity Catalog at the same grain as the label, so the two join cleanly, the access rules are the same as the rest of the data, and another team can discover and reuse it instead of rebuilding it.
- **Shared code for the last mile.** The encoding and filling rules live in one importable place, not copy-pasted into two scripts.

### Feature tables in Unity Catalog

This is where the platform does real work, and it's the part I'd most recommend to anyone starting now.

A **feature table** in Unity Catalog isn't just a table that happens to contain features. It is registered as a feature table, which means:

- It has a **declared primary key**. Here that key is subscriber plus billing cycle — the same grain as the label — so a lookup can only return the right row for the right period.
- Training and scoring **look up the same table** rather than each rebuilding features. That removes the most common cause of skew at its source.
- It carries the **governance and lineage** of everything else in Unity Catalog: the same access rules, and a visible link from the features to the model that used them.
- Other teams can **discover and reuse it**. A feature someone else has already defined, tested and monitored is worth more than a better one you build privately.

The lesson that transfers: a feature table is a *contract between training and scoring*, in the same way Episode 01's metric definition was a contract between teams. Both work for the same reason — the definition lives in one governed place instead of being re-derived by whoever needs it next.

### What's next for me

Today the lookups happen in batch: features are fetched when the nightly scoring job runs. The next step is **online lookup**, so the same features can answer a real-time question — a decision at the moment someone clicks cancel, rather than a score computed last night.

## 7. What it cost

| Decision | What it bought | What it cost |
|---|---|---|
| Behaviour over demographics | A stronger model, no personal data to govern | Nothing to say about subscribers with almost no activity |
| Splitting the window | The single strongest signal in the model | Many more columns to build and monitor |
| Strict point-in-time cut-off | Numbers that survive contact with production | Lower training scores — honest ones |
| Feature tables in Unity Catalog | One definition for training and scoring, with governance and lineage | A product to learn, and feature changes now need versioning discipline |

## 8. What you can copy

- [ ] Never ship a model whose features are only **totals** — split the window and add a trend
- [ ] Write down the **grain** and the **cut-off** before writing any feature SQL
- [ ] Check every feature against one question: *would I have had this value at prediction time?*
- [ ] Keep the **last mile of transformation in one shared place**, not in two notebooks
- [ ] Test behaviour features before enriching demographics — behaviour usually wins
- [ ] Register features as a **feature table with a declared key**, rather than a plain table you join by hand — the key is what makes correctness structural

## 9. Key terms

| Term | Plain English |
|---|---|
| **Feature** | One number describing a subscriber at prediction time |
| **Grain** | What one row represents — here, one paid billing cycle |
| **Observation window** | The period features are measured over |
| **Cut-off** | The moment the prediction is made; no feature may use data after it |
| **Leakage** | A feature containing information from after the cut-off — flatters training, fails live |
| **Point-in-time correctness** | Every row reflects only what was known at its own cut-off |
| **Recency features** | Features about how recently something happened, not how much |
| **One-hot encoding** | Turning a category such as device type into separate yes/no columns |
| **Training/serving skew** | Features built differently at training and scoring time, so inputs drift |
| **Feature table** | A governed table of ready-made features, shared by models |
| **Feature Engineering in Unity Catalog** | Databricks' feature store: feature tables with a key and timestamp, and point-in-time lookups |

## 10. Check yourself

1. Two subscribers have identical 30-day watch totals. Why might one be about to leave?
2. What is leakage, and which clause of the feature query usually prevents it?
3. Why are the prediction clock and the label clock different here?
4. What is training/serving skew, and why is it quiet rather than loud?
5. What does a feature store give you that a plain gold table doesn't?

---

## Next episode

The features are built, honest, and point-in-time correct. Here's the thing that follows from it: **good features are why a boring model was enough.** I ran the bake-off across four algorithms, per-market models and per-tenure models — then threw most of it away.

**Episode 04 · Why the boring model won.**

---

**Prateek Kashyap** · Databricks at Scale · LinkedIn: **pratkashyap**
