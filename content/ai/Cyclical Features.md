---
title: Cyclical Features
date created: 2025-11-22T21:30:08-06:00
date modified: 2025-11-22T21:38:28-06:00
tags:
  - machine_learning
  - feature_engineering
---
In [[feature engineering]], cyclical features are a type of feature that have a linear relationship but at the same time have a ring-like disposition of its elements, where the last element in the sequence is followed by the first element in the sequence.

Easy to grasp examples might be the hour in a day (0, 1, 2, ..., 23, 0, 1...) or day of the week (Monday, Tuesday, ..., Saturday, Sunday, Monday, ...).

Linear representation of these features don't properly capture the close relationship between the last and first elements in the sequence.

Trigonometric functions can be used to encode this features while preserving these relationships, thinking about the whole sequence like a unit circle and placing each element along its circumference.

![[CyclicalFeatureDayOfWeekUnitCircle.png]][^1]

Example, using $\sin$ to encode the hour of the day (although $\cos$ could be used as well):

$$
\sin \frac{\text{hour} \cdot 2\pi}{24}
$$ 

[^1]: Cyclical feature encoding, [Daily Dose of DS](https://www.dailydoseofds.com/), Nov 22nd 2025
