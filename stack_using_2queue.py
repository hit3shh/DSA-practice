class StackUsingTwoQueues:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, val):
        self.q2.append(val)

        while len(self.q1) > 0:           # Move all elements from q1 to q2
            self.q2.append(self.q1.pop(0))

        self.q1, self.q2 = self.q2, self.q1         # swap queues so q1 holds ele of stack

    def pop(self):
        return self.q1.pop(0)

    def top(self):
        return self.q1[0]

    def is_empty(self):
        return len(self.q1) == 0

stack = StackUsingTwoQueues()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)

print(stack.top())       
print(stack.pop())    
print(stack.pop())    
print(stack.pop())    
print(stack.top())    
print(stack.is_empty())  
