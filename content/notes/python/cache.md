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