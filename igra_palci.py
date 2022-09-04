import random
class Chet_nechet():
    #метод init инициализирует атрибут palec значением nechet:
    def __init__(self):
        self.__palec='Нечет'

    #метод bros_palec генерирует случайное число от 1 до 2, если 1-нечет,2-чет.
    def bros_palec(self):
        if random.randint(1,2)==1:
            self.__palec='Нечет'
        else:
            self.__palec='Чет'

    #метод get_palec возвращает значение, на котрое теперь ссылается палец:
    def get_palec(self):
        return self.__palec

    # метод для проверки текущего состояния объекта:
    def __str__(self):
        return 'Состояние объекта в данный момент: '+self.__palec
