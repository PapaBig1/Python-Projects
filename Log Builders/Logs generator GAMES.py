import random
import time
#class Default:
    #def __init__(self,name,game,phone):
        #self.name = name
        #self.game = game


with open("names.txt", "r") as file:
    allText = file.read()
    file.close()
    names = list(map(str, allText.split()))

with open("games.txt", "r") as file2:
    allText2 = file2.read()
    file2.close()
    game2 = list(map(str, allText2.split()))

num1list = range(100,999)
num2list = range(1000,9999)

#Main log file


log = open('gameLogs.txt','a')

amount = int(input('Enter amount of numbers: '))

for x in range(amount):
    num1 = random.choice(num1list)
    num2 = random.choice(num2list)
    name = random.choice(names)
    game = random.choice(game2)

    print()
    print('=' * 35)
    print(f'Name: {name}\nGame purchased: {game}\nPhone number: (402){num1}-{num2}')
    log.write('.\n')
    log.write('=' * 35)
    log.write('.\n')
    log.write(f'Name: {name}\nGame purchased: {game}\nPhone number: (402){num1}-{num2}\n')
    log.write('=' * 35)
    print('=' * 35)
        
    #print(f'{name}  (402){num1}-{num2}')

print('Done!')
edd = input('Enter: ')
log.close()



#p1 = Default("John", 36, 50)

#print(p1.name)
#print(p1.game)
