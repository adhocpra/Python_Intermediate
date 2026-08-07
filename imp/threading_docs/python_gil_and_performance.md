# Python GIL and Threading Performance

## What is the Global Interpreter Lock (GIL)?

The GIL is a mutex that protects access to Python objects in CPython. It ensures only one thread executes Python bytecode at a time.

## Impact on CPU-bound workloads

For CPU-intensive tasks, Python threads do not run Python code in true parallelism on multiple cores due to the GIL.

Example: calculating large prime numbers in threads may not speed up execution.

## I/O-bound workloads

Threading is effective for I/O-bound tasks, such as:

- network requests
- file I/O
- waiting on external systems

While one thread waits for I/O, another thread can run.

## When to use threads vs processes

- Use `threading` for I/O-bound tasks and concurrent waiting.
- Use `multiprocessing` for CPU-bound tasks to bypass the GIL.

## Thread pools

`ThreadPoolExecutor` from `concurrent.futures` simplifies thread management.

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(worker, i) for i in range(10)]
```

## GIL and C extensions

If Python threads call C extensions that release the GIL, those threads can run in parallel. Many libraries, like `numpy`, do this.

## Python `threading` module limitations

- No true parallel execution for pure Python CPU tasks
- Shared memory makes synchronization necessary
- Debugging race conditions can be difficult

## Practical guidance

- Prefer threads when the workload is I/O-bound.
- Use `ThreadPoolExecutor` for simpler high-level concurrency.
- Profile your code to decide whether threads help.
