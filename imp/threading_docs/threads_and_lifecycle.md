# Threads and Lifecycle

## What is a thread?

A thread is a separate flow of execution within a program. Multiple threads can run concurrently inside a single process and share the same memory space.

## Creating threads in Python

Use the `threading` module to create threads.

Example:

```python
import threading

def worker(name):
    print(f"Thread {name} is running")

thread = threading.Thread(target=worker, args=("A",))
thread.start()
thread.join()
```

## Thread lifecycle

- `Thread` object created
- `start()` begins execution and invokes `run()`
- `run()` executes the target function
- `is_alive()` checks if the thread is still running
- `join()` waits for thread completion

## `target`, `args`, and `kwargs`

When creating a thread, pass the callable with any positional and keyword arguments.

```python
thread = threading.Thread(target=worker, args=("A",), kwargs={"verbose": True})
```

## Naming threads

Each thread can have a name for debugging:

```python
thread = threading.Thread(target=worker, name="worker-thread")
print(thread.name)
```

## Daemon vs non-daemon threads

- Non-daemon threads keep the program running until they finish.
- Daemon threads are killed when the main program exits.

```python
thread.daemon = True
thread.start()
```

Daemon threads are useful for background tasks that should not block program shutdown.

## Inheriting from `Thread`

You can subclass `threading.Thread` and override `run()`:

```python
class MyThread(threading.Thread):
    def run(self):
        print("Thread running")

thread = MyThread()
thread.start()
```
