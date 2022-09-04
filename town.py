import turtle
import random
def main_town():
    turtle.speed(9)
    contur_neba_i_zvezdi()
    contur_zdaniya()
    okna()
    turtle.hideturtle()
########################
def contur_zdaniya():
    # нарисуем контуры здания:
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-340,-70)
    turtle.pendown()
    turtle.fillcolor("grey")
    turtle.begin_fill()
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(700)
    turtle.right(90)
    turtle.forward(850)
    turtle.end_fill()
########################
def okna():
    base_x=50
    base_y=-75
    square=30
    ugol=90
    # 1 window
    turtle.penup()
    turtle.home()
    turtle.goto(base_x,base_y)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(square)
        turtle.left(ugol)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    # 2 window:
    turtle.goto(base_x-170, base_y+200)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(square)
        turtle.left(ugol)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    # 3 window:
    turtle.goto(base_x - 230, base_y + 200)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(square)
        turtle.left(ugol)
    turtle.end_fill()
    turtle.penup()
    turtle.home()

    # 4 window:
    turtle.goto(base_x - 230, base_y - 120)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(square)
        turtle.left(ugol)
    turtle.end_fill()
    turtle.penup()
    turtle.home()

    # 5 window:
    turtle.goto(base_x +80, base_y +120)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(square)
        turtle.left(ugol)
    turtle.end_fill()
    turtle.penup()
    turtle.home()

    # 6 window:
    turtle.goto(base_x -10, base_y + 120)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(square)
        turtle.left(ugol)
    turtle.end_fill()
    turtle.penup()
    turtle.home()

    # 7 window:
    turtle.goto(base_x +75, base_y -90)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(square)
        turtle.left(ugol)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
########################
def contur_neba_i_zvezdi():
    turtle.bgcolor("black")
    zvezdi = random.randint(75, 100)
    for i in range(zvezdi):
        random_x=random.randint(-400,400)          # попытка рандомно разбрасывать звезды по рандомным координатам
        random_y = random.randint(0,400)
        turtle.goto(random_x,random_y)
        turtle.dot(6,"white")
########################


main_town()
turtle.done()
