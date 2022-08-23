---
title: Theil Sen Regression
tags:
- ai
- data science
---

Theil Sen regression involves fitting multiple regression models on subsets of the training data and combining the coefficients together in the end.

The algorithm calculates least square solutions on subsets with size $n$ of the samples in $X$. In a final step, the spatial median (or L1 median) is calculated of all least square solutions.

Sources:
- [Theil Sen Regressor](https://scikit-learn.org/stable/modules/linear_model.html#theil-sen-regression), SciKit User Guide
- [TheilSenRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html), SciKit Documentation
- [Robust Regression for Machine Learning in Python](https://machinelearningmastery.com/robust-regression-for-machine-learning-in-python/), Machine Learning Mastery
