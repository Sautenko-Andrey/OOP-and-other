class Tovar:
    def __init__(self,name,count,price):
        self.__name=name
        self.__count=count
        self.__price=price

    def set_name(self,name):
        self.__name=name

    def set_count(self,count):
        self.__count=count

    def set_price(self,price):
        self.__price=price


    def get_name(self):
        return self.__name
    def get_count(self):
        return self.__count
    def get_price(self):
        return self.__price

    def get_ostatok(self,price,count):
        self.__ostatok=price*count
        return self.__ostatok
