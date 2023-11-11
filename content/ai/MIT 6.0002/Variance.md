---
title: Variance
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

When sampling, it's not guaranteed to get perfect accuracy, because it's always possible to get a "weird" sample that skews the results. How many samples to take before we get a justifiable answer? It depends on the variability and underlying possibilities.

Quantifying variation in data: **Variance**

$$variance(X) = \frac{\sum_{x \in X}(x-\mu)^2}{|X|}$$

$$\sigma(X) = \sqrt{\frac{1}{|X|} \sum_{x \in X} (x-\mu)^2}$$

- The standard deviation ($\sigma(X)$) is just the square root of the variance.
- Outliers can have a big effect.
- The standard deviation should aways be considered relative to the mean ($\mu$).
- $|X|$ is the cardinality (size) of the set, the number of members in the set.

Squaring the distance means that:
- It doesn't matter the direction of the difference
- Outliers (big distances) get emphasized.