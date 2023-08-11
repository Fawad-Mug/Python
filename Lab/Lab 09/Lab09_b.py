from random import *
def main():
    n = randint(5,8)
    print(f'N: {n}')
    for i in range(n):
        #print first lower triangular spaces
        for j in range(i):
            print (end=' ')
        print(end='*')
        #print second upper double triangular spaces
        for j in range((n - i) * 2 - 2):
            print(end=' ')
        if i < n - 1:
            print(end='*')
        # print third lower double triangular spaces
        for j in range(i * 2 - 1):
            print(end=' ')
        if i > 0 and i < n - 1:     #print third start for lines second to second last
            print(end='*')
        elif i == n - 1:            #for last line print one space before *
            print(' *')
            return
        # print fourth upper double triangular spaces
        for j in range((n - i) * 2 - 2):
            print(end=' ')
        if i < n - 1:
            print('*')
        else:
            print()

main()


