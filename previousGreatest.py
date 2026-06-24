'''
find previous greatest ele in lst

'''

lst = [5,7,1,2,10,9]
ans = []  
stack = []    

for i in range(0,len(lst)):
    curr = lst[i]
    while(len(stack)!=0):
        if curr < stack[-1] :
            ans.append(stack[-1])
            stack.append(curr)
            break
        stack.pop()
    if len(stack)==0:
        ans.append(-1)
        stack.append(curr)
    
print(ans)

