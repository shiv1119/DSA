class Queue:
    def __init__(self):
        self.items = []
            
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "Element is inserted at last of the queue."
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the queue."
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the queue."
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None
        
    
    

customQueue = Queue()
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
# print(customQueue.dequeue())
# print(customQueue.peek())
customQueue.delete()

    