---
title: Welford's method for computing variance
tags:
  - math
  - statistics
  - variance
---
The [[standard deviation]] is defined as the root square of the variance:

> $$s^2 = \frac{\sum_{i=1}^N{\left(x_i-\bar{x}\right)^2}}{N-1}$$
> $$s = \sqrt{s^2}$$ 
> The definition can be converted directly into an algorithm that computes the variance and standard deviation in two passes: compute the mean in one pass over the data, and then do a second pass to compute the squared differences from the mean.
> 
> \[...]
> 
> **Welford’s method** is a usable single-pass method for computing the variance. It can be derived by looking at the differences between the sums of squared differences for N and N-1 samples
> 
> \[...]
> $$\left(x_N-\bar{x}_N\right)\left(x_N-\bar{x}_{N-1}\right)$$
>
> This means we can compute the variance in a single pass using the following algorithm:

```
variance(samples):
  M := 0
  S := 0
  for k from 1 to N:
    x := samples[k]
    oldM := M
    M := M + (x-M)/k
    S := S + (x-M)*(x-oldM)
  return S/(N-1)
```
[^1]

> The algorithm can be extended to handle unequal sample weights, replacing the simple counter _n_ with the sum of weights seen so far. West suggests this incremental algorithm:

```python
def weighted_incremental_variance(data_weight_pairs):
    w_sum = w_sum2 = mean = S = 0

    for x, w in data_weight_pairs:
        w_sum = w_sum + w
        w_sum2 = w_sum2 + w**2
        mean_old = mean
        mean = mean_old + (w / w_sum) * (x - mean_old)
        S = S + w * (x - mean_old) * (x - mean)

    population_variance = S / w_sum
    # Bessel's correction for weighted samples
    # Frequency weights
    sample_frequency_variance = S / (w_sum - 1)
    # Reliability weights
    sample_reliability_variance = S / (w_sum - w_sum2 / w_sum)
```
[^2]
## Sources:

[^1]: https://jonisalonen.com/2013/deriving-welfords-method-for-computing-variance/
[^2]: https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance