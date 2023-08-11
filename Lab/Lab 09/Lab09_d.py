from random import *
def main():
    rows = randint(5,8)
    print(f'Rows: {rows}')
    for i in range(1, rows+1):
        for j in range(rows - i):
            print (end=' ')
        for j in range(i, 1, -1):
            print(j, end='')
        for j in range(1, i+1):
            print(j, end='')
        print ()

main()


