import turtle
SIZE = int(input("Введи размер квадратика доски: "))
def main_doska():
    turtle.speed(9)
    turtle.penup()
    turtle.goto(-125, 0)
    turtle.pendown()
    for j in range(2):
        for i in range(2):
            kvadrat_vertikal_black(SIZE)
            turtle.forward(SIZE)
            kvadrat_vertikal_white(SIZE)
            turtle.forward(SIZE)
        kvadrat_vertikal_black(SIZE)
        turtle.back(4 * SIZE)
        turtle.right(90)
        turtle.penup()
        turtle.forward(SIZE)
        turtle.left(90)
        turtle.pendown()
        # меняем белые на черные:
        for i in range(2):
            kvadrat_vertikal_white(SIZE)
            turtle.forward(SIZE)
            kvadrat_vertikal_black(SIZE)
            turtle.forward(SIZE)
        kvadrat_vertikal_white(SIZE)
        turtle.back(4 * SIZE)
        turtle.right(90)
        turtle.penup()
        turtle.forward(SIZE)
        turtle.left(90)
        turtle.pendown()
    # дорисовываем недостающую строку:
    for k in range(2):
        kvadrat_vertikal_black(SIZE)
        turtle.forward(SIZE)
        kvadrat_vertikal_white(SIZE)
        turtle.forward(SIZE)
    kvadrat_vertikal_black(SIZE)
    turtle.hideturtle()


def kvadrat_vertikal_black(distance):
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(distance)
        turtle.left(90)
    turtle.end_fill()


def kvadrat_vertikal_white(distance):
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(distance)
        turtle.left(90)
    turtle.end_fill()


main_doska()
turtle.done()
