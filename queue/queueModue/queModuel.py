# we will use Queue?(maxsize=0) class for fifo
#methods
# 1)qsize() - returns approximate size of the queue
# 2)empty() - returns true if the queue is empty and false if the queue is not empty
# 3)full() - returns true if the queue is full and flase if not full
# 4)put() - alternative of enqueue, adding element at the end of the queue
# 5)get() - it returns element from begning of the queue and removes it from queue
# 6)task_done() - it tells the the processing of any task on the queue is done or not
# 7)join() - 

import queue as q

customQueue = q.Queue(maxsize=3)
# print(customQueue.qsize())
# print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)

# print(customQueue.qsize())
# print(customQueue.full())
# print(customQueue.get())
# print(customQueue.qsize())