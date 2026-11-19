# Episode 05 · LinkedIn post

> Written to the template of Episode 03 **as published**: hook first with no recap, each problem joined to its fix with `→` on one line, `Next for me` / `What it cost` / pointer, then the tag block. The poster shows the same three pairs in the same order.
> Copy the box, paste into LinkedIn, attach [`ep05-poster.png`](ep05-poster.png). **1,876 of 3,000 characters.** Full detail: [`ep05-learn.md`](ep05-learn.md).

```
𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗮𝘁 𝗦𝗰𝗮𝗹𝗲 · 𝗘𝗽 𝟱 · 𝗠𝘆 𝗺𝗲𝘁𝗿𝗶𝗰 𝘄𝗮𝘀 𝗹𝘆𝗶𝗻𝗴 𝘁𝗼 𝗺𝗲
The score went up. The model hadn't improved.
This is the episode I'd most want someone to have shown me earlier.

𝗪𝗵𝗮𝘁 𝗵𝗮𝗽𝗽𝗲𝗻𝗲𝗱 : as I pooled more markets into the model, PR AUC rose. It looked like progress. It wasn't.
PR AUC depends on how common the outcome is. Add markets where churn is more common, and the score climbs on its own. Same model, better-looking number.

𝗧𝗵𝗿𝗲𝗲 𝗽𝗿𝗼𝗯𝗹𝗲𝗺𝘀, 𝗮𝗻𝗱 𝘄𝗵𝗮𝘁 𝘀𝗼𝗹𝘃𝗲𝗱 𝗲𝗮𝗰𝗵 𝗼𝗻𝗲 :
𝟭. A score that moves with the base rate can't compare models→ 𝗟𝗶𝗳𝘁 𝗼𝘃𝗲𝗿 𝗯𝗮𝘀𝗲 𝗿𝗮𝘁𝗲 : how many more churners the model finds than random picking would. Comparable across markets, and honest.

𝟮. One threshold treats a cheap nudge and an expensive offer the same→ 𝗔 𝘃𝗮𝗹𝘂𝗲-𝘁𝗼-𝗮𝗰𝘁𝗶𝗼𝗻 𝘁𝗮𝗯𝗹𝗲 : a cut-off per action, each with its precision, recall and how many people it reaches. The model ranks; the business picks the cut-off.

𝟯. You can't judge a score until the renewal window closes→ 𝗘𝘃𝗲𝗿𝘆 𝘀𝗰𝗼𝗿𝗲 𝗸𝗲𝗽𝘁 𝗶𝗻 𝗗𝗲𝗹𝘁𝗮 : each day's scores stored with the model version and threshold that produced them. When the labels land, evaluation is a join, not an archaeology dig.
A metric that moves when the data mix changes isn't measuring the model.

𝗡𝗲𝘅𝘁 𝗳𝗼𝗿 𝗺𝗲: MLflow's built-in evaluation, so lift and the action table are logged with every run instead of computed afterwards.
𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: a less impressive headline number. A true one.

Next Episode 6 · 𝗔 𝗺𝗼𝗱𝗲𝗹 𝘁𝗵𝗮𝘁 𝗿𝘂𝗻𝘀 𝗶𝘁𝘀𝗲𝗹𝗳 drops next week.
#Databricks #DataScience #MachineLearning #Analytics #Lakehouse #DeltaLake #ModelEvaluation #mlops #churn #SingaporeAI #agenticAI Databricks Anthropic Microsoft Copilot #Dubai #Singapore #TechinAsia #claude #claudecode #cursor Cursor
```

## Before you post

- [ ] **Confirm before posting:** the post says PR AUC rose as you pooled more markets. Discovery Q20 records this as the lesson from the build; check it matches what you actually saw before saying it in the first person
- [ ] The value-to-action table is described by its structure only — no cut-offs or volumes
- [ ] No campaign results are claimed (discovery Q25 is unconfirmed)
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Reply to every comment in the first hour
