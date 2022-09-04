class Contact:
    # инициализируем атрибуты класса
    def __init__(self,name,phone,email):
        self.__name=name
        self.__phone=phone
        self.__email=email

    # устанавливаем атрибуты:
    def set_name(self,name):
        self.__name=name

    def set_phone(self,phone):
        self.__phone=phone

    def set_email(self,email):
        self.__email=email

    # возвращаем данные

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    # метод __str__ для просомтра состояния объекта в любое время
    def __str__(self):
        return 'Имя: '+self.__name+\
            '\nТелефон: '+self.__phone+\
            '\nПочта: '+self.__email