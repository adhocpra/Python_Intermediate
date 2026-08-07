# Common Threading Problems and Patterns

## Race conditions

A race condition occurs when threads access shared data without proper synchronization.

Symptoms:

- inconsistent values
- wrong results
- unpredictable behavior

Prevent race conditions with locks, queues, or immutable data.

## Deadlocks

Deadlocks occur when two or more threads wait on each other forever.

Example:

- thread A holds lock 1 and waits for lock 2
- thread B holds lock 2 and waits for lock 1

Avoid deadlocks by:

- acquiring locks in a consistent order
- using timeouts with `acquire(timeout=...)`
- reducing lock scope

## Livelock and starvation

- Livelock: threads keep responding to each other but make no progress.
- Starvation: a thread never gets CPU time or lock access.

Avoid these by carefully designing thread interaction and using fair queues.

## Producer-consumer pattern

A common threading pattern where one or more producers generate data and one or more consumers process it.

Use `queue.Queue` for safe communication.

```python
from queue import Queue
from threading import Thread

queue = Queue()

def producer():
    for item in range(10):
        queue.put(item)
    queue.put(None)

def consumer():
    while True:
        item = queue.get()
        if item is None:
            break
        process(item)
        queue.task_done()

Thread(target=producer).start()
Thread(target=consumer).start()
```

## Exception handling in threads

Exceptions inside a thread do not propagate to the main thread automatically.

To capture them, store exceptions in a shared structure or use `concurrent.futures.ThreadPoolExecutor`.

## Best practices

- keep critical sections short
- prefer `with lock:` over manual acquire/release
- use higher-level primitives when possible (`Queue`, `Event`, `Condition`)
- avoid sharing mutable state across threads when possible
- validate thread-safe behavior with tests

## Debugging tips

- reproduce race conditions with stress testing
- add logging around synchronization points
- use thread names to identify thread activity
- separate threading concerns into small functions
