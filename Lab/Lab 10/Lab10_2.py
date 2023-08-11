from random import *

def main():
    length = 10
    first = [0] * length
    second = [0] * length
    third = [0] * length
    for i in range(length):
        first[i] = randint(1, 9)
        second[i] = randint(1, 9)
    score = 0
    for i in range(length):
        print (end = f'{first[i]} + {second[i]} = ')
        third[i] = int(input())
        if first[i] + second[i] == third[i]:
            score += 1  
    print (f'Score {score} / 10')
    for i in range(length):
        if first[i] + second[i] != third[i]:
            print (f'{first[i]} + {second[i]} = {third[i]}\t{first[i]} + {second[i]} = {first[i] + second[i]}')

main()