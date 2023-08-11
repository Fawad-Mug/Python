from random import *
def main():
    rows = randint(3,6)
    columns = randint(3,8)
    print(f'Rows: {rows}')
    print(f'Columns: {columns}')
    i = 1
    while i <= rows:
        j = 1
        while j <= columns:
            print(end='* ')
            j = j + 1
        print('>')
        i = i + 1

main()

