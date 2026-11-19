# Episode 03 · LinkedIn post — as published

**Status: published.** The text as it went live. Compared with the draft it opens straight on the hook, joins each problem to its fix with `→` on one line, drops the closing takeaway and bridge lines, and uses US spelling — all now part of the house style (design-log Ref 08).

```
𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗮𝘁 𝗦𝗰𝗮𝗹𝗲 · 𝗘𝗽 𝟯 · 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝘁𝗵𝗮𝘁 𝗱𝗼𝗻'𝘁 𝗹𝗶𝗲
Two subscribers, same 30 days, same 20 hours of viewing.
One watched 4 hours early and 16 late. The other watched 18 early and 2 late.
Identical totals. 𝗢𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗹𝗲𝗳𝘁.

𝗪𝗵𝗮𝘁 𝘄𝗲𝗻𝘁 𝗶𝗻 four families, all behavior :
→ 𝗧𝗲𝗻𝘂𝗿𝗲 : which paid month, returning subscriber or not
→ 𝗘𝗻𝗴𝗮𝗴𝗲𝗺𝗲𝗻𝘁 : active days, sessions, time to first play, weekend and evening ratios
→ 𝗖𝗼𝗻𝘁𝗲𝗻𝘁 : distinct genres and titles, variety of viewing, weekly trend
→ 𝗣𝗹𝗮𝗻 & 𝗱𝗲𝘃𝗶𝗰𝗲 : price tier, mobile / TV / other
No demographics. What people did predicted leaving far better than who they were.

𝗧𝗵𝗿𝗲𝗲 𝘁𝗿𝗮𝗽𝘀, 𝗮𝗻𝗱 𝘄𝗵𝗮𝘁 𝗳𝗶𝘅𝗲𝗱 𝗲𝗮𝗰𝗵 𝗼𝗻𝗲 :
𝟭. A total hides the trend→ 𝗦𝗽𝗹𝗶𝘁 𝘁𝗵𝗲 𝘄𝗶𝗻𝗱𝗼𝘄 : early vs late sub-windows and a weekly slope. Late-window engagement turned out to be the strongest signal in the model.

𝟮. Using something the model won't have yet. Brilliant in training, fails live→ 𝗟𝗲𝘁 𝘁𝗵𝗲 𝗸𝗲𝘆 𝗰𝗮𝗿𝗿𝘆 𝘁𝗵𝗲 𝗰𝘂𝘁-𝗼𝗳𝗳 : the feature table is keyed on subscriber and billing cycle, so a lookup returns what was true for that cycle. Point-in-time correctness stops being something you have to remember.

𝟯. Features built twice once for training, once for scoring quietly drift apart→ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲 𝘁𝗮𝗯𝗹𝗲𝘀 𝗶𝗻 𝗨𝗻𝗶𝘁𝘆 𝗖𝗮𝘁𝗮𝗹𝗼𝗴 : one keyed, governed table that training and scoring both look up. One definition, not two notebooks and other teams can find and reuse it.
This is the part I'd most recommend to anyone starting now. A feature table is not just a table with features in it : the key, the governance and the lineage back to the model are what stop quiet drift.

𝗡𝗲𝘅𝘁 𝗳𝗼𝗿 𝗺𝗲: online lookups, so the same features can serve a real-time decision and not only tonight's batch.
𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: lower training scores. Honest ones.

Next Episode 4 · 𝗪𝗵𝘆 𝘁𝗵𝗲 𝗯𝗼𝗿𝗶𝗻𝗴 𝗺𝗼𝗱𝗲𝗹 𝘄𝗼𝗻 drops next week.
#Databricks #DataScience #MachineLearning #Analytics #Lakehouse #FeatureStore #UnityCatalog #mlops #churn #SingaporeAI #agenticAI Databricks Anthropic Microsoft Copilot #Dubai #Singapore #TechinAsia #claude #claudecode #cursor Cursor
```
