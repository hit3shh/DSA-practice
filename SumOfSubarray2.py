'''
find the longest subarray with sum=k

'''


lst = eval(input())
k = int(input())
l=0
max=0
sum=0

for r in range(len(lst)):   # iterate from 0 to last index of list :
    sum += lst[r]
    if sum == k and r-l+1 > max :
        max = r-l+1
    while sum>k :
        sum -= lst[l]
        l += 1

print(max)

