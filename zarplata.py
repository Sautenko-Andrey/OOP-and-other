#данный класс будет принимать данные по зарплате и оперировать ими
class Zarplata:
    # иницируем данные:
    def __init__(self,imya,spec,zp):
        self.__name=imya
        self.__doljnost=spec
        self.__zarplata=zp

    # принимаем данные по работнику(фамилия,должность,оклад)
    def get_info(self,name,position,sallary):
        self.__name=name
        self.__position=position
        self.__sallary=sallary

    # прочитываем эти данные
    def show_name(self):
        return self.__name
    def show_position(self):
        return self.__position
    def show_sallary(self):
        return self.__sallary

    # считаем зарплату работника
    def calc_zp(self,oklad,premiya,staj):
        return oklad+(oklad*premiya)+staj



