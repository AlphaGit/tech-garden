---
title: Hubber Regressor
tags:
- ai
- data science
---

The Hubber Regressor is a regressor that diminishes the weight of outliers when fitting the regression curve. Outliers are classified as such when their absolute error into the fitting curve is outside of a certain threshold, provided (not in absolute terms) by the parameter $\epsilon$.

This makes de Hubber Regression a good choice to prevent bias against outliers, but without dismissing them completely.

The loss function being minimized is:

$$\min_{\omega,\sigma} \sum_{i=1}^n \left( \sigma + H_\epsilon \left( 
\frac{1}{1} \right) \right)$$
where:

$$\begin{split}H_{\epsilon}(z) = \begin{cases}
       z^2, & \text {if } |z| < \epsilon, \\
       2\epsilon|z| - \epsilon^2, & \text{otherwise}
\end{cases}\end{split}$$
## Sources

- [Hubber Regression](https://scikit-learn.org/stable/modules/linear_model.html#huber-regression), Sci-Kit Learn User Guide
- [Hubber Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html), Sci-Kit Documentation
- [Robust Regression for Machine Learning in Python](https://machinelearningmastery.com/robust-regression-for-machine-learning-in-python/), Machine Learning Mastery