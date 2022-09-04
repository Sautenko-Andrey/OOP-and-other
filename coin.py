import random
class Coin:
    #инициализируем первональное значение монеты:
    def __init__(self):
        self.__sideup='Орел'

    #генерируем случайное число от 0 до 1 для подбрасывания монеты:
    def toss(self):
        if random.randint(0,1)==0:
            self.__sideup='Орел'
        else:
            self.__sideup='Решка'

    # вернем значение монеты,на какую сторону она упала:
    def get_sideup(self):
        return self.__sideup