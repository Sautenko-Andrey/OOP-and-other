# класс, который содержит данные о кроссовках
class Sneakers:
    # инициализируем данные по кроссовкам:
    def __init__(self,art,name,price):
        self.__articul=art
        self.__name_model=name
        self.__opt_price=price

    #создадим методы ,которые записывают или изменяют данные
    def set_art(self,art):
        self.__articul=art

    #создадим переменную,для чтения:
    def get_art(self):
        return self.__articul

    def get_name(self):
        return self.__name_model

    def get_price(self):
        return self.__opt_price

