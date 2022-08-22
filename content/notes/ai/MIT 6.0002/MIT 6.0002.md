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

Another example, a field that transports to a different place, like a wormhole.

```python
class OddField(Field):
	def __init__(self, num_holes: int = 1000,
				 x_range: int = 100, y_range: int = 100):
		Field.__init__(self)
		self.wormholes = {}
		
		for w in range(num_holes):
			x = random.randint(-x_range, x_range)
			y = random.randint(-y_range, y_range)
			new_x = random.randint(-x_range, x_range)
			new_y = random.randint(-y_range, y_range)
			new_location = Location(new_x, new_y)
			self.wormholes[(x, y)] = new_location

	def move_drunk(self, drunk: Drunk):
		Field.move_drunk(self, drunk)
		x = self.drunks[drunk].get_x()
		y = self.drunks[drunk].get_y()
		if (x, y) in self.wormholes:
			self.drunks[drunk] = self.wormholes[(x, y)]
```

Incremental changes to simulations can help answer different questions. But it's important to understand what's right about the first simulation. 

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