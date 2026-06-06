---
title: Model metrics
date created: 2024-12-20T22:06:48-05:00
date modified: 2024-12-20T22:08:14-05:00
tags:
  - ai
  - mit
  - ocw
  - machine_learning
---
During the construction of the model we might need to make design choices about which kinds of error the model will make, like prioritizing minimizing false positives.

Accuracy: measure of how many instances the model got right.

$$
accuracy = \frac
{
	true\ positive + true\ negative
}
{
	true\ positive + true\ negative + false\ positive + false\ negative
}
$$

PPV: Positive predictive value: how may true positives the model came up from the things it labeled positive.

$$
positive\ predictive\ value = \frac
{
	true\ positive
}
{
	true\ positive + false\ positive
}
$$

Sensitivity: what percentage did the model correctly find.

$$
sensitivity = \frac
{
	true\ positive
}
{
	true\ positive + false\ negative
}
$$

Specificity: what percentage did the model correctly reject.

$$
specificity = \frac
{
	true\ negative
}
{
	true\ negative + false\ positive
}
$$

Sensitivity and specificity suffer a trade off between each other.