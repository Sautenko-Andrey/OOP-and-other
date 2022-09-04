class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # методы-модификаторы
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # методы-получатели
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

class Customer(Person):
    def __init__(self,name,address,phone,customer_number,subscribe):
        Person.__init__(self,name,address,phone)

        self.__customer_number=customer_number
        self.__subscribe=subscribe

    def set_customer_number(self,customer_number):
        self.__customer_number=customer_number

    def set_subscribe(self,subscribe):
        self.__subscribe=subscribe

    def get_custtomer_number(self):
        return self.__customer_number

    def get_subscribe(self):
        return self.__subscribe

class Saler(Person):
    def __init__(self):
        Person.__init__(self,'Продавец','Адресс не важен','0950180611')
    def what_doing(self):
        print('Продает людям вещи!')
