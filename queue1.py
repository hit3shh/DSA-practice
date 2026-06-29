'''
implement QUEUE : using linkedlist
 
'''
class Node:
        data = 0
        next = None
        
        def __init__(self,val):
            self.data = val

class Queue :
    size = 0
    front , rear = None , None

    def enqueue(self,val):
        newnode = Node(val)

        if self.rear == None:
            self.rear = newnode
            self.front = newnode
            self.size += 1
            return
        self.rear.next = newnode
        self.rear = newnode
        #to maintain size of queue while enqueue  ele
        self.size += 1

    def dequeue(self):
        if self.front == None :
            return -1
        val = self.front.data
        self.front = self.front.next
        # to maintain size while dequeue ele
        self.size -= 1

        return val

    def peek(self):
        if self.front == None :
            return -1
        return self.front.data

    def contains(self,key):
        if self.front == None :
            return False
        
        temp = self.front
        while temp != None :
            if temp.data == key :
                return True
            temp = temp.next
        return False
    
    def reverse(self):
        self.rear = self.front
        prev = None
        curr = self.front

        while curr != None :
            agla = curr.next
            curr.next = prev
            prev = curr
            curr = agla

        self.front = prev

    def display(self):
        if self.front == None :
            return
        temp = self.front
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    que = Queue()
    que.enqueue(10)
    que.enqueue(20)
    que.enqueue(30)
    que.enqueue(40)
    que.enqueue(50)
    que.enqueue(60)

    que.display()

    print("\n")

    que.dequeue()
    que.display()

    print("\n")

    print(que.peek())

    que.reverse()
    que.display()

    print("\n")
    que.enqueue(80)
    que.display()