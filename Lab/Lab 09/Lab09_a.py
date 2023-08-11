from random import *
def main():
    rows = randint(3,6)
    print(f'Rows: {rows}')
    letter = ord('A')
    for i in range(rows):
        for j in range(1, rows+1):
            print(chr(letter), end=' ')
            for k in range(1, j+1):
                print (k, end=' ')
            letter = letter + 1
        print()
Rows: 5

main()


