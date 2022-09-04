#  Используя функции для работы с графикой библиотеки pygame,
#  нарисуйте дом с квадратным основанием и треугольной крышей.

import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
pygame.display.set_caption("My first draw by PYGAME :) ")
screen=pygame.display.set_mode((500,500))
screen.fill(THECOLORS["black"])
font=pygame.font.SysFont("couriernew",30)
text=font.render(str("HOME SWEET HOME"),True, THECOLORS["white"])
screen.blit(text,(0,0))
#второе словосочетание:
font=pygame.font.SysFont("couriernew",20)
text=font.render(str("WELL DONE,ANDREY!:)"),True, THECOLORS["white"])
screen.blit(text,(10,450))
# нарисуем квадратное основание домика:
osnovanie=pygame.Rect(175,150,150,150)
pygame.draw.rect(screen,THECOLORS["white"],osnovanie,0)
# нарисуем треугольную крышу домика:
# нарисуем первую линию:
line_1_x_start=175
line_1_y_start=150
line_1_x_end=250
line_1_y_end=45
pygame.draw.line(screen,THECOLORS["red"],(line_1_x_start,line_1_y_start),(line_1_x_end,line_1_y_end),width=3)

# нарисуем вторую линию:
line_2_x_start=250
line_2_y_start=45
line_2_x_end=325
line_2_y_end=150
pygame.draw.line(screen,THECOLORS["red"],(line_2_x_start,line_2_y_start),(line_2_x_end,line_2_y_end),width=3)

# нарисуем третью линию:
line_3_x_start=325
line_3_y_start=150
line_3_x_end=175
line_3_y_end=150
pygame.draw.line(screen,THECOLORS["red"],(line_3_x_start,line_3_y_start),(line_3_x_end,line_3_y_end),width=3)

# нарисуем линии:
pointlist=((150,150),(200,50),(300,150))
pygame.draw.lines(screen,THECOLORS["green"],True,pointlist,width=3)

# нарисуем круг:
pos=(400,400)
radius=75
pygame.draw.circle(screen,THECOLORS["yellow"],pos,radius,width=0)

# нарисуем эллипс:
rect_2=pygame.Rect(100,300,100,60)
pygame.draw.ellipse(screen,THECOLORS["blue"],rect_2,width=0)

# нарисуем многоугольник:
pointlist_2=((0,0),(50,0),(100,20),(200,60),(250,250))
pygame.draw.polygon(screen,THECOLORS["orange"],pointlist_2,width=0)

# главный цикл:
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()




