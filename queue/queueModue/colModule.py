# The collections.dequeue Class

# Methods:- 
# 1)deque() - To create queue with capacity or without capacity
# 2)append() - adding elements to queue
# 3)popleft - remove and return the first element of queue
# 3)clear() - removing all element from queue



from collections import deque

customQueue = deque(maxlen=3)


customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
# customQueue.append(4)
# customQueue.popleft()
# customQueue.clear()
print(customQueue.popleft())