class RetailItem:
    def __init__(self, opisanie, kol, cena):
        self.__opisanie = opisanie
        self.__kol = kol
        self.__cena = cena

    def set_opisanie(self, opisanie):
        self.__opisanie = opisanie

    def set_kol(self, kol):
        self.__kol = kol

    def set_cena(self, cena):
        self.__cena = cena

    def get_opisanie(self):
        return self.__opisanie

    def get_kol(self):
        return self.__kol

    def get_cena(self):
        return self.__cena

    def __str__(self):
        return 'Описание:' + self.__opisanie + \
               '\nКоличество:' + str(self.__kol) + \
               '\nЦена:' + str(self.__cena)
