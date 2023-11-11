---
title: Cross validation
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

For small datasets, let's use leave-one-out cross-validation. Walk through a number of trials, and for each drop an example from the dataset, fit a model and test it on the left-out datapoint.

For big datasets, we can use k-fold cross-validation, or repeated random sampling. Divide the sample in k-equal sized chunks. Pick a chunk and leave it out, fit the model to the rest of the data, test it with that chunk.

Repeated random sampling. Reserve an amount of the dataset, and pick random examples.

It's important to run multiple trials and see the mean and the standard deviation of the calculated R-squared values of those tests. This is because otherwise, we run the risk of just looking at a bad or good run and making decisions based on that.