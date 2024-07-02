# kth Smallest Element in an Array

arr = [1, 3, 2, 1, 4, 2, 5, 6, 3, 3, 4]
k = 4

arr.sort()

i = 0
count = 0

while i < len(arr):
    
    while i<len(arr)-1 and arr[i]==arr[i+1]:
        i+=1
    
    k-=1
    
    if k == 0:
        break
    
    i+=1

print( arr[i] )