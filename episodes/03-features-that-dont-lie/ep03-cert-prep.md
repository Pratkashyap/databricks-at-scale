# Episode 03 · Certification prep

> Runs alongside the series, **never mentioned in posts.** About 15 minutes.
> Check the current official exam guide before relying on any summary, including this one.

---

## Recall — cover the right column

| Prompt | Answer |
|---|---|
| What is a feature table? | A governed table of ready-made features, shared across models, so they're built once rather than per notebook |
| What two things must a Unity Catalog feature table have for point-in-time lookups? | A **primary key** and a **timestamp** column |
| What is a point-in-time lookup? | Fetching each training row's features as they were at that row's own cut-off, not as they are today |
| What is leakage? | A feature built from data dated after the prediction point. Training scores look excellent; live performance collapses |
| What is training/serving skew? | Features computed differently at training and scoring time, so the model sees inputs that don't match what it learned |
| Two ways to prevent skew | One shared feature table both paths read, and one shared code path for the final transformations |
| Why keep grain consistent with the label? | Features and label join cleanly, and each row has exactly one outcome |
| Why split an observation window? | A total hides direction. Early vs late sub-windows and a trend separate "declining" from "steady" |
| Where do feature aggregations usually run? | SQL over silver event tables, published as a gold table — a job cluster for scheduled runs, a SQL warehouse for exploration |
| What does one-hot encoding do? | Turns a category into separate yes/no columns so a model can use it |

## Applied questions

**1.** A churn model scores 0.95 AUC in training and barely beats random in production. Nothing about the data pipeline failed. What is the most likely cause, and how do you confirm it?

<details><summary>Answer</summary>
Leakage. A feature includes information from after the prediction point. Confirm by listing every feature with the latest date its source data can carry, and compare that against the cut-off; the offender is usually an aggregate whose window runs past the cut-off, or a status column updated after the event.
</details>

**2.** Training builds features in a notebook; the daily scoring job rebuilds them in its own notebook. Both pass their tests. What risk remains, and what removes it?

<details><summary>Answer</summary>
Training/serving skew — the two implementations can diverge (a different null fill, a different category order) with no error raised. Remove it by having both read one governed feature table, and by sharing one code module for the final transformations. A feature store makes this the platform's responsibility.
</details>

**3.** Why does a feature table need a timestamp as well as a primary key?

<details><summary>Answer</summary>
The key identifies the entity; the timestamp lets the platform return the feature values as they were at a given moment. Without it you can only fetch current values, which leaks the future into historical training rows.
</details>

## Spaced repetition

- **Now:** answer everything above unaided.
- **At Episode 05:** re-answer these three, plus Episode 02's.
- **At Episode 07:** full sweep of Episodes 01–04.
