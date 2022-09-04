import random
# класс Вегас имитирует кубик,который будет выбрасываться
class Cube:
    # инициализируем для начала,что сторона куба выпала единицой
    def __init__(self):
        self.storona_kuba='1'

    # метод mix_cube генерирует случайное число от 1 до 6 и показывает
    # соответствующее число
    def mix_cube(self):
        if random.randint(1,6)==1:
            self.storona_kuba='1'
        elif random.randint(1,6)==2:
            self.storona_kuba='2'
        elif random.randint(1,6)==3:
            self.storona_kuba='3'
        elif random.randint(1,6)==4:
            self.storona_kuba='4'
        elif random.randint(1,6)==5:
            self.storona_kuba='5'
        else:
            self.storona_kuba='6'

    # метод get_side возвращает сторону куба,которая сейчас лежит
    def get_side(self):
        return self.storona_kuba