# Episode 02 · LinkedIn post

> Each problem is paired with the Databricks feature that actually solves it, and the poster shows the same three pairs. **1,799 of 3,000 characters.** Full detail: [`ep02-learn.md`](ep02-learn.md).

```
𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗮𝘁 𝗦𝗰𝗮𝗹𝗲 · 𝗘𝗽 𝟮 · 𝗪𝗵𝗲𝗿𝗲 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗹𝗶𝘃𝗲𝘀

In Episode 1 we agreed what churn meant. Then I looked at what it was built on.

𝗜 𝗱𝗶𝗱𝗻'𝘁 𝗼𝘄𝗻 𝗮 𝘀𝗶𝗻𝗴𝗹𝗲 𝘁𝗮𝗯𝗹𝗲 𝗜 𝗱𝗲𝗽𝗲𝗻𝗱𝗲𝗱 𝗼𝗻.


Databricks keeps data in three layers : 𝗯𝗿𝗼𝗻𝘇𝗲 (raw) · 𝘀𝗶𝗹𝘃𝗲𝗿 (cleaned) · 𝗴𝗼𝗹𝗱 (business-ready).

Other teams own bronze and silver. I read their gold, and publish my own. Every risk sits on that one boundary.


Three things broke there. Each one has a Databricks answer :

𝟭. A number arrived as text. The job died.
→ 𝗧𝗥𝗬_𝗖𝗔𝗦𝗧 turns a bad value into an empty one instead of killing the run. And I count them, because a rising count is an early warning.

𝟮. The month hadn't landed. The job ran on half the data.
→ A 𝗳𝗿𝗲𝘀𝗵𝗻𝗲𝘀𝘀 𝗴𝗮𝘁𝗲 as the first task in the Workflow : no new month, no run.

𝟯. Nobody announced the change.
→ 𝗗𝗲𝗹𝘁𝗮 keeps every version of a table, so "when did this change?" is a query, not a guess.


𝗧𝗵𝗲 𝗼𝗻𝗲 𝘁𝗼 𝗿𝗲𝗺𝗲𝗺𝗯𝗲𝗿 : a job that fails wakes you up. A job that quietly succeeds goes straight into a dashboard.


𝗡𝗲𝘅𝘁 𝗳𝗼𝗿 𝗺𝗲: Lakeflow and Auto Loader, for data that arrives continuously instead of once a month.

𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: slower queries and less elegant code. Worth it.

𝗬𝗼𝘂 𝗰𝗮𝗻'𝘁 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝘁𝗵𝗲 𝘁𝗮𝗯𝗹𝗲𝘀 𝘆𝗼𝘂 𝗱𝗼𝗻'𝘁 𝗼𝘄𝗻. 𝗬𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝗵𝗼𝘄 𝘆𝗼𝘂 𝗿𝗲𝗮𝗱 𝘁𝗵𝗲𝗺.


Next Episode 3 · 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝘁𝗵𝗮𝘁 𝗱𝗼𝗻'𝘁 𝗹𝗶𝗲 drops next week.

#Databricks #DataScience #MachineLearning #Analytics #Lakehouse #DeltaLake #dataengineering #mlops #churn #SingaporeAI #agenticAI Databricks Anthropic Microsoft Microsoft Copilot #Dubai #Singapore #TechinAsia #claude #claudecode #cursor Cursor
```

## Before you post

- [ ] Truth check: every claim is something that actually happened
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Reply to every comment in the first hour
