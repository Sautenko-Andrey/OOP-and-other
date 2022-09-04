import turtle

DLINNA = int(input("Введи длину прямоугольника: "))
START_X = -100
START_Y = 0


def main_uzor():
    turtle.speed(1)
    for i in range(4):
        turtle.showturtle()
        turtle.goto(START_X, START_Y)
        big_square(DLINNA)
        small_square(DLINNA - DLINNA/5 )
        black_square(DLINNA - DLINNA/2 )
        diagonals((DLINNA ** 2 + DLINNA ** 2) ** 0.5)


def big_square(distance):
    for i in range(4):
        turtle.forward(distance)
        turtle.left(90)


def small_square(distance):
    for i in range(4):
        turtle.forward(distance)
        turtle.left(90)


def black_square(distance):
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(distance)
        turtle.left(90)
    turtle.end_fill()


def diagonals(distance):
    turtle.left(45)
    turtle.forward(distance)
    turtle.back(distance)
    turtle.left(45)


main_uzor()
turtle.done()
