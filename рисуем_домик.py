"""
Нарисуем домик и лужайку, а на небе солнышко и тучу,
так же подпишем автора. Выполним все благодаря "черепашке"
"""
import turtle
turtle.setup(800,600) #задаем размер окна рисования

turtle.penup() #поднимаем перо

#зададим некоторые именованные переменные с координатами

#Центральная точка травы
ground_x=0
ground_y=-200

#Координаты точек для стен домика:
#левая стена
stena_doma_1_x=-300
stena_doma_1_y=-200

stena_doma_2_x=-300
stena_doma_2_y=0

#правая стена:
stena_doma_3_x=0
stena_doma_3_y=0

stena_doma_4_x=0
stena_doma_4_y=-200

#фундамент:
fundament_doma_x=-300
fundament_doma_y=-200

#крыша:
roof_x=-150
roof_y=100

#окно:
window_1_x=-150
window_1_y=-125

window_2_x=-200
window_2_y=-125

window_3_x=-200
window_3_y=-50

window_4_x=-150
window_4_y=-50

#координаты надписи:
text_x=-350
text_y=275

#далее мы будем прорисовывать землю,для этого:
turtle.goto(ground_x,ground_y) #помещаем по координатам
turtle.dot("green") #ставим точку,которая будет по центру и от которой в обе стороны нарисуем линии
turtle.pendown() #опускаем перо для того,чтобы прорисовать линию
turtle.pencolor("green") #задаем цветзеленый,т.к. трава у дома именно такого цвета
turtle.fillcolor("green") #зальем грунт зеленым в цвет травы
turtle.begin_fill()
turtle.forward(400) #от точки вправо идем на 400 пикселей (по ширине экран у нас 800 пикселей)
turtle.goto(ground_x,ground_y) #возвращаемся в центр к точке
turtle.setheading(180) #разворачиваем курсор в обратную сторону ( на 180 градусов )
turtle.forward(400) #от точки влево идем на 400 пикселей (по ширине экран у нас 800 пикселей)
turtle.setheading(270)
turtle.forward(100)
turtle.setheading(360)
turtle.forward(800)
turtle.setheading(90)
turtle.forward(100)
turtle.end_fill()

#Рисуем стены домика
#левая стена:
turtle.fillcolor("grey")
turtle.begin_fill()
turtle.goto(stena_doma_1_x,stena_doma_1_y)
turtle.pencolor("black")
turtle.dot()
turtle.goto(stena_doma_2_x,stena_doma_2_y)
turtle.dot()
#правая стена:
turtle.goto(stena_doma_3_x,stena_doma_3_y)
turtle.dot()
turtle.goto(stena_doma_4_x,stena_doma_4_y)
turtle.dot()
#фундамент дома:
turtle.goto(fundament_doma_x,fundament_doma_y)
turtle.dot()
turtle.end_fill()
#крыша дома:
turtle.penup()
turtle.goto(0,0) #возвращаем курсор на исходную нулевую позицию
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.goto(roof_x,roof_y)
turtle.goto(-300,0)
turtle.end_fill()

#рисуем дверь
turtle.penup()
turtle.goto(0,-125)
turtle.pendown()
turtle.goto(-50,-125)
turtle.goto(-50,-200)
turtle.penup()
turtle.goto(-40,-165)
turtle.pendown()
turtle.dot()

#рисуем окно:
turtle.penup()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(window_1_x,window_1_y)
turtle.pendown()
turtle.pencolor("blue")
turtle.goto(window_2_x,window_2_y)
turtle.goto(window_3_x,window_3_y)
turtle.goto(window_4_x,window_4_y)
turtle.goto(window_1_x,window_1_y)
turtle.end_fill()

#риусем небо:
turtle.bgcolor("blue")

#рисуем солнце:
turtle.penup()
turtle.goto(250,200)
turtle.pendown()
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()
#text:
turtle.penup()
turtle.goto(text_x,text_y)
turtle.pendown()
turtle.pencolor("black")
turtle.write("ЭТО ХОМКИН ДОМИК")



















turtle.done()
