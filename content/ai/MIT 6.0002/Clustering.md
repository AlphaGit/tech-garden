---
title: Clustering
date created: 2024-12-20T22:04:47-05:00
date modified: 2024-12-20T22:07:13-05:00
tags:
  - ai
  - mit
  - ocw
  - machine_learning
---
Clustering examples into groups (example of [[Supervised-Unsupervised Learning|Unsupervised learning]]):
- Pick $k$ examples (at random?) as exemplars
- Cluster remaining samples by minimizing distance between samples in same cluster (objective function) -- put sample in group with closest exemplar
- Find median example in each cluster as new exemplar
- Repeat until there is no change

This works with unlabeled data, but if we had it labeled, we'd want to find a subsurface (e.g. for 2D data ⇒ line) of the data that naturally divides them.