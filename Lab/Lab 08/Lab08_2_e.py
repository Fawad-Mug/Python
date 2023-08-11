from random import *
def main():
    rows = randint(3,6)
    i = 0
    while i < rows:     #for ease, I have started i with 0 and replace <= with < operator
        sum = 0
        j = 1
        while j <= 5 + i:
            print(j, end=' ')
            sum = sum + j
            j = j + 1
        print(f' = {sum}')
        i = i + 1
main()

