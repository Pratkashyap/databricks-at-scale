# Episode 05 · Certification prep

> Runs alongside the series, **never mentioned in posts.** About 15 minutes.
> Check the current official exam guide before relying on any summary, including this one.

---

## Recall — cover the right column

| Prompt | Answer |
|---|---|
| Precision? | Of the cases predicted positive, the share that are truly positive |
| Recall? | Of all true positives, the share the model caught |
| What does raising the threshold usually do? | Increases precision and lowers recall |
| ROC AUC vs PR AUC on a rare class? | ROC AUC can look strong even when the rare class is poorly ranked; PR AUC focuses on the positive class |
| What PR AUC does a random model score? | Roughly the base rate — so the baseline changes with the data |
| What is lift? | The positive rate in a selected group divided by the overall base rate |
| Why is lift better than raw PR AUC across segments? | It normalises by each segment's base rate, so segments with different churn levels compare fairly |
| What is F1? | The harmonic mean of precision and recall at one threshold |
| What does `mlflow.evaluate` provide? | Standard evaluation metrics and plots for a model, with support for custom metrics, logged to a run |
| Why store predictions with the model version? | So outcomes arriving later can be joined back and attributed to the exact model and threshold that made each decision |

## Applied questions

**1.** A model's PR AUC rises from one quarter to the next. The code, features and hyperparameters are unchanged. What should you check first?

<details><summary>Answer</summary>
The base rate of the evaluation data. If the share of positives rose — a new market, a seasonal spike — PR AUC rises with it even for an unchanged model. Compare lift, or PR AUC relative to the base rate, before concluding the model improved.
</details>

**2.** The business wants one threshold "for the churn model". Why might that be the wrong question?

<details><summary>Answer</summary>
Different actions have different costs of a wrong guess. A cheap action tolerates low precision for high reach; an expensive one needs high precision. Provide cut-offs per action, each with its precision, recall and volume, and let the business choose.
</details>

**3.** Labels for a churn model arrive six weeks after each prediction. What has to be in place on the day you score?

<details><summary>Answer</summary>
Each score persisted with its key (entity and period), the model name and version, the threshold applied and a timestamp, so the outcomes can be joined back when they arrive and every decision graded against the model that made it.
</details>

## Spaced repetition

- **Now:** answer everything above unaided.
- **At Episode 07:** re-answer these three, plus Episode 04's.
- **At Episode 09:** full sweep of Episodes 01–06.
