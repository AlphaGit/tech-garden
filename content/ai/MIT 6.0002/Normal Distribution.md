---
title: Normal Distribution
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

Normal distribution:

$$P(x) = \frac{1}{\sigma\sqrt{2\pi}}*e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

$$e = \sum_{n=0}^{\infty}\frac{1}{n!}$$

![[gaussian distribution curve.png]]

- Symmetric around the mean
- Peaks at the mean (the most probably value)

We can generate normal (Gaussian) distributions in Python by using `random.gauss(mean, std)`.