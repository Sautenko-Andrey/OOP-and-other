class Patient:
    def __init__(self, fio, address, phone, extra_contact):
        self.__fio = fio
        self.__address = address
        self.__phone = phone
        self.__extra_contact = extra_contact

    def set_fio(self, fio):
        self.__fio = fio

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_extra_contact(self, extra_contact):
        self.__extra_contact = extra_contact

    def get_fio(self):
        return self.__fio

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_extra_contact(self):
        return self.__extra_contact

    def __str__(self):
        return 'ФИО: ' + self.__fio + \
               '\nАдрес,город,область и почтовый индекс: ' + self.__address + \
               '\nТелефон пациента: ' + self.__phone + \
               '\nИмя и телефон котактного лица для экстренной связи: ' + self.__extra_contact


class Procedure:
    def __init__(self, nazvanie, data, doctor_name, stoimost):
        self.__nazvanie = nazvanie
        self.__data = data
        self.__doctor_name = doctor_name
        self.__stoimost = stoimost

    def set_nazvanie(self, nazvanie):
        self.__nazvanie = nazvanie

    def set_data(self, data):
        self.__data = data

    def set_doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name

    def set_stoimost(self, stoimost):
        self.__stoimost = stoimost

    def get_nazvanie(self):
        return self.__nazvanie

    def get_data(self):
        return self.__data

    def get_doctor_name(self):
        return self.__doctor_name

    def get_stoimost(self):
        return self.__stoimost

    def __str__(self):
        return 'Название процедуры: ' + str(self.__nazvanie) + \
               '\nДата процедуры: ' + str(self.__data) + \
               '\nИмя врача, который выполнил процедуру: ' + str(self.__doctor_name) + \
               '\nСтоимость процедуры: ' + str(self.__stoimost)
