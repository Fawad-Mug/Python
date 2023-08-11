from random import *
def main():
    rows = randint(5,8)
    print(f'Rows: {rows}')
    for i in range(rows):
        #print first lower triangular spaces
        for j in range(i):
            print (end=' ')
        print(end='|_')
        #print second upper double triangular spaces
        for j in range((rows - i) * 2 - 2):
            print(end=' ')
        #to remove one hyphen from last line, use if condition
        if i < rows - 1:
            print('_|')
        else:
            print ('|')

main()


