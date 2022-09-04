class Animals:
    def __init__(self,vid):
        self.__vid=vid

    def show_vid(self):
        # метод показывает вид животного
        print('Это',self.__vid)

    def make_sound(self):
        # издает характерный звук для всех животных
        print('Rrrrrrrrrrr')

class Dog(Animals):
    def __init__(self):
        Animals.__init__(self,'Собачка')

    def make_sound(self):
        print('Гав-гав!')

class Cat(Animals):
    def __init__(self):
        Animals.__init__(self,'Котик')
    def make_sound(self):
        print('Мяууу!')

class Spider(Animals):
    def __init__(self):
        Animals.__init__(self,'Паучок')

    def make_sound(self):
        print('Шшшшшш')

class Homka(Animals):
    def __init__(self):
        Animals.__init__(self,'Хомячок')

    def make_sound(self):
        print('Хом-хом')

