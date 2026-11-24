# Episode 06 · A model that runs itself

**Season 2 · The Build** — *From a notebook to a system* · **season finale**

> **The learning doc.** The LinkedIn post is the short version; this is the detail.
> No Databricks experience needed — every term is explained where it first appears.

---

## 1. Where we left off

Episode 04 chose the model: one class-weighted XGBoost model, pooled across markets. Episode 05 made judging it honest: lift instead of a raw score, a cut-off per action, and every daily score kept in Delta so it can be graded when the outcome arrives.

All of that still worked only if someone remembered to run it. This episode is about removing that someone.

## 2. The situation

A model in a notebook is a demo. To be a system it has to do four things on its own:

| Step | How often | What happens |
|---|---|---|
| **Score** | Every day | Every active subscriber gets a churn score, appended to the predictions table |
| **Check** | Every month | Once last month's outcomes are known, the inputs and the results are compared with the past |
| **Retrain** | Only when the check says so | The model is refit on fresh data with the same settings |
| **Promote** | Only if it's better | The new model replaces the current one, or it doesn't |

The everyday picture is a **thermostat**. It doesn't heat the room on a timetable. It checks the temperature, and acts only when it drifts.

Three questions decide whether that loop can run without anyone watching.

## 3. Question 1 — will it deploy the same way every time?

### The problem

The same jobs have to exist in development, integration, staging and production. Built by hand in the workspace UI, they drift apart: a different cluster size here, a missed schedule there, a catalog name typed wrong in one place. Nobody can say exactly what is running in production, or rebuild it.

### The Databricks part: Asset Bundles

A **Databricks Asset Bundle** describes jobs, clusters, schedules and their settings as **YAML files kept in git**. One bundle can deploy to several **targets** — named environments — with **variables** filling in whatever differs between them, such as the catalog name.

The project uses **one bundle with four targets**. Here's the shape of it, with generic names:

```yaml
# databricks.yml  (illustrative — names are generic)
bundle:
  name: churn-model

variables:
  catalog:
    description: Unity Catalog catalog for this environment

targets:
  dev:
    mode: development        # resources are prefixed per developer
    default: true
    variables: { catalog: dev_analytics }
  int:
    variables: { catalog: int_analytics }
  stg:
    variables: { catalog: stg_analytics }
  prd:
    mode: production
    variables: { catalog: analytics }

resources:
  jobs:
    churn_daily_score:
      name: churn-daily-score
      schedule:
        quartz_cron_expression: "0 0 6 * * ?"   # every morning
        timezone_id: UTC
      tasks:
        - task_key: score
          notebook_task:
            notebook_path: ./notebooks/score.py
            base_parameters:
              catalog: ${var.catalog}
```

Deploying is then one command per environment:

```bash
databricks bundle validate -t stg     # check the config before deploying
databricks bundle deploy   -t prd     # create or update the jobs in production
databricks bundle run churn_daily_score -t prd   # run a job on demand
```

The jobs themselves run as **Workflows** — Databricks' scheduler. A Workflows job is a set of **tasks** with dependencies between them, each running on a **job cluster** that starts for the run and stops after it.

## 4. Question 2 — who decides the new model is better?

### The problem

Without a rule, a model goes live because it's *newer*, not because it's *better*. And if the scoring code names a specific model version, every promotion means a code change.

### The Databricks part: aliases in the Unity Catalog model registry

Models are registered in **Unity Catalog**, with the same three-part name as a table — `catalog.schema.model`. Each registration creates a numbered **version**. An **alias** is a movable label that points at one version.

The project uses two:

- **`@champion`** — the version that scores production today
- **`@candidate`** — the version that has just been retrained and is waiting to be judged

The daily scoring job always loads `@champion`. It never names a version number, so it never needs to change.

```python
import mlflow
from mlflow import MlflowClient

mlflow.set_registry_uri("databricks-uc")      # use the Unity Catalog registry
client = MlflowClient()
MODEL = "analytics.ml.churn_model"            # generic name

# The scoring job: whatever holds the champion label
champion = mlflow.pyfunc.load_model(f"models:/{MODEL}@champion")

# After a retrain: label the new version as the candidate
client.set_registered_model_alias(MODEL, "candidate", new_version)

# The gate: promote only if the candidate is better, by a statistical test
if candidate_beats_champion(holdout):
    client.set_registered_model_alias(MODEL, "champion", new_version)
```

**The gate** compares candidate and champion on the same held-out data and promotes only when the difference is statistically meaningful — not just a higher number on one run. Episode 05's lesson applies: the comparison is on lift, per market, not on the raw score.

There is a second gate before this one: a **reproducibility checklist**. The training job refuses to register a model at all unless a set of checks all pass — the same data window, the same locked settings, the expected columns.

Rolling back is moving the label back to the previous version. Nothing is redeployed.

## 5. Question 3 — when should it retrain?

### The problem

Retraining on a calendar does two wrong things. When nothing has changed, it spends compute and risks swapping a good model for a different one. When something *has* changed — a price change, a new market — it waits for the date.

### The fix: drift checks, then retrain

Once a month, after the previous month's outcomes are known, a monitoring job compares the present with a rolling reference of past months. It checks two kinds of drift:

| Kind | What it asks | Typical test |
|---|---|---|
| **Data drift** | Do the inputs look different? | **KS** for numeric features, **PSI** for categories |
| **Performance drift** | Does the model still separate churners from stayers? | Lift per market against a stability band; the churn rate itself |

- **KS (Kolmogorov–Smirnov)** measures the biggest gap between two distributions. 0 means identical.
- **PSI (Population Stability Index)** measures how much the share in each bucket has shifted. Common rules of thumb: under 0.10 stable, 0.10–0.25 worth a look, over 0.25 a real shift.

A sketch of PSI:

```python
import numpy as np

def psi(reference, current, bins=10):
    edges = np.quantile(reference, np.linspace(0, 1, bins + 1))
    current = np.clip(current, edges[0], edges[-1])
    ref = np.histogram(reference, edges)[0] / len(reference)
    cur = np.histogram(current,   edges)[0] / len(current)
    ref, cur = np.clip(ref, 1e-6, None), np.clip(cur, 1e-6, None)
    return float(np.sum((cur - ref) * np.log(cur / ref)))
```

Every result is written to a **drift-log table** and rolled into a monthly health brief with one headline: **GREEN, AMBER or RED**. That headline is the retrain trigger.

When it fires, the retrain refits on the full rolling history including the new month, with **locked hyperparameters** — the settings chosen in Episode 04. No fresh search each time. Same settings, fresh data, so a change in the model can be traced to a change in the data.

The new version becomes `@candidate`, and Question 2's gate decides the rest.

## 6. Why batch, not a serving endpoint

Databricks can host a model behind a **serving endpoint** that answers in milliseconds. This project doesn't, on purpose: the action is a retention contact the next day, so a daily batch score written to a table is the right speed. Real-time serving would add cost and moving parts for no gain. The predictions table *is* the serving layer.

## 7. What it cost

| Decision | What it bought | What it cost |
|---|---|---|
| One bundle, four targets | Every environment built the same way, from git | YAML to learn and maintain |
| Aliases with a statistical gate | No code change to promote or roll back; no "newer wins" | A candidate can wait a month to be judged |
| Retrain on drift, not a calendar | Compute spent only when something changed | A monitoring job to build and trust |
| Locked hyperparameters | Changes traceable to data, not tuning | Possible small gains from re-tuning left unclaimed |
| Tests as in-pipeline gates | Bad models stopped before registration | No automated tests run on a pull request yet |

## 8. What you can copy

- [ ] Put every job, cluster and schedule in an **Asset Bundle**; deploy with `bundle deploy -t <env>`, never by hand
- [ ] Use **variables** for anything that differs between environments, starting with the catalog name
- [ ] Load models by **alias**, never by version number
- [ ] Promote only through a **gate**: the candidate must beat the champion on the same data, per segment
- [ ] Write every drift result to a **table**, not just a chart, and turn it into one headline
- [ ] Retrain on a **trigger**, with **locked settings**, so changes can be explained
- [ ] Choose batch or real-time by **when the action happens**, not by what sounds modern

## 9. Learning next

- **Lakehouse Monitoring** — Databricks' built-in monitoring for tables and model inputs. It could replace the custom data-drift half. The performance half stays custom, because it depends on outcomes that arrive weeks late.
- **Automated tests on every pull request** — unit tests on the preprocessing, plus `databricks bundle validate`, run by a CI service before anything merges. Today the tests are gates inside the pipeline.

## 10. Key terms

| Term | Plain English |
|---|---|
| **Asset Bundle** | Jobs, clusters and settings described as YAML in git, deployable to any environment |
| **Target** | A named environment a bundle deploys to — dev, staging, production |
| **Workflows job** | A scheduled set of tasks with dependencies between them |
| **Job cluster** | Compute that starts for one run and stops after it |
| **Model registry (Unity Catalog)** | Where model versions are stored and governed, named `catalog.schema.model` |
| **Model version** | One registered copy of a model, numbered |
| **Alias** | A movable label on a model version, such as `@champion` |
| **Promotion gate** | The rule a new model must pass before it takes over |
| **Drift** | When the data or the model's results move away from what it was trained on |
| **KS** | The biggest gap between two distributions |
| **PSI** | How much the share in each bucket has shifted |
| **Locked hyperparameters** | Model settings fixed after selection, reused on every retrain |
| **Serving endpoint** | A hosted model that answers requests in real time |

## 11. Check yourself

1. Why load the model by alias rather than by version number?
2. What goes in a bundle's `targets` section, and what do variables do there?
3. Retraining every month on a schedule — what two things can go wrong?
4. What's the difference between data drift and performance drift?
5. Why was a daily batch score the right choice instead of a serving endpoint?

---

## Next episode

Season 2 ends with a model that runs itself. But a score of 0.83 doesn't tell anyone *why* this subscriber is at risk, or what to say to them. Season 3 opens with the model explaining itself — in plain language, with guardrails.

**Episode 07 · Making it explain itself.**

---

**Prateek Kashyap** · Databricks at Scale · LinkedIn: **pratkashyap**
