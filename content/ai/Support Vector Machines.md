---
title: Support Vector Machines
date created: 2025-11-15T16:07:23-06:00
date modified: 2025-11-15T16:28:20-06:00
tags:
  - machine_learning
---
$$
\min_{w,b} \frac{1}{2} \parallel w \parallel^2 +
C \sum_{i=1}^n \max
\left(
	0,
	1 - y_i
	\left(
		w \cdot x_i - b
	\right)
\right)
$$