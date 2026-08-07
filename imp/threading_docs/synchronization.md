# Synchronization and Thread Safety

## Why synchronization is needed

Threads share memory, so two threads can access and modify the same data at the same time. Without protection, this can produce inconsistent results.

Example of a race condition:

```python
counter = 0

def increment():
    global counter
    temp = counter
    temp += 1
    counter = temp
```

Multiple threads running `increment()` may interleave and lose updates.

## Locks

A `Lock` enforces exclusive access to a critical section.

```python
lock = threading.Lock()

with lock:
    counter += 1
```

### `acquire()` and `release()`

- `lock.acquire()` blocks until the lock is available.
- `lock.release()` releases the lock.
- Using `with lock:` is safer and cleaner.

## Reentrant lock (`RLock`)

An `RLock` allows the same thread to acquire the lock multiple times.

Use case: nested functions need the same lock.

```python
rlock = threading.RLock()

with rlock:
    with rlock:
        pass
```

## Condition variables

A `Condition` allows threads to wait until some state is true.

Common pattern:

- `wait()` releases the associated lock and waits
- `notify()` wakes one waiting thread
- `notify_all()` wakes all waiting threads

```python
condition = threading.Condition()

with condition:
    condition.wait()
    # resumed after notification
```

## Semaphore

A `Semaphore` limits the number of threads that can access a resource.

```python
sem = threading.Semaphore(3)

with sem:
    do_work()
```

A `BoundedSemaphore` raises an error if released more times than acquired.

## Event

An `Event` is a simple on/off signal shared across threads.

- `event.wait()` blocks until the event is set
- `event.set()` wakes waiting threads
- `event.clear()` resets the event

```python
event = threading.Event()

# thread A
event.wait()

# thread B
event.set()
```

## Barrier

A `Barrier` makes threads wait until a fixed number of threads have reached the same point.

```python
barrier = threading.Barrier(3)
barrier.wait()
```

## Thread-safe queues

`queue.Queue` provides safe producer-consumer communication without manual locking.

```python
from queue import Queue

q = Queue()
q.put(item)
item = q.get()
```
