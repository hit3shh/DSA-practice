'''
implement merge sort or lst=[5,7,2,6,9,3,1]

divide-----
5726931
5726   931
57  26       93  1
5 7  2 6    9 3  1
--------------------------
conqure/merge -----
5 7  2 6    9 3  1
57  26    39  1
2567   139
1235679
----------------------

sorted arr-  [1,2,3,5,6,7,9]

'''

def mergesort(lst,p,r):   # accept lst-arr tobe sorted, p-leftmost index,  r-rightmost index   # divide arr
    if p<r:
        q = (p+r)//2   # mid index
        mergesort(lst,p,q)
        mergesort(lst,q+1,r)
        merge(lst,p,q,r)

def merge(lst,p,q,r):
    left = []
    right = []

    for i in range(p,q+1):
        left.append(lst[i])
    for j in range(q+1,r+1):
        right.append(lst[j])

    n1 = q-p+1
    n2 = r-q

    i,j,k = 0,0,p

    while i<n1 and j<n2 :
        if left[i]<=right[j]:
            lst[k] = left[i]
            i+=1
        else:
            lst[k] = right[j]
            j+=1
        k+=1
    while i<n1 :
        lst[k] = left[i]
        k+=1
        i+=1
    while j<n2 :
        lst[k] = right[j]
        k+=1
        j+=1


lst=[5,7,2,6,9,3,1]
print("lit: ",lst)
mergesort(lst,0,len(lst)-1)

print("sorted list: ",lst)

