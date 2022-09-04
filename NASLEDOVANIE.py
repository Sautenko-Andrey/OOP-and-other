class Person:
    name='Рисование фигур'

    def set_coords(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def draw(self):
        print('Рисование любых фигур')

def main1():

    class Line(Person):
        name='Линия'
        def draw(self):
            print('Рисуем линию')


    class Rect(Person):
        pass

    r=Rect()
    r.draw()
    l=Line()
    l.draw()

#main1()

def main2():
    class Name:
        pass

    class Surname(Name):
        pass

    ob=Name()
    print(ob.__class__)
    ob2=Surname()
    print(ob2.__class__)
    print(issubclass(Surname,Name))
    print(isinstance(ob2,Name))
    print(isinstance(ob2,object))
    print(issubclass(int,object))
    print(issubclass(list,object))
    print(issubclass(dict,object))
    print(issubclass(float,object))

#main2()

def main3():
    class Vector(list):
         def __str__(self):
             return 'Мы переопределили метод __str__'


    ob=Vector([1,2,3,4,5])
    print(ob)
    print(type(ob))
#main3()

def main4():
    class Geom:
        def __init__(self,x1,x2,y1,y2):
            print(f'Инициализатор для {self.__class__}')
            self.x1=x1
            self.x2=x2
            self.y1=y1
            self.y2=y2

    class Line(Geom):
        def draw(self):
            print('Я рисую линию!')

    class Rect(Geom):
        def __init__(self,x1,x2,y1,y2,fill=None):
            super().__init__(x1,x2,y1,y2)
            print('Инициализатор для Rect')
            self.fill=fill

        def draw(self):
            print('Я рисую прямоугольник!')


    obj=Line(1,1,0,0)
    print(obj.__dict__)
    print('---------------------------------------')
    obj2=Rect(20,20,20,20)
    print(obj2.__dict__)

#main4()

def main5():
    class Automobile:
        def __init__(self,frame,wheel,motor):
            print(f'Идет инициализация класса {self.__class__}')
            self.frame=frame
            self.wheel=wheel
            self.motor=motor

        def set_conder(self,conder):
            print('Устанавливаем самый обычный кондер')
            self.conder=conder


    class Car(Automobile):
        def create_car(self):
            print('Создаем легковушку!')

    class Truck(Automobile):
        def __init__(self,trailer):
            super(Truck, self).__init__('blue',16,5.5)
            print('Идет переопределение инициализатора Truck')
            self.trailer=trailer


        def made_trailer(self):
            print('Делаем прицеп!')

        def set_conder(self,conder,gaz):
            super().set_conder()
            print('Устанавливаем спец.кондер')
            self.conder=conder
            self.gaz=gaz


    lanos=Car('red',4,1.6)
    print(lanos.__dict__)
    print('----------------------------------------------------------')
    volvo=Truck(20)
    print(volvo.__dict__)
    print('------------------------------------------------------------')



#main5()


def main6():
    class Footballer:
        def __init__(self,speed,height,weight):
            print('вызывается инициализатор Footballer')
            self.speed=speed
            self.height=height
            self.weight=weight

        def scream(self):
            print('I am footballer!')


    class Defender(Footballer):
        def tackle(self):
            print('I can tackle the ball')

    class Goalkeeper(Footballer):
        def __init__(self,reaction):
            super(Goalkeeper, self).__init__(60,195,77)
            self.reaction=reaction

        def catch_the_ball():
            print('i can catch the ball')


    gabriel=Defender(60,180,85)
    print(gabriel.__dict__)
    print('-----------------------------------------------')
    ramsdell=Goalkeeper(5)
    print(ramsdell.__dict__)

#main6()

def main7():
    class Fruits:
        def __init__(self,color,weight):
            self.color=color
            self.weight=weight

    class Apple(Fruits):
        def __init__(self,price):
            super(Apple, self).__init__('red',22)
            self.price=price

    class Banana(Fruits):
        def eat_me(self):
            print('Ты сожрал меня!')

    apple=Apple(1)
    print(apple.__dict__)
    banan=Banana('yellow',5)
    print(banan.__dict__)

#main7()

def main8():
    class Figures:
        def __init__(self,x1,y1,x2,y2):
            print(f'Работает инициализатор Figures для {self.__class__}')
            self.__x1=x1
            self.__y1=y1
            self.__x2 = x2
            self.__y2 = y2


        def show_coords(self):
            return self.__x1,self.__y1,self.__x2,self.__y2



    class Square(Figures):
        def __init__(self,x1,y1,x2,y2,fill='blue'):
            super(Square, self).__init__(x1,y1,x2,y2)
            self.__fill=fill




    figure=Square(0,22,67,0)
    print(figure.__dict__)
    print(figure.show_coords())

#main8()


def main9():
    class Girls:
        def __init__(self,body,head,brain):
            self._verify_brain(brain)
            self._body=body
            self._head=head
            self._brain=brain

        def _verify_brain(self,brain):
            return brain<=2

    class Latina(Girls):
        def __init__(self,body,head,brain,color='brown'):
            super(Latina, self).__init__(body,head,brain)
            self._color=color

        def show_body(self):
            return self._body

    girl=Latina(1,1,1)
    print(girl.__dict__)
    print(girl.show_body())
    girl22=Girls(1,2,2.5)
    print(girl22.__dict__)

main9()











