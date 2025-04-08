---
title: Complexity classes
tags:
- math
- complexity
---

## PSPACE-complete

> P is the set of all problems that can be solved in polynomial time, relative to the input. PSPACE is the set of all problems that can be solved with polynomial _space_. It’s assumed, but not proven, that PSPACE is strictly larger than NP. [^1]

## EXPTIME-complete

> EXPTIME is the set of all problems that are solvable in exponential time, ie the difficult grows with $O(2^n)$. It’s suspected that EXPTIME is strictly larger than PSPACE and NP, meaning there are problems that take more than polynomial space to solve and more than polynomial time to verify. [^1]

## 2-EXPTIME-complete

> 2-EXPTIME is like EXPTIME except instead of the Big-O being $O(2^n)$, it’s $O(2^{2^n})$. [^1]

## ELEMENTARY-complete

> ELEMENTARY is EXPTIME + 2-EXPTIME + 3-EXPTIME + (etc). [^1]

## TOWER-complete

> Let’s define **tetration** `^^` as repeated exponentiation, so 3^^2 = 3^3, 3^^3 = 3^(3^3), etc. TOWER-complete, then, is O(2^^n). [^1]

## Ackermann-complete

> Define (a variant of) the [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function) like this:
>
> A(1) = 1\*1
> A(2) = 2^2
> A(3) = 3^^3
> A(4) = 4^^^4
> etc
> 
> Ackermann-complete problems take time growing with O(A(n)). [^1]

## Hyperackermann-complete

> The paper [Complexity Hierarchies Beyond Elementary](https://arxiv.org/abs/1312.5686) introduces the HAck complexity class and gives examples of it. [^1]

[^1]: [Problems Harders than NP-Complete](https://buttondown.email/hillelwayne/archive/problems-harder-than-np-complete/), ComputerThings