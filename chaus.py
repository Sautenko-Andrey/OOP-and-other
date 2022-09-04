import random
class Buhlo:
    def __init__(self):
        self.__varianty=['Черниговское','Львовское','БАД','Карлсберг']

    def choice(self):
        vibor_Chausa=random.choice(self.__varianty)
        print('Сегодня будем пить:',vibor_Chausa)
        print('Теперь определимся сколько будет выпито пива за вечер!')
        kol_vo=random.randint(1,12)
        print(kol_vo,'бутылок!')
        if kol_vo>8:
            print('Жесткая пьянка!')
        else:
            print('Все будет норм:)')

    def show(self):
        print('Выбираем пиво из этого ассортимента:')
        print(self.__varianty)

