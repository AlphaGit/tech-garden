---
title: Validation
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

We also want to be able to predict, so in order to verify it, we'll give it data from the source of the data that it has not seen when generating the model.

Validation (or cross validation), is to test models from one dataset with values obtained from another the dataset we used to fit another model, and vice-versa. When doing this, we might see that the models that fitted perfectly in the dataset we used it for did not work so well, but rather, simpler models worked better. Letting too many degrees of freedom into the model means that we're adjusting not to the phenomena but rather the data, and this is called overfitting. More complex models might start fitting the noise in the data.