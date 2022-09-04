# В данном примере будем рисовать множество квадратов, используя
# возможности функций.

import turtle

def main_square():
    turtle.speed(5)
    drawing_square(50,50,100,"red")
    drawing_square(0, 0, 50, "green")
    drawing_square(-100, -50, 30, "black")
    drawing_square(-100, 50, 25, "yellow")

def drawing_square(x,y,distance,color):
    #Какие параметры нам необходимы для рисования квадрата?
    # 1. Координаты первой точки х и у ( левой нижней )
    # 2. Длина стороны квадрата в пикселях
    # 3. Цвет заливки квадрата

    #Отправим курсор в заданную точку по координатам:
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    #с помощью цикла нарисуем кввадрат:
    turtle.fillcolor(color)
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(distance)
        turtle.left(90)
    turtle.end_fill()

main_square()
turtle.done()