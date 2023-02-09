def main():
    file2search = input('Enter file name and type: ')
    file = open (f'{file2search}.txt','r')
    file2 = file.readlines()
    end444 = 'x'
    while end444 != 'q':
        x = 0
        findr = input('Enter item you would like to find: ')
        for findrz in file2:
            if findr in findrz:
                x += 1
        print(f'{findr} was found {x} time(s)')

        end444 = input('Press q to exit: ')

if __name__ == '__main__':
    main()
