# Episode 02 · LinkedIn post

> Matches Episode 01 **as published**: heading line `Databricks at Scale · Ep N · Title`, no blank line after it, lead-ins merged onto the same line as their first sentence, a space before colons, no "link in the comments" line, long tag block with company tags.
> Copy the box, paste into LinkedIn, attach [`ep02-poster.png`](ep02-poster.png). **2,405 of 3,000 characters.** Full detail: [`ep02-learn.md`](ep02-learn.md).

```
𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗮𝘁 𝗦𝗰𝗮𝗹𝗲 · 𝗘𝗽 𝟮 · 𝗪𝗵𝗲𝗿𝗲 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗹𝗶𝘃𝗲𝘀
In Episode 1 we agreed what churn meant. Then I looked at what it was built on.
𝗜 𝗱𝗶𝗱𝗻'𝘁 𝗼𝘄𝗻 𝗮 𝘀𝗶𝗻𝗴𝗹𝗲 𝘁𝗮𝗯𝗹𝗲 𝗜 𝗱𝗲𝗽𝗲𝗻𝗱𝗲𝗱 𝗼𝗻.

Billing facts, session summaries, viewing events : all owned by other teams. You get the data, but no say in when it arrives and no warning when it changes.

Three things went wrong. All three are normal :
→ A number arrived as 𝘁𝗲𝘅𝘁 in some markets. The job died.
→ The month 𝗵𝗮𝗱𝗻'𝘁 𝗳𝘂𝗹𝗹𝘆 𝗹𝗮𝗻𝗱𝗲𝗱. The job succeeded, on half the data.
→ Nothing 𝗮𝗻𝗻𝗼𝘂𝗻𝗰𝗲𝗱 the change.
The second one is the dangerous one. A job that fails wakes you up. A job that quietly succeeds goes straight into a dashboard.

𝗟𝗮𝘆𝗲𝗿𝘀, 𝗮𝗻𝗱 𝗸𝗻𝗼𝘄𝗶𝗻𝗴 𝘄𝗵𝗶𝗰𝗵 𝗼𝗻𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿𝘀: Databricks organises data in three layers — 𝗯𝗿𝗼𝗻𝘇𝗲 (raw) · 𝘀𝗶𝗹𝘃𝗲𝗿 (cleaned) · 𝗴𝗼𝗹𝗱 (business-ready).
I read other teams' gold. I publish my own. I never touch bronze or silver. A healthy place to sit — it just means the risk lives at the boundary.

𝗪𝗵𝗮𝘁 𝗗𝗲𝗹𝘁𝗮 𝗴𝗶𝘃𝗲𝘀 𝘆𝗼𝘂 𝘂𝗻𝗱𝗲𝗿𝗻𝗲𝗮𝘁𝗵 :
→ 𝗦𝗰𝗵𝗲𝗺𝗮 𝗲𝗻𝗳𝗼𝗿𝗰𝗲𝗺𝗲𝗻𝘁 — a bad shape is rejected, not silently mangled
→ 𝗧𝗶𝗺𝗲 𝘁𝗿𝗮𝘃𝗲𝗹 — read the table as it was last month, so "why did this number move?" stops being a guess

𝗧𝗵𝗲 𝘁𝘄𝗼 𝗵𝗮𝗯𝗶𝘁𝘀 𝘁𝗵𝗮𝘁 𝘀𝘁𝗼𝗽𝗽𝗲𝗱 𝘁𝗵𝗲 𝟮 𝗮.𝗺. 𝗳𝗮𝗶𝗹𝘂𝗿𝗲𝘀:
𝗡𝗲𝘃𝗲𝗿 𝘁𝗿𝘂𝘀𝘁 𝗮 𝗰𝗼𝗹𝘂𝗺𝗻'𝘀 𝘁𝘆𝗽𝗲 : cast safely, so a bad value becomes empty instead of killing the job — and count how often it happens.
𝗖𝗵𝗲𝗰𝗸 𝗯𝗲𝗳𝗼𝗿𝗲 𝘆𝗼𝘂 𝗿𝘂𝗻 : no new month, no run. The job stops itself.

𝗡𝗲𝘅𝘁 𝗳𝗼𝗿 𝗺𝗲: Lakeflow and Auto Loader, for data that arrives continuously instead of once a month.
𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: slower queries, less elegant code, and some mornings when the pipeline simply doesn't run. All worth it.
𝗬𝗼𝘂 𝗰𝗮𝗻'𝘁 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝘁𝗵𝗲 𝘁𝗮𝗯𝗹𝗲𝘀 𝘆𝗼𝘂 𝗱𝗼𝗻'𝘁 𝗼𝘄𝗻. 𝗬𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝗵𝗼𝘄 𝘆𝗼𝘂 𝗿𝗲𝗮𝗱 𝘁𝗵𝗲𝗺.

Next Episode 3 · 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝘁𝗵𝗮𝘁 𝗱𝗼𝗻'𝘁 𝗹𝗶𝗲 drops next week.
#Databricks #DataScience #MachineLearning #Analytics #Lakehouse #DeltaLake #dataengineering #mlops #churn #SingaporeAI #agenticAI Databricks Anthropic Microsoft Microsoft Copilot #Dubai #Singapore #TechinAsia #claude #claudecode #cursor Cursor
```

## Before you post

- [ ] Truth check: every claim is something that actually happened
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Reply to every comment in the first hour
