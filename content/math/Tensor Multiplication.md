---
title: Tensor Multiplication
date created: 2025-07-13T11:06:22-04:00
date modified: 2025-07-13T13:04:34-04:00
tags:
  - math
---
Tensor multiplication is a mixture of different procedures on which tensors can be combined together. Depending on the desired output, several algorithms can be applied.

Most specifically, the tensor product is a bilinear map between pairs of tensors (vector spaces) in the same field[^1]:

$$
\begin{align}
&
(v, w) \rightarrow V \otimes W
\\
& V \times W \rightarrow V \otimes W
\\
\text{where } & v \in V
\\
& w \in W
\end{align}
$$

## Tensor contraction

Out of those mappings, one of them is tensor contraction, which is mapped by obtains the values by summing over various indexes.

$$T^r_s (V) \to T^{r-1}_{s-1}(V)$$
When two tensors are contracted together, their multiplication is given by the following contraction:[^2]

$$\Lambda^\alpha {}_\beta M^\beta {}_\gamma = N^\alpha {}_\gamma$$
This is, in turn, what gives rise to the definition for matrix multiplication:[^3]

$$
c_{ij} = \sum_{k=1}^m a_{ik} b_{kj}
$$

Which is just an example of tensor contraction applied to two tensors of dimensionality 2.

The same definition can be applied to tensors of arbitrary dimensionality, such as the contraction of two 3-dimension tensors into one 4-dimension tensor:[^4]

$$
c_{ijlm} = \sum_k a_{ijk} b_{klm}
$$

[^1]: [Tensor product](https://en.wikipedia.org/wiki/Tensor_product), Wikipedia

[^2]: [Contraction on a pair of tensors, Tensor Contraction](https://en.wikipedia.org/wiki/Tensor_contraction#Contraction_of_a_pair_of_tensors), Wikipedia

[^3]: [Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm), Wikipedia

[^4]: [Is there a 3-dimensional "matrix" by "matrix" product?](https://math.stackexchange.com/a/63139/22733), Maths Stack Exchange
