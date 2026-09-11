# Discovery questionnaire

The questions a Databricks Specialist Solutions Architect would ask before designing anything — turned inward, at your own environment and your own churn project.

**Why this exists:** the project can only be built on what you have actually done. Answering these turns "I used Databricks" into specific, defensible claims — and shows exactly where the real skill gaps are.

**How to use it:** answer what you know, write **"don't know"** where you don't. *Don't know* is the useful answer — it maps the gap. Don't research before answering.

⭐ = highest leverage. Answer these first if short on time.

---

## A. Your environment

1. ⭐ Which cloud is the workspace on — AWS, Azure or GCP? Same across regions?
2. How many workspaces, and split how — by region, business unit, or dev/prod?
3. ⭐ Unity Catalog, or still Hive metastore? If UC — migrated or greenfield?
4. What compute do you use — all-purpose clusters, job clusters, SQL warehouses, serverless? Who chooses the config?
5. Is there a central platform/data engineering team, or does analytics own its own compute?
6. Is Databricks SQL in use, or is everything notebooks?
7. Which Databricks Runtime version? Photon on or off?
8. Do you have admin rights anywhere, or are you purely a workspace user?

## B. Data — what you consume vs what you own

9. ⭐ Where does data land before you touch it, and who owns bronze/silver?
10. Do you own any tables, or is it read-only? Do you publish any gold tables others depend on?
11. Delta everywhere, or mixed formats? Any Iceberg or external tables?
12. Batch or streaming? What's the freshness SLA on the data you use?
13. How does data arrive — Fivetran, ADF, Lakeflow, custom jobs? Do you have visibility into it?
14. Have you ever had to debug a pipeline you didn't write? What happened?

## C. The churn project — what you actually built

15. ⭐ What was the real scope — one market, one business unit, or regional from day one?
16. ⭐ Did you actually split voluntary and involuntary churn, or is that aspirational?
17. What features went in — behavioural (viewing), transactional (payments), demographic, tenure?
18. Feature Store / feature engineering in Unity Catalog — used it, or engineered inside the training notebook?
19. What model? What did you benchmark it against?
20. ⭐ How was it evaluated — AUC alone, or a business metric (uplift, revenue retained, campaign ROI)?
21. How is it served — batch scores to a table, a serving endpoint, or pushed into a campaign tool?
22. What cadence — scoring daily/weekly? Retraining on what trigger?
23. ⭐ What did the CI/CD actually cover — notebooks, jobs, model promotion, tests? Which tooling (Asset Bundles, GitHub Actions, Azure DevOps, Jenkins)?
24. Is anything monitored — data drift, model performance, data quality? Lakehouse Monitoring, or custom?
25. ⭐ Did it go live and get used by a business team? What intervention did it drive?
26. Can you state impact generically without breaching confidentiality — e.g. "a single-digit percentage improvement in retention among targeted subscribers"?
27. What would you build differently if you started it again today?

## D. Scaling APAC → global — the live problem

28. ⭐ What's actually blocking the global rollout — technical, governance, or organisational?
29. ⭐ Are there data residency constraints? Any market legally unable to move data cross-border?
30. One catalog or per-region catalogs? How is access split today?
31. ⭐ One global model, or a model per market? Which do you believe is right, and why?
32. Do different markets define the same metric differently? (Almost always yes — this is the metric contract problem at global scale.)
33. Who pays for compute — central budget or per-market? Is cost attributed anywhere?
34. Do you have visibility into Databricks spend at all? System tables, usage dashboards, tags?
35. What breaks first when you go from 8 markets to 40 — data volume, governance, cost, or people?

## E. GenAI and agents

36. The multi-agent assistant — what does it run on? Databricks, or elsewhere?
37. Does it touch governed data, documents, or both?
38. Was it evaluated in any structured way, or judged by user feedback?
39. Vector Search, Foundation Model APIs, external models — any of these in play?
40. Who uses it, and what would break if it gave a wrong answer?

## F. You — skills and target

41. ⭐ For each, mark **can do unaided / could with docs / never touched**:

| Capability | Level |
|---|---|
| Unity Catalog design (catalogs, grants, row filters) | |
| Delta optimisation (OPTIMIZE, Z-order, liquid clustering) | |
| Lakeflow / DLT pipeline authoring | |
| Auto Loader / Structured Streaming | |
| Feature Store / feature engineering in UC | |
| MLflow tracking, registry, model aliases | |
| Model serving endpoints | |
| Databricks Asset Bundles | |
| Workflows / job orchestration | |
| Cluster config and cost tuning | |
| Databricks SQL / AI-BI dashboards | |
| Genie / semantic layer | |
| Vector Search / RAG on Databricks | |
| Agent framework and evaluation | |
| System tables / cost attribution | |
| Delta Sharing / Clean Rooms | |

42. ⭐ Have you read actual JDs for the roles you want? Paste two or three — they should drive what this project emphasises.
43. Which certification are those JDs asking for, if any?
44. Realistic weekly time budget, honestly?
45. Do you have a real workspace you can experiment in, or is Free Edition the lab?
46. What do you want a hiring manager to conclude in the first 30 seconds of seeing this repo?

---

## Answering notes

- **"Don't know" is data.** Every one is a candidate module.
- **Nothing confidential.** Shapes and methods, never figures, market names or internal tool names.
- Questions marked ⭐ are the ones that change the project's design. The rest refine it.
