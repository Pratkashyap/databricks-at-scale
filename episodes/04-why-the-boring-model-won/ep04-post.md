# Episode 04 · LinkedIn post

> Written to the template of Episode 03 **as published**: hook first with no recap, each problem joined to its fix with `→` on one line, `Next for me` / `What it cost` / pointer, then the tag block. The poster shows the same three pairs in the same order.
> Copy the box, paste into LinkedIn, attach [`ep04-poster.png`](ep04-poster.png). **1,873 of 3,000 characters.** Full detail: [`ep04-learn.md`](ep04-learn.md).

```
𝗗𝗮𝘁𝗮𝗯𝗿𝗶𝗰𝗸𝘀 𝗮𝘁 𝗦𝗰𝗮𝗹𝗲 · 𝗘𝗽 𝟰 · 𝗪𝗵𝘆 𝘁𝗵𝗲 𝗯𝗼𝗿𝗶𝗻𝗴 𝗺𝗼𝗱𝗲𝗹 𝘄𝗼𝗻
Season 2 starts here : the build.
I ran the bake-off. Four algorithms, per-market models, per-tenure models, resampling tricks.
Then I threw most of it away, on purpose.

𝗪𝗵𝗮𝘁 𝗜 𝘁𝗿𝗶𝗲𝗱 :
→ XGBoost, LightGBM and two more algorithms
→ One model per market, and one per tenure month
→ SMOTE, to rebalance the rare churners
𝗪𝗵𝗮𝘁 𝘀𝘂𝗿𝘃𝗶𝘃𝗲𝗱 : one XGBoost model, class-weighted, pooled across markets.

𝗧𝗵𝗿𝗲𝗲 𝗽𝗿𝗼𝗯𝗹𝗲𝗺𝘀, 𝗮𝗻𝗱 𝘄𝗵𝗮𝘁 𝘀𝗼𝗹𝘃𝗲𝗱 𝗲𝗮𝗰𝗵 𝗼𝗻𝗲 :
𝟭. Dozens of runs, and no memory of which settings produced which score→ 𝗠𝗟𝗳𝗹𝗼𝘄 𝗲𝘅𝗽𝗲𝗿𝗶𝗺𝗲𝗻𝘁𝘀 : every run logs its parameters, metrics and the model itself. The bake-off becomes a table you can sort, not a story you have to remember.

𝟮. Churners are rare, so a model can look accurate by predicting nobody leaves→ 𝗖𝗹𝗮𝘀𝘀 𝘄𝗲𝗶𝗴𝗵𝘁𝗶𝗻𝗴 : one setting, scale_pos_weight, tells the model a missed churner costs more. SMOTE added complexity and no measurable gain, so it went.

𝟯. One model per market multiplies everything : training, monitoring, explaining→ 𝗢𝗻𝗲 𝗽𝗼𝗼𝗹𝗲𝗱 𝗺𝗼𝗱𝗲𝗹 with market as a feature. It won on the metric and on simplicity. The bigger reason comes in Episode 8.
The best model is the one you can still retrain, monitor and explain a year from now.

𝗡𝗲𝘅𝘁 𝗳𝗼𝗿 𝗺𝗲: AutoML as a baseline, to test the bake-off against something I didn't hand-pick.
𝗪𝗵𝗮𝘁 𝗶𝘁 𝗰𝗼𝘀𝘁: a few small gains left on the table. Unproven ones.

Next Episode 5 · 𝗠𝘆 𝗺𝗲𝘁𝗿𝗶𝗰 𝘄𝗮𝘀 𝗹𝘆𝗶𝗻𝗴 𝘁𝗼 𝗺𝗲 drops next week.
#Databricks #DataScience #MachineLearning #Analytics #Lakehouse #MLflow #XGBoost #mlops #churn #SingaporeAI #agenticAI Databricks Anthropic Microsoft Copilot #Dubai #Singapore #TechinAsia #claude #claudecode #cursor Cursor
```

## Before you post

- [ ] Truth check: the bake-off really was XGBoost, LightGBM and two more algorithms, plus per-market and per-tenure models and SMOTE (discovery Q19)
- [ ] AutoML is framed as **next**, never as something already used
- [ ] Nothing names the employer, its brands, markets or figures
- [ ] Reply to every comment in the first hour
