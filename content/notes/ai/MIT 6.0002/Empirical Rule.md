---
title: Empirical Rule
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

Aside from providing a single value to describe a probability, it's always better to provide a [[notes/ai/MIT 6.0002/Confidence intervals|confidence interval]]. 

Confidence intervals are calculated through the **empirical rule**. Given the mean and standard deviations from a dataset:
- ~68% will be within one standard deviation from the mean.
- ~95% will be within 1.96 standard deviations from the mean.
- ~99.7% will be within 3 standard deviations from the mean.

The empirical rule doesn't always work because it makes a couple of assumptions:
- The mean estimation error is 0, meaning that estimating errors in both sides of the mean is equally likely, not biased to any direction in particular.
- The distribution of the errors is normal, Gaussian.