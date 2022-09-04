class Sportive_itrms:
    'Надкласс для общей инфы всех спортивных товаров'

    def __init__(self, name, articul, price):
        self.__name = name
        self.__articul = articul
        self.__price = price

    # методы-модификаторы
    def set_name(self, name):
        self.__name = name

    def set_articul(self, articul):
        self.__articul = articul

    def set_price(self, price):
        self.__price = price

    # методы-получатели
    def get_name(self):
        return self.__name

    def get_articul(self):
        return self.__articul

    def get_price(self):
        return self.__price

    # метод состояния
    def __str__(self):
        return 'Наименование товара: ' + str(self.__name) + \
               '\nАртикул: ' + str(self.__articul) + \
               '\nЦена: ' + str(self.__price)


class Krossovki(Sportive_itrms):
    def __init__(self, name, articul, price, type_for):
        Sportive_itrms.__init__(self, name, articul, price)
        self.__type_for = type_for

    def set_type_for(self, type_for):
        self.__type_for = type_for

    def get_type_for(self):
        return self.__type_for


class Suits(Sportive_itrms):
    def __init__(self, name, articul, price, gender):
        Sportive_itrms.__init__(self, name, articul, price)
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


class Bags(Sportive_itrms):
    def __init__(self, name, articul, price, size):
        Sportive_itrms.__init__(self, name, articul, price)
        self.__size = size

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
