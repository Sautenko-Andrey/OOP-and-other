class PhonesFriends:
    def __init__(self,phones):
        self.__phones_list=phones

    #добавление телефонов в список контактов:
    def add_phones(self,name,number,some_dict):
        some_dict[name]=number

    #это не работает со словарями!
    def __str__(self):
        return print('Мои контакты--',self.__phones_list)

    def show_book(self):
        return print(self.__phones_list)

    #удалим контакт из телефонной книги:
    def delete_number(self,some_dict,name):
        if name in some_dict:
            del some_dict[name]
        else:
            print('Нет такого контакта в телефоне!')





