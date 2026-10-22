# Episode 03 · LinkedIn post

> The four feature families, then each trap paired with its fix, then the bridge into Episode 04. The poster shows the same families and the same three pairs.
> Copy the box, paste into LinkedIn, attach [`ep03-poster.png`](ep03-poster.png). **2,649 of 3,000 characters.** Full detail: [`ep03-learn.md`](ep03-learn.md).

```
𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗮𝘁 𝗦𝗰𝗮𝗹𝗲 · 𝗘𝗽 𝟯 · 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝘁𝗵𝗮𝘁 𝗱𝗼𝗻'𝘁 𝗹𝗶𝗲

Episode 2 made the data safe to read. Then came the question that decides whether any model works :

𝘄𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗳𝗲𝗲𝗱 𝗶𝘁?


Two subscribers, same 30 days, same 20 hours of viewing.

One watched 4 hours early and 16 late. The other watched 18 early and 2 late.

Identical totals. 𝗢𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗹𝗲𝗳𝘁.


𝗪𝗵𝗮𝘁 𝘄𝗲𝗻𝘁 𝗶𝗻 — four families, all behaviour :

→ 𝗧𝗲𝗻𝘂𝗿𝗲 : which paid month, returning subscriber or not
→ 𝗘𝗻𝗴𝗮𝗴𝗲𝗺𝗲𝗻𝘁 : active days, sessions, time to first play, weekend and evening ratios
→ 𝗖𝗼𝗻𝘁𝗲𝗻𝘁 : distinct genres and titles, variety of viewing, weekly trend
→ 𝗣𝗹𝗮𝗻 & 𝗱𝗲𝘃𝗶𝗰𝗲 : price tier, mobile / TV / other

No demographics. What people did predicted leaving far better than who they were.


𝗧𝗵𝗿𝗲𝗲 𝘁𝗿𝗮𝗽𝘀, 𝗮𝗻𝗱 𝘄𝗵𝗮𝘁 𝗳𝗶𝘅𝗲𝗱 𝗲𝗮𝗰𝗵 𝗼𝗻𝗲 :

𝟭. A total hides the trend.
→ 𝗦𝗽𝗹𝗶𝘁 𝘁𝗵𝗲 𝘄𝗶𝗻𝗱𝗼𝘄 : early vs late sub-windows and a weekly slope. Late-window engagement turned out to be the strongest signal in the model.

𝟮. Using something the model won't have yet. Brilliant in training, fails live.
→ 𝗟𝗲𝘁 𝘁𝗵𝗲 𝗸𝗲𝘆 𝗰𝗮𝗿𝗿𝘆 𝘁𝗵𝗲 𝗰𝘂𝘁-𝗼𝗳𝗳 : the feature table is keyed on subscriber and billing cycle, so a lookup returns what was true for that cycle. Point-in-time correctness stops being something you have to remember.

𝟯. Features built twice — once for training, once for scoring — quietly drift apart.
→ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲 𝘁𝗮𝗯𝗹𝗲𝘀 𝗶𝗻 𝗨𝗻𝗶𝘁𝘆 𝗖𝗮𝘁𝗮𝗹𝗼𝗴 : one keyed, governed table that training and scoring both look up. One definition, not two notebooks — and other teams can find and reuse it.


This is the part I'd most recommend to anyone starting now. A feature table is not just a table with features in it : the key, the governance and the lineage back to the model are what stop quiet drift.

𝗡𝗲𝘅𝘁 𝗳𝗼𝗿 𝗺𝗲: online lookups, so the same features can serve a real-time decision and not only tonight's batch.

𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: lower training scores. Honest ones.

𝗪𝗵𝗮𝘁 𝘁𝗵𝗲𝘆 𝗱𝗶𝗱 𝗯𝗲𝗮𝘁 𝘄𝗵𝗼 𝘁𝗵𝗲𝘆 𝘄𝗲𝗿𝗲. 𝗔𝗻𝗱 𝘄𝗵𝗲𝗻 𝘁𝗵𝗲𝘆 𝗱𝗶𝗱 𝗶𝘁 𝗯𝗲𝗮𝘁 𝗵𝗼𝘄 𝗺𝘂𝗰𝗵.


Good features are why a boring model was enough.

Next Episode 4 · 𝗪𝗵𝘆 𝘁𝗵𝗲 𝗯𝗼𝗿𝗶𝗻𝗴 𝗺𝗼𝗱𝗲𝗹 𝘄𝗼𝗻 drops next week.

#Databricks #DataScience #MachineLearning #Analytics #Lakehouse #FeatureStore #UnityCatalog #mlops #churn #SingaporeAI #agenticAI Databricks Anthropic Microsoft Microsoft Copilot #Dubai #Singapore #TechinAsia #claude #claudecode #cursor Cursor
```

## Before you post

- [ ] **Check the detail before a commenter does:** the post says the feature table is keyed on subscriber and billing cycle. If you also declared a *timestamp key* and used `create_training_set()`, that is worth saying in the comments — it is the strongest Databricks-specific point in this episode
- [ ] Truth check: every claim is something that actually happened
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Reply to every comment in the first hour
