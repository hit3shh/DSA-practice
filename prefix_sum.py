# prefix sum + hashing
'''
find the length of the largest subarray : sum of subarray == k .. 
input:   arr=[1,2,3,-2,5],  k=5

'''

'''
sum(0-4) - sum(0-1) = sum(2-4)

'''
# 1,2,3,-2,5    k=5

# {sum:index   1:0, 3:1, 6:2, 4:3, 9:4}   
# we can find remaining sum of subarray index wise.. means at index 0 we need 4 more(5-1  : k-sum(0)) to meet required sum
# similarily..  at index 1.. we need 2 more (5-3 ) to meet required sum
# we can find if requred sum exist in prefix-sum or not.. if it exist.. wwe can calculate subarray..


lst = eval(input())   # input array
k = int(input())      # input k # to find sum of subarray == k

sum,max,l = 0,0,0  # to store sum
dict = {}  # to store sum index-wise..

# arr = [1,2,3,-2,5]

for i in range(len(lst)):
    sum += lst[i]   # this will  ends at sum of whole array
    if dict.get(sum-k)!=None :
        l = i - dict.get(sum-k)
        
        if max<l :
            max = l
        
    dict[sum]=i  # to add into dict

print(max)


# time complexity:  O(1) :   we traverse each element only once


