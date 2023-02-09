import time
import random



def main():
    aa1 = 'BillyBilly'
    logg = 'log'
    log = 'log'
    zz1 = 'BillyBilly'
    password444 = open('Password for menu screen.txt', 'r')
    password = password444.read()
    password444.close()
    #startup
    while log == logg:
        print('Welcome to ZZ corperations!')
        print('---------------------------')
        print('Please enter a password to continue')
        while aa1 == zz1:
            passwordGuess = input('Enter: ')
            while passwordGuess != password:
                print('ERROR incorrect password')
                passwordGuess = input('Enter: ')
                if passwordGuess == 'ShowMeDaWay1':
                    time.sleep(2)
                    print('Oh?')
                    time.sleep(0.7)
                    print('Let me pull that up for you... sir')
                    time.sleep(2)
                    cheatr1 = 'cheat'
                    cheatr2 = 'cheat'
                    print()
                    print()
                    print('Welcome to the underground control pannel BETA')
                    print('==============================================')
                    print()
                    print('What would you like to do?')
                    print('1. View password')
                    passhax = '1'
                    aB = input('Enter: ')
                    if aB == passhax:
                        print('Alright, the password is:', password)
                        time.sleep(0.65)
                        print()
                        print()
                
            time.sleep(1.6)
            log = 'logy'
            aa1 = 'billy'
            print()


    while log != logg:
        #Welcome screen/home menu
        print('Welcome.')
        print('=========================================')
        print()
        time.sleep(0.5)
        print('What would you like to do?')
        print('1. Change password')
       # print('2. Logout')
        print('2. Do a payrate calculator')
        print('3. Color guessing game')
        print('4. Exit')
        print('5. Turtle controller')
        print('6. Count to')
        print('7. Box Company')
        print('8. Rock Paper Scissors')
        print('9. Social Credit System')
        print('10. Bomb Travel NEW')
        a = input('Enter: ')
        #selection define
        pas = '1'
        #logout = '2'
        payrate = '2'
        colorGuessr = '3'
        exiter = '4'
        turtleeb = '5'
        countTo = '6'
        BoxCompany = '7'
        RPS = '8'
        Social = '9'
        bomba = '10'
        #Change password
        if a == pas:
            print()
            passwordNEW = input('Please enter new password: ')
            passwordNEW2 = open('Password for menu screen.txt', 'w')
            passwordNEW2.write(passwordNEW)
            passwordNEW2.close()
            print('Alright!', passwordNEW, 'is the new password')
            time.sleep(0.7)
            print()
            print()
        elif a == payrate:
            print()
            print('Starting Payrate...')
            time.sleep(1)
            import payrate
        elif a == colorGuessr:
            print()
            print('Starting Color Guesser..')
            time.sleep(1)
            import Color_Guesser
        #Exit program
        elif a == exiter:
            print('Exiting program')
            time.sleep(0.75)
            exit()
        elif a == turtleeb:
            print()
            print('Starting Turtle Controller...')
            time.sleep(1)
            import turtle_controller
        elif a == countTo:
            print()
            print('Starting Count to...')
            time.sleep(1)
            import count2
        elif a == BoxCompany:
            print()
            print('Starting Box Company...')
            time.sleep(1)
            import Box_Company
        elif a == RPS:
            print()
            print('Starting Rock Paper Scissors...')
            time.sleep(1)
            import RPS
        elif a == Social:
            print()
            print('Starting Social Credit System...')
            import Social
        elif a == bomba:
            print()
            print('Starting Bomb Travel...')
            import BombTravel
        #Error trap
        else:
            print('Please enter a valid answer')
            time.sleep(1)
            print()
            print()
            print()







if __name__ == '__main__':
    main()
