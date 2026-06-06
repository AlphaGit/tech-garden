---
title: Depth-first search in a graph
tags:
- ai
- machine learning
- courses
- data science
- computer science
- mit ocw
- mit ocw 6.0002
- algorithms
- trees
- graphs
---

# Algorithm
- Start off with initial node
- Consider all the edges that leave that node, in some order
- Follow the first edge, and check to see if at goal node
- If not, repeat the process from new node
- Continue until either find goal node, or run out of options
	- When run out of options, backtrack to the previous node and try the next edge, repeating this process

# Example code

```python
def DS(graph, start, end, path, shortest):
	path = path + [start]
	if start == end:
		return path

	for node in graph.childrenOf(start):
		if node not in path: # avoid cycles
			if shortest == None or len(path) < len(shortest):
				newPath = DFS(graoh, node, end, path, shortest)
				if newPath != None
					shortest = newPath

	return shortest

def shortestPath(graph, start, end):
	return DFS(graph, start, end, [], None)
```
