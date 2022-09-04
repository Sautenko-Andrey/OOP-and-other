import turtle

# global constans:
TOP_POINT_X = 0
TOP_POINT_Y = 100
LEFT_POINT_X = -100
LEFT_POINT_Y = -100
RIGHT_POINT_X = 100
RIGH_POINT_Y = -100


def main_triangle():
    turtle.speed(1)
    turtle.showturtle()
    drawing_triangle(TOP_POINT_X, TOP_POINT_Y, LEFT_POINT_X, LEFT_POINT_Y, "blue")
    drawing_triangle(LEFT_POINT_X, LEFT_POINT_Y, RIGHT_POINT_X, RIGH_POINT_Y, "blue")
    drawing_triangle(RIGHT_POINT_X, RIGH_POINT_Y, TOP_POINT_X, TOP_POINT_Y, "blue")


def drawing_triangle(start_x, start_y, end_x, end_y, color):
    # задать точки начала и конца для всех вершин треугольника
    # нарисовать между ними линии
    # start_x - начало по х
    # start_y - начало по у
    # end_x - конец по х
    # end_y - конец по у

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(end_x, end_y)
    turtle.end_fill()


main_triangle()
turtle.done()
