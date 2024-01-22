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

- [[Computer Models|Computer Models]]
- [[Optimization models|Optimization models]]
- [[Knapsack problem|Knapsack problem]]
- [[Brute force for optimization problems|Brute force for optimization problems]]
- [[Greedy algorithms for optimization problems|Greedy algorithm for optimization problems]]

# Lecture 2: Optimization problems
Source: https://www.youtube.com/watch?v=uK5yvoXnkSk

- [[Greedy algorithms for optimization problems#Pros and cons of greedy algorithms|Pros and cons of greedy algorithms]]
- [[Brute force for optimization problems#Using search trees|Brute force through search trees]]
- [[Dynamic programming|Dynamic programming]]

# Lecture 3: Graph-theoretic models
Source: https://www.youtube.com/watch?v=V_TulH374hw

- [[Graphs|Graphs]]
- [[Shortest path in a graph|Shortest path in a graph]]
- [[Depth-first search in a graph|Depth-first search in a graph]]
- [[Breadth-first search in a graph|Breadth-first search in a graph]]

# Lecture 4: Stochastic Thinking
Source: https://www.youtube.com/watch?v=-1BnXEwHUok

- [[Uncertainty|Uncertainty]]
- [[Stochastic process|Stochastic processes]]
- [[Probability|Probability]]
- [[Random numbers|Random numbers]]
- [[Probability#Sample probability|Sample probability]]
- [[The Birthday Problem|The Birthday Problem]]
- [[Simulation models|Simulation Models]]

# Lecture 5: Random Walks
Source: https://www.youtube.com/watch?v=6wUD_gp5WeE

- [[Random Walks|Random Walks]]
- [[Sanity checks|Sanity checks]]

# Lecture 6: Monte Carlo Simulation
Source: https://www.youtube.com/watch?v=OgO1gpXSUzU

- [[Monte Carlo Simulations|Monte Carlo Simulations]]
- [[Inferential Statistics|Inferential Statistics]]
- [[Confidence intervals|Confidence intervals]]
- [[Law of Large Numbers|Law of Large Numbers]]
- [[Gambler's Fallacy|Gambler's Fallacy]]
- [[Regression to the Mean|Regression to the Mean]]
- [[Variance|Variance]]
- [[Empirical Rule|Empirical Rule]]
- [[Probability Distributions|Probability Distributions]]
- [[Probability Density Function|Probability Density Function]]
- [[Normal Distribution|Normal Distributions]]

# Lecture 7: Confidence Intervals
Source: https://www.youtube.com/watch?v=rUxP7TM8-wo

- [[Normal Distribution|Normal Distribution]]
- [[Probability Density Function|Probability Density Function]]
- [[Central Limit Theorem|Central Limit Theorem]]
- [[Sanity checks|Sanity checks]]

# Lecture 8: Sampling and standard error
Source: https://www.youtube.com/watch?v=soZv_KKax3E

- [[Inferential Statistics|Inferential Statistics]]
- [[Monte Carlo Simulations|Monte Carlo Simulations]]
- [[Sampling|Sampling]]
- [[Confidence intervals|Confidence intervals]]
- [[Standard Error of the Mean|Standard of the Error Mean]]
- [[Skew|Skew]]

# Lecture 9: Understanding Experimental Data
Source: https://www.youtube.com/watch?v=vIFKGFl1Cn8

- [[Data]]
- [[Modelling a spring]]
- [[Objective Functions]]
- [[Least Squares Objective Function]]
- [[Linear regression]]
- [[Coefficient of Determination]]

# Lecture 10: Understanding Experimental Data (Cont.)
Source: https://www.youtube.com/watch?v=fQvg-hh9dUw

- [[Linear regression|Linear regression]]
- [[Testing a model|Testing a model]]
- [[Validation|Validation]]
- [[How to find the right model|How to find the right model]]
- [[Cross Validation|Cross Validation]]

# Lecture 11: Introduction to Machine Learning
Source: https://www.youtube.com/watch?v=h0e2HAPTGF4

- [[Linear regression]]

#to_complete 

You could say that all computer programs learn a little. The grade varies on the kind of algorithm. In this case, particularly, we're interested in programs that learn from experience, seeing examples and generalizing from them instead of having to program that generalization ourselves.

In "regular" programming we program so that the system can process data (that we also provide) to generate output. In machine learning, we want to provide data and output so that the computer generates a program.

Memorization is declarative knowledge, it's the accumulation of individual facts. It is limited by the time to observe them and the memory required to store them.

Generalizaton, instead, is imperative knowledge. Is to deduce new facts from old facts, limited just by the accuracy of the deduction process. It assumes taht the past predicts the future.

Observations: training data. 

Supervised learning: for each example we have a label, and we'll find a way to predict that label associated with the input.

Unsupervised: we have a set of feature vectors without labels, and we'll try to group them into "natural clusters" (or labels for those groups). In some cases we'll know how many labels there should be, in some other cases we'll find which is the best number of them.

Clustering examples into groups:
- Pick $k$ examples (at random?) as exemplars
- Cluster remaining samples by minimizing distance between samples in same cluster (objective function) -- put sample in group with closest exemplar
- Find median example in each cluster as new exemplar
- Repeat until there is no change

This works with unlabeled data, but if we had it labeled, we'd want to find a subsurface (e.g. for 2D data ⇒ line) of the data that naturally divides them.

Features are the information pieces we can gather from our examples. They never fully describe the situation. Extra features might actually hurt the model as there is the danger of finding sporadic correlations. Or it might generate overfitting, depending on how our process of feature engineering mixes them together to separate instances.

Feature engineering is the process of representing examples by feature vectors that will facilitate generalization.

During the construction of the model we might need to make design choices about which kinds of error the model will make, like prioritizing minimizing false positives.

Minkowski Metric:

$$dist(X1, X2, p) = 
\left(
	\sum_{k=1}^{len}
	{
		abs
		\left(
			X1_k - X2_k
		\right)^p
	}
\right)^{1/p}
$$

When $p = 1$, we get the Manhattan distance
When $p = 2$, we get the Euclidean distance

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