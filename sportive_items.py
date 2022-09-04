class Sport1:
    'Класс который получает данные о спортивных товарах и показывает эти данные'

    # инициализируем данные:
    def __init__(self, name, articul, count, price):
        self.__name = name
        self.__articul = articul
        self.__count = count
        self.__price = price

    # пропишем ряд методов get,которые будут возвращать значения атрибутов:
    def get_name(self):
        return self.__name

    def get_articul(self):
        return self.__articul

    def get_count(self):
        return self.__count

    def get_price(self):
        return self.__price
