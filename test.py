import random

def tren_9():

    """
    Генератор лотерейных чисел. Разработайте программу, которая генерирует семизначную
комбинацию лотерейных чисел. Программа должна сгенерировать семь случайных
чисел, каждое в диапазоне от О до 9, и присвоить каждое число элементу списка. (Случайные
числа рассматривались в главе 5.) Затем напишите еще один цикл, который показывает
содержимое списка.
    :return:
    """
    try:
        KOL_CHISEL=7
        lotery_list=[0]*KOL_CHISEL
        index=0
        while index<KOL_CHISEL:
            lotery_list[index]=random.randint(0,9)
            index=0
        for num in lotery_list:
            print(num)
    except Exception:
        print(Exception)

tren_9()