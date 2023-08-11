from random import * 
# task 9
li=[0]*20
li2=[]
for i in range(20):
    li[i]=randint(0,9)
li2.append(li[0])
li2.append(li[1])
for i in range(2,len(li)-2):
    avg=(li[i-1]+li[i-2]+li[i+1]+li[i+2])//4
    li2.append(avg)
li2.append(li[18])
li2.append(li[19])
print(li)
print(li2)