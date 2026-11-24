# Episode 06 · Certification prep

> Runs alongside the series, **never mentioned in posts.** About 15 minutes.
> Check the current official exam guide before relying on any summary, including this one.

---

## Recall — cover the right column

| Prompt | Answer |
|---|---|
| What is a Databricks Asset Bundle? | A project that declares jobs, pipelines, clusters and settings as YAML (`databricks.yml`), deployed with the Databricks CLI |
| What is a bundle target? | A named deployment environment (e.g. dev, staging, prod) with its own settings and variable values |
| `mode: development` vs `mode: production`? | Development prefixes resources per user and pauses schedules; production enforces stricter checks for shared deployment |
| Validate, deploy, run? | `databricks bundle validate`, `databricks bundle deploy -t <target>`, `databricks bundle run <job> -t <target>` |
| How is a model named in the Unity Catalog registry? | Three levels, like a table: `catalog.schema.model` |
| How do you point MLflow at the UC registry? | `mlflow.set_registry_uri("databricks-uc")` |
| What is a model alias? | A movable, named pointer to one model version, e.g. `@champion` |
| How do you load a model by alias? | `mlflow.pyfunc.load_model("models:/catalog.schema.model@champion")` |
| How do you move an alias? | `MlflowClient().set_registered_model_alias(name, alias, version)` |
| Job cluster vs all-purpose cluster? | A job cluster is created for a run and terminated after it; all-purpose clusters are shared and interactive |
| What is a repair run? | Re-running only the failed tasks of a Workflows job run, and their dependants |
| KS vs PSI? | KS: largest gap between two cumulative distributions. PSI: weighted shift in bucket shares; > 0.25 is commonly read as a significant shift |
| Data drift vs concept drift? | Data drift: the inputs change. Concept drift: the relationship between inputs and outcome changes |
| What does Lakehouse Monitoring provide? | Managed profile and drift metrics for a table, including inference tables, written to metric tables with a dashboard |
| Batch inference vs a serving endpoint? | Batch scores many rows on a schedule into a table; an endpoint answers individual requests in real time |

## Applied questions

**1.** A team deploys the same job to staging and production by recreating it in the UI each time. Production fails after a change that worked in staging. What would prevent this?

<details><summary>Answer</summary>
Declare the job once in an Asset Bundle, with environment differences as variables per target, and deploy both environments from the same git commit with `databricks bundle deploy -t <target>`. The configuration can then only differ where a variable says it should.
</details>

**2.** A scoring notebook loads `models:/analytics.ml.churn_model/7`. Version 8 is better. What's the cleaner design?

<details><summary>Answer</summary>
Load by alias — `models:/analytics.ml.churn_model@champion` — and promote by moving the alias to version 8 after it passes a gate. The scoring code never changes, and rollback is moving the alias back.
</details>

**3.** A model is retrained on the first of every month whatever happens. What are the risks, and what's the alternative?

<details><summary>Answer</summary>
When nothing changed, it spends compute and may swap a good model for a merely different one; when something did change, it waits for the date. Monitor data and performance drift, retrain only when it's flagged, and promote the new version only if it beats the current one.
</details>

## Spaced repetition

- **Now:** answer everything above unaided.
- **At Episode 08:** re-answer these three, plus Episode 05's.
- **At Episode 09:** full sweep of Episodes 01–07.
