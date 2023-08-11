from random import*
row=col=10
x=[[randint(0,9) for j in range (col)]for i in range (row)]
for i in range (row):
    for j in range (col):
        if x[i][j]==0:
            print(f'{i} {j}')