# Queues in Python

[Queues](https://www.educative.io/blog/data-structures-stack-queue-java-tutorial) are a linear data structure that store data in a “first in, first out” (FIFO) order. Unlike arrays, you cannot access elements by index and instead can **only pull the next oldest element.**

This makes it great for order-sensitive tasks like online order processing or voicemail storage.

We could use a Python list with `append()` and `pop()` methods to implement a queue. Instead, it’s best practice to use the `deque` class from Python’s `collections` module. 

Deques are optimized for the append and pop operations. The deque implementation also allows you to create double-ended queues, which can access both sides of the queue through the `popleft()` and `popright()` methods.

## Applications:

- Operations on a shared resource like a printer or [CPU core](https://www.educative.io/blog/beginners-guide-to-computers-and-programming)


- Serve as temporary storage for batch systems

- Provides an easy default order for tasks of equal importance

## Common queue interview questions in Python

- Reverse first *k* elements of a queue

- Implement a *queue using a linked list*

- Implement a *stack using a queue*