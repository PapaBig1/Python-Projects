import time
def payrate2():
    print('alright! Booting calculator...')
    time.sleep(1)
    print()
    print('Welcome to ZZ corperations payrate calculator!')
    print('----------------------------------------------')
    time.sleep(0.5)
    a3 = 'a3'
    aa3 = 'a3'
    while a3 == aa3:
        print('1.Gross\n2.Back')
        gross = '1'
        finda3 = '2'
                
        b = input('Enter: ')
        if b == gross:
            hour = float(input('Please enter your hourly wage: '))
            week = float(input('Please enter your hours per week: '))
            print()
            print('Alright your gross pay is $',hour * week)
            print()
        elif b == finda3:
            print('Exiting calculator...')
            time.sleep(1)
            print()
            a3 = 'HAAAAA'
        else:
            print('Please enter a valid choice')
            print()
            print()
payrate2()
