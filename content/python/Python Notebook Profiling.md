---
title: Python Notebook Profiling
tags:
  - python
  - jupyter
  - performance
  - profiling
---
There are several [[IPython Notebook magic commands]] that are specially helpful at the moment of profiling code.

`%timeit` for line-magic and `%%timeit` for cell-magic is one of them. It can be used to time the repeated execution of snippets of code. It automatically does a large number of repetitions. For slower commands, `%timeit` will automatically adjust and perform fewer repetitions.

However, sometimes repeating an operation is not the best option. For this, the `%time` magic function may be a better choice. It also is a good choice for longer-running commands, when short, system-related delays are unlikely to affect the result.

`%timeit` does some clever things under the hood to prevent system calls from interfering with the timing. For example, it prevents [[garbage collection]] which might otherwise affect the timing. For this reason, `%timeit` results are usually noticeably faster than `%time` results.

Python contains a built-in code profiler (which you can read about in the Python documentation), but IPython offers a much more convenient way to use this profiler, in the form of the magic function `%prun`

```python
%load_ext line_profiler

#---

%lprun -f function_name function_name(arguments)
```

It will do a line-by-line profiling of the specified function.

In a similar fashion, `%memit` and `%mprun` can be used to do memory profiling, in the same fashion that we did speed profiling. `%memit` offers a memory-measuring equivalent of `%timeit` `%mprun` offers a memory-measuring equivalent of `%lprun`. They are also an external extension, so it needs to be installed and loaded. 

`%load_ext memory_profiler`

For a line-by-line description of memory use, we can use `%mprun`. Unfortunately, this magic works only for functions defined in separate modules rather than the notebook itself, so we can use the `%%file` magic command to create a simple module.

```python
%%file test_mprun.py
def some_function():
	...

# ---

from test_mprun import some_function

# ---

%mprun -f some_function some_function()
```

## Sources

- [Timing and Profiling](https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html), Python Data Science Handbook
