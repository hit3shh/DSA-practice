'''
find next greatest element in arr
arr = [5,7,1,2,10,9]
return = [7,10,2,10,-1,-1] 


# min element->  pop
# max ele -> push

'''

arr = [5,7,1,2,10,9]
ans = []  
stack = []    

for i in range(len(arr)-1 , -1,-1):
    while(len(stack)!=0):    # untill stack becomes empty
        current = arr[i]
        if current < stack[-1] :
            ans.append(stack[-1])  
            stack.append(current)
            break
        stack.pop()
    if len(stack)==0:
        ans.append(-1)
        stack.append(arr[i])

ans.reverse()
print(ans)

    