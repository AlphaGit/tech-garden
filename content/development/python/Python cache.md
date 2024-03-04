---
title: Python cache
tags:
- cache
- python
- snippets
---

`@lru_cache` can be used elegantly to create a cache with a time-to-live, if a time parameter is used to invalidate previous responses:

```python
from functools import lru_cache
import time


@lru_cache()
def my_expensive_function(a, b, ttl_hash=None):
    del ttl_hash  # to emphasize we don't use it and to shut pylint up
    return a + b


def get_ttl_hash(seconds=3600):
    """Return the same value within `seconds` time period"""
    return round(time.time() / seconds)


# somewhere in your code...
res = my_expensive_function(2, 2, ttl_hash=get_ttl_hash())
# cache will be updated once in an hour
```

([Source](https://stackoverflow.com/a/55900800/147507))

A more elegant version that does not require external parameters ([source](https://realpython.com/lru-cache-python/)):

```python
from functools import lru_cache, wraps
from datetime import datetime, timedelta

def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache
```

