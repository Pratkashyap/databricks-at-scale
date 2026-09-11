# Episode 01 · LinkedIn post

> **Summary of [`learn.md`](learn.md).** Copy the text in the box, paste it into LinkedIn and attach [`poster.png`](poster.png).
> Bold is Unicode bold, so it stays bold when pasted. **2,374 of 3,000 characters.**

**Before "…see more":** 🎬 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟭 · Databricks at Scale / 𝗡𝗼𝗯𝗼𝗱𝘆 𝗮𝗴𝗿𝗲𝗲𝗱 𝘄𝗵𝗮𝘁 𝗰𝗵𝘂𝗿𝗻 𝗺𝗲𝗮𝗻𝘁. /  / Before I trained a single model, I had to answer a question that sounds too simple to matter: / 𝘄𝗵𝗮𝘁 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗰𝗼𝘂𝗻𝘁𝘀 𝗮𝘀 𝗰𝗵𝘂𝗿𝗻? /  / Across eight mark…

---

```
🎬 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟭 · Databricks at Scale
𝗡𝗼𝗯𝗼𝗱𝘆 𝗮𝗴𝗿𝗲𝗲𝗱 𝘄𝗵𝗮𝘁 𝗰𝗵𝘂𝗿𝗻 𝗺𝗲𝗮𝗻𝘁.

Before I trained a single model, I had to answer a question that sounds too simple to matter:
𝘄𝗵𝗮𝘁 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗰𝗼𝘂𝗻𝘁𝘀 𝗮𝘀 𝗰𝗵𝘂𝗿𝗻?

Across eight markets, it didn't mean the same thing.
Different renewal windows. Different rules for someone who cancels and comes back. Different views on whether a failed payment counts.

Pool that into one model and you're not predicting one thing.
𝗬𝗼𝘂'𝗿𝗲 𝗽𝗿𝗲𝗱𝗶𝗰𝘁𝗶𝗻𝗴 𝗲𝗶𝗴𝗵𝘁 𝗱𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁 𝘁𝗵𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗰𝗮𝗹𝗹𝗶𝗻𝗴 𝘁𝗵𝗲𝗺 𝗼𝗻𝗲.

So the first thing I built wasn't a model. It was a 𝗰𝗼𝗻𝘁𝗿𝗮𝗰𝘁 👇

📌 𝗘𝗻𝘁𝗶𝘁𝘆 — one paid billing cycle, not a user
📌 𝗘𝘃𝗲𝗻𝘁 — the subscriber chose to cancel
📌 𝗣𝗼𝗽𝘂𝗹𝗮𝘁𝗶𝗼𝗻 — first and second paid months only
📌 𝗘𝘅𝗰𝗹𝘂𝗱𝗲𝗱 — payment failures
📌 𝗧𝗶𝗺𝗶𝗻𝗴 — labelled only once the renewal window closes
📌 𝗥𝗼𝗹𝗹-𝘂𝗽 — add up across markets, then divide. 𝗡𝗲𝘃𝗲𝗿 𝗮𝘃𝗲𝗿𝗮𝗴𝗲 𝘁𝗵𝗲 𝗿𝗮𝘁𝗲𝘀.

The biggest call: 𝘃𝗼𝗹𝘂𝗻𝘁𝗮𝗿𝘆 𝗮𝗻𝗱 𝗶𝗻𝘃𝗼𝗹𝘂𝗻𝘁𝗮𝗿𝘆 𝗰𝗵𝘂𝗿𝗻 𝗮𝗿𝗲 𝘁𝘄𝗼 𝗱𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁 𝗽𝗿𝗼𝗯𝗹𝗲𝗺𝘀.
Someone who cancels needs a reason to stay.
Someone whose card failed needs a payment retry.
Mix them, and the retention budget goes to people who never meant to leave.

🧱 𝗪𝗵𝗲𝗿𝗲 𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗰𝗼𝗺𝗲𝘀 𝗶𝗻
A contract only works if it lives where everyone reads from, not in five different dashboards.
In Databricks that's Unity Catalog: one governed home for the churn label, the features and even the model, all under the same access rules.

𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: a narrower target, fewer examples to learn from, and a model that deliberately says nothing about failed payments. Every one of those on purpose, and written down.

💡 𝗜𝗳 𝘁𝘄𝗼 𝘁𝗲𝗮𝗺𝘀 𝗰𝗮𝗻'𝘁 𝗮𝗴𝗿𝗲𝗲 𝗼𝗻 𝘁𝗵𝗲 𝗻𝘂𝗺𝗯𝗲𝗿, 𝗮 𝗯𝗲𝘁𝘁𝗲𝗿 𝗺𝗼𝗱𝗲𝗹 𝘄𝗼𝗻'𝘁 𝗳𝗶𝘅 𝗶𝘁. 𝗔 𝘄𝗿𝗶𝘁𝘁𝗲𝗻 𝗱𝗲𝗳𝗶𝗻𝗶𝘁𝗶𝗼𝗻 𝘄𝗶𝗹𝗹.

The full breakdown — the SQL, the "you can't average churn rates" trap, and a checklist for any metric — is in my GitHub repo (link in the comments).

Next week · 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟮: 𝗪𝗵𝗲𝗿𝗲 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗹𝗶𝘃𝗲𝘀

What's the metric at your company with the most definitions? 👇

#Databricks #DataScience #MachineLearning #UnityCatalog #Analytics
```

---

## Before you post

- [ ] **Truth check:** the markets really did define churn differently (renewal window, reconnects, failed payments)
- [ ] **The repo link:** the post says "link in the comments". Only add that comment if the GitHub repo is **public**. While it's private, delete that line from the post.
- [ ] Nothing names your employer, markets, figures or internal systems
- [ ] Post a week after the trailer, on a weekday morning in your audience's time zone
- [ ] Reply to every comment in the first hour
