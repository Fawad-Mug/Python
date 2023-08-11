'''
x=int(input())
if x>=1 and x<=100:
    if x==2:
        print('No')
    elif x%2==0:
        print('YES')
    else:
        print('NO')


#z='A'
x=int(input())
if x>=1 and x<=100:
    for i in range(x):
        y=input()
        print(y)

c=0
x=int(input())
if x>=1 and x<=1000:
    for i in range (x):
        petya=int(input())
        vasya=int(input())
        tonya=int(input())
        print(petya , vasya , tonya)
        if (petya and vasya) == 1 or (petya and tonya) == 1 or (vasya and tonya) == 1:
            c+=1
print(c)


x=input()
sen= [0]
for i in list(x):
    if x[i]!= sen:
        for j in list(x):
            x[i]=sen
            print(x,end='') 
            c+=1
            print(c)

print(f)
if c %2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

''' 
x=int(input())
if x>1:
    while x>=1:
        print(x,end=' ')
        x=x-1
elif x==1:
        print('-1')


