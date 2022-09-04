class Automobile:
    "Надкласс , содержащий общие данные об автомобиляхна складе"

    def __init__(self, firma, model, probeg, cena):
        # метод инициализирует атрибуты: фирма-изготовитель,
        # модель, пробег и цена
        self.__firma = firma
        self.__model = model
        self.__probeg = probeg
        self.__cena = cena

    # модификаторы
    def set_firma(self, firma):
        self.__firma = firma

    def set_model(self, model):
        self.__model = model

    def set_probeg(self, probeg):
        self.__probeg = probeg

    def set_cena(self, cena):
        self.__cena = cena

    # методы-получатели
    def get_firma(self):
        return self.__firma

    def get_model(self):
        return self.__model

    def get_probeg(self):
        return self.__probeg

    def get_cena(self):
        return self.__cena

# класс Car является подклассом Automobile и представляет легковой автомобиль
class Car(Automobile):
    def __init__(self, firma, model, probeg, cena,dveri):
        #вызываем метод __init__ надкласса и передаем требуемые аргументы
        Automobile.__init__(self,firma, model, probeg, cena)
        # инициализируем атрибут двери
        self.__dveri=dveri

    # метод-модификатор
    def set_dveri(self,dveri):
        self.__dveri=dveri

    # метод-получатель
    def get_dveri(self):
        return self.__dveri


