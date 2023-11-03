# pop()-remove last and return
# push()-push value in stack
# peek() - return peak element but peak element is not removed
# isEmpty() - return true or false, used to check weather stack is empty or it contain element
# isFull() - used to check tht stack is full or not, returns true or false
# delete() - used to delete entire stack 


"""stack
1- using list - easy to implement but speed probem when it grows
2 - using linked list - fast performence,implementation is not easy
"""

class Stack:
    def __init__(self):
        self.list = [] #o(1) - time
        
    def __str__(self):
        velues = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isempty(self):
        if self.list == []:
            return True
        else:
           return False
            
    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted."
    def pop(self):
        if self.isempty():
            return "There is no element in stack"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isempty():
            return "There is no element in stack"
        else:
            return self.list[len(self.list)-1] #O(1)
    def delete(self):
        self.list = None
        
        
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack.pop())
# print(customStack.peek())
customStack.delete()
print(customStack)