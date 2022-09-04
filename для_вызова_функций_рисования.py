import turtle
import drawing_modul
# будем вызывать модули для рисования
# именованные глобальные константы:
X_BEGIN=100
Y_BEGIN=100
X_END=-50
Y_END=-84
DLINA_LINII=100
COLOR_1="red"
COLOR_2="blue"
RADIUS=75
def main_drawing():
    #нарисуем квадрат

    drawing_modul.kvadrat(X_BEGIN,Y_BEGIN,DLINA_LINII,"black")

    # нарисуем круг:

    drawing_modul.krug(X_BEGIN,Y_BEGIN,RADIUS,COLOR_1)

    #нарсуем каку-то чепуху из линий:

    drawing_modul.treygolnik(X_BEGIN,Y_BEGIN,X_END,Y_END,COLOR_2)
    drawing_modul.treygolnik(X_END, Y_END, 45,35,COLOR_2)
main_drawing()
turtle.done()
