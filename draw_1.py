import pygame

# инициализируем игровой движок
pygame.init()

# определяем цвета,которые мы будем использовать в формате RGB

BLACK=(  0,  0,  0)
WHITE=(255,255,255)
RED=(255,  0,  0)
GREEN=(  0,100,  0)

# устанавливаем высоту и ширину экрана,на котром будем рисовать

size=[400,400]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Андрюха,давай порисуем:)")

# создаем цикл пока пользователь не нажмет кнопку закрытия

done=False
clock=pygame.time.Clock()

while not done:
    clock.tick(10)
    for event in pygame.event.get(): #пользователь делает что-то
        if event.type==pygame.QUIT: #если пользователь нажимает "закрыть"
            done=True #отмечаем,что закончили,поэтому выходим из цикла
    screen.fill("WHITE") # очищаем экран и устанавливаем его фон
    #рисуем черную линию от (0,0) до (50,30) шириной 3 пикселей
    pygame.draw.line(screen,BLACK,[50,10],[50,200],3)
    pygame.draw.circle(screen,RED,[150,50],30)
    pygame.draw.circle(screen, BLACK, [250, 250], 45)
    pygame.draw.line(screen, GREEN, [150, 750], [50, 200], 7)

    pygame.display.flip() #обновляем экран и показыаем,что нарисовали

pygame.quit()


