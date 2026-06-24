# linked list is created using multiple functions :

class Node :
    data = 0
    next = None

    def __init__(self,d):
        self.data = d

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print(head.next.data)


