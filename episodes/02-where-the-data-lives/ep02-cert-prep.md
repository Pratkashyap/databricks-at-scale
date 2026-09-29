# Episode 02 · Certification prep

> Runs alongside the series, **never mentioned in posts.** About 15 minutes.
> Check the current official exam guide before relying on any summary, including this one.

---

## Recall — cover the right column

| Prompt | Answer |
|---|---|
| The three medallion layers? | Bronze (raw as it arrived), silver (cleaned and conformed), gold (business-ready) |
| What is a Delta table made of? | Data files plus a transaction log recording every change |
| What does the transaction log enable? | All-or-nothing writes, schema enforcement, time travel, concurrent reads and writes |
| How do you read a table as it was earlier? | Time travel — by version or by timestamp |
| `CAST` vs `TRY_CAST`? | `CAST` fails the query on bad input; `TRY_CAST` returns NULL and keeps going |
| Job cluster vs all-purpose cluster? | Job: created per run, destroyed after, lower rate. All-purpose: interactive, persists until stopped, higher rate |
| Why is the driver never on spot? | Losing a worker retries a task; losing the driver kills the whole run |
| What does Photon accelerate? | Vectorised SQL and DataFrame work — not plain Python on the driver |
| Why an LTS runtime in production? | Stability: it's supported and patched, and doesn't shift under a running job |
| What is schema enforcement? | Writes that don't match the table's schema are rejected rather than silently accepted |

## Applied questions

**1.** A scheduled job that has run for months suddenly fails with a type conversion error. Nothing in your code changed. What happened, and what are the two fixes — immediate and structural?

<details><summary>Answer</summary>
An upstream schema change (schema drift): a column's type or contents changed. Immediate: read defensively with <code>TRY_CAST</code> and count the failures. Structural: agree a contract with the upstream owner so schema changes are announced, and add a data-quality check that alerts on a rise in unparseable values.
</details>

**2.** A monthly pipeline ran on the 1st and produced a number that looked plausible but was too low. No errors. Why, and what stops it happening again?

<details><summary>Answer</summary>
It ran before the source month had fully landed, so it built on partial data. A freshness gate as the job's first step — refuse to run until the expected data is present — converts a silent wrong answer into a visible "not yet".
</details>

**3.** Someone asks why last month's churn number is different from the figure they wrote down in a review. How do you answer without guessing?

<details><summary>Answer</summary>
Time travel: read the table as of the earlier date and compare it with today's version. That shows whether the data changed (late-arriving records, a restatement) or the definition did.
</details>

## Spaced repetition

- **Now:** answer everything above unaided.
- **At Episode 04:** re-answer the three applied questions, plus Episode 01's.
- **At Episode 07:** full sweep of Episodes 01–04.
