---
title: Coefficient of Determination
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

However, these are relative fits, meaning that they are not absolute in how good the prediction is to the true real data.

For an absolute measure, we can use the **coefficient of determination**, $R^2$.

$$
R^2 = 1 - \frac{\sum_i(y_i-p_i)^2}{\sum_i(y_i-\mu)^2}
$$

Where $y_i$  are measured values, $p_i$  are predicted values and $\mu$ is the mean of measured values.

The numerator is calculating the error in the estimates. The denominator is calculatin the variuability in the measured data.

In other words, it's calculating which variation of the data is being accounted for the model. If the ratio is 0, then the model explains all of the data, because there's no error inthe model itself (and $R^2$ becomes 1). A $R^2$ of 0.83, says that we're accounting for 83% of the variability in the data.

However, just because a model has a high $R^2$ value doesn't mean that we should run along with it.