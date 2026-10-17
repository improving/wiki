---
type: Reference
title: "Ten Days of Miscalibrated Sensors Before the Calendar Noticed"
resource: "https://www.devlinliles.com/ten-days-of-miscalibrated-sensors-before-the-calendar-noticed/"
author: "Devlin Liles"
published: '2026-10-12'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I built a predictive-maintenance model once that scored vibration and temperature readings from forty machines to predict equipment failure seven days out. On day twenty, a firmware update recalibrated the vibration sensors, shifting the feature distribution without changing what normal vibration actually meant physically. The model, trained on the pre-update calibration, started misreading every value it received from that point forward.

## The problem

Retraining ran on a fixed monthly schedule, days thirty, sixty, and ninety across a ninety-day window, regardless of whether anything had actually changed. From day twenty to day thirty, the model ran on miscalibrated inputs it was never trained to interpret, missing real failures and firing false alarms it shouldn't have, for a full ten days before the next scheduled retrain even had a chance to fire. And when day thirty finally arrived, the scheduled retrain wasn't actually safe either. It retrained and redeployed automatically with no comparison against the previous model on any shared holdout, so if the retraining window itself happened to catch a messy mix of old and new calibration data, there was no check confirming the new model was actually better before it went live. A fixed schedule doesn't know the difference between "nothing changed, retrain anyway" and "something changed ten days ago, retrain now," and it doesn't check its own homework once it does retrain.

## The pattern

I didn't need a third mechanism to fix this. I composed two I'd already built. A drift signal, a daily Population Stability Index check on the sensor features, triggers a retraining run on demand, replacing the fixed calendar schedule entirely. The resulting candidate model still has to clear a champion-versus-challenger holdout comparison before it's allowed to take over. Drift starts the pipeline. Comparison gates the outcome.

Running that against the same predictive-maintenance scenario, the daily PSI check on the sensor features fired a retrain trigger within days of the true day-twenty shift, instead of waiting for day thirty. The system trained a challenger on the most recent drift-aware data and evaluated it against the current champion on a shared holdout before promoting anything, so nothing shipped without clearing the same bar an ordinary champion-challenger comparison already enforces. Days-to-remediation came in under ten, against the unaddressed ten-day gap the fixed schedule leaves open by construction, and every retrain that did happen was proven against a holdout before it ever touched live traffic.

## Design considerations

This pattern only answers when to retrain. It says nothing about how. Chip Huyen's writeup on real-time machine learning separates those as genuinely independent axes: most production retraining is stateless, a full retrain from scratch every time, versus stateful, fine-tuning the existing model on only the new data since the last update. Huyen cites a reported case from Grubhub where stateful retraining cut training cost by a factor of forty-five compared to a full retrain. I haven't distinguished stateless from stateful retraining in what I built here, and the two carry genuinely different infrastructure requirements. Stateful retraining needs model lineage and fine-tune-from-checkpoint tracking that a stateless full retrain doesn't, and skipping that distinction means you might be paying for a full retrain every time a partial one would have done the job for a fraction of the cost.

The trigger itself needs real calibration, and I don't think there's a universal right answer here. Too sensitive a drift threshold and you're retraining constantly, chasing noise instead of real shifts, which burns compute and erodes trust in the alert the same way any false-alarm-heavy system does. Too loose a threshold and you've rebuilt the fixed-schedule problem you were trying to escape, just with extra steps, because now drift has to get severe enough to clear a high bar before anything happens, and severe drift sitting unaddressed for days is exactly the failure this pattern exists to prevent.

I'd also name a real gap this pattern doesn't touch, one that sits quietly underneath a lot of retraining pipelines: closed-loop feedback contamination. A model's own production decisions can determine what labels even exist to retrain on later. A demand-forecasting model that under-predicts causes under-ordering, which produces fewer transactions to learn from, which reinforces the under-prediction. Neither drift monitoring nor an otherwise well-calibrated retrain catches this, because the model can be statistically sound at the moment it's deployed and still quietly corrupt its own future training signal purely by acting on its own predictions. Drift-triggered retraining fixes staleness. It doesn't fix a model that's slowly poisoning its own future data, and I don't think you can solve that second problem with a better drift threshold. It needs a different kind of intervention entirely, one that changes what gets logged as ground truth, not one that changes when you retrain.
