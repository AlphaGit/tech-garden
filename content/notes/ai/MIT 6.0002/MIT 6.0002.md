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

Random walks is important in many domains, for example, some argue stock market is a random walk, or physical processes (difussion models).

Drunkard's Walk: a drunk person takes a step in a random direction. Is there a relationship between the number of steps he takes and how far away he is from the origin?

Random walk simulation:

```python
class Location(object):
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def move(self, delta_x: float, delta_y: float):
		return Location(self.x + delta_x, self.y + delta_y)

	def get_x():
		return self.x

	def get_y():
		return self.y

	def distance_from(self, other: Location) -> float:
		x_dist = self.x - other.get_x()
		y_dist = self.y - other.get_y()
		return (x_dist**2 + y_dist**2)**0.5

class Drunk(object):
	def __init__(self, name: str):
		self.name = name

import random

class UsualDrunk(Drunk):
	""" Walks a random step in any given direction (N/S/E/W). """
	def take_step(self):
		step_choices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
		return random.choice(step_choices)

class MasochisticDrunk(Drunk):
	""" Always tries to walk north. """
	def take_step(self):
		step_choices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
		return random.choice(step_choices)

class Field(object):
	def __init__(self):
		self.drunks = {}

	def add_drunk(self, drunk: Drunk, location: Location):
		if drunk in self.drunks:
			raise ValueError('Duplicate drunk')
		else:
			# drunks need to be inmutable so they can be used as keys
			# in the dictionary
			self.drunks[drunk] = location 

	def get_location(self, drunk: Drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		return self.drunks[drunk]

	def move_drunk(self, drunk: Drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')

		x_dist, y_dist = drunk.take_step()
		self.drunks[drunk] = self.drunks[drunk].move(x_dist, y_dist)

# Simulating a single walk:
def walk(field: Field, drunk: Drunk, num_steps: int):
	start = field.get_location(drunk)
	for s in range(num_steps):
		field.move_drunk(drunk)
	return start.distance_from(field.get_location(drunk))

def simulate_walks(num_steps: int, num_trials: int, drunk_class):
	drunk = drunk_class()
	origin = Location(0, 0)
	distances = []
	for t in range(num_trials):
		f = Field()
		f.add_drunk(drunk, origin)
		distances.append(round(walk(f, drunk, num_steps), 1))
	return distances

def drunk_test(walk_lengths: List[int], num_trials: int, drunk_class):
	for num_steps in walk_lengths:
		distances = simulate_walks(num_steps, num_trials, drunk_class)
		print(drunk_class.__name__, 'random walk of', num_steps, 'steps')
		print('Mean =', round(sum(distances) / len(distances), 4))
		print('Max =', max(distances))
		print('Min =', min(distances))
```

Biased-random walk: random walk where the choices are not all balanced.

Sanity check: run the simulation on known results, to validate that the results are the ones that we'd expect. A wrong result proves the simualtion is wrong. A right result does not prove the simulation is correct but helps in being hopeful about it.

# Lecture 6: Monte Carlo Simulation
Source: https://www.youtube.com/watch?v=OgO1gpXSUzU

(Pending)

# Lecture 7: Confidence Intervals
Source: https://www.youtube.com/watch?v=rUxP7TM8-wo

(Pending)

# Lecture 8: Sampling and standard error
Source: https://www.youtube.com/watch?v=soZv_KKax3E

(Pending)

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