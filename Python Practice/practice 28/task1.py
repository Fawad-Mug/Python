from random import *
# Task 1
x=[0]*10
for i in range(10):
    x[i]=randint(20,50)
print(x)
for j in range(len(x)-1,0,-1):
    print(x[j],end=' ')