'''
find max no of cars passed in any k consecutive minutes

input-  cars= [4,8,15,3,10,12,5,9]   k=3
output-  28  (15+3+10)

'''

lst = eval(input("enter list: "))
k = int(input("enter k: "))
sum,max = 0,0

for ele in range(k):
    sum += lst[ele]

if sum>max:
    max=sum

for i in range(k,len(lst)):   #  when i=3 we have to remove 0 :
    sum -= lst[i-k]
    sum += lst[i]

    # also check if new sum > max or not :
    if sum > max :
        max = sum

print(max)

