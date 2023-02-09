import random
import time
start = input('Press Enter to begin the code: ')
num1 = (0.1, 0.2, 0.3)
code1 = range(2, 100)
x = 0
codezs = open('my fake execution code.txt','w')
for zz in range(1000):
    num2 = random.choice(num1)
    code = random.choice(code1)
    print('=' * code)
    codezs.write('\n.')
    codezs.write('=' * code)
    time.sleep(num2)
codezs.close()
