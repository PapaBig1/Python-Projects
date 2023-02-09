import random
import time
#x = 0.005
#x = 0

#DEFINE VALUES
i = 0
j = 50
p = 0
g = 1
n = 0
d = 1

#CHOOSE MODE
question = print('1. Record mode\n2. Free mode')
question2 = input('Enter: ')
print()


if question2 == '2':

    #GET SPEED
    x = float(input('Enter speed 0 is FAST: '))
    start = input('Enter to start: ')


    #LOOP WAVE
    while p == 0:
        while g == 1:
            time.sleep(x)
            c = '0' * i
            c2 = '0' * j
            
            print('0' * i, '♣♣♣♣♣', '0' * j)
            #wave.write(f'{c}XXXXX{c2}')
            print('0' * j, '♣♣♣♣♣', '0' * i)
            i += 1
            j -= 1
            if j <= 0:
                g = 0
                n = 1
        while n == 1:
            time.sleep(x)
            print('0' * i, '♣♣♣♣♣', '0' * j)
            print('0' * j, '♣♣♣♣♣', '0' * i)
            i -= 1
            j += 1
            if i <= 0:
                n = 0
                g = 1

elif question2 == '1':

    start = input('Enter to start: ')
    x = 0


    #CREATE WAVE FILE
    wave = open("wave.txt", "w")
    for o in range(7):
        i = 0
        j = 50
        while g == 1:
            time.sleep(x)
            c = '.' * i
            c2 = '.' * j
            
            print('.' * i, 'XXXXX', '.' * j)
            wave.write(f'{c}XXXXX{c2}')
            wave.write('\n')
            print('.' * j, 'XXXXX', '.' * i)
            wave.write(f'{c2}XXXXX{c}')
            wave.write('\n')
            i += 1
            j -= 1
            if j <= 0:
                g = 0
                n = 1
        while n == 1:
            time.sleep(x)
            print('.' * i, 'XXXXX', '.' * j)
            wave.write(f'{c}XXXXX{c2}')
            wave.write('\n')
            print('.' * j, 'XXXXX', '.' * i)
            wave.write(f'{c2}XXXXX{c}')
            wave.write('\n')
            i -= 1
            j += 1
            if i <= 0:
                n = 0
                g = 1
        o += 1
    for bbb in range(100):
        G = 'X' * 215
        print(G)
        wave.write(G)
        wave.write('\n')
    wave.close()
