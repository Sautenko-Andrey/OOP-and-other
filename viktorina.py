class Question:
    def __init__(self, vopros, otvet1, otvet2, otvet3, otvet4, nomer_prav_otveta):
        self.__vopros = vopros
        self.__otvet1 = otvet1
        self.__otvet2 = otvet2
        self.__otvet3 = otvet3
        self.__otvet4 = otvet4
        self.__nomer_prav_otveta = nomer_prav_otveta

    def set_vopros(self, vopros):
        self.__vopros = vopros

    def set_otvet1(self, otvet1):
        self.__otvet1 = otvet1

    def set_otvet2(self, otvet2):
        self.__otvet2 = otvet2

    def set_otvet3(self, otvet3):
        self.__otvet3 = otvet3

    def set_otvet4(self, otvet4):
        self.__otvet4 = otvet4

    def set_nomer_prav_otveta(self, nomer_prav_otveta):
        self.__nomer_prav_otveta = nomer_prav_otveta

    def get_vopros(self):
        return self.__vopros

    def get_otvet1(self):
        return self.__otvet1

    def get_otvet2(self):
        return self.__otvet2

    def get_otvet3(self):
        return self.__otvet3

    def get_otvet4(self):
        return self.__otvet4

    def get_nomer_prav_otveta(self):
        return self.__nomer_prav_otveta
