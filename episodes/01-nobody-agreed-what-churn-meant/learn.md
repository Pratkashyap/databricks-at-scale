# Episode 01 · Nobody agreed what churn meant

**Season 1 · The Problem** — *What are we even measuring?*

> **This is the learning doc.** The LinkedIn post is the summary; this is everything behind it.
> No Databricks experience needed — every term is explained where it first appears, and there's a glossary at the end.

---

## 1. The situation

A subscription streaming business. Eight markets. One question from the business:

> *Which subscribers are about to cancel — and what should we do about them?*

The obvious first move is to open a notebook and train a model. The first real piece of work was something else: **agreeing what "churn" meant.**

Across eight markets, it didn't mean exactly the same thing. The differences were small and easy to miss:

- **How long the renewal window is** — the period in which a subscriber can still renew
- **What counts as a customer choosing to leave**, versus a payment simply failing
- **How a "reconnect" is treated** — someone who cancels and comes back
- **How plans and tenure are defined** — what "first paid month" even means

Pool eight markets into one model without settling those, and you aren't predicting one thing. **You're predicting eight slightly different things and calling them one.**

---

## 2. Why the definition comes before the model

A model learns whatever the label tells it. (The **label** is the answer column the model is trained to predict — here, "did this subscriber churn: yes or no?")

- **A vague label produces a confident, wrong model.** The algorithm can't tell that the target is inconsistent. It just fits it.
- **Every number downstream inherits the definition** — dashboards, targeting lists, campaign ROI, the board deck.
- **AI makes this worse, not better.** Ask a human analyst an ambiguous question and they'll ask "do you mean including trials?" Ask an AI assistant and it picks one meaning and answers with total confidence. Ambiguity that used to be annoying becomes dangerous the moment you put natural language on top of it.

---

## 3. The metric contract

A **metric contract** is a written definition of a metric that leaves nothing to interpretation. Any metric breaks into six decisions. Change one, and you get a different number.

Here's the contract for the churn project:

| Field | The question it answers | The decision in this project | Why |
|---|---|---|---|
| **Entity** | What are we counting? | One paid **billing cycle** — not a user | Each row has exactly one outcome. A user with several cycles doesn't blur the target. |
| **Event** | What counts as churning? | The **subscriber cancels** themselves | That's the behaviour a retention action can actually change. |
| **Population** | Who's in scope? | **Early tenure** — a subscriber's first or second paid month | One clearly bounded group, so the base the rate is measured against doesn't shift underneath you. |
| **Exclusions** | Who's deliberately out? | **Payment failures** (involuntary churn) | Different cause, different fix — see section 4. |
| **Timing** | When is the outcome known? | Only **after the renewal window closes** | You can't label a cycle until the subscriber has had the chance to renew. |
| **Roll-up** | How does it combine across markets? | Add up across markets, **then** divide | Averaging market rates gives a small market the same weight as a large one — see section 5. |

**The contract is the artifact.** Not the query, not the dashboard — the written decisions. Two people holding the same contract will get the same number.

> **One decision worth writing down explicitly:** when payment-failure cycles are excluded, are they *dropped from the data* or *kept and labelled "not churned"*? The two give different base rates. Neither is wrong — but leaving it unstated is.

---

## 4. The biggest call: voluntary vs involuntary churn

Both end with a lapsed account. They look identical in the subscription table. They are **completely different problems.**

| | Voluntary churn | Involuntary churn |
|---|---|---|
| **What happened** | The subscriber chose to cancel | A payment failed — expired card, declined charge |
| **Root cause** | Product, content, price, value | Payments |
| **Who owns the fix** | Product, content, marketing | Billing, finance |
| **The right intervention** | A reason to stay — content, engagement, an offer | Retry the payment, update the card, offer another payment method |

**The decision in this project: voluntary churn only.** Payment failures were excluded from the label from day one — a design lock, not a later refinement.

### What happens if you mix them

Train one model on both, and it quickly discovers that *"days until the card expires"* is extremely predictive — because for involuntary churn, it is. The model scores well. Then the retention team sends a discount to a list full of people whose cards expired: people who never wanted to leave and just needed to update their payment details.

You spend budget on customers who weren't at risk, and the people genuinely deciding to leave are diluted in the list. **Splitting the two isn't a modelling nicety. It's the difference between a model that saves money and one that quietly spends it.**

---

## 5. The trap: you can't average churn rates

This one reaches board decks. *(Numbers below are made up for illustration.)*

| Market | Subscribers | Churn rate | Churners |
|---|---|---|---|
| A | 2,000,000 | 3% | 60,000 |
| B | 50,000 | 9% | 4,500 |

- **Averaging the two rates:** (3% + 9%) ÷ 2 = **6%**
- **The real combined rate:** 64,500 churners ÷ 2,050,000 subscribers = **about 3.1%**

The average treats a market of 50,000 as if it were as big as a market of 2 million. **Always add up the churners and add up the base, then divide.** That's what the "Roll-up" row of the contract exists to enforce.

---

## 6. Where a definition should live

Writing the contract down is step one. Where it *lives* decides whether anyone follows it.

| Level | Where the definition lives | What happens |
|---|---|---|
| **0** | In people's heads and spreadsheets | Nobody can find it |
| **1** | Hard-coded inside each dashboard | **Where most companies are.** Every dashboard is its own private definition — this is how three teams end up with three numbers |
| **2** | In a shared SQL view | Better — but a view gives you a table, not the rules. Someone can still average the rates |
| **3** | Governed in the data platform | Defined once, with its rules attached, and every tool reads the same one |

The goal is level 3. That's where Databricks comes in.

---

## 7. The Databricks part

### What a lakehouse is

Traditionally companies ran two systems:

- A **data lake** — cheap storage for everything, as raw files. Flexible, but messy and hard to trust.
- A **data warehouse** — clean, structured tables for reporting. Reliable, but expensive and rigid.

That meant two copies of the data, two sets of rules, and constant drift between them.

A **lakehouse** keeps **one copy of the data** in open file formats, and adds warehouse-style reliability and governance on top. **Databricks is a lakehouse platform.** The file format underneath is **Delta Lake** — covered properly in Episode 02.

### Unity Catalog — where the definition lives

**Unity Catalog** is Databricks' governance layer: one place that knows every table, who is allowed to read it, and where its data came from.

Everything in it has a three-part name:

```
catalog . schema . table
   │        │       └─ the table itself        e.g. churn_label
   │        └─ a group of related tables       e.g. gold
   └─ the top-level container                  e.g. analytics
```

How the churn project used it:

- **Separate catalogs per environment** — development, staging, production — so nothing in development can touch production data
- The churn label and the features published as governed **"gold" tables** — *gold* meaning the curated, trusted layer that other teams build on (Episode 02 explains the layers)
- **The model registered in Unity Catalog too** — so the model and the data it depends on follow the same access rules

### The contract, written as code

One way to turn the contract into a governed table. *(Illustrative — table and column names are generic.)*

```sql
-- The churn contract as a governed gold table
CREATE OR REPLACE TABLE analytics.gold.churn_label AS
SELECT
  subscription_id,
  billing_cycle_start,
  market,
  CASE WHEN end_reason = 'subscriber_cancelled' THEN 1 ELSE 0 END AS churned_voluntary
FROM analytics.silver.billing_cycles
WHERE paid_month_number IN (1, 2)        -- Population: early tenure
  AND end_reason <> 'payment_failed'     -- Exclusion: involuntary churn is out
  AND renewal_window_closed = TRUE;      -- Timing: only once the outcome is known

-- Write the contract onto the table itself, so it travels with the data
COMMENT ON TABLE analytics.gold.churn_label IS
  'Voluntary churn, early tenure (paid months 1-2). One row per paid billing cycle.
   Payment failures excluded. Labelled only after the renewal window closes.';
```

And the roll-up, done the right way:

```sql
-- Sum, then divide. Never AVG() a column of market-level rates.
SELECT SUM(churned_voluntary) / COUNT(*) AS voluntary_churn_rate
FROM analytics.gold.churn_label;
```

The comment matters more than it looks: anyone who finds this table in Unity Catalog reads the contract right next to the data, without having to find a document.

### What I'm learning next: metric views and Genie

In the project, the contract lives as a governed table plus its documentation — solidly level 3, but the *aggregation rule* still depends on people writing the query correctly.

Databricks has two features aimed at exactly that gap, which I'm learning in the open:

- **Metric views in Unity Catalog** — define a measure *and its aggregation rule* once, so "churn rate" is always calculated the same way, whichever tool asks
- **AI/BI Genie** — lets people ask questions in plain English against governed data. It's only as trustworthy as the definitions underneath it, which is why this episode comes first

*Feature names and availability change quickly — check the current Databricks documentation before relying on either.*

---

## 8. The decision, and what it cost

Every clause in the contract bought something and cost something:

| Decision | What it bought | What it cost |
|---|---|---|
| Voluntary only | A clean target and the right intervention | The model says nothing about failed payments — another process has to own recovery |
| Early tenure only | A stable, well-defined group | Longer-tenure subscribers aren't scored by this model |
| Billing cycle, not user | One unambiguous outcome per row | More rows, and more care when joining behaviour to cycles |
| Wait for the renewal window | Labels you can trust | Outcomes arrive late — you always evaluate last month, never today (Episode 06) |
| A narrower label overall | Precision | Fewer positive examples to learn from — a rarer class the model has to be helped with (Episode 04) |

**Every one of those was a price paid on purpose.** Writing them down is what turns them into decisions instead of accidents.

---

## 9. What you can copy

Use this on any metric, at any company, before anyone builds anything on it:

- [ ] **Write the six fields down** — entity, event, population, exclusions, timing, roll-up
- [ ] **Look for two different things hiding under one name** — like voluntary and involuntary churn. If they need different fixes, they need different metrics
- [ ] **Decide the roll-up rule explicitly.** Sum then divide — never average rates
- [ ] **Put the definition where the data lives** — on the table, in the catalog — not in a slide or a wiki page
- [ ] **Write down what each decision costs.** If you can't name the cost, you haven't really made the decision
- [ ] **Get one owner to sign it.** A contract nobody owns drifts back into five definitions within a quarter

---

## 10. Key terms

| Term | Plain English |
|---|---|
| **Churn** | A customer stopping their subscription |
| **Voluntary churn** | The customer chose to cancel |
| **Involuntary churn** | The subscription lapsed because a payment failed |
| **Label** | The answer column a model is trained to predict |
| **Early tenure** | A subscriber's first or second paid month |
| **Billing cycle** | One paid period of a subscription — usually a month |
| **Renewal window** | The period in which a subscriber can still renew before their cycle ends |
| **Base rate** | How often the outcome happens overall — e.g. 3% of cycles end in churn |
| **Metric contract** | A written definition of a metric, precise enough that two people always get the same number |
| **Data lake** | Cheap storage for raw files of any kind |
| **Data warehouse** | Structured, cleaned tables built for reporting |
| **Lakehouse** | One copy of the data, with warehouse reliability on top of lake storage |
| **Delta Lake** | The open table format Databricks stores data in (Episode 02) |
| **Unity Catalog** | Databricks' governance layer — every table, who can access it, and where it came from |
| **Catalog · schema · table** | Unity Catalog's three-part naming: container → group → table |
| **Gold table** | The curated, trusted layer other teams build on |
| **Metric view** | A Unity Catalog object that defines a measure and how it aggregates |
| **AI/BI Genie** | A Databricks feature for asking data questions in plain English |

---

## 11. Check yourself

Try answering these out loud, without looking back:

1. Why does the definition of a metric have to come before the model?
2. What are the six fields of a metric contract?
3. Why are voluntary and involuntary churn different problems — and what goes wrong if you mix them?
4. Market A has 2M subscribers at 3% churn, Market B has 50K at 9%. What's the combined rate, and why isn't it 6%?
5. What does Unity Catalog give you that a well-written SQL view doesn't?

---

## Next episode

The contract is written. But the data it depends on comes from tables owned by other teams — and the first time a column arrives in a different type than it's supposed to, the whole job fails.

**Episode 02 · Where the data actually lives** — building on tables I didn't own.

---

**Prateek Kashyap** · Databricks at Scale · LinkedIn: **pratkashyap**
