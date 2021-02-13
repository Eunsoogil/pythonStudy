from random import randint
import sys

#answer = randint(int(sys.argv[1]), int(sys.argv[2]))
answer = randint(1, 10)
while True:
    try:
        guess = int(input('guess a number 1~10  '))
        if 0 < int(guess) < 11:
            if guess == answer:
                print('all good')
                break
            else:
                print('wrong number')
        else:
            print('number!')
    except ValueError:
        print('number!')
        continue
