class Sotrudnik:
    def __init__(self, name, id, otdel, doljnost):
        self.__name = name
        self.__id = id
        self.__otdel = otdel
        self.__doljnost = doljnost

    # сеттеры
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_otdel(self, otdel):
        self.__otdel = otdel

    def set_doljnost(self, doljnost):
        self.__doljnost = doljnost

    # получатели
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_otdel(self):
        return self.__otdel

    def get_doljnost(self):
        return self.__doljnost
