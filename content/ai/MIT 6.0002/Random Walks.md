---
title: Random Walks
tags:
- ai
- machine learning
- courses
- data science
- computer science
- mit ocw
- mit ocw 6.0002
- probability
---

Random walks are important in many domains, for example, some argue stock market is a random walk, or physical processes (difussion models).

Drunkard's Walk: a drunk person takes a step in a random direction. Is there a relationship between the number of steps he takes and how far away he is from the origin?

Random walk simulation for this example:

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