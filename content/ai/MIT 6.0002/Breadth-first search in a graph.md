---
title: Breadth-first search in a graph
tags:
- ai
- machine learning
- courses
- data science
- computer science
- mit ocw
- mit ocw 6.0002
- graph theory
- algorithms
---

Explores all nodes at distance 1, then all nodes at distance 2, etc.

Because it goes with increasing distances, once a solution is found, we know it's the shortest path.

# Algorithm

- Start at an initial node
- Consider all the edges that leave that node, in some order
- Follow the first edge, and check to see if at goal node
- If not, try the next edge rom the current node
- Continue until either find goal node, or run out of options
	- When run out of edge options, move to next node at same distance from start, and repeat
	- When run out of node options, move to next level in the graph (all nodes one step fruther from start) and repeat

# Example code

```python
def BFS(graph, start, end):
	initPath = [start]
	pathQueue = [initPath]
	while len(pathQueue) != 0:
		tmpPath = pathQueue.pop(0)
		lastNode = tmpPath[-1]

	if lastNode == end:
		return tmpPath

	for nextNode in graph.childrenOf(lastNode):
		if nextNode not in tmpPath:
			newPath = tmpPath + [nextNode]
			pathQueue.append(newPath)
```
