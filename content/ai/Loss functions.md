---
title: Loss functions
tags:
  - ai
  - machine learning
date created: 2025-06-22T09:48:36-06:00
date modified: 2025-11-15T15:57:18-06:00
---

Loss functions are metrics of how much different the predictions from a model are to the real values that it should predict.

You'd think that a regular difference ($\hat{y} - y$) would be enough, but the differences can compensate each other, giving you a wrong value.

## Mean Squared Error (MSE)

Generally preferred. Useful if the target variable has a gaussian distribution.
$$MSE = \frac{1}{n} \sum^{n}(Y-\hat{Y})^2$$

```python
np.mean((y - y_hat) ** 2)
```

## Mean Squared Error with L2 Regularization

Same as above, expect that it also includes the L2 regularization factor.

$$
\text{MSE}_\text{regularized} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y_i})^2 + \lambda \sum_{j=1}^p \beta_j^2
$$

## Mean Squared Logarithmic Error (MLE)

The concept is the same as MSE but using logarithms. Usually used when the target variable has a spread over absolute values (this is, large differences) and MSE might be too unforgiving.

$$
\begin{aligned}
MSLE = & \frac{1}{n} \sum^n\left(
	\log\left(Y + 1\right) - \log\left(\hat{Y} + 1\right)
\right) ^2 \\
= & \frac{1}{n} \sum^n \log\left(\frac{Y + 1}{\hat{Y} + 1}\right)^2
\end{aligned}
$$

```python
np.mean((np.log(y + 1) - np.log(y_hat + 1)) ** 2)
```
