## How to use collections.deque as a FIFO queue

from collections import deque

customQueue = deque(maxlen=3)

# append method
customQueue.append(10)
customQueue.append(20)
customQueue.append(30)
print(customQueue)

# popleft method
print(customQueue.popleft())
print(customQueue)

# clear all method
customQueue.clear()
print(customQueue)