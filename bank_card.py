class Money_card:
    def __init__(self,balance):
        self.__my_card=balance    # создадим объект карточку с балансом,который потом надо будет задавать

    #метод для просмотрта баланса на карточке:
    def check_balance(self):
        return self.__my_card

    #метод для внесения денег на карточку:
    def put_money(self,summa):
        self.__my_card+=summa

    # метод для снятия денег с карточки:
    def took_money(self,summa):
        self.__my_card-=summa

    # метод __str__ возвращает строковое значение состояния объекта:
    def __str__(self):
        return 'Остаток составляет:'+format(self.__my_card,'.2f')
