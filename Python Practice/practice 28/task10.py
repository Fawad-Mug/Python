from random import *
# Task 10 
li=[0]*10
for i in range(10):
    li[i]=randint(3,7)
for i in range(len(li)):
    for j in range(li[i]):
        print(f'*',end=' ')
    print()