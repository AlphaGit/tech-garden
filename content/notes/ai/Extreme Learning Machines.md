---
title: Extreme Learning Machines
tags:
- ai
- data science
---

Extreme Learning Machines are single hidden-layer feedforeward [[neural networks]]. They are one of the [[neural network]] approaches to timeseries forecasting (opposed to [[statistical timeseries forecasting]]).

Original paper by Hung et al, 2004. 

## Training
The training process consists of these steps:

1. All weights and biases are initialized with random values.
	1. Which distribution?
2. The hidden layer output matrix ($H$) is calculated by multiplying the inputs with the randomly assigned weights, adding biases, and finally applying an activation function on the output.
3. The output weight matrix is calculated by multiplying the [Moore Penrose inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) of $H$ (hidden layer output matrix) with the training data matrix ($T$).
4. The output weight matrix is finally used to make predictions on new data.

In short, with a single shot we can avoid the multi-step process of iterative training and the backpropagation algorithm that is usually used with feed-forward neural networks.

The tuning of the network will mostly be around its hyperparameters:
- Hidden layer size
- Selection of activation function
- Selection of input sources
- Selection of the distribution for random values used in the initialization step

## Sources
- [Time Series Forecasting with Extreme Learning Machines](https://www.analyticsvidhya.com/blog/2021/12/time-series-forecasting-with-extreme-learning-machines/)
- [Extreme Learning Machines: Theory and applications](https://www.sciencedirect.com/science/article/abs/pii/S0925231206000385)
- [Exreme Learning Machines for Regression and Multiclass classification](https://ieeexplore.ieee.org/document/6035797)
- [Universal Approximation using Incremental Constructive Feedforward Networks with Random Hidden Nodes](https://www.researchgate.net/publication/6928613_Universal_Approximation_Using_Incremental_Constructive_Feedforward_Networks_With_Random_Hidden_Nodes)
