import random
import time

def colorguess():
    #hi
    print()
    a4 = 'a4'
    aa4 = 'a4'
    while a4 == aa4:
        print('Alright... randomizing colors')
        time.sleep(1.5)
        colorAnswerStart = ['red','orange','yellow','green','blue','purple']
        ColorYESYES = random.choice(colorAnswerStart)
     #   yellow = '1'
     #   red = '2'
    #    blue = '3'
        colorGuess = input("Guess a color (HINT: it's in the rainbow): ")
        if colorGuess == ColorYESYES:
            print()
            print('You got it!')
            print()
        else:
            print()
            print(f'Sorry, it was {ColorYESYES}')
            print()
            time.sleep(0.5)
            print('Would you like to try again?')
            print('1. Yes\n2. No/Back')
            c = input('Enter: ')
            if c == '1':
                print('Great!')
                print()
                print()
            else:
                print('Exiting Color Guesser...')
                print()
                print()
                print()
                a4 = 'NOPE'
colorguess()
