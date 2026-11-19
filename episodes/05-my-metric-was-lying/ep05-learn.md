# Episode 05 · My metric was lying to me

**Season 2 · The Build** — *From a notebook to a system* · ⭐ **the turn**

> **The learning doc.** The LinkedIn post is the short version; this is the detail.
> No Databricks experience needed — every term is explained where it first appears.

---

## 1. Where we left off

Episode 04 settled the model: one class-weighted XGBoost model, pooled across markets, every run tracked in MLflow. As more markets were pooled in, the main score — PR AUC — went up.

That looked like progress. This episode is about why it wasn't, and how to tell the difference.

## 2. The situation

PR AUC was the primary metric, for a good reason: it focuses on how well the model finds the rare class, which accuracy can't do. But PR AUC has a property that's easy to miss:

> **PR AUC depends on how common the outcome is.**

A model that guesses at random gets a PR AUC roughly equal to the **base rate** — the share of rows that are churners. So the floor moves with the data:

| *(Numbers made up for illustration)* | Base rate | PR AUC of a random guess |
|---|---|---|
| Market with rare churn | 2% | about 0.02 |
| Market with common churn | 8% | about 0.08 |

Pool a market with more churn into the training and evaluation data, and the overall base rate rises — so PR AUC rises with it, **even if the model is exactly as good as before.** The number moved because the data mix moved.

That's the turn in this series: **a better score is not the same as a better model.** And it's a trap you can fall into with any metric whose floor depends on the base rate.

## 3. Problem 1 — a score that moves with the base rate can't compare models

If the floor moves, comparing raw PR AUC across markets, or across a single-market and a pooled model, is comparing numbers measured on different rulers.

### The fix: lift over base rate

**Lift** asks a simpler question: *how many more churners does the model find than random picking would?*

- Take the people the model ranks as highest risk — say the top 10%.
- Measure what share of them actually churned.
- Divide by the base rate.

A lift of 3 means the model's top 10% contains three times as many churners as a random 10% would. Because it divides by the base rate, **lift is comparable across markets with different churn levels**, which raw PR AUC is not.

Here's the shape of it on Databricks — per-market lift in the top decile, computed from the stored scores and the labels:

```sql
-- How many times better than random is the top 10%, per market?
WITH scored AS (
  SELECT p.market,
         l.churned_voluntary,
         NTILE(10) OVER (PARTITION BY p.market
                         ORDER BY p.churn_score DESC)   AS risk_decile
  FROM   analytics.gold.churn_predictions p
  JOIN   analytics.gold.churn_label       l
         USING (subscription_id, billing_cycle_start)
)
SELECT market,
       AVG(CASE WHEN risk_decile = 1 THEN churned_voluntary END)
         / AVG(churned_voluntary)                        AS top_decile_lift
FROM   scored
GROUP BY market;
```

PR AUC is still reported. It just isn't the number used to decide whether one model beats another.

## 4. Problem 2 — one threshold treats every action the same

A model produces a score between 0 and 1. To act, you pick a **threshold**: everyone above it gets contacted. But "contacted" isn't one thing:

- A **cheap** action — a reminder message — can go to a lot of people, because a wrong guess costs almost nothing.
- An **expensive** action — a discount — should only go to people the model is very sure about, because every wrong guess is money given to someone who was staying anyway.

One threshold can't serve both. So instead of one cut-off, the project uses a **value-to-action table**:

| Action *(structure only, values not shown)* | Cut-off | Precision | Recall | People flagged |
|---|---|---|---|---|
| Cheap — e.g. a reminder | Low | Lower | Higher | Many |
| Mid — e.g. a content nudge | Medium | Medium | Medium | Some |
| Expensive — e.g. an offer | High | Higher | Lower | Few |

**Precision** is how many of the flagged people really churn; **recall** is how many of all churners got flagged. Raising the cut-off trades recall for precision. The table makes that trade visible, per action.

The important shift is who decides: **the model ranks; the business picks the cut-off**, because only the business knows what each action costs.

## 5. Problem 3 — you can't judge a score until the renewal window closes

Episode 01 set the rule that churn is only labelled once the renewal window has closed. That has a consequence for evaluation: **today's scores can't be judged today.** The outcome arrives weeks later.

If scores aren't kept, that later evaluation becomes archaeology — reconstructing which model, which version and which threshold produced a decision a month ago.

### The Databricks part: keep every score in Delta

Every daily scoring run appends its output to a **Delta table**, and every row carries what's needed to judge it later:

| Column | Why it's there |
|---|---|
| Subscriber and billing cycle | Joins to the label once it exists |
| Score and high-risk flag | What the model said |
| Model name and version | Which model said it |
| Threshold used | Which decision rule applied |
| Run timestamp | When it was said |

When the labels land, evaluation is a **join** between the predictions table and the label table — the SQL in section 3. And because it's Delta, earlier versions of the table stay readable, so a past evaluation can be re-run exactly as it was.

## 6. What it cost

| Decision | What it bought | What it cost |
|---|---|---|
| Lift over base rate as the decision metric | Honest comparison across markets and models | A less impressive headline number |
| Value-to-action table | Each action gets the right cut-off | More to explain than "anyone above 0.5" |
| Keeping every score with its model version | Evaluation is a join, any month, re-runnable | More storage, and a table to maintain |
| Waiting for labels | Judging on real outcomes | A lag of weeks before any score can be graded |

## 7. What you can copy

- [ ] Before trusting a rise in any metric, ask: **did the model change, or did the data mix change?**
- [ ] Report the **base rate next to every precision-based metric** — and what a random guess would score
- [ ] Compare models with **lift**, not raw PR AUC, whenever segments have different base rates
- [ ] Replace "the threshold" with **a cut-off per action**, and let the business choose
- [ ] Store every score with its **model version and threshold** so it can be graded when labels arrive
- [ ] Evaluate **per segment** as well as overall — a pooled average can hide a market getting worse

## 8. Learning next

Today, lift and the action table are computed after training, from stored scores. **MLflow's built-in evaluation** can calculate custom metrics like these and log them with every run, so the comparison in Episode 04's experiment table would already be on the honest number. That's next for me.

## 9. Key terms

| Term | Plain English |
|---|---|
| **Base rate** | How common the outcome is overall — the share of rows that are churners |
| **PR AUC** | Area under the precision-recall curve; its floor equals the base rate |
| **Precision** | Of the people flagged, how many really churned |
| **Recall** | Of all churners, how many were flagged |
| **Threshold / cut-off** | The score above which you act |
| **Lift** | How many times better than random the model's top group is |
| **Top-decile lift** | Lift measured on the 10% the model ranks as highest risk |
| **Value-to-action table** | A cut-off per action, with the precision, recall and reach of each |
| **Predictions table** | A Delta table holding every score with the model version and threshold |
| **Late-arriving labels** | Outcomes that are only known weeks after the prediction |
| **MLflow evaluation** | MLflow's tooling for computing and logging evaluation metrics with a run |

## 10. Check yourself

1. Why does a random model's PR AUC roughly equal the base rate?
2. Pooling a market with more churn raised PR AUC. What else would you check before calling the model better?
3. What does a top-decile lift of 3 mean in plain English?
4. Why does a discount need a higher cut-off than a reminder?
5. Which columns must a predictions table carry so it can be evaluated a month later?

---

## Next episode

The model is chosen and judged honestly. Now it has to run every day without anyone pressing a button — trained, promoted, scored and watched, all as config.

**Episode 06 · A model that runs itself.**

---

**Prateek Kashyap** · Databricks at Scale · LinkedIn: **pratkashyap**
