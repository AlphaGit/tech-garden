---
title: Standard Error of the Mean
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

For times where we can only get a sample (like political polls), we can exploit the third aspect of the [[notes/ai/MIT 6.0002/Central Limit Theorem|Central Limit Theorem]]:

> The variance of the sample means will be close to the variance of the population, divided by the sample size.

This allows us to calculate the _Standard Error of the Mean (SEM or SE)_.

$$SE = \frac{\sigma}{\sqrt{n}}$$
Where:
- $\sigma$: Standard deviation of the population
- $n$, size of the sample

However, this requires us to calculate the standard deviation of the **population**, which is not always possible. In cases, we can use the standard deviation of the sample, if that's all we got.