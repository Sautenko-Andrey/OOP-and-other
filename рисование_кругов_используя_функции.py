import turtle


def main_circle():
    turtle.speed(8)
    drawing_circle(0, 0, 75, "black")
    drawing_circle(0, 0, 65, "white")
    drawing_circle(0, 0, 55, "red")
    drawing_circle(0, 0, 45, "white")
    drawing_circle(0, 0, 35, "blue")
    drawing_circle(0, 0, 25, "white")
    drawing_circle(0, 0, 15, "orange")
    drawing_circle(0, 0, 5, "white")

def drawing_circle(x, y, radius, color):
    # Необходимые параметры для рисования круга:
    # 1.Координаты х и у для позиционирования круга
    # 2.Радиус круга
    # 3.Цвет заливки

    # рисуем круг:
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x, y-radius) # ЦЕНТРУЕТ КРУГ!!!!!
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


main_circle()
turtle.done()
