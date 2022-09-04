class Sberegatelniy_schet:
    def __init__(self, nomer_scheta, procent_stavka, ostatok_scheta):
        self.__nomer_scheta = nomer_scheta
        self.__procent_stavka = procent_stavka
        self.__ostatok_scheta = ostatok_scheta

    def set_nomer_scheta(self, nomer_scheta):
        self.__nomer_scheta = nomer_scheta

    def set_procent_stavka(self, procent_stavka):
        self.__procent_stavka = procent_stavka

    def set_ostatok_scheta(self, ostatok_scheta):
        self.__ostatok_scheta = ostatok_scheta

    def get_nomer_scheta(self):
        return self.__nomer_scheta

    def get_procent_stavka(self):
        return self.__procent_stavka

    def get_ostatok_scheta(self):
        return self.__ostatok_scheta


class DepositSertificat(Sberegatelniy_schet):
    def __init__(self, nomer_scheta, procent_stavka, ostatok_scheta, data):
        Sberegatelniy_schet.__init__(self, nomer_scheta, procent_stavka, ostatok_scheta)
        self.__data = data

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
