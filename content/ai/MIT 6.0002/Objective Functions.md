---
title: Objective functions
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

From the multiple measurements, we might have noise and inexactitudes that prevent us from fitting a line (the known relationship between variables). For that, we want to fit a line, but we need to know if it's a good fit. For that, we define what's called an **objective function**. From it, we can find the line that minimizes the objective function.

Finding the distance between that line and each of the values can be done through the distance:
- In the $x$ distance: the horizontal displacement between the point and the line -- it doesn't make a lot of sense
- The distance perpendicular to the line that crosses the point, this makes sense for some machine learning models (like [[Classifiers]])
- The $y$ distance: the vertical displacement between the point and the line -- this is the one that we'll use most of the time, representing the distance between the predicted value by the line and the actual value from the measurement.