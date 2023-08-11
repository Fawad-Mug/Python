from random import*
x=[0]*20
x[0]=randint(1,20)
for i in range (1,20):
    s=randint(1,4)
    x[i]=x[i-1]+s
for i in range (len(x)):
    print(x[i],end=' ')
print()
m=[]
for i in range (len(x)-1):
    while x[i]!=x[i+1]-1:
        x[i]+=1
        m.append(x[i])
for i in range (len(m)):
    print(m[i],end=' ') 

