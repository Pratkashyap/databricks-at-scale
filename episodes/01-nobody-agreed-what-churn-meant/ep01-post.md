# Episode 01 · LinkedIn post

> Copy the box, paste into LinkedIn, attach [`ep01-poster.png`](ep01-poster.png). Bold is Unicode, so it survives pasting.
> **2,272 of 3,000 characters.** Full detail: [`ep01-learn.md`](ep01-learn.md).

```
🎬 𝗘𝗣𝗜𝗦𝗢𝗗𝗘 𝟭 - 𝗡𝗢𝗕𝗢𝗗𝗬 𝗔𝗚𝗥𝗘𝗘𝗗 𝗪𝗛𝗔𝗧 𝗖𝗛𝗨𝗥𝗡 𝗠𝗘𝗔𝗡𝗧
Databricks at Scale · Season 1: The Problem

Last week I said the model was the easy part.
This is the first thing that proved it.

I built a churn prediction system that scores subscribers across eight markets, every day. Before any of it, one question had to be settled: 𝘄𝗵𝗮𝘁 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗰𝗼𝘂𝗻𝘁𝘀 𝗮𝘀 𝗰𝗵𝘂𝗿𝗻?

Across eight markets, it didn't mean the same thing:

→ When does the 𝗿𝗲𝗻𝗲𝘄𝗮𝗹 𝘄𝗶𝗻𝗱𝗼𝘄 close?
→ Someone cancels, then 𝗰𝗼𝗺𝗲𝘀 𝗯𝗮𝗰𝗸 - churned or not?
→ Does a 𝗳𝗮𝗶𝗹𝗲𝗱 𝗽𝗮𝘆𝗺𝗲𝗻𝘁 count?

One word. 𝗘𝗶𝗴𝗵𝘁 𝘃𝗲𝗿𝘀𝗶𝗼𝗻𝘀 𝗼𝗳 𝘁𝗵𝗲 𝘀𝗮𝗺𝗲 𝗻𝘂𝗺𝗯𝗲𝗿.

Pool that into one model and you're not predicting one thing. You're predicting eight, and calling them one.

𝗧𝗛𝗘 𝗗𝗘𝗖𝗜𝗦𝗜𝗢𝗡 𝗧𝗛𝗔𝗧 𝗦𝗛𝗔𝗣𝗘𝗗 𝗘𝗩𝗘𝗥𝗬𝗧𝗛𝗜𝗡𝗚

𝗩𝗼𝗹𝘂𝗻𝘁𝗮𝗿𝘆 - they chose to cancel → give them a reason to stay.
𝗜𝗻𝘃𝗼𝗹𝘂𝗻𝘁𝗮𝗿𝘆 - their payment failed → retry the payment.

Two different problems. Only voluntary went into the model. Mix them, and the retention budget goes to people who never meant to leave.

🧱 𝗪𝗛𝗘𝗥𝗘 𝗗𝗔𝗧𝗔𝗕𝗥𝗜𝗖𝗞𝗦 𝗖𝗔𝗠𝗘 𝗜𝗡

The agreed definition doesn't live in a slide or a wiki. It lives in 𝗨𝗻𝗶𝘁𝘆 𝗖𝗮𝘁𝗮𝗹𝗼𝗴 - the governance layer - as one table, with one name.

→ Dashboards, notebooks and the model all read 𝘁𝗵𝗮𝘁 𝘀𝗮𝗺𝗲 𝘁𝗮𝗯𝗹𝗲
→ The rules (who counts, what's excluded, when it's known) sit 𝗶𝗻𝘀𝗶𝗱𝗲 𝗶𝘁
→ The description travels 𝗼𝗻 𝘁𝗵𝗲 𝘁𝗮𝗯𝗹𝗲 𝗶𝘁𝘀𝗲𝗹𝗳

Next for me: 𝗺𝗲𝘁𝗿𝗶𝗰 𝘃𝗶𝗲𝘄𝘀 and 𝗚𝗲𝗻𝗶𝗲.

𝗪𝗛𝗔𝗧 𝗜𝗧 𝗖𝗢𝗦𝗧

A narrower target, fewer examples to learn from, and a model that says nothing about failed payments. On purpose, and written down.

💡 𝗔 𝗯𝗲𝘁𝘁𝗲𝗿 𝗺𝗼𝗱𝗲𝗹 𝗰𝗮𝗻'𝘁 𝗳𝗶𝘅 𝗮 𝗻𝘂𝗺𝗯𝗲𝗿 𝗻𝗼𝗯𝗼𝗱𝘆 𝗮𝗴𝗿𝗲𝗲𝘀 𝗼𝗻. 𝗢𝗻𝗲 𝗱𝗲𝗳𝗶𝗻𝗶𝘁𝗶𝗼𝗻, 𝗶𝗻 𝗼𝗻𝗲 𝗽𝗹𝗮𝗰𝗲, 𝗰𝗮𝗻.

𝗡𝗘𝗫𝗧 𝗘𝗣𝗜𝗦𝗢𝗗𝗘

𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟮 - 𝗪𝗵𝗲𝗿𝗲 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗹𝗶𝘃𝗲𝘀: I didn't own a single table I depended on.

Full write-up in the repo - link in the comments.

What's the metric at your company with the most definitions? 👇

#Databricks #UnityCatalog #DataEngineering #DataScience #MachineLearning
```

## Before you post

- [ ] Truth check: every claim is something that actually happened
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Add the repo link as the first comment: https://github.com/Pratkashyap/databricks-at-scale/tree/main/episodes/01-nobody-agreed-what-churn-meant
- [ ] Reply to every comment in the first hour
