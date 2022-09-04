class Save:
    'Класс для записи ТМЦ на складе'
    #инициализируем атрибуты класса:
    def __init__(self,name,art,count):
        self.__name=name
        self.__art=art
        self.__count=count

    # метод для возврата значения атрибута:
    def get_name(self):
        return self.__name

    def get_art(self):
        return self.__art

    def get_count(self):
        return self.__count

