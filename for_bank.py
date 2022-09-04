class Your_card:
    def __init__(self,balance):
        self.__balance=balance

    # метод для пополнения карты
    def put_money(self,money):
        self.__balance+=money

    # метод для снятия денег с карты
    def get_money(self,money):
        if money<=self.__balance:
            self.__balance-=money
        else:
            print('Увы, у Вас недостаточно средств на карте!')

    # показывает остаток на карте
    def show_money(self):
        return self.__balance

    # метод,возвращающуй строковое значение текцщего состояния объекта
    def __str__(self):
        return 'Остаток денег на карте составляет:'+format(self.__balance,'.2f')

