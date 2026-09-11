# Setup

Follow along hands-on in about 15 minutes. You don't need a cloud account or a credit card.

## 1. Get a free Databricks workspace

Sign up for **Databricks Free Edition** at [databricks.com](https://www.databricks.com/learn/free-edition). It includes the parts this series uses: notebooks, the SQL editor, Unity Catalog and serverless compute.

## 2. Create a schema to work in

Open the **SQL editor** and run:

```sql
CREATE SCHEMA IF NOT EXISTS databricks_at_scale;
USE SCHEMA databricks_at_scale;
```

This creates the schema in your workspace's default catalog. Unity Catalog's three-part naming (`catalog.schema.table`) is explained in [Episode 01](episodes/01-nobody-agreed-what-churn-meant/learn.md).

## 3. Read and run each episode

Each episode's `learn.md` includes example SQL. In **Season 1** the examples are **illustrative**: they show the pattern, using generic table names. A synthetic subscription dataset you can run everything against will arrive in a later episode, along with a script to generate it.

## About the data

Everything in this repo is synthetic or illustrative. No real subscribers, figures or markets.
