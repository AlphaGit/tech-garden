---
title: Greedy algorithms for optimization problems
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

## For the [[Knapsack problem|Knapsack problem]]

```
while knapsack is not full
  put the best valued item in the knapsack
```

What does "best" mean? $value$? Or ratio $value/weight$?

Efficiency: $O(n \log{n})$ (from sorting $O(n \log{n})$ and iterating over items to add them $O(n)$).

Greedy algorithms make a sequence of local optimizations, and it might not make it to the global solution.

## Pros and cons of greedy algorithms
- Pro: really easy to implement
- Pro: really fast ($O(n \log{n})$)
- Con: does not always get to the best solution (not really optimized?)
- Con: we don't know how close to optimal it is