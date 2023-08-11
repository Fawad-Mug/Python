from random import*
row=col=10
x=[[randint(0,9) for j in range (col)]for i in range (row)]
 
for i in range (col):
    for j in range (row):
        print(x[i][j],end=' ')
        
    print()
for i in range (col):
    j=0
    while j <i:
         print(end='  ')
         j+=1
    print(x[i][i])