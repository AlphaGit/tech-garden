---
title: R-squared Score
date created: 2025-11-15T15:51:37-06:00
date modified: 2025-11-15T16:22:02-06:00
tags:
  - machine_learning
aliases:
  - R2 Score
---

A statistical measure that represents the proportion of variance explained by a regression model

$$
R^2 = 1 - \frac{
	\sum_{i=1}^n (y_i - \hat{y_i})^2
}{
	\sum_{i=1}^n (y_i - \bar{y_i})^2
}
$$

(notice the difference between $\hat{y_i}$ and $\bar{y_i}$)
