# Модуль с функцией,считающей наценку на товар
#opt - это оптовая цена товара
#marja - это коэффициент маржи на товар

import math

def plus_price(opt,marja):
    return opt+(opt*marja)
