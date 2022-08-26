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

Monte Carlo simulation: a method of estimating the value of an unknown quantity, using the principles of inferential statistics.

**Inferential statistics**:
- **Population**: universe of all possible examples
- **Examples**: a proper subset of the population
- A **random sample** tends to exhibit the same properties as the population from which is drawn

These are the principles we applied when testing random walks.

Given a coin, estimate the fraction of heads you would get if you flipped the coin an infinite number of times. It, of course, depends on the evidence that we see in the first flips.

The confidence in our estimate depends on two things: 
- Size of the sample (100 vs 2)
- Variance of the sample (all heads vs. 52 heads)

As the variance grows, we need larger samples to have the same degree of confidence.

More simulations (a larger sample) usually drives the variance down, which is why we have a better confidence in the results. This is the Law of Large numebrs:

> In repeated independent tests with the same actual probability $p$ of a particular outcome in each test, the chance that the franction of times that outcome occurs differs from $p$ converges to zero as the number of trials goes to infinity.

The Gambler's Fallacy: people expect that deviations from the expected occur, they will be evened out in the future.

>On August 18th, 1913, at the casino in Monte Carlo, black came up a record twenty-six times in succession \[in roulette]. ... \[There] was a near panicky-rush to bet on red, beggining about the time black had come up a phenomenal fifteen times."
>-- Huff and Geis, _How to take a chance_

Probability of 26-consecutive blacks: $1/{2^{26}} = 1/67,108,865$

Probability of 26-consecutive blacks when the previous 25 rolls where black: $1/2$, because the events are independent.

Regression to the mean, similar to the glambers fallacy but this one is true: following an extreme event, the following event is likely to be less extreme.

When sampling, it's not guaranteed to get perfect accuracy, because it's  always possible to get a "weird" sample that skews the results. How many samples to take before we get a justifiable answer? It depends on the variability and underlying possibilities.

Quantifying variation in data: **Variance**

$$variance(X) = \frac{\sum_{x \in X}(x-\mu)^2}{|X|}$$

$$\sigma(X) = \sqrt{\frac{1}{|X|} \sum_{x \in X} (x-\mu)^2}$$

- The standard deviation ($\sigma(X)$) is just the square root of the variance.
- Outliers can have a big effect.
- The standard deviation should aways be considered relative to the mean ($\mu$).
- $|X|$ is the cardinality (size) of the set, the number of members in the set.

Squaring the distance means that:
- It doesn't matter the direction of the difference
- Outliers (big distances) get emphasized.

Aside from providing a single value to describe a probability, it's always better to provide a confidence interval. 

Confidence intervals are calculated through the empirical rule. Given the mean and standard deviations from a dataset:
- ~68% will be within one standard deviation from the mean.
- ~95% will be within 1.96 standard deviations from the mean.
- ~99.7% will be within 3 standard deviations from the mean.

The empirical rule doesn't always work because it makes a couple of assumptions:
- The mean estimation error is 0, meaning that estimating errors in both sides of the mean is equally likely, not biased to any direction in particular.
- The distribution of the errors is normal, Gaussian.

Probability distributions capture the notion of relative frequency with which some random variable takes on different values.
- Discrete: values are drawn from a finite set of values. Example: flipping coins, only heads and tails.
- Continuous: drawn from a set of reals between two numbers. 
	- For these, we'll calculate a probability density function. PDF.

PDF: Probability of the random variable lying between two values. We define a curve showing how it works between those.

Normal distributions:

$$P(x) = \frac{1}{\sigma\sqrt{2\pi}}*e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

$$e = \sum_{n=0}^{\infty}\frac{1}{n!}$$

![[notes/ai/MIT 6.0002/assets/gaussian distribution curve.png]]

- Symmetric around the mean
- Peaks at the mean (the most probably value)

To find the probability of the random value between two values (say, 0 and 1), we can integrate the curve between those two values and we'll find the probability.

![[notes/ai/MIT 6.0002/assets/gaussian distribution, integrated.png]]

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