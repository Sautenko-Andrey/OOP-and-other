class Family:
    def __init__(self,pos):
        self.__pos=pos

    def show_pos(self):
        print('Это:',self.__pos)

    def make_events(self):
        print('Что-то делает')


class Mother(Family):
    def __init__(self):
        Family.__init__(self,'Мамулик')

    def make_events(self):
        print('Занимается домашними делами.')

class Father(Family):
    def __init__(self):
        Family.__init__(self,'Папанька')

    def make_events(self):
        print('Подрабатывает на автостоянке.')

class Son(Family):
    def __init__(self):
        Family.__init__(self,'Сын')

    def make_events(self):
        print('Учится и продает кроссовки онлайн.')




