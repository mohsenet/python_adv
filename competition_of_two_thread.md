Competition of two thread
```python
"""
Two thread start(t1 and t2).
they competition to access resource(increment function)

TODO:
    Show the number of successful accesses to resources, which are also irregular, in a chart.
"""

import threading
import time

# Shared resource
counter = 0

# Create the lock
lock = threading.Lock()

def increment():
    global counter

    tid = threading.get_ident()


    for _ in range(100000):
        # Acquire the lock before modifying shared data
        with lock:
            counter += 1
            if counter % 2 == 0:
                print(f"[thread {tid}] counter = {counter}")

# Create two threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final counter: {counter}") # Will reliably be 200000
```
