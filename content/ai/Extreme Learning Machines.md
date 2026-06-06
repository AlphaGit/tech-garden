---
title: Extreme Learning Machines
tags:
  - ai
  - data
  - science
  - papers
---
Extreme Learning Machines are single hidden-layer feed-forward [[neural networks]]. They are one of the [[neural network]] approaches to timeseries forecasting (opposed to [[statistical timeseries forecasting]]).

Original paper by Hung et al, 2004. 

## Training
The training process consists of these steps:

1. All weights and biases are initialized with random values.
2. The hidden layer output matrix ($H$) is calculated by multiplying the inputs with the randomly assigned weights, adding biases, and finally applying an activation function on the output.
3. The output weight matrix is calculated by multiplying the [Moore Penrose inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) of $H$ (hidden layer output matrix) with the training data matrix ($T$).
4. The output weight matrix is finally used to make predictions on new data.

In short, with a single shot we can avoid the multi-step process of iterative training and the backpropagation algorithm that is usually used with feed-forward neural networks.

The tuning of the network will mostly be around its [[Hyperparameters|hyperparameters]]:

- Hidden layer size
- Selection of [[Activation functions|activation function]]
- Selection of input sources
- Selection of the distribution for random values used in the initialization step

## Notes
It is [not as popular as DNN](https://www.researchgate.net/post/Why-Extreme-Learning-machine-is-not-so-popular-as-Deep-Learning) because it still does not reach the accuracy required for non-linear data.

## Sources
- [Time Series Forecasting with Extreme Learning Machines](https://www.analyticsvidhya.com/blog/2021/12/time-series-forecasting-with-extreme-learning-machines/)
- [Extreme Learning Machines: Theory and applications](https://www.sciencedirect.com/science/article/abs/pii/S0925231206000385) ([Full PDF](https://web.njit.edu/~usman/courses/cs675_fall20/ELM-NC-2006.pdf))
- [Exreme Learning Machines for Regression and Multiclass classification](https://ieeexplore.ieee.org/document/6035797)
- [Universal Approximation using Incremental Constructive Feedforward Networks with Random Hidden Nodes](https://www.researchgate.net/publication/6928613_Universal_Approximation_Using_Incremental_Constructive_Feedforward_Networks_With_Random_Hidden_Nodes)
