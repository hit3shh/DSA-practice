'''
there are n seats in a row, represented as an array of 0s and 1s ( 0 = empty, 1 = booked).
you need to find the longest stretch of consecutive empty seats(0s), so that a large family can sit together.

input-   seats = [1,0,0,0,1,0,0]
output-  3

'''

lst = eval(input())
max,count = 0,0

for i in lst :
    if i == 0 :
        count += 1
    else: 
        if count > max :
            max = count
        count = 0
if count > max :
    max = count

print(max)



