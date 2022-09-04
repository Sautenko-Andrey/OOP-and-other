# Игра "Порази цель"
import turtle

#Заведем именованные константы :
SCREEN_WIDTH=600                # ширина экрана
SCREEN_HEIGHT=600               # высота экрана

TARGET_LLEFT_X=100              # ЛЕВАЯ НИЖНЯЯ КООРДИНАТА Х ЦЕЛИ
TARGET_LLEFT_Y=250              # ЛЕВАЯ НИЖНЯЯ КООРДИНАТА У ЦЕЛИ
TARGET_WIDTH=25                 # ШИРИНА ЦЕЛИ
FORCE_FACTOR=30                 # ФАКТОР ПРОИЗВОЛЬНОЙ СИЛЫ
PROJECTILE_SPEED=1              # СКОРОСТЬ АНИМАЦИИ СНАРЯДА
NORTH = 90                      # Угол северного направления.
SOUTH = 270                     # Угол южного направления.
EAST = 0                        # Угол восточного направления.
WEST = 180                      # Угол западного направления.

# Настраиваем окно :
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
# Нарисовать цель.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Центрировать черепаху.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
# Получить угол и силу от пользователя.
angle=float(input("Bвeдитe угол снаряда: "))
force = float(input("Bвeдитe пусковую силу (1-10): "))

# Рассчитать расстояние.
distance = force * FORCE_FACTOR
# Задать направление.
turtle.setheading(angle)
# Запустить снаряд.
turtle.pendown()
turtle.forward(distance)
# Снаряд поразил цель?
if (turtle.xcor() >= TARGET_LLEFT_X and
turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
turtle.ycor() >= TARGET_LLEFT_Y and
turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print ('Цель поражена! ')
else:
    print ('Вы промахнулись. ')

turtle.done()