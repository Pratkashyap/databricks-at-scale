# Episode 01 · LinkedIn post

> **Summary of [`learn.md`](learn.md).** Copy the box, paste into LinkedIn, attach [`poster.png`](poster.png).
> Bold is Unicode bold, so it survives pasting. **2,461 of 3,000 characters** (bold letters count double).

**Before "…see more":** 🎬 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟭 · Databricks at Scale / 𝗡𝗼𝗯𝗼𝗱𝘆 𝗮𝗴𝗿𝗲𝗲𝗱 𝘄𝗵𝗮𝘁 𝗰𝗵𝘂𝗿𝗻 𝗺𝗲𝗮𝗻𝘁. /  / I built a churn prediction system that scores subscribers across eight markets, every day. Before any of it, one question: 𝘄𝗵𝗮𝘁 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗰𝗼𝘂𝗻𝘁𝘀…

---

```
🎬 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟭 · Databricks at Scale
𝗡𝗼𝗯𝗼𝗱𝘆 𝗮𝗴𝗿𝗲𝗲𝗱 𝘄𝗵𝗮𝘁 𝗰𝗵𝘂𝗿𝗻 𝗺𝗲𝗮𝗻𝘁.

I built a churn prediction system that scores subscribers across eight markets, every day. Before any of it, one question: 𝘄𝗵𝗮𝘁 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗰𝗼𝘂𝗻𝘁𝘀 𝗮𝘀 𝗰𝗵𝘂𝗿𝗻?

Across eight markets it didn't mean the same thing. Different renewal windows. Different rules for someone who cancels and comes back. Different views on whether a failed payment counts.

Pool that into one model and 𝘆𝗼𝘂'𝗿𝗲 𝗽𝗿𝗲𝗱𝗶𝗰𝘁𝗶𝗻𝗴 𝗲𝗶𝗴𝗵𝘁 𝗱𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁 𝘁𝗵𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗰𝗮𝗹𝗹𝗶𝗻𝗴 𝘁𝗵𝗲𝗺 𝗼𝗻𝗲.

━━━━━━━━━━

𝗧𝗵𝗲 𝗱𝗲𝗰𝗶𝘀𝗶𝗼𝗻 𝘁𝗵𝗮𝘁 𝗰𝗮𝗺𝗲 𝗯𝗲𝗳𝗼𝗿𝗲 𝘁𝗵𝗲 𝗺𝗼𝗱𝗲𝗹

𝗩𝗼𝗹𝘂𝗻𝘁𝗮𝗿𝘆 — they chose to cancel → give them a reason to stay.
𝗜𝗻𝘃𝗼𝗹𝘂𝗻𝘁𝗮𝗿𝘆 — their payment failed → retry the payment.

Two different problems. Only voluntary went into the label. Mix them, and the retention budget goes to people who never meant to leave.

━━━━━━━━━━

🧱 𝗧𝗵𝗲𝗻 𝗜 𝘄𝗿𝗼𝘁𝗲 𝗶𝘁 𝗶𝗻𝘁𝗼 𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀, 𝗻𝗼𝘁 𝗶𝗻𝘁𝗼 𝗮 𝘀𝗹𝗶𝗱𝗲

→ 𝗰𝗮𝘁𝗮𝗹𝗼𝗴.𝘀𝗰𝗵𝗲𝗺𝗮.𝘁𝗮𝗯𝗹𝗲 — one name (analytics.gold.churn_label) that every notebook, dashboard and job resolves the same way. No more five private versions of "churn".

→ 𝗧𝗵𝗲 𝗿𝘂𝗹𝗲𝘀 𝗹𝗶𝘃𝗲 𝗶𝗻 𝘁𝗵𝗲 𝗾𝘂𝗲𝗿𝘆. Three WHERE clauses carry the contract: who counts, what's excluded, when it's known.

→ 𝗖𝗢𝗠𝗠𝗘𝗡𝗧 𝗢𝗡 𝗧𝗔𝗕𝗟𝗘 — the definition is attached to the table, so whoever finds it reads the contract next to the data.

→ 𝗢𝗻𝗲 𝗴𝗼𝘃𝗲𝗿𝗻𝗮𝗻𝗰𝗲 𝗹𝗮𝘆𝗲𝗿. The same Unity Catalog rules cover the label, the features and the registered model.

Next for me: 𝗺𝗲𝘁𝗿𝗶𝗰 𝘃𝗶𝗲𝘄𝘀 and 𝗚𝗲𝗻𝗶𝗲, so the aggregation rule stops depending on everyone writing the query correctly.

𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: a narrower target, fewer examples, and a model that says nothing about failed payments. On purpose, and written down.

💡 𝗔 𝗯𝗲𝘁𝘁𝗲𝗿 𝗺𝗼𝗱𝗲𝗹 𝘄𝗼𝗻'𝘁 𝗳𝗶𝘅 𝗮 𝗻𝘂𝗺𝗯𝗲𝗿 𝗻𝗼𝗯𝗼𝗱𝘆 𝗮𝗴𝗿𝗲𝗲𝘀 𝗼𝗻. 𝗔 𝗴𝗼𝘃𝗲𝗿𝗻𝗲𝗱 𝗱𝗲𝗳𝗶𝗻𝗶𝘁𝗶𝗼𝗻 𝘄𝗶𝗹𝗹.

Full breakdown — the SQL, the "you can't average churn rates" trap, and a checklist for any metric — is in the repo (link in the comments).

Next week · 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟮: 𝗪𝗵𝗲𝗿𝗲 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗹𝗶𝘃𝗲𝘀

What's the metric at your company with the most definitions? 👇

#Databricks #UnityCatalog #DataEngineering #DataScience #MachineLearning
```

---

## Before you post

- [ ] **Truth check:** the markets really did define churn differently (renewal window, reconnects, failed payments)
- [ ] **Truth check:** `analytics.gold.churn_label` and the SQL are illustrative with generic names — confirm they resemble nothing internal
- [ ] **The repo link:** right after posting, add this as the first comment: https://github.com/Pratkashyap/databricks-at-scale/tree/main/episodes/01-nobody-agreed-what-churn-meant
- [ ] Nothing names your employer, its brands, markets, figures or internal systems
- [ ] Post a week after the trailer, on a weekday morning in your audience's time zone
- [ ] Reply to every comment in the first hour
