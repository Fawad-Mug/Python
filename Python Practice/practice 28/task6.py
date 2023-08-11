from random import *


arr=[]
while True:
    num=randint(1,15)
    if num not in arr:
        arr.append(num)
    if len(arr)==10:
        break
print(arr)