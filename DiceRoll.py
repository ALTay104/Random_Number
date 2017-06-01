import random

def RandomDiceRoll(n):
    b = 0
    while b < n:
        a = random.choice([1,2,3,4,5,6])
        print a
        b = b+1

def GuessNumber(n):
    flag = False
    while flag is False:
        a = random.randint(0,10)
        if n is not a:
            print ('your guess is wrong')
            if n > a:
                print ('too high: ', a)
            else:
                print ('too low', a)
        else:
            print ('your guess is correct', a)
            flag = True
