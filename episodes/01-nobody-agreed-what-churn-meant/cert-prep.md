# Episode 01 · Certification prep

> Runs silently alongside the series — **never mentioned in posts.** About 15 minutes.
> **Target exam not confirmed yet** (see `PROGRESS.md`). These topics sit in the foundations of every Databricks associate-level exam. Pull the current official exam guide before relying on any summary, including this one.

---

## Recall — cover the right column

| Prompt | Answer |
|---|---|
| What problem does a lakehouse solve? | Two systems (lake + warehouse) holding two copies with drifting rules. A lakehouse keeps one copy in open formats, with warehouse-grade reliability and governance on top |
| What is Delta Lake? | The open table format Databricks stores data in — Parquet files plus a transaction log that adds reliability (details: Episode 02) |
| What is Unity Catalog? | Databricks' governance layer: one place for every data asset, its access rules, and its lineage |
| Unity Catalog's naming levels? | `catalog.schema.table` |
| What else besides tables can Unity Catalog govern? | Views, volumes (files), functions and registered ML models, among others |
| Why a separate catalog per environment? | Isolation — development work can't read or overwrite production data, and access can differ per environment |
| How do you attach a description to a table? | `COMMENT ON TABLE <name> IS '<text>'` — it's stored in the catalog and shown wherever the table is browsed |
| How do you combine a rate across groups correctly? | Sum the numerators, sum the denominators, then divide — never average the group-level rates |

## Applied questions

**1.** Two dashboards report different churn rates from the same governed table. Both queries run without errors. What's the most likely cause?

<details><summary>Answer</summary>
A definition difference, not a data error — a different filter, time window, population or roll-up method (for example, one averages market rates while the other sums then divides). The fix is a single written definition applied in one place, not "better data".
</details>

**2.** A team wants every analyst to calculate "churn rate" identically, whichever tool they use. A shared SQL view exists already. Why might that not be enough?

<details><summary>Answer</summary>
A view returns rows, not rules: consumers can still aggregate it incorrectly. Defining the measure together with its aggregation logic in the governed layer (for example, a metric definition in Unity Catalog) removes that freedom.
</details>

**3.** Why register an ML model in Unity Catalog rather than keeping it only in a workspace?

<details><summary>Answer</summary>
The model is then governed like the data: the same access controls, discoverability and lineage apply, and it can be promoted across environments under one set of rules.
</details>

## Spaced repetition

- **Now:** answer everything above without looking.
- **At Episode 03:** re-answer the three applied questions cold.
- **At Episode 06:** re-answer any you missed twice.
