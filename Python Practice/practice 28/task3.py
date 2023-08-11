from random import *


# Task3
x=[0]*10
for i in range(10):
    x[i]=randint(20,50)
print(x)
li=[x[i] for i in range(10)]
print(li)