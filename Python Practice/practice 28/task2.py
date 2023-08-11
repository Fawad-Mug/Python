from random import *

# Task 2
x=[0]*10
sum=0
for i in range(10):
    x[i]=randint(20,50)
    sum+=x[i]
print(x)
print(sum)
