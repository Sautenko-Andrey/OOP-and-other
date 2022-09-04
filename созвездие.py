#Эта программа рисует звезды созвездия Ореона
#Пишет названия звезд и рисует линии созвездия
import turtle
turtle.setup(500,600)  #задаем размер окна для рисования

turtle.penup() #поднимаем перо
turtle.hideturtle() #прячем иконку черепашки

#Создаем именнованные константы для каждой звезды с координатами
left_shoulder_x=-70
left_shoulder_y=200

right_shoulder_x=80
right_shoulder_y=180

left_beltstar_x=-40
left_beltstar_y=-20

middle_beltstar_x=0
middle_beltstar_y=0

right_beltstar_x=40
right_beltstar_y=20

left_knee_x=-90
left_knee_y=-180

right_knee_x=120
right_knee_y=-140

#Наносим точки по координатам звезд
turtle.goto(left_shoulder_x,left_shoulder_y) #помещаем по координатам
turtle.dot() #ставим точку
turtle.goto(right_shoulder_x,right_shoulder_y)
turtle.dot()
turtle.goto(left_beltstar_x,left_beltstar_y)
turtle.dot()
turtle.goto(middle_beltstar_x,middle_beltstar_y)
turtle.dot()
turtle.goto(right_beltstar_x,right_beltstar_y)
turtle.dot()
turtle.goto(left_knee_x,left_knee_y)
turtle.dot()
turtle.goto(right_knee_x,right_knee_y)
turtle.dot()

#Прописываем названия к каждой звезде
turtle.goto(left_shoulder_x,left_shoulder_y)
turtle.write("Бетельгейзе")
turtle.goto(right_shoulder_x,right_shoulder_y)
turtle.write("Хатиса")
turtle.goto(left_beltstar_x,left_beltstar_y)
turtle.write("Альнитак")
turtle.goto(middle_beltstar_x,middle_beltstar_y)
turtle.write("Альнилам")
turtle.goto(right_beltstar_x,right_beltstar_y)
turtle.write("Минтака")
turtle.goto(left_knee_x,left_knee_y)
turtle.write("Саиф")
turtle.goto(right_knee_x,right_knee_y)
turtle.write("Ригель")

#Наносим линию из левого плеча в левую звезду( совмещаем Бетельгейзе и Альнитак  )
turtle.goto(left_shoulder_x,left_shoulder_y)
turtle.pendown()
turtle.goto(left_beltstar_x,left_beltstar_y)
turtle.penup()
#Наносим линию и совмещаем Альнитак и Саиф.
turtle.goto(left_beltstar_x,left_beltstar_y)
turtle.pendown()
turtle.goto(left_knee_x,left_knee_y)
turtle.penup()
#Наносим линию и совмещаем Альнитак и Альнилам.
turtle.goto(left_beltstar_x,left_beltstar_y)
turtle.pendown()
turtle.goto(middle_beltstar_x,middle_beltstar_y)
turtle.penup()
#Наносим линию и совмещаем Альнилам и Минтака.
turtle.goto(middle_beltstar_x,middle_beltstar_y)
turtle.pendown()
turtle.goto(right_beltstar_x,right_beltstar_y)
turtle.penup()
#Наносим линию и совмещаем Минтака и Хатиса.
turtle.goto(right_beltstar_x,right_beltstar_y)
turtle.pendown()
turtle.goto(right_shoulder_x,right_shoulder_y)
turtle.penup()
#Наносим линию и совмещаем Минтака и Ригель.
turtle.goto(right_beltstar_x,right_beltstar_y)
turtle.pendown()
turtle.goto(right_knee_x,right_knee_y)
turtle.penup()

turtle.done() #оставляем окно рисования открытым