from random import*
row=col=10
x=[[randint(0,9) for j in range (col)]for i in range (row)]
 
for i in range (col):
    for j in range (row):
        if x[i][j]==0:
            x[i][j]=1
        print(x[i][j],end=' ')
    print()