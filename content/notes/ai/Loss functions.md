---
title: Loss functions
tags:
- ai
- machine learning
---

Loss functions are metrics of how much different the predictions from a model are to the real values that it should predict.

You'd think that a regular difference ($\hat{y} - y$) would be enough, but the differences can compensate each other, giving you a wrong value.

## Mean Squared Error (MSE)

Generally preferred. Useful if the target variable has a gaussian distribution.
$$MSE = \frac{1}{n} \sum^{n}(Y-\hat{Y})^2$$
```python
np.mean((y - y_hat) ** 2)
```

## Mean Squared Logarithmic Error (MLE)

The concept is the same as MSE but using logarithms. Usually used when the target variable has a spread over absolute values (this is, large differences) and MSE might be too unforgiving.

$$
\begin{align*}
MSLE

= & \frac{1}{n} \sum^n\left(
	\log\left(Y + 1\right) - \log\left(\hat{Y} + 1\right)
\right)
^2
\\
= & \frac{1}{n} \sum^n
	\log\left(\frac{Y + 1}{\hat{Y} + 1}\right)
^2
\end{align*}$$

```python
np.mean((np.log(y + 1) - np.log(y_hat + 1)) ** 2)
```
