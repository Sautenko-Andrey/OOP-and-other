# В данном модуле функции будут расчитывать выплаты сотруднкам магазина
# на основании их продаж и полученных ими авансов

# Получить месячные продажи продавца.
# Получить сумму авансовой выплаты.
# Применить сумму месячных продаж для определения ставки комиссионных.
# Рассчитать выплату продавцу с использованием ранее показанной формулы. Если сумма
# отрицательная, то указать, что продавец должен возместить компании разницу.

import math
def main():
    month_sales=prodajy()
    month_avans=avans_vidal()
    month_komiss=komissionnie(month_sales)
    # рассчитаем выплату:
    viplata = month_komiss - month_avans
    # проверим на долги:
    if viplata < 0:
        print(f"Ты должен вернуть в бухгалтерию {viplata} грн")
    else:
        print(f"Твоя зарплата составляет: ", {viplata}, "грн")
    return viplata
def komissionnie(sales):
    if sales<10000:
        komiss=0.1
    elif sales>=10000 and sales<15000:
        komiss=0.12
    elif sales>=15000 and sales<18000:
        komiss=0.14
    elif sales>=18000 and sales < 22000:
        komiss = 0.16
    else:
        komiss = 0.18
    return komiss



def prodajy():
    total_sales=float(input("На какую сумму напродавал?"))
    return total_sales
def avans_vidal():
    total_avans=float(input("Сумма выданного аванса: "))
    return total_avans




