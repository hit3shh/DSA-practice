'''
# Stock span problem

find all previous small and eual ele in lst:
return-> num of elements

lst = [100,80,60,70,60,75,85]
ans = [1,1,1,2,2,4,6]

'''

lst = [100,80,60,70,60,75,85]
stack = []
ans = []

for i in range(0,len(lst)):
    temp=[]   # stores popped ele
    curr = lst[i]
    count = 1
    while len(stack) != 0 :
        
        if curr >= stack[-1]:
            count+=1
            temp.append(stack.pop())   # pop ele and push into temp 
        else:
             break
    
    ans.append(count)
    stack.append(curr)
    temp.reverse()
    stack.extend(temp)

print(ans)
