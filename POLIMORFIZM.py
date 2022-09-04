def main1():

    class Kvadrat:
        def __init__(self,storona):
            self.storona=storona

        def perimetr(self):
            return 4*self.storona

    class Treygolnik:
        def __init__(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c

        def perimetr(self):
            return self.a+self.b+self.c

    class Pryamougolnik:
        def __init__(self,a,b):
            self.a=a
            self.b=b

        def perimetr(self):
            return self.a*self.b

    all_figures=[
        Kvadrat(4),Treygolnik(5,5,5),Pryamougolnik(1,2)
    ]

    for figure in all_figures:
        print(figure.perimetr())

#main1()

# пример,если не будет переопределен метод в одном из классов ,что нужно делать
def main2():

    class My_friends:
        def describe(self):
            raise NotImplementedError('Ты забыл переопределить метод describe в одном из классов!')

    class Volleyballer(My_friends):
        def __init__(self,name,work_hand,height):
            self.name=name
            self.work_hand=work_hand
            self.height=height

        def describe(self):
            return f'{self.name}-is a volleyball player with height {self.height}.'


    class Footballer(My_friends):
        def __init__(self,name,position,work_foot):
            self.name=name
            self.position=position
            self.work_foot=work_foot

        def describe(self):
            return f'{self.name}-is a football player, who plays in {self.position} position'

    class Alcoholic(My_friends):
        def __init__(self, name, alco_type):
            self.name = name
            self.alco_type = alco_type

        def describe(self):
            return f'{self.name}-is an alcoholic with addiction in {self.alco_type}.....'

    people=[
        Volleyballer('Andrey','right',192),
        Footballer('Roman','defender','right'),
        Alcoholic('Ivan','beer')
    ]

    for man in people:
        print(man.describe())

#main2()

def main3():

    class SportBrands:
        def __init__(self,item,price):
            self.item=item
            self.price=price

        def packing_item(self):
            print(f'Thanks for your order! We are going to pack up yor {self.item}')


    class Nike(SportBrands):

        def __init__(self,item,price,special_discount):
            super(Nike, self).__init__(item,price)
            self.discount=special_discount

        def retail(self):
            print( f'Retail price for Nike item "{self.item}" is {self.price*2.0}')

    class Asics(SportBrands):
        def retail(self):
            print( f'Retail price for Asics item "{self.item}" is {self.price * 1.5}')

    order=[
        Nike('Nike Zoom Pegasus 38',125,5),
        Asics('Asics Sonoma 6 GTX', 70)
    ]

    for item in order:
        item.retail()
        item.packing_item()

#main3()

def main4():
    class Beer:
        def __init__(self,name,value):
            self.name=name
            self.value=value

    class Chernigivske(Beer):
        def __init__(self,name,value,brand):
            super(Chernigivske, self).__init__(name,value)

        def discount(self):
            print(f'Price with discount programm for beer {self.name} is {self.value*0.75} usd')

    class StellaArtois(Beer):
        def __init__(self,name,value,chest):
            super(StellaArtois, self).__init__(name,value)
            self.chest=chest

        def discount(self):
            print(f'Price with discount programm for beer {self.name} is {self.value * 0.9} usd')

    orderStella=StellaArtois('Stella Artois lager',35.75,25)
    orderStella.discount()
    orderChernigivske=Chernigivske('Chernigivske Svitle',18,'Obolon')
    orderChernigivske.discount()
    print()
    print()
    print(orderStella.__dict__)
    print(orderChernigivske.__dict__)

main4()

