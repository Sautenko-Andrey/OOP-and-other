import phones_retail
class CashRegister:
    def __init__(self,some_list,object):
        self.__some_list=some_list
        self.__object=object

    def __str__(self):
        return 'Ваш заказ: ' + str(self.__object)

    def purchace_item(self,some_list,object):
        some_list=[]
        some_list.append(object)
        return some_list

    def get_total(self,some_list):
        some_list=[]



