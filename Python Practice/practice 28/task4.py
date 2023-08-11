from random import *

# Task 4
li1=[0]*5
li2=[0]*5
li3=[]
for i in range(5):
    li1[i]=randint(20,50)
    li2[i]=randint(20,50)
for i in range(5):
    for j in range(4):
        if li1[j]>li1[j+1]:
            li1[j],li1[j+1]=li1[j+1],li1[j]
        if li2[j]>li2[j+1]:
            li2[j],li2[j+1]=li2[j+1],li2[j]
print(f'sorted list1 : {li1}')
print(f'sorted list 2 : {li2}')
for i in range(5):
    li3.append(li2[i])
for i in range(5):
    li3.append(li1[i])
print(li3)
for j in range(10):
    for i in range(9):
        if li3[i]>li3[i+1]:
            li3[i],li3[i+1]=li3[i+1],li3[i]
print(li3)