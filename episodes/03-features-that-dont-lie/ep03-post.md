# Episode 03 · LinkedIn post

> Each trap is paired with the thing that fixed it, and the poster shows the same three pairs.
> Copy the box, paste into LinkedIn, attach [`ep03-poster.png`](ep03-poster.png). **1,938 of 3,000 characters.** Full detail: [`ep03-learn.md`](ep03-learn.md).

```
𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗮𝘁 𝗦𝗰𝗮𝗹𝗲 · 𝗘𝗽 𝟯 · 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝘁𝗵𝗮𝘁 𝗱𝗼𝗻'𝘁 𝗹𝗶𝗲

Episode 2 made the data safe to read. Then came the question that decides whether any model works :

𝘄𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗳𝗲𝗲𝗱 𝗶𝘁?


Two subscribers, same 30 days, same 20 hours of viewing.

One watched 4 hours early and 16 hours late. The other watched 18 early and 2 late.

Identical totals. 𝗢𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗹𝗲𝗳𝘁.


Three traps, and what fixed each one :

𝟭. A total hides the trend.
→ 𝗦𝗽𝗹𝗶𝘁 𝘁𝗵𝗲 𝘄𝗶𝗻𝗱𝗼𝘄 : early vs late sub-windows and a weekly slope, built with SQL window functions. Late-window engagement turned out to be the strongest signal in the model.

𝟮. Using something the model won't have yet. It looks brilliant in training, then fails live.
→ A 𝗽𝗼𝗶𝗻𝘁-𝗶𝗻-𝘁𝗶𝗺𝗲 𝗰𝘂𝘁-𝗼𝗳𝗳 : one row per billing cycle, features only from before the cut-off, the label only after the renewal window closes.

𝟯. Features built twice — once for training, once for scoring — quietly drift apart.
→ 𝗢𝗻𝗲 𝗴𝗼𝗹𝗱 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝘁𝗮𝗯𝗹𝗲 both of them read, and one shared code path for the final transformations.


𝗪𝗵𝗮𝘁 𝗜 𝗱𝗶𝗱𝗻'𝘁 𝘂𝘀𝗲 : demographics. What people did predicted leaving far better than who they were.


𝗡𝗲𝘅𝘁 𝗳𝗼𝗿 𝗺𝗲: Feature Engineering in Unity Catalog, so point-in-time lookups are the platform's job instead of mine.

𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: lower training scores. Honest ones.

𝗪𝗵𝗮𝘁 𝘁𝗵𝗲𝘆 𝗱𝗶𝗱 𝗯𝗲𝗮𝘁 𝘄𝗵𝗼 𝘁𝗵𝗲𝘆 𝘄𝗲𝗿𝗲. 𝗔𝗻𝗱 𝘄𝗵𝗲𝗻 𝘁𝗵𝗲𝘆 𝗱𝗶𝗱 𝗶𝘁 𝗯𝗲𝗮𝘁 𝗵𝗼𝘄 𝗺𝘂𝗰𝗵.


Next Episode 4 · 𝗪𝗵𝘆 𝘁𝗵𝗲 𝗯𝗼𝗿𝗶𝗻𝗴 𝗺𝗼𝗱𝗲𝗹 𝘄𝗼𝗻 drops next week.

#Databricks #DataScience #MachineLearning #Analytics #Lakehouse #FeatureStore #dataengineering #mlops #churn #SingaporeAI #agenticAI Databricks Anthropic Microsoft Microsoft Copilot #Dubai #Singapore #TechinAsia #claude #claudecode #cursor Cursor
```

## Before you post

- [ ] Truth check: every claim is something that actually happened
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Reply to every comment in the first hour
