---
title: "Strassen's Tensor Multiplication Algorithm"
date created: 2025-07-05T20:36:46-04:00
date modified: 2025-07-05T20:52:16-04:00
---
$$A*B = S^*_C \cdot
\left[
  \left(
    S^*_A \cdot z(A)
  \right)
  *
  \left(
	S^*_B \cdot z(B)
  \right)
\right]$$

where

$$
\begin{align}
S^*_A &= \prod_{i=0}^{l-1}{
	I_{7^i} \otimes S_a \otimes I_{4^{n-i+1}}
}

\\

S^*_B &= \prod_{i=0}^{l-1}{
	I_{7^i} \otimes S_b \otimes I_{4^{n-i+1}}
}

\\

S^*_C &= \prod_{i=l-1}^{0}{
	I_{7^i} \otimes S_a \otimes I_{4^{n-i+1}}
}

\end{align}
$$
and where $I_n$ is the Identity matrix of shape $n \times n$.

> From a computing perspective, naively multiplying together to matrices A and B, each of size n x n, takes O(n³) time. This is accomplished by implementing the formula for matrix multiplication directly on the matrices. For many years, it was assumed that no algorithm could do better than that worst case time.[^1]

The logic behind this algorithm is to de-compose each matrix into a vector form (done by the function $z$), and combine each prepared matrix through a vector multiplication.

$z$ represents a z-order vectorization, defined as:

$$
z(X) = \begin{bmatrix}
	X_{11} \\
	X_{21} \\
	X_{12} \\
	X_{22}
\end{bmatrix}
$$

where the $xy$ sub-indices specify which quadrants it refers to, the order being nort-west, south-west, north-east and south-east quadrants.

However, the z-order vectorization is recursive, meaning that the whole matrix will be decomposed in a single vector following that 

The preparation of each matrix can be done independently, 

[^1]: [Demistifying Strassen's Tensor Multiplication Algorithm](https://medium.com/@alex.liu.roc/demystifying-tensor-strassens-algorithm-c1eb5c9a972c), Alex Liu Roc
