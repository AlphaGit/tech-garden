---
title: Numba Performance notes
tags:
  - python
  - performance
  - profiling
  - numba
---
[[numba]] includes the following notes which are useful to profiling and identifying which things can be the cause of low performance on an execution:

[Supported Python Features](https://numba.readthedocs.io/en/stable/reference/pysupported.html): contains documentation on which features from [[python]] can be used directly by Numba.

[Supported NumPy features](https://numba.readthedocs.io/en/stable/reference/numpysupported.html): contains documentation on which functions from [[numpy]] can be used directly in [[numba]]. Note that the parameters supported are a subset of the parameters from [[numpy]].

[Command Line Interface / Debugging](https://numba.readthedocs.io/en/stable/user/cli.html#debugging): contains information on how to obtain the [[LLVM]] code or the optimized code, or the final assembly, which might help in identifying potential performance pitfalls.
