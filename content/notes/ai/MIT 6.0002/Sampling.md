---
title: Sampling
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

What about when the experiment is difficult to replicate?

**Probability sampling:** each member of the population has a non-zero probability of being included in a sample.

**Simple random sampling:** each member of the population has the same chance of being inluded in the sample. No bias.

**Stratified sampling:** we partition the population into subgroups, and then take a simple random sample from each subgroup, proportional to the size of the subgroups. This can be used to reduce the needed size of a sample.

**Sampling without replacement:** if you take a sample, the members are not reused for next samples.

**Sampling with replacement:** allows you to take the same elements again in the next sample.

More samples won't help improving the accuracy of the mean/standard deviation.

Larger sample sizes won't help improve the accuracy of the mean but will reduce the standard deviation (improve confidence intervals, making them smaller).

To estimate the mean of a population given a single sample, we choose a sample size based upon some estimate of the skew in the population. When you know the size, you choose a random sample from the population, and you compute the mean and standard deviation of that sample, and use it to estimate the standard error. This is an estimate, not the true standard error. Appropriately chosen, can be a good estimation. From it, we can calculate the confidence intervals around the sample mean.

Answering: are 200 samples enough?

```python
temps = ... # list with the population temperatures
sampleSize = 200
numTrials = ... # any number to run this experiment
popMean = ... # mean of the whole population

numBad = 0
for t in range(numTrials):
	sample = random.sample(temps, sampleSize)
	sampleMean = sum(sample)/sampleSize
	se = numpy.std(sample)/sampleSize ** 0.5
	if abs(popMean - sampleMean) > 1.96*se:
		numBad += 1
print(f'Fraction outside 95% confidence interval = {numBad/numTrials}')
```

Because this is a 95% confidence interval, we expect the result to be 0.5 (5%). If it's higher, our sample size is not good enough. If it's lower, our sample size is too conservative ("too good").