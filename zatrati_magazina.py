# В данном модуле функции будут считать
#все затраты магазина в течении месяца.

import math

#Создадим глобальные константы:
ARENDA=12000
UBORKA=250
NALOGI=2500
OHRANA=350
STOIMOST_1_KILOVATT=4
#Создадим главную функцию модуля:
def main_zatrati():
    plata_za_svet=elektrichestvo()
    plata_za_tekyshie=melkie_rashodi()
    plata_za_reklamu=reklama()
    #Выведем формулу для рассчета всех затрат:
    total_plata=plata_za_svet+plata_za_tekyshie+plata_za_reklamu+ARENDA+UBORKA+NALOGI+OHRANA
    return total_plata
def elektrichestvo():
    schetchik = float(input("Сколько киловатт накрутило?"))
    return schetchik*STOIMOST_1_KILOVATT
def melkie_rashodi():
    schetchik=float(input("Сколько потратил на всякие мелкие расходы?"))
    return schetchik
def reklama():
    schetchik=float(input("Сколько ты потратил на рекламу?"))
    return schetchik



