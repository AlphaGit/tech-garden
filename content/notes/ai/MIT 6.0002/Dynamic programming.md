---
title: Dynamic programming
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

# Name
Called like that just because Bell had to do something that didn't sound like it was math, to get funding from defense, and the word didn't really meant much.

# Memoization
Store a known result and use it instead of re-calcuating. Trading time usage for space usage.

It works better when these are true:

- **Optimal substructure**: a globally optimal solution can be found by combining optimal solutions to local subproblems
- **Overlapping subproblems**: finding an optimal solution involves solving the same problem multiple times (this includes the elements being considered)