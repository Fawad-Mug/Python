from random import*
li=[0]*10
for i in range (10):
    li[i]=randint(3,7)
print(li)
for i in range (len(li)):
    j=0
    while j<=i:
        print(li[j],end=' ')
        j+=1
    print()