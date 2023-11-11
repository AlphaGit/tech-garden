---
title: tracemalloc
tags:
- python
- performance
- profiling
- memory
---

Python works by using reference counting and a garbage collector of its own that reclaims back memory. It also manages its own heap memory, separately from the system heap. The heap is organized in fixed-size **blocks**, which are organized into **pools**, which are organized  into **arenas**.

`tracemalloc` is a python package that allows us to programatically collect information about the memory.

`tracemalloc.take_snapshot()` will generate a snapshot element.
`Snapshot`s  can be compared with their `compare_to()` method, which includes a `key_type`,  to group the results by `filename`, `lineno` or `traceback`.

## Example
Fast API endpoints

```python
import tracemalloc  
tracemalloc.start(25)  
  
FIRST_SNAPSHOT: tracemalloc.Snapshot = None  
LAST_SNAPSHOT: tracemalloc.Snapshot = None

@router.get('/some/operation')
async def some_operation():
	response = {...}
	
	gc.collect()  
	global FIRST_SNAPSHOT  
	global LAST_SNAPSHOT  
	LAST_SNAPSHOT = tracemalloc.take_snapshot()  
	if FIRST_SNAPSHOT is None:  
	    FIRST_SNAPSHOT = LAST_SNAPSHOT  

	return response

@router.get('/memory/snapshots', response_class=PlainTextResponse)  
async def get_memory_snapshots(top: int = 10) -> str:  
    result = ''  
  
    global FIRST_SNAPSHOT  
    global LAST_SNAPSHOT  
    diff = LAST_SNAPSHOT.compare_to(FIRST_SNAPSHOT, 'filename')  
  
    for stat in diff[:top]:  
		result += f'{stat.size_diff / 1024:.2f} new KiB, '\  
		          f'{stat.size / 1024:.2f} total KiB, '\  
		          f'{stat.count_diff} new blocks, '\  
		          f'{stat.count} total blocks\n''  
        for line in stat.traceback.format():  
            result += line + '\n'  
        result += '\n'  
  
    return result
```

This will yield a result like the following when calling the `GET /memory/snapshots` endpoint:

```
0.00 new KiB, 602.31 total KiB, 0 new blocks, 6161 total blocks
  File "<frozen importlib._bootstrap_external>", line 0

0.00 new KiB, 264.03 total KiB, 0 new blocks, 18 total blocks
  File "/usr/local/lib/python3.8/gzip.py", line 0

0.00 new KiB, 254.15 total KiB, 0 new blocks, 25 total blocks
  File "/usr/local/lib/python3.8/site-packages/uvloop/__init__.py", line 0

0.00 new KiB, 179.01 total KiB, 0 new blocks, 1777 total blocks
  File "/usr/local/lib/python3.8/abc.py", line 0

0.00 new KiB, 147.27 total KiB, 0 new blocks, 1510 total blocks
  File "<frozen importlib._bootstrap>", line 0

0.00 new KiB, 134.92 total KiB, 0 new blocks, 1163 total blocks
  File "/usr/local/lib/python3.8/site-packages/fastapi/utils.py", line 0

0.00 new KiB, 74.03 total KiB, 0 new blocks, 959 total blocks
  File "/usr/local/lib/python3.8/site-packages/uvicorn/protocols/http/httptools_impl.py", line 0

0.00 new KiB, 59.04 total KiB, 0 new blocks, 605 total blocks
  File "/usr/local/lib/python3.8/site-packages/pytz/__init__.py", line 0

0.00 new KiB, 50.82 total KiB, 0 new blocks, 303 total blocks
  File "/usr/local/lib/python3.8/site-packages/websockets/exceptions.py", line 0

0.00 new KiB, 48.31 total KiB, 0 new blocks, 709 total blocks
  File "/usr/local/lib/python3.8/site-packages/fastapi/routing.py", line 0
```

## Sources
- [Diagnosing and Fixing Memory Leaks in Python](https://www.fugue.co/blog/diagnosing-and-fixing-memory-leaks-in-python.html)
- [tracemalloc oficial documentation](https://docs.python.org/3/library/tracemalloc.html)
- [PEP-454](https://www.python.org/dev/peps/pep-0454/)