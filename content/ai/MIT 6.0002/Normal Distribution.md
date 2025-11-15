---
title: Normal Distribution
tags:
  - ai
  - courses
  - probability
  - machine_learning
  - data_science
  - computer_science
  - mit_ocw
  - mit/ocw/6-0002
date created: 2025-06-22T11:48:36-04:00
date modified: 2025-11-12T21:15:42-05:00
---

Normal distribution:

$$P(x) = \frac{1}{\sigma\sqrt{2\pi}}*e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

$$e = \sum_{n=0}^{\infty}\frac{1}{n!}$$

![[gaussian distribution curve.png]]

- Symmetric around the mean
- Peaks at the mean (the most probably value)

We can generate normal (Gaussian) distributions in Python by using `random.gauss(mean, std)`.