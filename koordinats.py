class Point:
    "Класс для определения точек на плоскости"
    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для'+str(cls))
        return super().__new__(cls)


    def __init__(self,x,y):
        print('Вызов __init__ для'+str(self))
        self.x=x
        self.y=y


