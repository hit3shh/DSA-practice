# linked list :

class Node :
    data = 0
    next = None

    def __init__(self,d):
        self.data = d
    
class Solution :
    def createNode(self,d):
        newNode = Node(d)
        return newNode
    
    def addAtHead(self,head,d):
        newNode = self.createNode(d)
        if head == None :
            head = newNode
            return head
        newNode.next = head
        head = newNode
        return head
        
    def addAtTail(self,head,d):
        newNode = self.createNode(d)
        if head == None :
            head = newNode
            return head
        temp = head   # make copy of headd.. so it will not affect actual head
        while temp.next != None:
            temp = temp.next
        
        temp.next = newNode
        return head
    def addAtnth(self,head,d,n):
        newNode = self.createNode(d)
        if head == None:
            head = newNode
            return head
        temp = head
        if n == 1:
            head = self.addAtHead(head,d)
            return head
        for i in range(n-2):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        return head
    
    def printList(self,head):
        if head == None:
            print("List is Empty!")
            return
        temp=head
        while temp!=None :    # iterate until end of list.. # last node points to None 
            print(temp.data,"->",end=" ")
            temp = temp.next

    # functions to delete nodes:
    def deleteHead(self,head):
        head=head.next
        return head
    
    def deleteTail(self,head):
        if head == None:
            return
        if head.next == None :
            return None
        temp=head
        while temp.next.next != None :
            temp = temp.next
        temp.next = None
        return head

    def deleteWithData(self,head,key):   # key is used for searching
        if head == None or (head.next == None and head.data == key) :
            return None
        
        if head.data == key :
            return head.next

        prev = None 
        curr = head

        while curr != None:
            if curr.data == key :
                prev.next = curr.next     # curr ke pehle wale node ko curr ke next node se link krege
                return head
            prev = curr
            curr = curr.next
        return head    # if curr becomes None .. so return head at last
    
    def deleteWithIndex(self,head,n):
        pass# task

    def findMiddleNode(self,head):
        if head == None :
            return -1
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        if fast.next == None:
            print(slow.data)
        else:
            print(slow.data, slow.next.data)

    def reverseList()

if __name__ == "__main__" :
    s = Solution()
    head = s.createNode(10)
    head = s.addAtHead(head,5)
    head = s.addAtHead(head,1)
    head = s.addAtTail(head,20)
    head = s.addAtTail(head,30) # list till now:  1,5,10,20,30
    head = s.addAtnth(head,25,5) # head,data,position

    head = s.deleteHead(head) # delete head

    s.printList(head)
