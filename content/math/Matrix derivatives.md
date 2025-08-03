---
title: Matrix derivatives
date created: 2025-08-02T10:44:38-04:00
date modified: 2025-08-02T23:07:24-04:00
tags:
  - math
  - matrices
---
In these differentiation rules, $X$ is assumed to be a matrix of no particular structure, $A$ is a constant.[^1]

$$
\begin{align}

\partial A                                          &= 0 \\
\partial \left( \alpha X \right)                    &= \alpha \partial X \\
\partial \left( X + Y \right)                       &= \partial X + \partial Y \\
\partial \left( \text{Tr}\left( X \right) \right)   &= \text{Tr} \left( \partial X \right) \\
\partial \left( XY\right)                           &= \left( \partial X \right) Y + X \left( \partial Y \right) \\
\partial \left( X \circ Y \right)                   &= \partial X \circ Y + X \circ \partial Y \\
\partial \left( X \otimes Y \right)                 &= \partial X \otimes Y + X \otimes \partial Y \\
\partial \left( X^{-1} \right)                      &= -X^{-1} \left( \partial X \right) X^{-1} \\
\partial \left( \det \left( X \right) \right)       &= \text{Tr} \left( \text{adj} \left( X \right) \partial X \right) \\
\partial \left( \det \left( X \right) \right)       &= \det \left( X \right) \text{Tr} \left( X^{-1} \partial X \right) \\
\partial \ln \left( \det \left( X \right) \right)   &= \text{Tr} \left( X^{-1} \partial X \right) \\
\partial X^T                                        &= \left( \partial X \right)^T \\
\partial X^H                                        &= \left( \partial X \right)^H \\

\end{align}
$$

Where:

- $\text{Tr}(X)$ is the trace of matrix $X$
- $\det(X)$ is the determinant of matrix $X$
- $X^{-1}$ is the inverse of matrix $X$
- $X^T$ is the transpose of matrix $X$
- $X^H$ is the transposed and conjugated matrix (Hermitian) of matrix $X$
- $X \circ Y$ is the Hadamard (elementwise) product of matrices $X$ and $Y$
- $X \otimes Y$ is the Kronecker product of matrices $X$ and $Y$

[^1]: [Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf), Petersen & Pedersen, University of Waterloo
