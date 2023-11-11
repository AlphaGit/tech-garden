---
title: The Knapsack Problem
tags:
- ai
- machine learning
- courses
- data science
- computer science
- mit ocw
- mit ocw 6.0002
- algorithms
---

(knapsack = backpack, bag)

A burglar breaks into a house and wants to steal. But the capacity of the knapsack is limited. They need to get the most valuable out of the robbery but it still needs to fit.

# Continuous (fractional) knapsack problem
You can take pieces of an object. This problem is easy to solve, with a greedy algorithm. You take the best thing first as long as you can.

# 0/1 knapsack problem
You either take the object or you don't. More complicated because making a decision impacts future decisions. A greedy algorithm is not guaranteed to give the best answer.

Each item is represented by a pair $<value, item>$.

The knapsack can accomodate items with a total weight no more than $w$.

A vector $I$ of length $n$ represents the set of available items.

A vector $V$ of length $n$ is used to indicate wether an item is taken or not. $V[i] = 1$ means that item $I[i]$ is taken.

A binary number can represent the items to take, using a single vector of zeroes and ones.

Find $V$ that maximizes:

$$\sum_{i=0}^{n-1} {V[i] * I[i].value}$$
(sum of the taken values)

subject to the constraint that:

$$\sum_{i=0}^{n-1} {V[i] * I[i].weight} \le w$$

(sum of the taken weights is less or equal than the capacity)