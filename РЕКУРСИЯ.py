def main_1():
    message()


def message():
    print('Это рекурсивная функция!')
    message()


# main_1()

def main_2():
    # сделаем пять вызовов
    message_1(5)


def message_1(times):
    if times > 0:
        print('Это рекурсивная функция')
        message_1(times - 1)


# main_2()

def main_3():
    show_info(3)


def show_info(times):
    x = 10
    if times > 0:
        print(x - 1)
        show_info(times - 1)


# main_3()

# Задача может быть решена на основе рекурсии, если ее разделить на уменьшенные задачи,
# которые по структуре идентичны общей задаче.

def main_4():
    "Реализация факториала числа при помощи рекурсии"
    # получим от пользователя число
    digit = int(input('Введи число: '))
    if digit < 0:
        digit = int(input('Введи целое число: '))

    # получим факториал
    fct = factorial(digit)

    # покажем факториал
    print('Факториал числа ', digit, 'равняется: ', fct)


def factorial(number):
    'Функция принимает в качестве аргумента число и вычисляет его факториал при помощи рекурсии'
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# main_4()

#                                Примеры алгоритмов на основе рекурcии

def main_5():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start = 2
    end = 5
    summa = range_sum(my_list, start, end)
    print('Сумма заданного диапазона равняется:', summa)


def range_sum(some_list, some_start, some_end):
    if some_start > some_end:
        return 0
    else:
        return some_list[some_start] + range_sum(some_list, some_start + 1, some_end)


# main_5()

def matryoshka(kolichestvo_matreshek):
    'реализуем изготовление и сбор матрешки'
    # пропишем крайний случай,т.е. уже последнюю цельную матрешечку
    if kolichestvo_matreshek == 1:
        print('Самая маленькая матрешечка')
    else:
        print('Вверх матрешки (номер матрешки)=', kolichestvo_matreshek)
        matryoshka(kolichestvo_matreshek - 1)
        print('Низ матрешки (номер матрешки)=', kolichestvo_matreshek)


# matryoshka(5)

#                                Последовательность Фибоначчи
def main_6():
    print('Первые 10 чисел Фибоначчи')
    for number in range(1, 11):
        print(fibonacci(number))


def fibonacci(chislo):
    if chislo == 0:
        return 0
    elif chislo == 1:
        return 1
    else:
        return fibonacci(chislo - 1) + fibonacci(chislo - 2)


# main_6()

def recursive(value):
    print(value)
    if value < 10:
        recursive(value + 1)
    print(value)


# recursive(1)

def fack(chislo):
    if chislo <= 0:
        return 1
    else:
        return chislo * fack(chislo - 1)


# faktorial=fack(6)
# print(faktorial)

def main_7():
    digit = int(input('введи любое число: '))
    rec_1(digit)


def rec_1(some_digit):
    print(some_digit)
    if some_digit > 0:
        rec_1(some_digit - 1)
    print(some_digit)


# main_7()

def main_8():
    chislo = int(input('Введи любое число,факториал которого хочешь посчитать: '))
    my_factorial = get_factorial(chislo)
    print(my_factorial)


def get_factorial(some_digit):
    if some_digit == 0:
        return 1
    else:
        return some_digit * get_factorial(some_digit - 1)


# main_8()

def main_9():
    kopilka = 100
    ostatok = get_from_kopilka(kopilka)


def get_from_kopilka(some_kopilka):
    print(some_kopilka)
    duty = float(input('Сколько берешь денег из копилки?'))
    if duty > some_kopilka:
        print('Нет столько денег в копилке...')
    else:
        print('Остаток в копилке:', end='')
        return get_from_kopilka(some_kopilka - duty)


# main_9()

def main_10():
    save_point = 15000
    print('Цель-собрать', save_point, 'usd')
    recur_2(save_point)


def recur_2(target):
    print('Осталось накопить: ', target, 'usd')
    put_money = float(input('Сколько будешь ложить денег?'))
    if target == 0:
        print('Ты накопил нужную сумму!')
    else:
        return recur_2(target - put_money)


# main_10()

def kopilka(balance):
    summa = 100
    put_money = float(input('Сколько будешь ложить?'))
    if balance == summa:
        print('Ты собрал нужную сумму!')
    else:
        kopilka(balance + put_money)


# kopilka(0)

def main_11():
    digit = int(input('Введи число: '))
    recurs(digit)


def recurs(some_num):
    print(some_num)
    if some_num > 100:
        print('Finished!')
    else:
        return recurs(some_num + 10)


# main_11()

def main_12():
    time = 60

    calk_down(time)


def calk_down(some_time):
    print('Время: ', some_time, 'сек')
    if some_time < 1:
        print('Время вышло!')
    else:
        calk_down(some_time - 1)


# main_12()

def main_13():
    chislo = 1
    my_factorial = factor_5(chislo)
    print(f'Факториал числа {chislo} равен =', my_factorial)


def factor_5(digit):
    if digit == 1:
        return 1
    else:
        return digit * factor_5(digit - 1)


# main_13()

def rec(num):
    if num < 4:
        print(num)
        rec(num + 1)
        print(num)


# rec(1)

#
def palindrom(stroka):
    if len(stroka) <= 1:
        return True
    elif stroka[0] != stroka[-1]:
        return False
    else:
        return palindrom(stroka[1:-1])


# print(palindrom('abba'))

def main_14():
    stroka = 'uihfewhfiwebcbewbcbwe'
    print('(', rec_6(stroka), ')')


def rec_6(some_text):
    if len(some_text) == 1 or len(some_text) == 2:
        return some_text
    else:
        return some_text[0] + '(' + rec_6(some_text[1:-1]) + ')' + some_text[-1]


# main_14()

def main_15():
    text = 'janera'
    print(rec_7(text))


def rec_7(some_text):
    if len(some_text) == 1 or len(some_text) == 2:
        return some_text
    else:
        return some_text[0] + '*' + rec_7(some_text[1:-1]) + '*' + some_text[-1]


# main_15()

def main_16():
    # наибольшый общий делитель
    chislo_1 = 49
    chislo_2 = 28
    print('НОД чисел равен: ', nod(chislo_1, chislo_2))


def nod(num_1, num_2):
    if num_1 % num_2 == 0:
        return num_2
    else:
        return nod(num_1, num_1 % num_2)


# main_16()

def main_17():
    'Ханойские башни'
    # зададим исходные значения для колец и башен
    kolichestvo_kolec = 3
    firs_bashnya = 1
    third_bashnya = 3
    vremennaya_bashnya = 2

    # решаем головоломку
    move_kolca(kolichestvo_kolec, firs_bashnya, third_bashnya, vremennaya_bashnya)
    print('Все кольца перемещены!')


def move_kolca(kol, from_b, to_b, temp_b):
    if kol > 0:
        move_kolca(kol - 1, from_b, temp_b, to_b)
        print('Переложить кольцо с', from_b, 'на', to_b)
        move_kolca(kol - 1, temp_b, to_b, from_b)


# main_17()


# Задача №1
# Рекурсивная печать. Разработайте рекурсивную функцию, которая принимает целочисленный
# аргумент п и распечатывает числа от 1 до п.
def task1():
    chislo = int(input('Введи до какого числа распечатывать цифры: '))
    recurs_1(chislo)


def recurs_1(num):
    if num > 0:
        recurs_1(num - 1)
        print(num)


# task1()

# Задача №2
# Рекурсивное умножение.
# Разработайте рекурсивную функцию, которая принимает два аргумента в параметры х
# и у. Данная функция должна вернуть значение произведения х на у. При этом умножение
# должно быть выполнено, как повторяющееся сложение, следующим образом:
# 7 х 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4.
# (Для того чтобы упростить функцию, исходите из того, что х и у будут всегда содержать
# положительные ненулевые целые числа.)
def task2():
    x = 7
    y = 4
    recurs_2(x, y)


def recurs_2(x, y):
    if y<=x*y:
        print('Итерация №', x, 'результат---', y)
        recurs_2(x - 1, y + y)


#task2()


