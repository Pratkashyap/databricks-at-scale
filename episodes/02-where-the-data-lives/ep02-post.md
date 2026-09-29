# Episode 02 · LinkedIn post

> Copy the box, paste into LinkedIn, attach [`ep02-poster.png`](ep02-poster.png). Bold is Unicode, so it survives pasting.
> **2,603 of 3,000 characters.** Full detail: [`ep02-learn.md`](ep02-learn.md).

```
🎬 𝗘𝗣𝗜𝗦𝗢𝗗𝗘 𝟮 - 𝗪𝗛𝗘𝗥𝗘 𝗧𝗛𝗘 𝗗𝗔𝗧𝗔 𝗔𝗖𝗧𝗨𝗔𝗟𝗟𝗬 𝗟𝗜𝗩𝗘𝗦
Databricks at Scale · Season 1: The Problem

In Episode 1 we agreed what churn meant.
Then I looked at what it was built on - and 𝗜 𝗱𝗶𝗱𝗻'𝘁 𝗼𝘄𝗻 𝗮 𝘀𝗶𝗻𝗴𝗹𝗲 𝘁𝗮𝗯𝗹𝗲 𝗜 𝗱𝗲𝗽𝗲𝗻𝗱𝗲𝗱 𝗼𝗻.

Billing facts, session summaries, viewing events: all owned by other teams. As a consumer you get the data, but not a say in when it arrives, and no warning when it changes.

Three things went wrong. All three are normal:

→ A number arrived as 𝘁𝗲𝘅𝘁 in some markets. The job died.
→ The month 𝗵𝗮𝗱𝗻'𝘁 𝗳𝘂𝗹𝗹𝘆 𝗹𝗮𝗻𝗱𝗲𝗱. The job succeeded - on half the data.
→ Nothing 𝗮𝗻𝗻𝗼𝘂𝗻𝗰𝗲𝗱 the change.

The second one is the dangerous one. 𝗔 𝗷𝗼𝗯 𝘁𝗵𝗮𝘁 𝗳𝗮𝗶𝗹𝘀 𝘄𝗮𝗸𝗲𝘀 𝘆𝗼𝘂 𝘂𝗽. 𝗔 𝗷𝗼𝗯 𝘁𝗵𝗮𝘁 𝗾𝘂𝗶𝗲𝘁𝗹𝘆 𝘀𝘂𝗰𝗰𝗲𝗲𝗱𝘀 𝗴𝗼𝗲𝘀 𝘀𝘁𝗿𝗮𝗶𝗴𝗵𝘁 𝗶𝗻𝘁𝗼 𝗮 𝗱𝗮𝘀𝗵𝗯𝗼𝗮𝗿𝗱.

𝗟𝗔𝗬𝗘𝗥𝗦 - 𝗔𝗡𝗗 𝗞𝗡𝗢𝗪𝗜𝗡𝗚 𝗪𝗛𝗜𝗖𝗛 𝗢𝗡𝗘 𝗜𝗦 𝗬𝗢𝗨𝗥𝗦

Databricks organises data in three layers: 𝗯𝗿𝗼𝗻𝘇𝗲 (raw), 𝘀𝗶𝗹𝘃𝗲𝗿 (cleaned), 𝗴𝗼𝗹𝗱 (business-ready).

I read other teams' gold. I publish my own. I never touch bronze or silver. That's a healthy place to sit - it just means the risk lives at the boundary.

🧱 𝗪𝗛𝗔𝗧 𝗗𝗘𝗟𝗧𝗔 𝗚𝗜𝗩𝗘𝗦 𝗬𝗢𝗨 𝗨𝗡𝗗𝗘𝗥𝗡𝗘𝗔𝗧𝗛

→ A write either 𝗳𝘂𝗹𝗹𝘆 𝗵𝗮𝗽𝗽𝗲𝗻𝘀 𝗼𝗿 𝗱𝗼𝗲𝘀𝗻'𝘁 - no half-written table
→ 𝗦𝗰𝗵𝗲𝗺𝗮 𝗲𝗻𝗳𝗼𝗿𝗰𝗲𝗺𝗲𝗻𝘁 - a bad shape is rejected, not silently mangled
→ 𝗧𝗶𝗺𝗲 𝘁𝗿𝗮𝘃𝗲𝗹 - read the table as it was last month, so "why did this number move?" stops being a guess

𝗧𝗛𝗘 𝗧𝗪𝗢 𝗛𝗔𝗕𝗜𝗧𝗦 𝗧𝗛𝗔𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗 𝗧𝗛𝗘 𝟮 𝗔.𝗠. 𝗙𝗔𝗜𝗟𝗨𝗥𝗘𝗦

𝗡𝗲𝘃𝗲𝗿 𝘁𝗿𝘂𝘀𝘁 𝗮 𝗰𝗼𝗹𝘂𝗺𝗻'𝘀 𝘁𝘆𝗽𝗲. Cast safely, so a bad value becomes empty instead of killing the job - and count how often it happens, because a slow drift upward is a warning.

𝗖𝗵𝗲𝗰𝗸 𝗯𝗲𝗳𝗼𝗿𝗲 𝘆𝗼𝘂 𝗿𝘂𝗻. No new month, no run. The job stops itself rather than producing a confident half-answer.

𝗪𝗛𝗔𝗧 𝗜𝗧 𝗖𝗢𝗦𝗧

Slower queries, less elegant code, and some mornings when the pipeline simply doesn't run. All worth it.

💡 𝗬𝗼𝘂 𝗰𝗮𝗻'𝘁 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝘁𝗵𝗲 𝘁𝗮𝗯𝗹𝗲𝘀 𝘆𝗼𝘂 𝗱𝗼𝗻'𝘁 𝗼𝘄𝗻. 𝗬𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗻𝘁𝗿𝗼𝗹 𝗵𝗼𝘄 𝘆𝗼𝘂 𝗿𝗲𝗮𝗱 𝘁𝗵𝗲𝗺.

𝗡𝗘𝗫𝗧 𝗘𝗣𝗜𝗦𝗢𝗗𝗘

𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟯 - 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝘁𝗵𝗮𝘁 𝗱𝗼𝗻'𝘁 𝗹𝗶𝗲: what people did mattered far more than who they were.

Full write-up in the repo - link in the comments.

Who owns the tables you depend on - and do they know you exist? 👇

#Databricks #DeltaLake #DataEngineering #DataScience #Lakehouse
```

## Before you post

- [ ] Truth check: every claim is something that actually happened
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Add the repo link as the first comment: https://github.com/Pratkashyap/databricks-at-scale/tree/main/episodes/02-where-the-data-lives
- [ ] Reply to every comment in the first hour
