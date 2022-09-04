#     ТУТ НАЧИНАЕТСЯ ПРАКТИКА ПО ФУНКЦИЯМ
def main():
    print("У меня для Вас есть известие!")
    message()
    print("До свидания")
def message():
    print("Меня зовут Артур,")
    print("Я король Англии!")
#main()

def main_zp():
    zarplata=15000
    nalogi=0.2
    chistaya=zarplata-zarplata*nalogi
    premii()
    print(chistaya)
def premii():
    coef=0.1
    prem=1350
    dobavka=prem*coef
    print(dobavka)
#main_zp()

def main_1():
    print("Принтуем все по главной функции")
    get_input()
    calc_gross_pay()
    calc_overtime()
    calc_withholdings()
    calc_net_pay()
def get_input():
    print("Спросим что-то ввести с экрана")
    days=int(input("Сколько дней отработал? "))
def calc_gross_pay():
    print("Посчитаем зарпалату")
    zp_per_day=float(input("Сколько получаешь в день? "))
def calc_overtime():
    print("Посчитаем переработки")
def calc_withholdings():
    print("Что-то посчитаем еще")
def calc_net_pay():
    print("Посчитаем какие-то еще выплаты")
#main_1()

def main_tehpodderjka():
    startup_message()
    input("Press 'ENTER' to continue ")
    step_1()
    input("Press 'ENTER' to continue ")
    step_2()
    input("Press 'ENTER' to continue ")
    step_3()
    input("Press 'ENTER' to continue ")
    step_4()
    print("JOB IS DONE!")
def startup_message():
    print("Привет! Сейчас я покажу последовательный алгоритм твоих действий!")
def step_1():
    print("отключить сушилку и отодвинуть ее от стены.")
def step_2():
    print("удалить шесть винтов с задней стороны сушилки.")
def step_3():
    print("удалить заднюю панель сушилки.")
def step_4():
    print("вынуть верхний блок сушилки.")
#main_tehpodderjka()

def main_rashodi():
    print("Эта программа будет подсчитывать все твои расходы за месяц.")
    kommunalka()
    input("Нажми 'ENTER'.чтобы ввести следующую статью расходов")
    produkti()
    input("Нажми 'ENTER'.чтобы ввести следующую статью расходов")
    karmannie_rashodi()
    input("Нажми 'ENTER'.чтобы ввести следующую статью расходов")
    avto()
    print("Программа завершена!")
def kommunalka():
    print("Сколько потратил на коммуналку?")
    pay_kommunalka=float(input("Введи сумму:"))
def produkti():
    print("Сколько потратил на продукты?")
    pay_produkti = float(input("Введи сумму:"))
def karmannie_rashodi():
    print("Сколько потратил на карманные расходы?")
    pay_pocket = float(input("Введи сумму:"))
def avto():
    print("Сколько потратил на машину?")
    pay_car = float(input("Введи сумму:"))
#main_rashodi()

def championship():
    shurovo()
    koropiv_hutor()
    print("Рограмма завершена")
def shurovo():
    wins=4
    lost=2
    print("Итоги тура в Щурово - Побед: ",wins,"Поражений: ",lost)
def koropiv_hutor():
    wins = 6
    lost = 1
    print("Итоги кубка в Коробках - Побед: ", wins, "Поражений: ", lost)
#championship()

def main_3():
    beer=5
    drink(beer)
def drink(kol_vo):
    result=kol_vo*0.5
    print(result)
#main_3()

def main_zarplata():
    zarplata=15000
    zp_posle_naloga(zarplata)
def zp_posle_naloga(chistaya_zp):
    result=chistaya_zp-chistaya_zp*0.2
    print(result)
#main_zarplata()

def main_alcocalc():
    bottles=int(input("Сколько бутылок пива вы купили?"))
    bottle_to_box(bottles)
def bottle_to_box(kol_vo_bottles):
    box=20
    result=kol_vo_bottles/box
    print(f"Вы купили {result} ящиков пива:)")
#main_alcocalc()

def main_sallary():
    sallary=float(input("Сколько получил денег?"))
    excange_to_usd(sallary)
    excange_to_eur(sallary)
    bank(sallary)
def excange_to_usd(money):
    kurs_dollara=27.3
    usd=money/kurs_dollara
    print(f"У тебя будет {usd} долларов.")
def excange_to_eur(money):
    kurs_euro=31.5
    eur=money/kurs_euro
    print(f"У тебя будет {eur} евро.")
def bank(money):
    procent_v_god=0.02
    nokoplenie_za_god=money+money*procent_v_god
    print(f"Через год в банке будет уже вот такая сумма: {nokoplenie_za_god}")
#main_sallary()

def main_kaitering():
    intro()
    chashki=int(input("Сколько чашек?"))
    cups_to_ounces(chashki)
def intro():
    print("Это программа перевода из чашек в унции.")
def cups_to_ounces(cups):
    ounces=cups*8
    print(ounces)
#main_kaitering()

def main_srednee_arifm():
    print("Эта программа считает среднее арифметическое трех чисел")
    first=int(input("Введи первое число"))
    second = int(input("Введи второе число"))
    third= int(input("Введи третье число"))
    show_sum(first,second,third)
def show_sum(digit_1,digit_2,digit_3):
    result=(digit_1+digit_2+digit_3)/3
    print(f"Среднее арифметическое этих трех чисел={result}")
#main_srednee_arifm()

def fio():
    print("Программа будет выводить данные о человеке.")
    name=input("Ваше имя?")
    surname=input("Ваша фамилия?")
    years_old=int(input("Сколько Вам полных лет?"))
    driver_experience=int(input("Сколько полных лет Вы водите машину?"))
    kartochka_voditela(name,surname,years_old)
    vozrast_opit(driver_experience)
def kartochka_voditela(str1,str2,str3):
    print("name---------------",str1,)
    print("surname------------",str2)
    print("old----------------",str3)
def vozrast_opit(staj):
    print("Стаж вождения",staj,"лет.")
    if staj<1:
        print("Вы сосвсем неопытный водитель.")
    elif 1<=staj<5:
        print("Вы более-менее опытный водитель.")
    else:
        print("Да ты опытнейший водила:)")
#fio()

def main_volavaya_pribil():
    valovaya_pribil=float(input("Какая валовая прибыль в этом месяце?"))
    arenda(valovaya_pribil)
    komun_platej(valovaya_pribil)
def arenda(total):
    plata_za_arendu=float(input("Какова цена аренды в месяц?"))
    total=total-plata_za_arendu
    print("После уплаты стоимости аренды,остается: ",total,"грн.")
def komun_platej(total):
    plata_za_komun=float(input("Сколько стоит коммуналка?"))
    total=total-plata_za_komun
    print("После уплаты коммуналки,остается: ", total, "грн.")
#main_volavaya_pribil()

def main_name():
    name=input("What is your name?")
    surname=input("Whatis your second name?")
    reverse_name(surname,name)
def reverse_name(familia,imya):
    print(familia,imya)
#main_name()

def main_years():
    year=32
    print("Изначально тебе ",year,"лет")
    change_year(year)
    print("а теперь",year)
def change_year(age):
    age=33
    print("теперь значение лет равняется",age)
#main_years()

def main_price():
    print("Эта программа считает конечную цену продукта: ")
    cenoobrazovanie(dostavka=120,navar=1.5,opt_cena=500)
def cenoobrazovanie(navar,dostavka,opt_cena):
    final_price=opt_cena*navar+dostavka
    print("Конечная цена равна ",final_price,"грн")
#main_price()

def main_area():
    print("Посчитаем площадь прямоугольника: ")
    a=int(input("for 'a': "))
    b = int(input("for 'b': "))
    area_calc(b,a)
def area_calc(a,b):
    area=a*b
    print(area,"- это и есть площадь прямоугольника")
#main_area()

def main_names():
    print("Эта программа переставляет местами имя и фамилию: ")
    imya=input("What is your name?")
    fam=input("What is your sec name?")
    change_names(fam,imya)
def change_names(imya,fam):
    print("Теперь это будет выглядеть вот так: ")
    print(fam,imya)
#main_names()

def main_sheta():
    print("Посчитаем все платежки: ")
    schetchik(100,50,svet=25)
def schetchik(voda,gaz,svet):
    total=voda+gaz+svet
    print(total)
#main_sheta()

#создадим глобальную переменную:
#oklad=12000
#создадим несколько функций:
def main__():
    print("Ниже приведутся все необходимые расчеты с окладом:",oklad)
    nalogi()
    premiya()
def nalogi():
    nalogi=oklad*0.25
    print('Это налоги: ',nalogi)
def premiya():
    premiya=oklad*0.1
    print("Это премия:", premiya)
#main__()

#Используем глобальную константу
#Ставка взноса компании.
contribution_rate=0.05

def main_company():
    gross_pay_1=float(input("Введите заработную плату: "))
    bonus_1=float(input("Введите сумму премий: "))
    show_pay_contrib(gross_pay_1)
    show_bonus_contrib(bonus_1)

# Функция show_pay_contrib принимает заработную
# плату в качестве аргумента и показывает взнос
# в пенсионные накопления исходя из этого размера оплаты.
def show_pay_contrib(gross):
    contrib=gross*contribution_rate
    print("Взнос исходя из заработной платы = ",format(contrib,'.2f'))

# Функция show_bonus_contrib принимает сумму премий
# в качестве аргумента и показывает взнос
# в пенсионное накопление исходя из этой суммы оплаты.
def show_bonus_contrib(bonus):
    contrib=bonus*contribution_rate
    print("Взнос исходя из премий = ",format(contrib,'.2f'))
#main_company()

#потреним с глобальными константами:

#Глобальные константы прописываются большими буквами
#BOOST_COEF=0.1 #коэфициент, на который будет увеличиваться дистанция с каждой тренировкой
#KOLICHESTVO_TRENEROVOK=10
def main_run():
    print("Эта программа будет считать"
          " сколько километров ты будешь"
          " пробегать с каждой треней")
    distance = int(input("Сколько метров пробежишь на первой тренировке?"))
    boosting_run(distance)

def boosting_run(dlinna):
    for dlinna in range(KOLICHESTVO_TRENEROVOK):
        dlinna*=BOOST_COEF
        print(dlinna)
#main_run()

def bibl_1():
    import random
    for i in range(5):
        some_digit=random.randint(1,72)
        print(some_digit)
#bibl_1()

import random
def main_bingo():
    for i in range(10):
        chisla=random.randint(1,1000)
        print(chisla)
#main_bingo()

#Кодовый замок!
#CODE_DIGITS=int(input("Сколько цифр будет в коде?"))
#DIAPAZON_DIGITS_FROM=int(input("Диапазон цифр от : "))
#DIAPAZON_DIGITS_TO=int(input("Диапазон цифр до : "))
def main_code():
    for cifra in range(1,CODE_DIGITS):
        your_door_code=random.randint(DIAPAZON_DIGITS_FROM,DIAPAZON_DIGITS_TO)
        print(cifra,"-",your_door_code)
#main_code()

#Программа про кубики:
import random
def main_kubik():
    answer = "Да"
    while answer=="Да":
        kubik_1=random.randint(1,6)
        kubik_2=random.randint(1,6)
        print(kubik_1,"и",kubik_2)
        answer=input("Хочешь бросить кубики еще раз? Пиши ДА для продолжения")
#main_kubik()

def some_main():
    x=random.randint(1,100)*2
    print(x)
#some_main()

#Эта программа будет подбрасывать монету и показывать Орел или Решку:
#KOLICHESTVO_VBROSOV=int(input("Сколько вбрасываний производить?"))
#RESHKA=1
#OREL=2
def main_orel_or_reshka():
    for vbros in range(1,KOLICHESTVO_VBROSOV+1):
        moneta=random.randint(RESHKA,OREL)
        if moneta==1:
            print(vbros,"РЕШКА")
        else:
            print(vbros,"ОРЕЛ")
#main_orel_or_reshka()


#ФУНКЦИИ randrange, random и uniform!!!!!

def some_94278():
    z=random.randrange(1,10)
    print(z)
#some_94278()

def some_13():
    number=random.random()
    print(number)
#some_13()

def some_97():
    x=random.uniform(1.0,100.0)
    print(x)
#some_97()

# random.seed() если нужно начальное значение повторять
def main_seed_1():
    random.seed(10)
    for chislo in range(1,11):
        x=random.randint(1,100)
        print(chislo,x)
#main_seed_1()

def main_seed_2():
    random.seed(10)
    for chisla in range(1,11):
        x=random.randint(1,100)
        print(chisla,x)
#main_seed_2()



# НАПИСАНИЕ ФУНКЦИЙ С ВОЗВРАТОМ ЗНАЧЕНИЙ RETURN
#chislo_1=float(input("1st digit: "))
#chislo_2 = float(input("2nd digit: "))
def sum(chislo_1,chislo_2):
    result=chislo_1+chislo_2
    return result
#sum(chislo_1,chislo_2)

# Эта программа использует возвращаемое значение функции:
def main_age_1():
    # получить возраст пользователя:
    your_age=int(input("Введите свой возраст: "))

    # получить возраст лучшего друга пользователя:
    frind_age=int(input("Введи возраст своего друга: "))

    # получить сумму обоих возрастов:
    total_age=sum(your_age,frind_age)

    # показать общий возраст:
    print("Вместе вам",total_age,"лет")
#main_age_1()

# Эта программа вычисляет отпускную цену товара:
DISCOUNT_PERCENTAGE=0.20 # глобальная константа для процента скидки

# главная функиця:
def main_1141():
    # получить обычную цену товара:
    get_price=get_regular_price()
def get_regular_price():
    # функция предалагает пользователю ввести обычную цену товара и возращает ее:
    price=float(input("Введи обычную цену товара: "))
    return price
#main_1141()


#def get_sqrt(x):
    #res=x**0.5
    #return res


#a=get_sqrt(25)
#print(a)


# Напишем прогу про цены в магазине:
DISCOUNT_PROC=0.20 # это скидка

# напишем главную функицю:
def main_store():
    # получить первоначальную цену
    cena_tovara=final_price()
    # рассчитать отпускную цену с учетом скидки
    summa_skidki=discount(cena_tovara)
    # считаем цену с учетом скидки:
    konechnaya_stoimost=cena_tovara-summa_skidki
    # печатаем результат:
    print(konechnaya_stoimost)
def final_price():
    price=float(input("Введи полную стоимость товара: "))
    return price
def discount(price):
    return price*DISCOUNT_PROC
#main_store()

# напишем прогу про платежки Чауса:
# объявим глобальную константу - это его зарплата:
#ZARPLATA=float(input("Введи зарплату Чауса: "))

#Создадим главную функцию:
def main_chaus():
    # получить  сумму  квартплаты
    first_pay=kvartira()
    # получить сумму, потраченную на продукты
    second_pay=produkty()
    # посчитать,сколько останется
    ostatok=ZARPLATA-(first_pay+second_pay)
    #показываем результат:
    print("Осталось денег на карточке:",ostatok,"грн")
def kvartira():
    plata_za_kvartiru=float(input("Сколько заплатил за квартиру: "))
    return plata_za_kvartiru
def produkty():
    plata_za_produkty=float(input("Сколько заплатил за проукты: "))
    return plata_za_produkty
#main_chaus()


# Напишем программу для розгничного магазина:
# Создадим глобальные константы:
#NAKRUTKA=0.75 # накрутка цены в магазине
#DISCOUNT=float(input("Какая скидка у клиента: ")) # скидка у клиента

# Создадим главную функцию:
def store_main():
    #Что мы хотим получить от этой функции?
    #Получить оптовую цену товара:
    #wholesale_price = float(input("Введи оптовую цену:"))
    #Посчитаем и выведем на экран накрутку в гривнах:
    summa_nakrutki=nacenka(wholesale_price)
    # получить цену с учетом накрутки:
    retail_price = wholesale_price + summa_nakrutki
    print("Сумма накрутки на данный товар составляет: ",summa_nakrutki,"грн")
    #Посчитаем и выведем на экран скидку в гривнах:
    summa_skidki=discount_prog(retail_price)
    print("Сумма скидки на данный товар составляет: ",summa_skidki,"грн")
    #Посчитаем отпускную цену для клиента в гривнах:
    final_price=(wholesale_price+summa_nakrutki)-summa_skidki
    #Выводим конечную сумму на экран:
    print("Отпускная цена для клиента с учетом скидки составляет: ",final_price,"грн")

def nacenka(price):
    return price*NAKRUTKA
def discount_prog(price):
    return price*DISCOUNT
def print_text():
    print("Программа завершена.")
#store_main()

#Создадим функцию для подсчета расходов магазина за месяц.
#Заведем именованные константы:
#ARENDA=12000
#NALOGI=2500
#UBORKA=250
#OHRANA=350
#NAME=input("Как тебя зовут?")
#Создадим главную функцию:
def main_shop():
    print(f"Привет,{NAME}!")
    print("Эта программа подсчитает все твои расходы за месяц.")
    #узнать какая цена за свет
    schet_svet=plata_za_svet()
    #узнать какая цена за воду
    schet_voda=plata_za_vody()
    #посчитать и вывести на экран сумму всех расходов за месяц
    total=ARENDA+NALOGI+UBORKA+OHRANA+schet_svet+schet_voda
    print("Всего в этом месяце ты заплатил: ",total,"грн")
    print(f"До свидания,{NAME}!")

def plata_za_svet():
    #svet=float(input("Сколько пришло за свет?"))
    return svet
def plata_za_vody():
    #voda=float(input("Сколько пришло за воду?"))
    return voda
#main_shop()

# Напишем программу для расчета финансовых операций в магазине музыки.
# Создадим именованные константы:
# Создадим главную функцию:
def music_shop_main():
    """
   1) Получить месячные продажи продавца.
   2)Получить сумму авансовой выплаты.
   3)Применить сумму месячных продаж для определения ставки комиссионных.
   4)Рассчитать выплату продавцу с использованием ранее показанной формулы. Если сумма
отрицательная, то указать, что продавец должен возместить компании разницу.
    :return:
    """
    #print("Эта программа расчитает выплату продавцу с учетом аванса")
   # manager_name = input("Введи имя менеджера: ")
    mesyachnie_prodaji = func_sale_result()
    summa_avans_viplati = func_avans()
    stavka_komissii = func_komissionnie(mesyachnie_prodaji)
    # расчитаем сумму месячной выплаты продавцу с учетом аванса:
    #viplata = mesyachnie_prodaji * stavka_komissii - summa_avans_viplati
    #if viplata < 0:
        #print(f"{manager_name}, ты должен возместить: ", viplata, "usd")
    #else:
        #print(f"{manager_name}, выплата тебе составляет: ", viplata, "usd")

    # для каждой операции заведем отдельную внутреннюю функцию.


def func_sale_result():
    #sale_result = float(input("Введи, на какую сумму напродавал менеджер: "))
    return sale_result


def func_avans():
   # avans = float(input("Введи, какой был выдан аванс менеджеру: "))
    return avans


def func_komissionnie(sale):
    # рассчитаем комисионные продавца:
    if sale < 10000:
        komiss = 0.1
    elif sale > 10000 and sale < 15000:
        komiss = 0.12
    elif sale > 15000 and sale < 18000:
        komiss = 0.14
    elif sale > 18000 and sale < 22000:
        komiss = 0.16
    else:
        komiss = 0.18
    return komiss


#music_shop_main()



#number=int(input("Enter digit: "))
#def chet_nechet(number):
   # if number%2==0:
       # status=True
   # else:
       # status=False
  #  return status
#if chet_nechet(number):
    #print("Четное")
#else:
   # print("Нечетное")


# Возвращение многочисленных значений!!!!!

#def get_name():
   #first=input("what is your name?")
    #second=input("what is your surname?")
    #return first,second

#name,surname=get_name()
#print(name,surname,sep=" ")

#def get_info():
    #get_name=input("what is your name?")
    #get_surname=input("what is your surname?")
    #year_of_birth=int(input("in what year you were born?"))
    #get_status=input("what is your family status?")
   # return get_name,get_surname,year_of_birth,get_status

#name,second_name,year,status=get_info()
#print(name,second_name,year,status,end=" ")


import math
def main_math():
    digit=float(input("enter digit: "))
    koren_iz_chisla=math.sqrt(digit)
    print(koren_iz_chisla)
#main_math()


#программа для вычисления длины гипотенузы прямоугольного треугольника:
def main_gipotenuza():
    katet_1=float(input("ДЛина первого катета: "))
    katet_2 = float(input("ДЛина второго катета: "))
    #вычисляем гипотенузу:
    gipotenuza=math.hypot(katet_1,katet_2)
    print("Длина гипотенузы составляет: ",gipotenuza)
#main_gipotenuza()

#Программа для вычисления площади любого круга:
#import math
def main_circle_square():
    circle_radius=float(input("Какой радиус круга? "))
    result=get_square(circle_radius)
    print("Площадь круга равна: ",result)
def get_square(radius):
    circle_square=math.pi*radius**2
    return circle_square
#main_circle_square()


def main_zadacha_1():
    """
    Напишите инструкцию, которая применяет функцию модуля math для получения квадратного
корня из 100 и присваивает его значение переменной.
    :return:
    """
    import math
    get_digit=float(input("put here any digit: "))
    result=koren_iz_chisla(get_digit)
    print(f"Корень из {get_digit} равен ",result)
def koren_iz_chisla(chislo):
    koren=math.sqrt(chislo)
    return koren
#main_zadacha_1()

def main_gradus_in_radian():
    """
    Напишите инструкцию, которая применяет функцию модуля math для преобразования
45° в радианы и присваивает значение переменной.
    :return:
    """
    import math
    get_gradus=float(input("Какой угол в градусах? "))
    result=get_radians(get_gradus)
    print(f"Заданный угол {get_gradus} в пересчете на радианы равен: {result}")
def get_radians(ugol):
    radians=math.radians(ugol)
    return radians
#main_gradus_in_radian()


#Программа , которая производит различные геометрические вычисления:
def main_geometrik():