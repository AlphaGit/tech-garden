---
title: Softmax
tags:
  - activation
  - ai
  - neural_networks
date created: 2025-06-22T09:48:36-06:00
date modified: 2025-11-15T15:51:21-06:00
---

[[Activation functions|Activation function]], mostly used in [[neural networks]].

$$f(X) = \frac{e^{x_i}}{\sum{e^{x_i}}}$$

Another definition:

$$
P(y = j|x) = \frac{e^{x^T w_j}}{\sum_{k=1}^K e^{x^T w_k}}
$$
