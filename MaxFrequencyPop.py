'''
maximun freq ele -> "pop"

'''

# create stack using class and constructor

class Stack :
    st=[]
    size = 0
    top = -1
    
    def push(self,val):
        self.st.append(val)

    def pop(self):
        dict={}  # to track freq of ele
        temp = []

        while len(self.st) != 0 :
            curr = self.st.pop()
            if curr in dict.keys():
                dict[curr] = dict[curr]+1
            else:
                dict[curr] = 1
            temp.append(curr)
        
        maxvalue = 0
        maxkey = 0
        for key in dict.keys():
            if dict[key] > maxvalue :
                maxvalue = dict[key]
                maxkey = key
        while len(temp) != 0 :
            ele = temp.pop()
            if ele != maxkey :
                self.st.append(ele)

    def display(self):
        for i in range(len(self.st)-1,-1,-1):
            print(self.st[i],end=" ")

s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.push(10)
s.push(20)
s.push(10)
s.push(20)
s.push(30)
s.push(10)

print("before pop opn:")
s.display()

print("\n\nafter pop opn:")
s.pop()
s.display()

