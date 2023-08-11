from random import *

# task 5
odd=[]
even=[]
count_even=count_odd=0
x=[0]*10
for i in range(10):
    x[i]=randint(20,50)
print(x)
for i in range(10):
    if x[i]%2==0:
        count_even+=1
        even.append(x[i])
    else:
        count_odd+=1
        odd.append(x[i])
print(odd, even)

if count_even < count_odd:
    for i in range(10):
        if x[i]%2 ==0:
            x[i]+=1
elif count_even > count_odd:
    for i in range(10):
        if x[i]%2 !=0:
            x[i]-=1
print(count_odd,count_even)
print(x)