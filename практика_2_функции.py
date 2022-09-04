# ОТРАБОТАЕМ НАВЫКИ ПРИМИНЕНИЯ ФУНКЦИЙ И МОДУЛЕЙ!

def times_ten(some_argument):
    """Напишите функцию с именем times ten. Эта функция должна принимать аргумент и показывать
результат произведения аргумента на 1 О.

    :return:
    """
    result = some_argument * 10
    print("Результат равен ", result)


# times_ten(15)


def show_value(quantity):
    """Исследуйте приведенный ниже заголовок функции, затем напишите инструкцию, которая
вызывает эту функцию, передавая 12 в качестве аргумента.
def show_value(quantity):

    :param quantity:
    :return:
    """


# show_value(12)


def my_function(a=2, b=4, c=6):
    """
    Взгляните на приведенное ниже определение функции my_func:
def my_function(a, Ь, с):
d = (а + с) / Ь
print (d)
• Напишите инструкцию, которая вызывает эту функцию и применяет именованные
аргументы для передачи 2 в а, 4 в ь и 6 в с.
• Какое значение будет показано, когда исполнится вызов функции?
    :return:
    """
    d = (a + c) / b
    print(d)


# my_function()


# Напишите инструкцию, которая генерирует случайное число в диапазоне от 1 до 100
# и присваивает его переменной с именем rand.
import random


def some_1():
    rand = random.randint(1, 100)
    print(rand)


# some_1()


# Приведенная ниже инструкция вызывает функцию half, возвращающую значение, которое
# вдвое меньше аргумента. (Допустим, что переменная numЬer ссылается на вещественное
# значение с типом float.) Напишите код для этой функции.
# result = half(numЬer)

def half(number):
    return number / 2


# result=half(50)
# print(result)

# Программа содержит приведенное ниже определение функции:
# def cube (num) :
# return num * num * num
# Напишите инструкцию, которая передает значение 4 в эту функцию и присваивает
# возвращаемое ею значение переменной resul t.
def cube(num):
    return num * num * num


# result=cube(4)
# print(result)

# Напишите функцию times_ten, которая принимает numЬer в качестве аргумента. Когда
# функция вызывается, она должна возвращать значение ее аргумента, умноженное на 1 О.

def times_teen(number):
    result = number * 10
    # print(result)


# times_teen(22)


# Напишите функцию get_first_name, которая просит пользователя ввести свое имя и его
# возвращает.

def get_first_name():
    name = input("Enter your name: ")
    return name


# Конвертер километров. Напишите программу, которая просит пользователя ввести расстояние
# в километрах и затем это расстояние преобразует в мили. Формула преобразования:
# мили = километры х 0.6214.
def converter():
    kilometers = float(input("Enter kilometers: "))
    mili = kilometers * 0.6214
    print(format(mili, '.2f'))


# converter()


# Какова стоимость страховки? Многие финансовые эксперты рекомендуют собственникам
# недвижимого имущества страховать свои дома или здания как минимум на 80% суммы
# замещения строения. Напишите программу, которая просит пользователя ввести
# стоимость строения и затем показывает минимальную страховую сумму, на которую он
# должен застраховать недвижимое имущество.
def strahovka():
    stoimost_stroeniya = float(input("Стоимость строения здания?"))
    min_strahovka = stoimost_stroeniya * 0.8
    print("Минимальная сумма,на которую нужно застраховать имущество: ", min_strahovka, "грн")


# strahovka()


# Расходы на автомобиль. Напишите программу, которая просит пользователя ввести
# месячные расходы на следующие нужды, связанные с его автомобилем: платеж по кредиту,
# страховка, бензин, машинное масло, шины и техобслуживание. Затем программа
# должна показать общую месячную стоимость и общую годовую стоимость этих расходов.
def main_rashodi():
    kredit = platej_po_kredity()
    strahovka = platej_po_strahovke()
    benzin = platej_za_benzin()
    maslo = platej_za_maslo()
    shini = platej_za_shini()
    teh = platej_za_tehobsluj()
    total_per_month = kredit + strahovka + benzin + maslo + shini + teh
    total_year = total_per_month * 12
    print("Суммарные расходы на машину в месяц составляют:", total_per_month, "грн")
    print("Суммарные расходы на машину в год составляют:", total_year, "грн")


def platej_po_kredity():
    sum_kredit = float(input("Какая сумма платежа по кредиту в месяц? "))
    return sum_kredit


def platej_po_strahovke():
    sum_strahovka = float(input("Какая сумма платежа по страховке в месяц? "))
    return sum_strahovka


def platej_za_benzin():
    sum_benzin = float(input("Какая сумма платежа за бензин в месяц? "))
    return sum_benzin


def platej_za_maslo():
    sum_maslo = float(input("Какая сумма платежа за масло в месяц? "))
    return sum_maslo


def platej_za_shini():
    sum_shini = float(input("Какая сумма платежа за шины в месяц? "))
    return sum_shini


def platej_za_tehobsluj():
    sum_teh = float(input("Какая сумма платежа за техобслуживание в месяц? "))
    return sum_teh


# main_rashodi()


# Налог на недвижимое имущество. Муниципальный округ собирает налоги на недвижимое
# имущество на основе оценочной стоимости имущества, составляющей 60% его фактической
# стоимости. Например, если акр земли оценен в 1 О ООО долларов, то его оценочная
# стоимость составит 6000 долларов. В этом случае налог на имущество составит
# 72 цента за каждые 100 долларов оценочной стоимости. Налог на акр, оцененный
# в 6000 долларов, составит 43,20 доллара. Напишите программу, которая запрашивает
# фактическую стоимость недвижимого имущества и показывает оценочную стоимость и
# налог на имущество.
OCENKA = 0.6
TAX = 0.0072


def main_tax():
    price_nedvij = float(input("Введите фактическиую стоимость недвижимого имущества: "))
    price_ocen = ocenochnaya_stoimost(price_nedvij)
    print("Оценочная стоимость недвижимого имущества равна: ", price_ocen, "usd")
    nalog = nalog_na_imyshestvo(price_ocen)
    print("Налог на имущество составит: ", format(nalog, '.2f'), "usd")


def ocenochnaya_stoimost(fact_price):
    return fact_price * OCENKA


def nalog_na_imyshestvo(acr_nedvijimosti):
    return acr_nedvijimosti * TAX


# main_tax()


# Калории за счет жиров и углеводов. Диетолог работает в спортивном клубе и дает
# рекомендации клиентам в отношении диеты. В рамках своих рекомендаций он запрашивает
# у клиентов количество граммов жиров и углеводов, которые они употребили за день.
# Затем на основе приведенной ниже формулы он вычисляет количество калорий, которые
# получаются в результате употребления жиров:
# калории от жиров = граммы жиров х 9.
# Затем на основе еще одной формулы он вычисляет количество калорий, которые получаются
# в результате употребления углеводов:
# калории от углеводов = граммы углеводов х 4.
# Диетолог просит вас написать программу, которая выполнит эти расчеты.
KOEF_JIR = 9
KOEF_UGLEVOD = 4


def main_dietolog():
    print("Эта программа будет подсчитывать количество употребляемых калорий для жиров и углеводов.")
    name = input("Твое имя: ")
    kolichestvo_jir = float(input("Сколько жиров употребил за день: "))
    kolichestvo_uglevod = float(input("Сколько углеводов употребил за день: "))
    jir = kalorii_jiri(kolichestvo_jir)
    uglevod = kalorii_uglevod(kolichestvo_uglevod)
    print(f"За день {name} упортребил: {jir + uglevod} калорий!")


def kalorii_jiri(jir_gram):
    return jir_gram * KOEF_JIR


def kalorii_uglevod(uglevod_gram):
    return uglevod_gram * KOEF_UGLEVOD


# main_dietolog()


# Сидячие места на стадионе. На стадионе имеется три категории сидячих мест. Места
# класса А стоят 20 долларов, места класса В - 15 долларов и места класса С - 1 О долларов.
# Напишите программу, которая запрашивает, сколько билетов каждого класса было
# продано, и затем выводит сумму дохода, полученного за счет продажи билетов.
TIKETS_A = 20
TIKETS_B = 15
TIKETS_C = 10


def main_stadion():
    tikets_a = class_a()
    tikets_b = class_b()
    tikets_c = class_c()
    total_sold = tikets_a + tikets_b + tikets_c
    print("Всего стадион заработал на билетах: ", total_sold, "usd")


def class_a():
    tikets = int(input("Сколько было продано билетов класса А? "))
    return tikets * TIKETS_A


def class_b():
    tikets = int(input("Сколько было продано билетов класса B? "))
    return tikets * TIKETS_B


def class_c():
    tikets = int(input("Сколько было продано билетов класса C? "))
    return tikets * TIKETS_C


# main_stadion()


# Оценщик малярных работ. Малярная компания установила, что на каждые 10 квадратных
# метров поверхности стены требуется 5 литров краски и 8 часов работы. Компания
# взимает за работу 2000 руб. в час. Напишите программу, которая просит пользователя
# ввести площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски.
# Программа должна показать следующие данные:
# • количество требующихся емкостей краски;
# • количество требующихся рабочих часов;
# • стоимость краски;
# • стоимость работы;
# • общая стоимость малярных работ.

RAZMERNOST_METROV = 10
BANKA_KRASKI = 5
RABOCHIE_CHASI = 8
STOIMOST_RABOT_VCHAS = 2000


def main_remont():
    ploshad_pokraski = ploshad_rabot()
    cena_kraski = price_kraska()
    kol_vo_banok = skolko_banok(ploshad_pokraski)
    print(f"Для покраски помещения площадью {ploshad_pokraski} м требуется", format(kol_vo_banok, '.2f'), "банок")
    kol_vo_rab_chasov = skolko_rabotat(ploshad_pokraski)
    print(f"Для  помещения площадью {ploshad_pokraski} м потребуется работать: ", kol_vo_rab_chasov, "часов")
    summa_kraski = stoiost_kraski(cena_kraski, kol_vo_banok)
    print(f"Общая сумма затрат на красску составляет: {summa_kraski} грн")
    cena_raboti = stoimost_rabot(kol_vo_rab_chasov)
    print(f"Общая стоимость выполненной работы составляет: {cena_raboti} грн")
    total_sum = summa_kraski + cena_raboti
    print(f"Всего на ремонт помещения ты потратишь: {total_sum} грн")


def ploshad_rabot():
    # запросим площадь поверхности для покраски:
    square = float(input("Введи площадь поверхности: "))
    return square


def price_kraska():
    # запросим стоимость пятилитровой банки краски:
    price_bottle = float(input("введи цену 1 банки краски: "))
    return price_bottle


# рассчитаем количество требующихся емкостей краски:
def skolko_banok(ploshad):
    return ploshad / RAZMERNOST_METROV


# • количество требующихся рабочих часов
def skolko_rabotat(ploshad):
    return (ploshad / RAZMERNOST_METROV) * RABOCHIE_CHASI


# • стоимость краски
def stoiost_kraski(cena, kolichestvo):
    return cena * kolichestvo


# • стоимость работы;
def stoimost_rabot(vremya):
    return vremya * STOIMOST_RABOT_VCHAS


# main_remont()


# Месячный налог с продаж. Розничная компания должна зарегистрировать отчет о месячном
# налоге с продаж с указанием общего налога с продаж за месяц и взимаемых сумм
# муниципального и федерального налогов с продаж. Федеральный налог с продаж составляет
# 5%, муниципальный налог с продаж - 2,5%. Напишите программу, которая просит
# пользователя ввести общий объем продаж за месяц. Из этого значения приложение должно
# рассчитать и показать:
# • сумму муниципального налога с продаж;
# • сумму федерального налога с продаж;
# • общий налог с продаж (муниципальный плюс федеральный).

FEDERAL_TAX = 0.05
MUNICIPAL_TAX = 0.025


def main_taxes():
    total_sales = float(input("Введите общий объем продаж магазина: "))
    federal_nalog = fed_nal(total_sales)
    print(f"Сумма федерального налога равна: {federal_nalog} грн")
    municipal_nalog = mun_nal(total_sales)
    print(f"Сумма муниципального налога равна: {municipal_nalog} грн")
    total_taxes = federal_nalog + municipal_nalog
    print(f"Обзий налог с продаж составляет: {total_taxes} грн")


def fed_nal(sales):
    return sales * FEDERAL_TAX


def mun_nal(sales):
    return sales * MUNICIPAL_TAX


# main_taxes()


# Футы в дюймы. Один фут равняется 12 дюймам. Напишите функцию feet to inches,
# которая в качестве аргумента принимает количество футов и возвращает количество
# дюймов в этом количестве футов. Примените эту функцию в программе, которая предлагает
# пользователю ввести количество футов и затем показывает количество дюймов
# в этом количестве футов.

SIZE_KOEF = 12


def main_size():
    kol_vo_futov = float(input("Введи количество футов: "))
    dyimi = exchange_sizes(kol_vo_futov)
    print(f"Количество дюймов равняется {dyimi}")


def exchange_sizes(futs):
    return futs * SIZE_KOEF


# main_size()


# Математический тест. Напишите программу, которая позволяет проводить простые
# математические тесты. Она должна показать два случайных числа, которые должны
# быть просуммированы вот так:
# 247
# + 129
# Эта программа должна давать обучаемому возможность вводить ответ. Если ответ правильный,
# то должно быть показано поздравительное сообщение. Если ответ неправильный,
# то должно быть показано сообщение с правильным ответом.
import random


def random_sum():
    cont = "y"
    while cont == "y":
        chislo_1 = random.randint(1, 1000)
        chislo_2 = random.randint(1, 1000)
        sum_chisel = chislo_1 + chislo_2
        print(chislo_1)
        print("+", chislo_2)
        answer = int(input("Введи ответ: "))
        if answer == sum_chisel:
            print("Молодец! Ответ правильный!")
        else:
            print(f"Ответ неправильный...вот такой он должен быть:{sum_chisel}")
        cont = input("Нажми у для продолжения тестирования!")
    print("Программа завершена")


# random_sum()


# Максимальное из двух значений. Напишите функцию max, которая в качестве аргументов
# принимает два целочисленных значения и возвращает значение, которое является
# большим из двух. Например, если в качестве аргументов переданы 7 и 12, то функция
# должна вернуть 12. Примените функцию в программе, которая предлагает пользователю
# ввести два целочисленных значения. Программа должна показать большее значение из
# двух.

def max_chislo():
    chislo_1 = int(input("Введи первое число: "))
    chislo_2 = int(input("Введи второе число: "))
    result = sravnenie(chislo_1, chislo_2)
    print(f"Большее число: {result}")


def sravnenie(digit_1, digit_2):
    return max(digit_1, digit_2)


# max_chislo()


# Высота падения. При падении тела под действием силы тяжести для определения расстояния,
# которое тело пролетит за определенное время, применяется формула:
# d= 1/2gt2,
# где d- расстояние, м; g = 9.8, м/с2 ; t- время падения тела, с.
# Напишите функцию falling dtstance, которая в качестве аргумента принимает время
# падения тела (в секундах). Функция должна вернуть расстояние в метрах, которое тело
# пролетело во время этого промежутка времени. Напишите программу, которая вызывает
# эту функцию в цикле, передает значения от 1 до 1 О в качестве аргументов и показывает
# возвращаемое значение.

G = 9.8


def main_falling():
    rasstoyanie = 0
    vremya = float(input("Сколько тело падает? "))
    for i in range(1, 10):
        rasstoyanie += count_distance(vremya)
        print(i, format(rasstoyanie, '.2f'))


def count_distance(time):
    distance = 1 / 2 * G * time ** 2
    return distance


# main_falling()


# Кинетическая энергия. Из физики известно, что движущееся тело имеет кинетическую
# энергию. Приведенная ниже формула может использоваться для определения кинетической
# энергии движущегося тела:
# КЕ = 1/2mv2,
# где КЕ - это кинетическая энергия; т - масса тела, кг; v - скорость тела, м/с.
# Напишите функцию kinetic energy, которая в качестве аргументов принимает массу
# тела (в килограммах) и его скорость (в метрах в секунду). Данная функция должна
# вернуть величину кинетической энергии этого тела. Напишите программу, которая просит
# пользователя ввести значения массы и скорости, а затем вызывает функцию
# kinetic energy, чтобы получить кинетическую энергию тела.

def energy():
    massa_tela = float(input("Введи значение массы тела: "))
    skorost = float(input("Введи значение скорости тела: "))
    energy = kinetic_energy(massa_tela, skorost)
    print(f"Кинетическая энергия тела равна: {energy}")


def kinetic_energy(massa, speed):
    return (1 / 2) * massa * speed ** 2


# energy()


def main_grade():
    """
    Напишем Средний балл и его уровень. Напишите программу, которая просит пользователя ввести
пять экзаменационных оценок. Программа должна показать буквенный уровень
оценки для каждой оценки и средний балл. Напишите в программе приведенные ниже
функции:
• calc average
• determine grade
    :return: None
    """
    # попросим поьзователя ввести пять экзаменационных оценок:
    ocenka1 = int(input("Введи первую оценку: "))
    ocenka2 = int(input("Введи вторую оценку: "))
    ocenka3 = int(input("Введи третью оценку: "))
    ocenka4 = int(input("Введи четвретую оценку: "))
    ocenka5 = int(input("Введи пятую оценку: "))
    # выведем для каждой оценки буквенный уровень:
    bukv_yroven = determine_grade(ocenka1)
    print(f"GRADE = {ocenka1} - level {bukv_yroven}")
    bukv_yroven = determine_grade(ocenka2)
    print(f"GRADE = {ocenka2} - level {bukv_yroven}")
    bukv_yroven = determine_grade(ocenka3)
    print(f"GRADE = {ocenka3} - level {bukv_yroven}")
    bukv_yroven = determine_grade(ocenka4)
    print(f"GRADE = {ocenka4} - level {bukv_yroven}")
    bukv_yroven = determine_grade(ocenka5)
    print(f"GRADE = {ocenka5} - level {bukv_yroven}")
    # выведем среднюю оценку:
    sredn_ocenka = calc_average(ocenka1, ocenka2, ocenka3, ocenka4, ocenka5)
    print(f"YOUR MIDDLE LEVEL = {sredn_ocenka}")
    print("FINISH")


def calc_average(grade_1, grade_2, grade_3, grade_4, grade_5):
    kolichestvo_ocenok = 5
    """функция должна принимать в качестве аргументов пять оценок и
возвращать средний балл;

    :return: middle_grade
    """
    return (grade_1 + grade_2 + grade_3 + grade_4 + grade_5) / kolichestvo_ocenok


def determine_grade(grade):
    """функция должна принимать в качестве аргумента оценку и возвращать
буквенный уровень оценки, опираясь на приведенную в табл. 5.3 классификации.

    :return: level_class
    """
    if grade >= 90:
        level_class = "A"
    elif 90 > grade >= 80:
        level_class = "B"
    elif 90 > grade >= 70:
        level_class = "C"
    elif 70 > grade >= 60:
        level_class = "D"
    else:
        level_class = "F"
    return level_class


# main_grade()


# Счетчик четных/нечетных чисел. В этой главе вы увидели пример написания алгоритма,
# который определяет четность или нечетность числа. Напишите программу, которая
# генерирует 100 случайных чисел и подсчитывает количество четных и нечетных
# случайных чисел.
import random

count_nechet = 0


def main_schet_chisel():
    for count in range(100):
        chisla = random.randint(1, 100)
        total_sum_chet = 0
        total_sum_nechet = 0
        if chisla % 2 == 0:
            total_sum_chet += chisla
            print(f"ЧЕТНЫХ ЧИСЕЛ:{total_sum_chet} ")
        else:
            total_sum_nechet += chisla
            print(f"НЕЧЕТНЫХ ЧИСЕЛ:{total_sum_nechet}")


# main_schet_chisel()


# Простые числа. Простое число - это число, которое делится без остатка на само себя
# и 1. Например, число 5 является простым, потому что оно делится без остатка только
# на 1 и 5. Однако число 6 не является простым, потому что оно делится без остатка на 1,
# 2, 3 и 6.
# Напишите булеву функцию is prime, которая в качестве аргумента принимает целое
# число и возвращает истину, если аргумент является простым числом, либо ложь в противном
# случае. Примените функцию в программе, которая предлагает пользователю ввести
# число и затем выводит сообщение с указанием, является ли это число простым.
def main_prostie_chisla():
    number = int(input("Введи любое целое число: "))
    proverka = is_prime(number)


def is_prime(chislo):
    delitel = 2
    while chislo % delitel != 0:
        delitel += 1
        return chislo == delitel
    else:
        return chislo != delitel


# main_prostie_chisla()


# Список простых чисел. Это упражнение предполагает, что вы уже написали функцию
# is pr ime в задаче 17. Напишите еще одну программу, которая показывает все простые
# числа от 1до100. Программа должна иметь цикл, который вызывает функцию is prime.

def perebor():
    for i in range(1, 101):
        chet_nechet = is_prime_1(i)
        print(i, "-", chet_nechet)


def is_prime_1(chislo):
    delitel = 2
    while chislo % delitel != 0:
        delitel += 1
        return delitel == chislo
    else:
        return delitel != chislo


# perebor()

def main_prost_chisla():
    kon_chislo = int(input("Введи предел чисел: "))
    for chislo in range(2, kon_chislo):
        if prostoe(chislo) == True:
            print(chislo)


def prostoe(chislo):
    for delitel in (2, int(chislo ** 0.5) + 1):
        if chislo % delitel == 0:
            return False
    return True


# main_prost_chisla()


# Будущая стоимость. Предположим, что на вашем сберегательном счете есть определенная
# сумма денег, и счет приносит составной ежемесячный процентный доход. Вы хотите
# вычислить сумму, которую будете иметь после определенного количества месяцев.
# Формула приведена ниже:
# F = Р х ( 1 + i)2,
# 300 Глава 5. Функции
# где F - будущая сумма на счете после указанного периода времени; Р - текущая сумма
# на счете; i - ежемесячная процентная ставка; t - количество месяцев.
# Напишите программу, которая предлагает пользователю ввести текущую сумму на счете,
# ежемесячную процентную ставку и количество месяцев, в течение которых деньги
# будут находиться на счете. Программа должна передать эти значения в функцию, которая
# возвращает будущую сумму на счете после заданного количества месяцев. Программа
# должна показать будущую сумму на счете.

def main_bank():
    tekyshaya_summa = float(input("Введите текущую сумму на счете: "))
    proc_stavka = float(input("Введите ежемесячную процентную ставку: "))
    kol_mesyac = int(input("Введите количество месяцев: "))
    budushie_dengi = calc_bank(tekyshaya_summa, kol_mesyac, proc_stavka)
    print(f"Будущая сумма составляет: {budushie_dengi} грн")


def calc_bank(present_money, time, percent):
    future_money = present_money * (time + percent) ** 2
    return future_money


# main_bank()


# Игра в угадывание случайного числа. Напишите программу, которая генерирует случайное
# число в диапазоне от 1 до 100 и просит пользователя угадать это число. Если догадка
# пользователя больше случайного числа, то программа должна вывести сообщение
# "Слишком много, попробуйте еще раз". Если догадка меньше случайного числа, то программа
# должна вывести сообщение "Слишком мало, попробуйте еще раз". Если пользователь
# число угадывает, то приложение должно поздравить пользователя и сгенерировать
# новое случайное число, чтобы возобновить игру.
# Необязательное улучшение: улучшите игру, чтобы она вела подсчет догадок, которые
# делает пользователь. Когда пользователь угадывает случайное число правильно, программа
# должна показать количество догадок.
import random


def main_ugaday_chislo():
    # переменная для управления циклом:
    your_try = 0
    chislo = 0
    while your_try == chislo:
        chislo = random.randint(1, 100)
        print(chislo)
        your_try = int(input("Enter digit: "))
        if your_try > chislo:
            print("Слишком много, попробуйте еще раз")
        else:
            print("Слишком мало, попробуйте еще раз")


# main_ugaday_chislo()


# Игра "Камень, ножницы, бумага". Напишите программу, которая дает пользователю
# возможность поиграть с компьютером в игру "Камень, ножницы, бумага". Программа
# должна работать следующим образом:
# 1. Когда программа запускается, генерируется случайное число в диапазоне от 1 до 3.
# Если число равняется 1, то компьютер выбрал камень. Если число равняется 2, то
# компьютер выбрал ножницы. Если число равняется 3, то компьютер выбрал бумагу.
# (Пока не показывайте выбор компьютера.)
# 2. Пользователь вводит на клавиатуре выбранный вариант "камень", "ножницы" или
# "бумага".
# 3. Выбор компьютера выводится на экран.
# 4. Победитель выбирается согласно следующим правилам:
# 0 если один игрок выбирает камень, а другой игрок выбирает ножницы, то побеждает
# камень (камень разбивает ножницы);
# 0 если один игрок выбирает ножницы, а другой игрок выбирает бумагу, то побеждают
# ножницы (ножницы режут бумагу);
# 0 если один игрок выбирает бумагу, а другой игрок выбирает камень, то побеждает
# бумага (бумага заворачивает камень);
# 0 если оба игрока делают одинаковый выбор, то для определения победителя нужно
# сыграть повторный раунд.


import random


def main_igra():
    vibor_computera = 0
    vibor_polzovatelya = 0
    while vibor_polzovatelya == vibor_computera:
        chislo_computera = random.randint(1, 3)
        if chislo_computera == 1:
            vibor_computera = "камень"
        elif chislo_computera == 2:
            vibor_computera = "ножницы"
        else:
            vibor_computera = "бумага"
        vibor_polzovatelya = input("Вводи 'камень','ножницы'или 'бумага' : ")
        print("Выбор компьютера: ", vibor_computera)
    if vibor_computera == "камень" and vibor_polzovatelya == "ножницы":
        print("Победил компьютер!")
    elif vibor_polzovatelya == "камень" and vibor_computera == "ножницы":
        print("Победил пользователь!")
    elif vibor_computera == "ножницы" and vibor_polzovatelya == "бумага":
        print("Победил компьютер!")
    elif vibor_polzovatelya == "ножницы" and vibor_computera == "бумага":
        print("Победил пользователь!")
    elif vibor_computera == "бумага" and vibor_polzovatelya == "камень":
        print("Победил компьютер!")
    elif vibor_polzovatelya == "бумага" and vibor_computera == "камень":
        print("Победил пользователь!")


#main_igra()


# Черепашья графика: функция рисования треугольника. Напишите функцию
# triangle, которая использует библиотеку черепашьей графики для рисования треугольника
# (рис. 5.30). Функция должна принимать в качестве аргументов координаты Х и У
# сторон треугольника и цвет, которым треугольник должен быть заполнен. Продемонстрируйте
# эту функцию в программе.

import turtle

# для нижнего:
TOP_POINT_X = 0
TOP_POINT_Y = 0
LEFT_DOWN_X = -50
LEFT_DOWN_Y = -50
RIGHT_DOWN_X = 50
RIGHT_DOWN_Y = -50
# для верхнего:
DOWN_POINT_X = 0
DOWN_POINT_Y = 0
LEFT_TOP_X = -50
LEFT_TOP_Y = 50
RIGHT_TOP_X = 50
RIGHT_TOP_Y = 50


def main_treygolnik():
    # нарисуем нижний треугольник:
    liniya(TOP_POINT_X, TOP_POINT_Y, LEFT_DOWN_X, LEFT_DOWN_Y, "red")
    liniya(LEFT_DOWN_X, LEFT_DOWN_Y, RIGHT_DOWN_X, RIGHT_DOWN_Y, "red")
    liniya(RIGHT_DOWN_X, RIGHT_DOWN_Y, TOP_POINT_X, TOP_POINT_Y, "red")

    # нарисуем верхний треугольник:
    liniya(DOWN_POINT_X, DOWN_POINT_Y, LEFT_TOP_X, LEFT_TOP_Y, "blue")
    liniya(LEFT_TOP_X, LEFT_TOP_Y, RIGHT_TOP_X, RIGHT_TOP_Y, "blue")
    liniya(RIGHT_TOP_X, RIGHT_TOP_Y, DOWN_POINT_X, DOWN_POINT_Y, "blue")
def liniya(start_x, strat_y, end_x, end_y, color):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(start_x, strat_y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(end_x, end_y)
    turtle.end_fill()
#main_treygolnik()
#turtle.done()





# Черепашья графика: модульный снеговик. Напишите программу, которая использует
# черепашью графику для изображения снеговика (рис. 5.31). Помимо главной функции
# программа также должна иметь приведенные ниже функции:
# • drawвase - функция должна нарисовать основу снеговика, т. е. большой снежный ком
# внизу;
# • drawMidSection - функция должна нарисовать средний снежный ком;
# • drawArms - функция должна нарисовать руки снеговика;
# • drawHead - функция должна нарисовать голову снеговика, глаза, рот и другие черты
# лица по вашему усмотрению;
# • drawHat - эта функция должна нарисовать шляпу снеговика.


import turtle
def main_snegovik():
    turtle.speed(1)
    draw_base(0,-100,100)
    draw_mid_section(0,75,75)
    draw_arms(75,75,50,45,50,-75,75,50,45,50)
    draw_head(35,7)
    draw_hat()


def draw_base(base_x,base_y,base_radius):
    # рисуем основу снеговика ( большой снежный ком внизу ):
    # что нам нужно?
    # координаты круга и его потом зацентровать
    # радиус круга
    turtle.showturtle()
    turtle.penup()
    turtle.goto(base_x,base_y-base_radius)
    turtle.pendown()
    turtle.circle(base_radius)

    # нарисуем центральный ком снеговика:
def draw_mid_section(mid_x,mid_y,mid_radius):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(mid_x, mid_y - mid_radius)
    turtle.pendown()
    turtle.circle(mid_radius)

    #нарисуем руки снеговика:
    # нарисуем руки:
def draw_arms(pravaya_ruka_x,pravaya_ruka_y,
              right_ruka_distance,pravaya_gradus,
              rigt_plecho_distance,
              lev_ruka_x, lev_ruka_y,
              lev_ruka_distance,lev_gradus,lev_plecho_distance):
    # координаты откуда выходит правая рука
    # две линии для пальцев
    # координаты левой руки
    # нарисуем преплечье
    # две линии для пальцев
    turtle.showturtle()
    turtle.penup()
    turtle.goto(pravaya_ruka_x,pravaya_ruka_y)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(right_ruka_distance)
    turtle.left(pravaya_gradus)
    turtle.forward(rigt_plecho_distance)
    turtle.right(25)
    turtle.forward(10)
    turtle.back(10)
    turtle.left(25)
    turtle.forward(10)
    #для левой руки
    turtle.showturtle()
    turtle.penup()
    turtle.goto(lev_ruka_x, lev_ruka_y)
    turtle.pendown()
    turtle.forward(lev_ruka_distance)
    turtle.left(lev_gradus)
    turtle.forward(lev_plecho_distance)
    turtle.right(25)
    turtle.forward(10)
    turtle.back(10)
    turtle.left(25)
    turtle.forward(10)


    # нарисуем голову снеговика(глаза+рот):

def draw_head(head_radius,eye_radius):
    turtle.showturtle()
    turtle.penup()
    turtle.home()
    turtle.goto(0,185-head_radius)
    turtle.pendown()
    turtle.circle(head_radius)
    # рисуем глаза
    turtle.penup()
    turtle.goto(10,195-eye_radius)
    turtle.pendown()
    turtle.circle(eye_radius)
    turtle.penup()
    turtle.home()
    turtle.goto(-10, 195 - eye_radius)
    turtle.pendown()
    turtle.circle(eye_radius)
    #рисуем рот:
    turtle.penup()
    turtle.home()
    turtle.goto(0,175)
    turtle.pendown()
    turtle.forward(10)
    turtle.back(20)
    turtle.penup()
    turtle.home()
# нарисуем шапку снеговика:
def draw_hat():
    turtle.goto(0,215)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()
    turtle.penup()
    turtle.home()


#main_snegovik()
#turtle.done()



# Черепашья графика: прямоугольный узор. В программе напишите функцию
# drawPattern, которая использует библиотеку черепашьей графики, чтобы нарисовать
# прямоугольный узор (рис. 5.32). Функция drawPattern должна принимать два аргумента:
# один из них задает ширину узора, другой- его высоту. (Пример, приведенный на
# рис. 5.32, показывает, как узор будет выглядеть, когда ширина и высота одинаковые.)
# Когда программа выполняется, она должна запросить у пользователя ширину и высоту
# узора и затем передать эти значения в качестве аргументов в функцию drawPattern.

import turtle
DISTANCE_1=100
DISTANCE_2=75
DISTANCE_3=125
DISTANCE_4=85
DISTANCE_5=75
DISTANCE_6=57
START_X=0
START_Y=0
def main_uzor():
    draw_pattern()
    kvadrat()
    turtle.home()
    zapoln_treug()

def draw_pattern():
    turtle.speed(9)
# начнем рисовать треугольник:
    for i in range(4):
        turtle.showturtle()
        turtle.forward(DISTANCE_1)
        turtle.left(90)
        turtle.forward(DISTANCE_2)
        turtle.left(180)
        turtle.right(53.13)
        turtle.forward(DISTANCE_3)
        turtle.right(126.87)

def kvadrat():
    for i in range(4):
        turtle.goto(START_X,START_Y)
        turtle.forward(85)
        turtle.left(90)
        turtle.forward(63)

def zapoln_treug():
    for i in range(4):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(38)
        turtle.end_fill()
        turtle.goto(START_X,START_Y)














main_uzor()
turtle.done()



