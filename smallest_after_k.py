'''
str = "759816283"
k=3

Q- remove ele k times.. such that value in str becomes minimum..  do not change order of numbers in str

sol-  remove 7,9,8   -> str = "516283"

'''

str = "759816283"
k=3

stack = []  
result = ""   

stack.append(str[0])   # push 1st num of str into stack

for i in range(1,len(str)):   # traverse str from 2nd num 
    while k>0 and len(stack)!=0 and ord(stack[-1])-ord('0') >= ord(str[i])-ord('0'):     # untill stack becomes empty
    # st.code of top - st.code of '0' = we get number  # comprare top of stack with next num 
            stack.pop()
            k-=1       # decrease chances of remove
    stack.append(str[i])

for i in range(len(stack)-1,-1,-1):
    result = stack[i] + result  # automaticlly reversed str..  # num added before result..

print(result)

