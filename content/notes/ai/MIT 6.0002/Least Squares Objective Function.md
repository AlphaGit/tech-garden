---
title: Least Squares Objective Function
tags:
- ai
- machine learning
- courses
- data science
- computer science
- mit ocw
- mit ocw 6.0002
- probability
---

$$
\sum_{i=0}^{len(observed) - 1} \left( observed[i] - predicted[i] \right)^2
$$

The squares gets rid of the sign (we care about the distance, not the direction). It also gives us a nice property to calculate the best line.

This formula looks very similar to the [[Variance]] once, but it's not divided by the number of observations. This is valuable because it tells you how much variation there is in total. 