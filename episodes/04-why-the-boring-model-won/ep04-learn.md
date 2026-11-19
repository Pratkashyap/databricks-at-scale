# Episode 04 · Why the boring model won

**Season 2 · The Build** — *From a notebook to a system*

> **The learning doc.** The LinkedIn post is the short version; this is the detail.
> No Databricks experience needed — every term is explained where it first appears.

---

## 1. Where we left off

Season 1 settled what churn means (Episode 01), made the data safe to read (Episode 02), and built honest, point-in-time features in Unity Catalog (Episode 03). Season 2 is the build: turning those features into a model, then into a system.

This is the part most people expect to be hard. It turned out to be the part where the right answer was the plain one.

## 2. The situation

With good features in place, the obvious move is a bake-off: try several algorithms and designs, keep the best. I tried:

| Tried | What it was | Outcome |
|---|---|---|
| **XGBoost** | Gradient-boosted trees, the standard choice for tabular data | **Kept** |
| **LightGBM** | A faster cousin of XGBoost | Dropped |
| **Two more algorithms** | Rounding out a four-way comparison | Dropped |
| **Per-market models** | A separate model for each market | Dropped |
| **Per-tenure models** | A separate model for first-month and second-month subscribers | Dropped |
| **SMOTE** | Generating synthetic churners to balance the classes | Dropped |

What survived was **one XGBoost model, class-weighted, pooled across all markets**. It won on the metric *and* on operational simplicity — and the second of those matters more than people expect.

## 3. Problem 1 — dozens of runs, and no memory of which was which

A bake-off produces runs fast: four algorithms, several settings each, separate per-market and per-tenure variants. Within a day you have dozens of results and a spreadsheet you half-trust. A week later nobody can say which settings produced the score in the slide.

### The Databricks part: MLflow experiments

**MLflow** is the experiment tracker built into Databricks. An **experiment** is a named folder; every training attempt inside it is a **run**. Each run records:

- **Parameters** — the settings you chose (learning rate, tree depth, class weight)
- **Metrics** — the scores it achieved
- **Artifacts** — the trained model itself, plus anything else you attach (plots, feature lists)

```python
import mlflow
import xgboost as xgb

mlflow.set_experiment("/Shared/churn/model-bakeoff")

with mlflow.start_run(run_name="xgboost-weighted"):
    params = {
        "objective": "binary:logistic",
        "eval_metric": "aucpr",            # PR AUC: suited to a rare positive class
        "tree_method": "hist",
        "scale_pos_weight": n_negative / n_positive,
    }
    mlflow.log_params(params)

    booster = xgb.train(params, dtrain, num_boost_round=500,
                        evals=[(dvalid, "valid")], early_stopping_rounds=50)

    mlflow.log_metric("valid_pr_auc", booster.best_score)
    mlflow.xgboost.log_model(booster, "model")
```

The experiment page then becomes a table: every run, every parameter, every metric, sortable and comparable side by side. **The bake-off stops being a story you remember and becomes a record you can query.** And because the model is logged with the run, the winner can be registered straight from it — which is where Episode 06 picks up.

## 4. Problem 2 — churners are rare

Most subscribers renew. So a model that predicts "nobody leaves" is right most of the time — and completely useless. This is **class imbalance**, and it breaks two things:

- **Accuracy lies.** If 95% of rows are renewals, "always renew" scores 95% accuracy. *(Numbers illustrative.)*
- **Training drifts toward the majority.** Left alone, the model optimises for getting renewals right and treats churners as noise.

Two common fixes:

| Fix | How it works | Here |
|---|---|---|
| **Resampling (e.g. SMOTE)** | Invent synthetic churners until the classes balance | Added complexity, no measurable gain — dropped |
| **Class weighting** | Tell the model a missed churner costs more than a missed renewal | **Kept** — one setting, `scale_pos_weight` |

Class weighting won because it's one line, it doesn't fabricate data, and it changes nothing about the rows the model sees — so the training data still matches what scoring will see.

The choice of metric matters here too: `aucpr` (area under the precision-recall curve) focuses on how well the model finds the rare class, which is why it was the primary metric. Episode 05 is about the trap hiding inside that metric.

## 5. Problem 3 — one model per market multiplies everything

Per-market models are the obvious idea: each market has its own content, plans and habits, so give each its own model.

The cost shows up after training:

- **N models to retrain**, each with its own schedule and failures
- **N models to monitor** for drift
- **N models to explain** to the business, each slightly different
- **Small markets have few churners**, so their models learn from very little

A single **pooled model** with market as a feature gets most of the per-market nuance — the model can still learn that markets differ — while keeping one thing to run. In this project it won on the metric as well as on simplicity, which made the decision easy.

There's a bigger reason pooling won, and it only becomes visible when you try to scale from one region to many. That's Episode 08.

## 6. One more decision: tune once, then lock

Hyperparameters — the model's settings — were tuned during the bake-off and then **locked**. Later retrains refit the same settings on new data rather than re-running a search each time.

Re-tuning on every retrain looks diligent, but it mostly chases noise: each new search finds settings that happen to suit this month's sample, and the model's behaviour shifts for no real reason. Locking them means a change in performance is a signal about the data, not about the search. How retraining is triggered is Episode 06.

## 7. What it cost

| Decision | What it bought | What it cost |
|---|---|---|
| One algorithm, not an ensemble | Simple to retrain, monitor and explain | Possible small gains left on the table |
| Class weighting, not SMOTE | One setting; no synthetic rows | Less fine-grained control of the balance |
| One pooled model | One thing to run instead of one per market | Less room to tailor any single market |
| Locked hyperparameters | Stable behaviour between retrains | Not chasing every small improvement |

## 8. What you can copy

- [ ] Track **every** run in an experiment — parameters, metrics and the model — from the first day
- [ ] Never use accuracy on an imbalanced problem; pick a metric that focuses on the rare class
- [ ] Try **class weighting before resampling** — it's one setting and fabricates nothing
- [ ] Before building one model per segment, count what you'd have to retrain, monitor and explain
- [ ] Tune once, lock the settings, and let retrains refit rather than re-search
- [ ] Judge candidates on the metric **and** on what they cost to run

## 9. Key terms

| Term | Plain English |
|---|---|
| **Bake-off** | Training several candidate models and comparing them fairly |
| **XGBoost / LightGBM** | Gradient-boosted tree algorithms — the usual strong choice for table data |
| **MLflow** | The experiment tracker and model manager built into Databricks |
| **Experiment** | A named collection of training runs |
| **Run** | One training attempt, with its parameters, metrics and model recorded |
| **Parameters / hyperparameters** | The settings you choose before training |
| **Artifact** | A file saved with a run — most importantly the model itself |
| **Class imbalance** | One outcome is much rarer than the other |
| **SMOTE** | A resampling method that creates synthetic examples of the rare class |
| **`scale_pos_weight`** | XGBoost's setting for how much more a rare-class mistake should count |
| **PR AUC (`aucpr`)** | A score of how well the model finds the rare class across all thresholds |
| **Early stopping** | Stopping training when the validation score stops improving |
| **Pooled model** | One model trained across all segments, with the segment as a feature |

## 10. Check yourself

1. What does an MLflow run record, and why does that matter in a bake-off?
2. Why is accuracy misleading when churners are rare?
3. What's the difference between class weighting and SMOTE, and why did weighting win here?
4. List three costs of one-model-per-market that don't show up in the training score.
5. Why lock hyperparameters instead of re-tuning on every retrain?

---

## Next episode

The model was chosen and its score improved as more markets were pooled in. It looked like progress. It wasn't — the score had gone up, but the model hadn't got any better.

**Episode 05 · My metric was lying to me.**

---

**Prateek Kashyap** · Databricks at Scale · LinkedIn: **pratkashyap**
