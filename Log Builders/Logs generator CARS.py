import random
import time
#class Default:
    #def __init__(self,name,game,phone):
        #self.name = name
        #self.game = game

xwb = 0

with open("names.txt", "r") as file:
    allText = file.read()
    file.close()
    names = list(map(str, allText.split()))

with open("cars.txt", "r") as file2:
    allText2 = file2.read()
    file2.close()
    car2 = list(map(str, allText2.split()))

with open("colors.txt", "r") as file3:
    allText3 = file3.read()
    file3.close()
    color2 = list(map(str, allText3.split()))

with open("styles.txt", "r") as file4:
    allText4 = file4.read()
    file4.close()
    style2 = list(map(str, allText4.split()))

num1list = range(100,999)
num2list = range(1000,9999)

#Main log file


log = open('CarLogs.txt','a')

amount = int(input('Enter amount of numbers: '))

for x in range(amount):
    xwb += 1
    num1 = random.choice(num1list)
    num2 = random.choice(num2list)
    name = random.choice(names)
    car = random.choice(car2)
    color = random.choice(color2)
    style = random.choice(style2)

    print()
    print('=' * 35)
    print(f'ORDER NUMBER #{xwb}\nName: {name}\nCar purchased: {car}\nType: {style}\nColor chosen: {color}\nPhone number: (402){num1}-{num2}')
    log.write('.\n')
    log.write('=' * 35)
    log.write('.\n')
    log.write(f'ORDER NUMBER #{xwb}\nName: {name}\nCar purchased: {car}\nType: {style}\nColor chosen: {color}\nPhone number: (402){num1}-{num2}')
    log.write('.\n')
    log.write('=' * 35)
    print('=' * 35)
        
    #print(f'{name}  (402){num1}-{num2}')

print('Done!')
edd = input('Enter: ')
log.close()



#p1 = Default("John", 36, 50)

#print(p1.name)
#print(p1.game)
