# В данном модуле напишем несколько функций для рисования различных фигур

import turtle


# первая функция будет рисовать квадрат:
# что нам нужно:
# координаты первой точки квадрата х и у (левой нижней)
# длина линии квадрата
# цвет заливки
def kvadrat(x, y, length, color):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for line in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()




# функция рисует круг:
def krug(x, y, radius, color):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# функция,рисующая треугольник:
def treygolnik(x_start, y_start, x_end, y_end, color):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x_end, y_end)
    turtle.end_fill()



