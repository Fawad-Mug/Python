from random import *
def main():
    rows = randint(3, 6)
    columns = randint(3, 8)
    print(f'Rows: {rows}')
    print(f'Columns: {columns}')
    step = 1
    for i in range(rows):
        sum = 0
        k = 1
        for j in range(1, columns + 1):
            print(k, end='')
            if j < columns:
                print (end='+')
            sum = sum + k
            k = k + step
        print(f'={sum}')
        step += 1

main()


