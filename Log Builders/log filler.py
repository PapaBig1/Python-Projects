#Created by Zachary Post 8/9/2022
import random
def main():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    error_block = 1
    y = 1000000
    while error_block == 1:
        try:
            times = int(input('Enter amount of times: '))
        except ValueError as error:
            print('ERROR please enter a valid interger')
        else:
            error_block = 0
    name = input('Enter new text files name: ')
    file = open (f'{name}.txt','w')
    for x in range(times):
        s = random.choice(letters * 100)
        if times >= 1000000:
            if x == y:
                print(x)
                y += 1000000
        file.write(s)
    file.close()
    print(f'Done! Your file has been created with {times} random letters.')
    done = input('Enter to exit: ')


if __name__ == '__main__':
    main()
