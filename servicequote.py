# константа для ставки налога с продаж
TAX_RATE = 0.05


class ServiceQuote:
    def __init__(self, stoim_zapch, stoim_trud):
        self.__stoim_zapch = stoim_zapch # оценочная стоимость запчастей
        self.__stoim_trud = stoim_trud   # оценочная стоимость труда

    def set_stoim_zapch(self, stoim_zapch):
        self.__stoim_zapch = stoim_zapch

    def set_stoim_trud(self, stoim_trud):
        self.__stoim_trud = stoim_trud

    def get_stoim_zapch(self):
        return self.__stoim_zapch

    def get_stoim_trud(self):
        return self.__stoim_trud

    def get_sales_tax(self):
        return self.__stoim_zapch*TAX_RATE   # вычисление налога с продаж

    def get_total_zatrati(self):
        return self.__stoim_trud+self.__stoim_zapch/(self.__stoim_zapch*TAX_RATE) # общая оценочная стоимость расходов



