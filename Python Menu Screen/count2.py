import time
def count2():
    print('Starting counter...')
    time.sleep(1.2)
    countA = 'yes'
    countB = 'yes'
    print()
    print()
    print('Welcome to the counting machine!')
    print('================================')
    while countA == countB:
        print('To make it count, start by typing in the starting number.\nThen type in the number to count to.')
        count1 = int(input('Enter starting number: '))
        count2 = int(input('Enter number to count to: '))
        print('Counting...')
        time.sleep(1)
        while count1 < count2:
            count1 += 1
            print(count1)
        while count1 > count2:
            count1 -= 1
            print(count1)
        print()
        print('Done. It has reached', count2)
        print('Would you like to count again?\n1. Yes\n2. No')
        countAnswer = input('Enter: ')
        if countAnswer == '2':
            countA = 'no'
            print('Exiting counter...')
            time.sleep(1)
            print()
            print()
        else:
            print('Ok')

count2()
