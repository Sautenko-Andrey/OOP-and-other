class Bankaccount:
    #метод __init__ принимает аргумент с остатком на счете.ОН присваивается атрибуту __balance
    def __init__(self,bal):
        self.__balance=bal

    # метод deposit вносит на счет вклад:
    def deposit(self,amount):
        self.__balance+=amount

    #метод withdraw снимает сумму со счета:
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
        else:
            print('Ошибка,недостаточно средств!')
    # метод get_balance возвращает остаток средств на счете:
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return print('На карте в данный момент:',self.__balance)
