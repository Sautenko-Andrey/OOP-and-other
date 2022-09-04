class Finance:
    def __init__(self,balance):
        self.__my_finance=balance

    #метод пополнения баланса:
    def grove_balance(self,get_money):
        print('Ложить денежки на счет всегда приятно:)')
        self.__my_finance+=get_money

    #метод для вычисления чистой прибыли:
    def marja(self,arenda,kommunalka,ohrana,nalogi):
        self.__my_finance-=(arenda+kommunalka+ohrana+nalogi)

    #метод , показывающий текущий баланс на карте:
    def show_money(self):
        return self.__my_finance




