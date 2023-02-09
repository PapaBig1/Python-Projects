import time
def turtlecontroller():
    print('Starting Turtle Controller...')
    import turtle
    time.sleep(2)
    ssd = turtle.getscreen()
    turtlee = turtle.Turtle()
    print()
    print()
    print('Welcome to the ZZ corperations Turtle Controller (or ZZTC)')
    print('==========================================================')
    print()
    print('To control the turtle, please enter W, A, S, or D.\nYou may also enter in special commands listed on the screen')
    print('1. Draw a polygon\n2. Change line color\n3. Draw a circle\n4. Exit')
    aaa = 'a'
    zzz = 'a'
    poly = '1'
    lineColorT = '2'
    circle = '3'
    baxback = '4'
    while aaa == zzz:
        w = 'w'
        a = 'a'
        s = 's'
        d = 'd'
        g = input('Enter: ')
        if g == w:
            turtle.forward(50)
        elif g == d:
            turtle.right(90)
        elif g == s:
            turtle.backward(50)
        elif g == a:
            turtle.left(90)
        elif g == poly:
            print('Coming soon!')
        elif g == lineColorT:
            colorForT = input('Enter color: ')
            turtle.pencolor(colorForT)
        elif g == circle:
            circlesize = int(input('Enter circle size: '))
            turtle.circle(circlesize)
        elif g == baxback:
            print('Exiting Turtle Controller...')
            aaa = 'g'
            turtle.bye()
            time.sleep(1.1)
            print()
            print()
        else:
            print('ERROR, please enter a valid command.')

turtlecontroller()
