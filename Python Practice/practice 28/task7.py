from random import *

# #task 7
arr=[0]*10
for i in range(10):
    arr[i]=randint(1,5)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print(i,j)
print(arr)