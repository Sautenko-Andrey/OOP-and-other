# ВОзможно так будет выглядеть словарь. Но нужно создать как модуль,который будет вызываться в программе.
import random
def word():
    d1=dict.fromkeys(["ПРОТИВОРЕЧИЯ"],"CONTRADICTIONS")
    d1=1
    d2=dict.fromkeys(["ПОЯВЛЯТЬСЯ "],"APPEAR")
    d2=2
    word_give=random.randint(1,2)
    if word_give==1:
        print(d1)
    else:
        print("hahaha")
word()