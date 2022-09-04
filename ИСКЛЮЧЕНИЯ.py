# Исключение - это ошибка, которая происходит во время работы программы, приводящая
# к ее внезапному останову. Для корректной обработки исключений используется инструкция
# try / except.

def some_1441():
    first = int(input("1"))
    sec = int(input("2"))

    if sec != 0:
        result = first / sec
        print(result)
    else:
        print("ERROR! you can't / 0")


# some_1441()

def zarp():
    try:
        hours = int(input("how many hours have you worked?"))
        money_pr_hour = float(input("How much dollars per hour?"))

        sallary = hours * money_pr_hour
        print(sallary)
    except ValueError:
        print("Ошибка! Отработанные часы и зп должны быть допустимыми числами")


# zarp()

def prodagi():
    # создадим список продаж в магазине за месяц:
    answer = "y"

    file = open(r'D:\Фильмы\продажи.txt', 'a')

    while answer == "y" or answer == "Y":
        print("Пропишите все продажи: ")
        sales = float(input("на сколько продали? "))

        file.write(str(sales) + '\n')

        answer = input("Для продолжения нажми 'Y' или 'y': ")

    file.close()


# prodagi()


# эта программа показывает итоговый объем продаж из файла продажи.txt

def main_sales():
    # заведем накопитель
    total_sales = 0
    try:
        # открываем файл продажи.txt:
        file = open(r'D:\Фильмы\продажи.txt', 'r')

        # прочитать значения из файла:
        for lines in file:
            sales = float(file.readline())

            # суммировать все в total_sales:
            total_sales += sales

        # закрываем файл:
        file.close()

        # выводим данные на экран:
        print(f"Сумма всех продаж составляет:{total_sales} грн")

        # ожидаемые ошибки:
    except IOError:
        print("Произошла ошибка при попытке прочитать файл!")
    except ValueError:
        print("В файле найдены нечисловые данные!")
    except:
        print("Произошла какая-то ошибка!")


# main_sales()


#             ИСПОЛЬЗОВАНИЕ ОДНОГО ВЫРАЖЕНИЯ EXCEPT ДЛЯ ОТЛАВЛИВАНИЯ ВСЕХ ИСКЛЮЧЕНИЙ
def some_924():
    try:
        total = 0
        for i in range(5):
            digit = float(input("enter some digit: "))
            total += digit
            print(digit)
        print(total)
    except:
        print("SOME ERROR!")


# some_924()


# Вывод заданного по умолчанию сообщения об ошибке
# при возникновении исключения
def zp():
    try:
        hours = int(input("Сколько часов отработал? "))

        money_per_hour = float(input("Сколько платят за час? "))

        sallary = hours * money_per_hour
        print(f"Зарплата составляет:{sallary}грн")

    except ValueError as err:
        print(err)


# zp()


# Если для отлавливания всех исключений, которые вызываются в выражении except, требуется
# иметь всего одно выражение except, то можно определить Exception как тип.
def read_sales():
    try:
        total_sales = 0

        file = open(r'D:\Фильмы\продажи.txt', 'r')

        for string in file:
            sales = float(file.readline())
            total_sales += sales

        file.close()

        print(total_sales)

    except Exception as err:
        print(err)


# read_sales()


def some_985():
    try:
        total = 0
        for every_sale in range(5):
            whole_sale = float(input("Text wholesale price: "))
            koef_retail = 1.5

            retail = whole_sale * koef_retail

            total += retail

            print(retail)
        print(total)
    except Exception as err:
        print(err)


# some_985()


# Выражение else
def some_982():
    try:
        password = "3496"
        answer = input("what is your password?")
        while answer != password:
            print("Wrong password!")
            answer = input("try again!")
    except Exception as err:
        print("PROGRAMM ERROR!")
    else:
        print("well done!")


# some_982()

def rash():
    total = 0
    try:
        for i in range(3):
            zatrati = float(input("enter pay: "))
            total += zatrati

    except Exception as err:
        print("PROGRAMM ERROR!")
    else:
        print(total)


# rash()

# ВЫРАЖЕНИЕ FINALLY
def some_131():
    try:
        zp = float(input("enter your black sallary: "))
        stavka_nalog = 0.2

        tax = zp * stavka_nalog

    except Exception as err:
        print("PROGRAMM ERROR!")
    else:
        print(tax)
    finally:
        print("Have a good day!")


# some_131()

def my_name():
    try:
        name = input("Твое имя?")

        file = open(r'D:\Фильмы\имя.txt', 'w')

        file.write(str(name))

        file.close()
    except ValueError as err:
        print(err)


# my_name()

# Напишите программу, которая открывает файл my_name.txt, созданный программой в задаче
# 1, читает ваше имя из файла, выводит имя на экран и затем закрывает файл.
def read_name():
    try:
        file = open(r'D:\Фильмы\имя.txt', 'r')

        name = file.readline()

        print(name)

        file.close()

    except ValueError as err:
        print(err)


# read_name()

# Напишите программу, которая делает следующее: открывает выходной файл с именем
# number_list.txt, применяет цикл для записи в файл чисел с 1 по 100, а затем закрывает
# файл.

def practice_1():
    try:
        file = open(r'D:\Фильмы\number_list.txt', 'w')

        for num in range(1, 101):
            file.write(str(num) + '\n')

        file.close()

    except ValueError as err:
        print(err)


# practice_1()

# Напишите программу, которая делает следующее: открывает файл number_list.txt, созданный
# программой, которую вы написали в задаче 3, читает все числа из файла, выводит
# их на экран и затем закрывает файл.

def read_practice_1():
    try:
        file = open(r'D:\Фильмы\number_list.txt', 'r')

        num = file.readline()
        while num != "":
            num = file.readline()

            num = num.rstrip('\n')

            print(num)

            num = file.readline()

        file.close()

    except ValueError as err:
        print(err)


# read_practice_1()


def some_1232():
    try:
        file = open(r'D:Фильмы\100.txt', 'w')

        for num in range(1, 101):
            file.write(str(num) + '\n')

        file.close()
    except ValueError as err:
        print(err)


# some_1232()

def read_some_1232():
    try:
        file = open(r'D:Фильмы\100.txt', 'r')

        for line in file:
            digit = int(line)
            print(digit)
        file.close()
    except ValueError as err:
        print(err)


# read_some_1232()

def summa_chisel():
    total = 0
    try:
        file = open(r'D:Фильмы\100.txt', 'r')

        for line in file:
            digit = int(line)
            total += digit

        file.close()
        print(total)
    except ValueError as err:
        print(err)


# summa_chisel()


# Напишите программу, которая открывает файл вывода number_list.txt, но не стирает содержимое
# файла, если он уже существует.

def open_134():
    try:
        file = open(r'D:Фильмы\100.txt', 'a')

        file.close()

    except IOError as err:
        print(err)


# open_134()


# На диске существует файл students. txt. Он содержит несколько записей, и каждая запись
# имеет два поля: имя студента и оценку студента за итоговый экзамен. Напишите программу,
# которая удаляет запись с именем студента "Джон Перц".
import os


def delete_str():
    # эта программа позволяет удалить запись из файла

    # создаем булевую переменную для использования ее в качестве флага:
    found = False

    # получить строку,которую нужно удалить:
    search = input("какую строку будем удалять? ")

    # открываем файл:
    file = open(r'D:Фильмы\100.txt', 'r')

    # открываем временный файл:
    temp_file = open(r'D:Фильмы\temp_100.txt', 'w')

    # прочитать поле с описанием первой записи:
    name = file.readline()

    # прочитать остаток файла:
    while name != "":
        ocenka = int(file.readline())

        # удалить перенос из описания:
        name = name.rstrip('\n')

        # если эта запись не предназначена для удаления,
        # то записать ее во временный файл:
        if search == name:
            temp_file.write(name + '\n')
            temp_file.write(str(ocenka) + '\n')
        else:
            # назначить флагу значение True:
            found = True

        # прочитать первую строчку еще раз:
        name = file.readline()

        # закрыть оба файла:
        file.close()
        temp_file.close()

        # удаляем исходный файл:
        os.remove('100.txt')

        # переименовываем файлы:
        os.rename('temp_100.txt', '100.txt')


# delete_str()

# Вывод на экран верхней части файла. Напишите программу, которая запрашивает
# у пользователя имя файла. Программа должна вывести на экран только первые пять строк
# содержимого файла. Если в файле меньше пяти строк, то она должна вывести на экран
# все содержимое файла.

def first():
    try:
        file_name = input("Введи имя файла,который будем открывать: ")

        file = open(rf'D:\Фильмы\{file_name}', 'r')

        for line in range(1, 6):
            digit = int(line)

            print(digit)

        file.close()

    except Exception as err:
        print(err)


# first()

# Номера строк. Напишите программу, которая запрашивает у пользователя имя файла.
# Программа должна вывести на экран содержимое файла, при этом каждая строка должна
# предваряться ее номером и двоеточием. Нумерация строк должна начинаться с 1.
def second():
    try:
        file_name = input("Введи название файла: ")
        file = open(rf'D:\Фильмы\{file_name}.txt', 'r')

        str_number = 0

        for stroka in file:
            digit = float(stroka)
            str_number += 1

            print(f"{str_number}:{digit}")
        file.close()
    except ValueError as err:
        print(err)


# second()


# Счетчик значений. Допустим, что файл с серией имен (в виде строковых значений)
# называется names.txt и существует на диске компьютера. Напишите программу, которая
# показывает количество хранящихся в файле имен. (Подсказка: откройте файл и прочитайте
# каждую хранящуюся в нем строку . Примените переменную для подсчета количества
# прочитанных из файла значений.)

def third():
    try:
        name_file = input("Введи имя файла: ")
        file = open(rf'D:\Фильмы\{name_file}.txt', 'r')
        count = 0
        for line in file:
            stroka = str(line)
            count += 1
        file.close()
        print(f"Количество хранящихся имен в файле{name_file}={count}")
    except ValueError as err:
        print(err)
    except IOError as err_2:
        print(err_2)


# third()


# Сумма чисел. Допустим, что файл с рядом целых чисел называется numbers .txt и существует
# на диске компьютера. Напишите программу, которая читает все хранящиеся
# в файле числа и вычисляет их сумму.

def fourth():
    try:
        file_name = input("Введи имя файла: ")
        file = open(rf'D:\Фильмы\{file_name}.txt', 'r')

        total_sum = 0

        for line in file:
            digit = int(line)
            total_sum += digit

        file.close()
        print(f"Сумма всех чисел в файле равна: {total_sum}")
    except IOError as err:
        print(err)
    except ValueError as err_2:
        print(err_2)


# fourth()


# Среднее арифметическое чисел. Допустим, что файл с рядом целых чис~л называется
# numbers.txt и существует на диске компьютера. Напишите программу, которая вычисляет
# среднее арифметическое всех хранящихся в файле чисел.

def fifth():
    try:
        file_name = input("Введи имя файла: ")
        file = open(rf"D:\Фильмы\{file_name}.txt", 'r')
        count = 0
        total = 0
        for line in file:
            digit = int(line)
            count += 1
            total += digit

        file.close()
        result = total / count
        print(f"Среднее арифметическое чисел в файле {file_name} равно {result}")
    except ValueError as err:
        print(err)
    except IOError as err_2:
        print(err_2)


# fifth()


# Программа записи файла со случайными числами. Напишите программу, которая
# пишет в файл ряд случайных чисел . Каждое случайное число должно быть в диапазоне
# от 1 до 500. Приложение должно предоставлять пользователю возможность назначать
# количество случайных чисел, которые будут содержаться в файле.
import random


def sixth():
    try:
        file = open(r'D:\Фильмы\случайные.txt', 'w')
        count = int(input("Какое количество случайных чисел ты хочешь записать?"))
        for digit in range(1, count + 1):
            digit = random.randint(1, 500)
            file.write(str(digit) + '\n')

        file.close()

    except ValueError as err:
        print(err)


# sixth()


# Программа чтения файлов со случайными числами. Выполнив предыдущее задание
# (программу записи файла со случайными числами), напишите еще одну программу, которая
# читает случайные числа из файла, выводит их на экран и затем показывает приведенные
# ниже данные:
# • сумму чисел;
# • количество случайных чисел, прочитанных из файла.

def seventh():
    total = 0
    count = 0
    try:
        file = open(r'D:\Фильмы\случайные.txt', 'r')
        for line in file:
            digit = int(line)
            total += digit
            count += 1
            print(digit)
        file.close()
        print(f"Всего случайных чисел: {count}")
        print(f"Сумма случайных чисел равна: {total}")
    except ValueError as err:
        print(err)
    except IOError as err_2:
        print(err_2)


# seventh()


# Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные.
# Президент клуба попросил вас написать две программы:
# • программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиатуры,
# и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь
# поле для имени игрока и поле для счета игрока);
# • программу, которая читает записи из файла golf.txt и выводит их на экран.

def eighth():
    try:
        answer = "y"

        file = open(r'D:\Фильмы\golf.txt', 'w')

        while answer == "y" or answer == "Y":
            name = input("Введи имя игрока: ")
            scored_points = int(input(f"Сколько очков набрал {name}: "))

            file.write(name + '\n')
            file.write(str(scored_points) + '\n')

            answer = input("Для продолжения ввода нажми 'y'или'Y': ")

        file.close()
    except IOError as err:
        print(err)
    except ValueError as err_2:
        print(err_2)


# eighth()


def ninth():
    try:
        file = open(r'D:\Фильмы\golf.txt', 'r')

        name = file.readline()
        while name != "":
            scored_points = int(file.readline())

            name = name.rstrip("\n")

            print(name)
            print(scored_points)
            print()

            name = file.readline()

        file.close()
    except IOError as err:
        print(err)
    except ValueError as err_2:
        print(err_2)


# ninth()


# Среднее количество шагов. Браслет для занятий спортом - это носимое устройство,
# которое отслеживает вашу физическую активность, количество сожженных калорий,
# сердечный ритм, модели сна и т. д. Одним из самых распространенных видов физический
# активности, который отслеживает большинство таких устройств, является количество
# шагов, которые вы делаете каждый день.
# Среди исходного кода главы 6, а также в подпапке data "Решений задач по программированию"
# соответствующей главы, вы найдете файл steps.txt. Файл steps.txt содержит количество
# шагов, которые человек делал каждый день в течение года. В файле имеется
# 365 строк, и каждая строка содержит количество шагов, сделанных в течение дня. (Первая
# строка- это число шагов, сделанных 1-го января, вторая строка- число шагов,
# сделанных 2 января и т. д.) Напишите программу, которая читает файл и затем выводит
# среднее количество шагов, сделанных в течение каждого месяца. (Данные были записаны
# в год, который не был високосным, и поэтому февраль имеет 28 дней.)

import random


def shagomer():
    try:
        file = open(r'D:\Фильмы\steps.txt', 'w')

        for day in range(1, 366):
            step = random.randint(1000, 8000)
            file.write(str(step) + '\n')

        file.close()
    except ValueError as err:
        print(err)
    except IOError as err_2:
        print(err_2)


#shagomer()


def read_shagomer():
    try:
        file=open(r'D:\Фильмы\steps.txt', 'r')
        # просчет для января:
        jan_sum=0
        days=31
        for line in range(1, 32):
            step=int(file.readline())
            jan_sum+=step
            middle_jan=jan_sum/days
        # просчет для февраля:
        feb_sum = 0
        days = 28
        for line in range(32, 61):
            step = int(file.readline())
            feb_sum += step
            middle_feb = feb_sum / days
        # просчет для марта:
        march_sum = 0
        days = 31
        for line in range(61, 93):
            step = int(file.readline())
            march_sum += step
            middle_march = march_sum / days
        # просчет для апреля:
        april_sum = 0
        days = 30
        for line in range(93, 124):
            step = int(file.readline())
            april_sum += step
            middle_april = april_sum / days
        # просчет для мая:
        may_sum = 0
        days = 31
        for line in range(124, 156):
            step = int(file.readline())
            may_sum += step
            middle_may = may_sum / days
        # просчет для июня:
        june_sum = 0
        days = 30
        for line in range(156, 187):
            step = int(file.readline())
            june_sum += step
            middle_june = june_sum / days
        # просчет для июля:
        july_sum = 0
        days = 31
        for line in range(187, 219):
            step = int(file.readline())
            july_sum += step
            middle_july = july_sum / days
        # просчет для августа:
        august_sum = 0
        days = 31
        for line in range(219, 251):
            step = int(file.readline())
            august_sum += step
            middle_august = august_sum / days
        # просчет для сентября:
        sep_sum = 0
        days = 30
        for line in range(251, 282):
            step = int(file.readline())
            sep_sum += step
            middle_sep = sep_sum / days
        # просчет для октября:
        okt_sum = 0
        days = 31
        for line in range(282, 314):
            step = int(file.readline())
            okt_sum += step
            middle_okt = okt_sum / days
        # просчет для ноября:
        nov_sum = 0
        days = 30
        for line in range(314, 345):
            step = int(file.readline())
            nov_sum += step
            middle_nov = nov_sum / days
        # просчет для декабря:
        dec_sum = 0
        days = 31
        for line in range(345, 365):
            step = int(file.readline())
            dec_sum += step
            middle_dec = dec_sum / days

        file.close()
        print("Среднее количество шагов в январе:",middle_jan)
        print("Среднее количество шагов в феврале:", middle_feb)
        print("Среднее количество шагов в марте:", middle_march)
        print("Среднее количество шагов в апреле:", middle_april)
        print("Среднее количество шагов в мае:", middle_may)
        print("Среднее количество шагов в июне:", middle_june)
        print("Среднее количество шагов в июле:", middle_july)
        print("Среднее количество шагов в августе:", middle_august)
        print("Среднее количество шагов в сентябре:", middle_sep)
        print("Среднее количество шагов в октябре:", middle_okt)
        print("Среднее количество шагов в ноябре:", middle_nov)
        print("Среднее количество шагов в декабре:", middle_dec)
    except ValueError as err:
        print(err)
    except IOError as err_2:
        print(err_2)
#read_shagomer()