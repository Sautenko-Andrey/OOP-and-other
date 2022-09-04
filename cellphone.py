# Класс CellPhone содержит данные о мобильном телефоне

class CellPhone:

    # метод __init__ инициализирует атрибуты
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # метод set_manufact принимает аргумент для производителя телефона:
    def set_manufact(self, manufact):
        self.__manufact = manufact

    # метод set_model принимает аргумент для номера модели телефона:
    def set_model(self, model):
        self.__model = model

    # метод set_retail_price принимает аргумент для розничной цены телефона:
    def set_retail_price(self, price):
        self.__retail_price = price

    # метод get_manufact возвращает производителя телефона:
    def get_manufact(self):
        return self.__manufact

    # метод get_model возвращает номер модели телефона:
    def get_model(self):
        return self.__model

    # метод get_retail_price возвращает розничную цену телефона:
    def get_retail_price(self):
        return self.__retail_price
