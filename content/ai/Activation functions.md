---
title: Activation functions
tags:
- ai
- activation
- neural networks
---
Activation functions are a part of a "neuron" in a neural network. It introduces a non-linearity so that the network can learn more than linear (or polynomial) relationships in the input-to-output data.

It is called "activation function" because it decides how much that particular neuron will participate in the generation of the output.

They need to be:

- differentiable, so that learning algorithms based on gradients can calculate them
- continuous, to allow for differentiation, along with 
- bounded, to prevent exploding gradients
- the same function for all neurons in the layer
- monotonic (increasing or decreasing)
- cross the origin (0 value) for its domain

None of these rules are unbreakable, but good guidelines.

Example of activation functions:

- [[ReLU]]
- [[Binary or Step function]]
- [[Sigmoid]]
- [[Linear function]]
- [[Hyperbolic tangent function (tanh)]]
- [[Softmax]]

## Sources

- [Introduction to Activation Functions](https://www.enjoyalgorithms.com/blog/activation-functions-in-neural-networks), EnjoyAlgorithms.com