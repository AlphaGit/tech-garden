---
title: Linear Regression
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

We're going to assume that our solution to the model is a polynomial. Since we know that the solution to this relationship is a linear one, it'll be a degree-1 polynomial, a line, of the shape $y = ax + b$. This implies that the solution is to find the right values for $a$ and $b$ that minimizes the objective function.

If we were to plot all the possible values for $a$ and $b$ and put a surface on it (in a third dimension), where the value of the objective function for that combination is the height of that surface, we can find the line that takes us from the top of that surface to the lowest point (through multiple steps). This is why the regression method is called **linear regression**, even if it's used for higher-order polynomials.

And because the surface was produced as a sum of squares, we can guarantee that it has only one minimum.

We can use the values of the [[Objective Functions|objective function]] to simply identify, quantitatively, how good the fit is, in relation to different models, as long as we're using the same objective function.