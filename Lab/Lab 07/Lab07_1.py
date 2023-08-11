from random import *

def main():
    i = 1
    score = 0
    while i <= 10:
        choice = randint(1, 3)
        if choice == 1:                         #addition
            print (f'{i}. Addition')
            n1 = randint(0, 99)
            n2 = randint(0, 99)
            print (f'N1: {n1}\tN2: {n2}\nAnswer :', end='')
            res = int (input ())
            if res == n1 + n2:
                score = score + 1
        elif choice == 2:                       #subtraction
            print (f'{i}. Subtraction')
            n1 = randint(10, 99)
            n2 = randint(0, n1-1)
            print (f'N1: {n1}\tN2: {n2}\nAnswer :', end='')
            res = int (input ())
            if res == n1 - n2:
                score = score + 1
        else:                                   #product
            print (f'{i}. Product')
            n1 = randint(0, 9)
            n2 = randint(0, 9)
            print (f'N1: {n1}\tN2: {n2}\nAnswer :', end='')
            res = int (input ())
            if res == n1 * n2:
                score = score + 1
        i = i + 1
    print ('Total Score: ', score)

main()