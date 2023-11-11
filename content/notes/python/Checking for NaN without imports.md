---
title: Checking for NaN without imports
tags:
  - python
  - snippets
---
There's a nice trick to check for `NaN` values without using any imports (`np.isnan` or even `math.isnan`), and it relies on the fact that `NaN` will always be non-equal to anything else, including itself.

```python
value = float('nan')
value != value
#> True
```
