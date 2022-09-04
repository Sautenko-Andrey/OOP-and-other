class Geometrik:
    def __init__(self,figure):
        self.__figure=figure

    def show_figure(self):
        print('Перед тобой',self.__figure)

    def make_pic(self):
        print('][][&&/')

class Kvadrat(Geometrik):
    def __init__(self):
        Geometrik.__init__(self,'Квадрат')

    def make_pic(self):
        print('[]')

class Circle(Geometrik):
    def __init__(self):
        Geometrik.__init__(self,'Кружок')

    def make_pic(self):
        print('o')



