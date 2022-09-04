import pygame

from pygame.color import THECOLORS

pygame.init()
W,H=600,400
sc=pygame.display.set_mode((W,H),pygame.RESIZABLE)

clock=pygame.time.Clock()
FPS=60
pygame.display.set_caption("NEW PRACTICE")

rect=(265,180,75,50)
pygame.draw.rect(sc,THECOLORS["red"],rect,width=4)

line_start=(20,0)
line_end=(20,400)
pygame.draw.line(sc,THECOLORS['white'],line_start,line_end,width=3)

l_start=(0,0)
l_end=(600,400)
pygame.draw.aaline(sc,THECOLORS['blue'],l_start,l_end)

pointlist=((600,0),(300,200),(500,200))
pygame.draw.lines(sc,THECOLORS["green"],True,pointlist,width=2)

pointlist_2=((600,400),(300,200),(500,200))
pygame.draw.lines(sc,THECOLORS["green"],True,pointlist_2,width=2)

pointlist_3=((400,300),(150,100),(250,50))
pygame.draw.aalines(sc,THECOLORS["orange"],True,pointlist_3)

pointlist_4=((5,5),(595,5),(595,395),(5,395))
pygame.draw.polygon(sc,THECOLORS["purple"],pointlist_4,width=5)

pointlist_5=((5,5),(50,50),(5,60),(5,150))
pygame.draw.polygon(sc,THECOLORS["purple"],pointlist_5)

radius=30
coord=(450,200)
for i in range(10):
    pygame.draw.circle(sc,THECOLORS['yellow'],coord,radius,width=4)
    radius+=5

pygame.draw.ellipse(sc,THECOLORS["brown"],rect,3)

pi=3.14
rect_2=(250,50,100,75)
pygame.draw.arc(sc,THECOLORS["white"],rect_2,pi,2*pi,width=7)

pygame.display.update()

flRunning=True
while flRunning:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            flRunning=False

    clock.tick(FPS)
