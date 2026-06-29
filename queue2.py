'''
Implement QUEUE :  using 2 stacks

'''

class Node:
    data = 0 
    next = None

    def __init__(self,val):
        self.data = val

class Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,val):
        self.stack1.append(val)

    def dequeue(self):
        if self.isempty():
            return "queue is empty.."
        if not self.stack2 :
            while self.stack1 :
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
    
    def front(self):
        if self.isempty():
           return "queue is empty.."
        if not self.stack2 :
            while self.stack1 :
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def isempty(self):
        return len(self.stack1)==0 and len(self.stack2)==0 
    
