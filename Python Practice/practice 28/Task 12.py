from random import*
sum=0
li=[0]*10
for i in range (10):
    li[i]=randint(3,7)
print(li)
for i in range (len(li)):
    j=0
    sum=0
    while j<=i:
        sum+=li[j]
        print(li[j],end=' ')
        j+=1
    print(' = ',sum)