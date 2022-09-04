class Mobile:
    'Класс содержит данные о мобильно телефоне.'
    # инициализируем атрибуты класса:
    def __init__(self,proizvoditel,nomer_modeli,retail_price):
        self.__proizvoditel=proizvoditel
        self.__nomer_modeli=nomer_modeli
        self.__retail_price=retail_price

    # метод set_proizvoditel принимает аргумент
    # для производителя телефона и в случае необходимости меняет его.
    def set_proizvoditel(self,new_proizvoditel):
        self.__proizvoditel=new_proizvoditel

    def set_nomer_modeli(self,new_nomer_modeli):
        self.__nomer_modeli=new_nomer_modeli

    def set_retail_price(self,new_retail_price):
        self.__retail_price=new_retail_price

    # метод get возвращает данные для распечатки:
    def get_proizvoditel(self):
        return self.__proizvoditel

    def get_nomer_modeli(self):
        return self.__nomer_modeli

    def get_retail_price(self):
        return self.__retail_price

    def __str__(self):
        return 'Производитель: ' + str(self.__proizvoditel) + \
               '\nНомер модели: ' + str(self.__nomer_modeli) + \
               '\nРозничная цена: ' + str(self.__retail_price)


