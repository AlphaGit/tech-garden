---
title: MIT OCW 6.0002 Intro to Computational thinking and Data Science
tags:
- ai
- machine learning
- courses
- data science
- computer science
- mit ocw
- mit ocw 6.0002
---

Source: https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/

# Lecture 1: Introduction, Optimization Problems
Source: https://www.youtube.com/watch?v=C1lhuz6pZC0

- [[notes/ai/MIT 6.0002/Computer Models|Computer Models]]
- [[notes/ai/MIT 6.0002/Optimization models|Optimization models]]
- [[notes/ai/MIT 6.0002/Knapsack problem|Knapsack problem]]
- [[notes/ai/MIT 6.0002/Brute force for optimization problems|Brute force for optimization problems]]
- [[notes/ai/MIT 6.0002/Greedy algorithms for optimization problems|Greedy algorithm for optimization problems]]

# Lecture 2: Optimization problems
Source: https://www.youtube.com/watch?v=uK5yvoXnkSk

- [[notes/ai/MIT 6.0002/Greedy algorithms for optimization problems#Pros and cons of greedy algorithms|Pros and cons of greedy algorithms]]
- [[notes/ai/MIT 6.0002/Brute force for optimization problems#Using search trees|Brute force through search trees]]
- [[notes/ai/MIT 6.0002/Dynamic programming|Dynamic programming]]

# Lecture 3: Graph-theoretic models
Source: https://www.youtube.com/watch?v=V_TulH374hw

- [[notes/ai/MIT 6.0002/Graphs|Graphs]]
- [[notes/ai/MIT 6.0002/Shortest path in a graph|Shortest path in a graph]]
- [[notes/ai/MIT 6.0002/Depth-first search in a graph|Depth-first search in a graph]]
- [[notes/ai/MIT 6.0002/Breadth-first search in a graph|Breadth-first search in a graph]]

# Lecture 4: Stochastic Thinking
Source: https://www.youtube.com/watch?v=-1BnXEwHUok

- [[notes/ai/MIT 6.0002/Uncertainty|Uncertainty]]
- [[notes/ai/MIT 6.0002/Stochastic process|Stochastic processes]]
- [[notes/ai/MIT 6.0002/Probability|Probability]]
- [[notes/ai/MIT 6.0002/Random numbers|Random numbers]]
- [[notes/ai/MIT 6.0002/Probability#Sample probability|Sample probability]]
- [[notes/ai/MIT 6.0002/The Birthday Problem|The Birthday Problem]]
- [[notes/ai/MIT 6.0002/Simulation models|Simulation Models]]

# Lecture 5: Random Walks
Source: https://www.youtube.com/watch?v=6wUD_gp5WeE

- [[notes/ai/MIT 6.0002/Random Walks|Random Walks]]
- [[notes/ai/MIT 6.0002/Sanity checks|Sanity checks]]

# Lecture 6: Monte Carlo Simulation
Source: https://www.youtube.com/watch?v=OgO1gpXSUzU

- [[notes/ai/MIT 6.0002/Monte Carlo Simulations|Monte Carlo Simulations]]
- [[notes/ai/MIT 6.0002/Inferential Statistics|Inferential Statistics]]
- [[notes/ai/MIT 6.0002/Confidence intervals|Confidence intervals]]
- [[notes/ai/MIT 6.0002/Law of Large Numbers|Law of Large Numbers]]
- [[notes/ai/MIT 6.0002/Gambler's Fallacy|Gambler's Fallacy]]
- [[notes/ai/MIT 6.0002/Regression to the Mean|Regression to the Mean]]
- [[notes/ai/MIT 6.0002/Variance|Variance]]
- [[notes/ai/MIT 6.0002/Empirical Rule|Empirical Rule]]
- [[notes/ai/MIT 6.0002/Probability Distributions|Probability Distributions]]
- [[notes/ai/MIT 6.0002/Probability Density Function|Probability Density Function]]
- [[notes/ai/MIT 6.0002/Normal Distribution|Normal Distributions]]

# Lecture 7: Confidence Intervals
Source: https://www.youtube.com/watch?v=rUxP7TM8-wo

We can generate normal (Gaussian) distributions in Python by using `random.gauss(mean, std)`.

A PDF does not give probabilities, but **densities**. They're derivatives of the CDF (Cumulative Distribution Function). In PDFs, we're mostly interested about the area, and not the values in the curve. 

When we reason about the mean of multiple events, not about the probabilities of a single event, we can call on the Central Limit Theorem, which states:

> Given a sufficiently large sample:
> - The means of the samples in a set of samples will be approximately normally distributed.
> - This normal distribution will have a mean close to the mean of the population.
> - The variance of the sample means will be close to the variance of the population divided by the sample size.

This means that for an event:
- We can obtain samples (large enough)
- We can calculate their means
- The mean of these means --> close to population mean
- The variance of these means --> close to variance of population / sample size

When simulations close in on a number, with decreasing standard deviations, we don't know for sure about the _statistical true value_, but instead about what our simulation can infer only. A wrong simluation will still give good results, but the value might be wrong. It is why it's important to do a sanity check.

# Lecture 8: Sampling and standard error
Source: https://www.youtube.com/watch?v=soZv_KKax3E

Inferential statistics: we make inferences about populations by examining one or more random samples drawn from that population.

Monte Carlo: we use lots of random samples and we use them to generate confidence intervals. With the empirical rule we know what the values are of those confidence intervals.

What about when the experiment is difficult to replicate?

Probability sampling: each member of the population has a non-zero probability of being included in a sample.
Simple random sampling: each member of the population has the same chance of being inluded in the sample. No bias.

Stratified sampling: we partition the population into subgroups, and then take a simple random sample from each subgroup, proportional to the size of the subgroups. This can be used to reduce the needed size of a sample.

Sample without replacement: if you take a sample, the members are not reused for next samples.
Sampling with replacement: allows you to take the same elements again in the next sample.

Error bars: graphical visualization of the variability of the data. A way to visualize uncertainty.

![[error bars.png]]

When confidence intervals (error bars) overlap, we canot say that the difference is significant. But otherwise, we can concluse that the means are statistically significantly different.

More samples won't help improving the accuracy of the mean/standard deviation.

Larger sample sizes won't help improve the accuracy of the mean but will reduce the standard deviation (improve confidence intervals, making them smaller).

For times where we can only get a sample (like political polls), we can exploit the third aspect of the Central Limit Theorem:

> The variance of the sample means will be close to the variance of the population, divided by the sample size.

This allows us to calculate the _Standard Error of the Mean (SEM or SE)_.

$$SE = \frac{\sigma}{\sqrt{n}}$$
Where:
- $\sigma$: Standard deviation of the population
- $n$, size of the sample

However, this requires us to calculate the standard deviation of the **population**, which is not always possible. In cases, we can use the standard deviation of the sample, if that's all we got.

Skew: measure of asymmetry of a probability distribution.

More skew: more samples required for a good approximation.

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

# Lecture 9: Understanding Experimental Data
Source: https://www.youtube.com/watch?v=vIFKGFl1Cn8

(Pending)

# Lecture 10: Understanding Experimental Data (Cont.)
Source: https://www.youtube.com/watch?v=fQvg-hh9dUw

(Pending)

# Lecture 11: Introduction to Machine Learning
Source: https://www.youtube.com/watch?v=h0e2HAPTGF4

(Pending)

# Lecture 12: Clustering
Source: https://www.youtube.com/watch?v=esmzYhuFnds

(Pending)

# Lecture 13: Classification
Source: https://www.youtube.com/watch?v=eg8DJYwdMyg

(Pending)

# Lecture 14: Classification and statistical sins
Source: https://www.youtube.com/watch?v=K2SC-WPdT6k

(Pending)

# Lecture 15: Statistical Sins and Wrap Up
Source: https://www.youtube.com/watch?v=iOZVbILaIZc

(Pending)