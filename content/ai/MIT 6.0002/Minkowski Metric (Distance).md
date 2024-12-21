---
title: Minkowski Metric (Distance)
date created: 2024-12-20T22:06:15-05:00
date modified: 2024-12-20T22:08:03-05:00
tags:
  - ai
  - machine
  - learning
  - mit
  - ocw
---
Minkowski Metric:

$$dist(X1, X2, p) = 
\left(
	\sum_{k=1}^{len}
	{
		abs
		\left(
			X1_k - X2_k
		\right)^p
	}
\right)^{1/p}
$$

When $p = 1$, we get the Manhattan distance
When $p = 2$, we get the Euclidean distance