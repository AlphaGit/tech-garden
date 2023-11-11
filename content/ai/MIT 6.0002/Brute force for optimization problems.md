---
title: Brute force for an optimization problem
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

1. Generate all possible combinations (power set).
2. Remove combinations that do not fit the constraints.
3. From the remaining, choose any of the ones that maximizes the target.

Guaranteed to give a correct answer.

Usually not very practical.

It has an exponential performance. However, there's no guaranteed algorithm that performs better than exponentially. There's no perfect solution.

## Using search trees

**Tree**: [[Graphs|Graph]] with a root and children of the root.

We build a tree with the left branch signifying that we take an item, and right meaning that we don't take it. We iterate through all elements. Then we choose the node with the highest value that meets our constraints.

Computational complexity: depends on the amount of nodes to generate. We generate one level per each item. The deeper we go, the more nodes we have. Binary choices, so $2^i$ is the number of nodes at each level. All of it: $O(2^{n+1})$.

Optimization: don't generate subtrees that go over the constraints. But it doesn't improve the complexity.

A good trick is to not really build the tree, but rather recursively check the options and return the winning combination of that logical subtree.
