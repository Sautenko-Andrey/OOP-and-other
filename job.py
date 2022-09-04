class Employee:
    # имя сотрудника
    # номер сотрудника
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    # методы сеттеры
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    # методы получатели
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class ProductionWorker(Employee):
    def __init__(self, name, id, smena, sallary):
        Employee.__init__(self, name, id)
        # инициализируем отрибуты smena и sallary
        self.__smena = smena
        self.__sallary = sallary

    # методы сеттеры
    def set_smena(self, smena):
        self.__smena = smena

    def set_sallary(self, sallary):
        self.__sallary = sallary

    # методы получатели
    def get_smena(self):
        return self.__smena

    def get_sallary(self):
        return self.__sallary


class ShiftSupervisor(Employee):
    def __init__(self, name, id, year_sallary, year_prime):
        Employee.__init__(self, name, id)
        self.__year_sallary = year_sallary
        self.__year_prime = year_prime

    # функции-модификаторы
    def set_year_sallary(self, year_sallary):
        self.__year_sallary = year_sallary

    def set_year_prime(self, year_prime):
        self.__year_prime = year_prime

    # функции-получатели

    def get_year_sallary(self):
        return self.__year_sallary

    def get_year_prime(self):
        return self.__year_prime
