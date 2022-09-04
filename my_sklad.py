class Sklad:
    def __init__(self,name,nomenclatura,calk):
        self.__name=name
        self.__nomenclatura=nomenclatura
        self.__calk=calk

    def set_name(self,name):
        self.__name=name

    def set_nomenclatura(self,nom):
        self.__nomenclatura=nom

    def set_calk(self,calk):
        self.__calk=calk

    def get_name(self):
        return self.__name

    def get_nomenclatura(self):
        return self.__nomenclatura

    def get_calk(self):
        return self.__calk

    def __str__(self):
        return 'Название запчасти:'+self.__name+\
            '\nНоменклатурный номер:'+self.__nomenclatura+\
            '\nОстаток:'+self.__calk




