---
title: RANSAC Regression
tags:
- ai
- data science
---

The Random Sample Consensus (RANSAC) algorithm is a regressor algorithm that discards outliers automatically.

The algorithm works as follows:

1. Select a random subset from the data. Call this subset the _hypothetical inliners._
2. Fit a model to these hypotetical inliners.
3. Test all of the other data points against this model.
	1. For those points that, according to a loss function, perform well enough, are also considered part of the _consensus set_.
4. The model is considered good enough if a certain amount of points made it into the consensus set.
5. Iterate $n$ times, keeping the best model.

![[RANSAC regressor.png]]
Sources:
- [Random Sample Consensus](https://en.wikipedia.org/wiki/Random_sample_consensus), Wikipedia
- [RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html), SciKit Learn Documentation
- [RANdom SAmple Consensus](https://scikit-learn.org/stable/modules/linear_model.html#ransac-regression), SciKit User Guide
- [Robust Regression for Machine Learning in Python](https://machinelearningmastery.com/robust-regression-for-machine-learning-in-python/), Machine Learning Mastery
