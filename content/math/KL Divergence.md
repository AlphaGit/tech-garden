---
title: KL Divergence
date created: 2025-11-15T16:04:08-06:00
date modified: 2025-11-15T16:27:11-06:00
tags:
  - probability
---

Assess how much information is lost when one distribution is used to approximate another distribution. It is used as a loss function in the [[t-SNE]] algorithm.

$$
D_{KL}(P \parallel Q) = \sum_{x \in X} P(x) \log \frac{P(x)}{Q(x)}
$$
