# Episode 04 · Certification prep

> Runs alongside the series, **never mentioned in posts.** About 15 minutes.
> Check the current official exam guide before relying on any summary, including this one.

---

## Recall — cover the right column

| Prompt | Answer |
|---|---|
| What is an MLflow experiment? | A named collection of runs, so related training attempts can be compared side by side |
| What does an MLflow run record? | Parameters, metrics, artifacts (including the model), and tags |
| `log_param` vs `log_metric`? | Parameters are inputs set before training; metrics are results, and can be logged repeatedly as steps |
| What does autologging do? | Records parameters, metrics and the model automatically for supported libraries, without explicit log calls |
| How do you log a model with MLflow? | A flavor-specific call such as `mlflow.xgboost.log_model`, which stores the model as a run artifact |
| Why is accuracy a poor metric on imbalanced data? | Predicting only the majority class scores highly while finding none of the rare class |
| What does `scale_pos_weight` do in XGBoost? | Increases the weight of the positive (rare) class in the loss — commonly set near negatives ÷ positives |
| Class weighting vs resampling? | Weighting changes how errors count; resampling changes the rows (e.g. SMOTE creates synthetic positives) |
| What is early stopping? | Halting training when the validation metric stops improving for a set number of rounds |
| What is Databricks AutoML for? | Generating a baseline: it trains and tunes candidate models and produces editable notebooks for each |

## Applied questions

**1.** A team ran forty training jobs over two weeks and can't reproduce the model shown in a review deck. What would have prevented this?

<details><summary>Answer</summary>
Logging every attempt as an MLflow run inside one experiment, with its parameters, metrics and the model artifact. The experiment table then identifies exactly which run produced the result, and the model can be loaded from that run.
</details>

**2.** A churn model reports 96% accuracy on a dataset where 4% of customers churn. Is it a good model?

<details><summary>Answer</summary>
Unknown, and probably not. A model that predicts "nobody churns" also scores 96%. Evaluate with a metric focused on the rare class (precision, recall, PR AUC, lift) and compare against the base rate.
</details>

**3.** Per-segment models each score marginally better than a single pooled model. What else should decide the choice?

<details><summary>Answer</summary>
Operating cost: the number of models to retrain, monitor, register and explain, and whether small segments have enough positive examples to train reliably. A pooled model with the segment as a feature often keeps most of the benefit with a fraction of the overhead.
</details>

## Spaced repetition

- **Now:** answer everything above unaided.
- **At Episode 06:** re-answer these three, plus Episode 03's.
- **At Episode 08:** full sweep of Episodes 01–05.
