import turtle


def alco_calc():
    """
    Напишем функцию определения тяжести похмелья
    :return: ничего
    """
    # присвоим значения именнованным переменным для дальнейшего сравнения:
    predel_vipitogo = 10
    perehod_vozrasta = 30

    # просим ввести данные,необходимые для расчета:
    kol_vipitogo = int(input("Сколько бутылок пива 0,5 ты вчера выжрал? "))
    age = int(input("Сколько тебе лет? "))

    if age > perehod_vozrasta:
        if kol_vipitogo > predel_vipitogo:
            print(f"Чувак, ты выпил {kol_vipitogo} бутылок пива и тебе больше {perehod_vozrasta} лет"
                  f", у тебя будет жуткий бадун!  ")
        else:
            print(f"Чувак,ты выпил {kol_vipitogo} бутылок пива и тебе больше {perehod_vozrasta} лет,"
                  f"у тебя будет легкое похмелье!")
    else:
        print("ДА ты молодой, пей сколько хочешь, быстро отойдешь!")
# alco_calc()

def ocenka_v_shkole():
    """
    Напишем программу,которая будет показывать оценки учащимся
    :return: ничего
    """
    A = 90
    B = 80
    C = 70
    D = 60
    E = 50
    F = 40
    tvoya_ocenka = int(input("Введи свой балл : "))
    if tvoya_ocenka >= A:
        print(f"Круто, твоя оценка {tvoya_ocenka} - это 'A', т.е. отлично! ")
    elif tvoya_ocenka > B and tvoya_ocenka < A:
        print(f"Хорошо, твоя оценка {tvoya_ocenka} - это 'В', т.е. почти отлично! ")
    elif tvoya_ocenka >= C and tvoya_ocenka < B:
        print(f"Неплохо, твоя оценка {tvoya_ocenka} - это 'С', т.е. хорошо! ")
    else:
        print("Тебе нужно подучиться, дружище :(")
# ocenka_v_shkole()

def shet():
    digit = int(input('enter digit: '))
    if digit == 1:
        print("ONE")
    elif digit == 2:
        print("TWO")
    elif digit == 3:
        print("THREE")
    else:
        print("sorry, digit is more than THREE")
# shet()

def pravda_i_loj():
    dengi = int(input("how much? "))
    limit = 1000
    if dengi >= limit:
        no_money = True
    else:
        no_money = False
    if no_money:
        print("No money on your card! ")
    else:
        print("you have some money!")
# pravda_i_loj()

def some_practice():
    candy_box = 50
    max_order = 100

    zakaz = int(input("how much ? "))

    if zakaz > max_order:
        prize = True
    else:
        prize = False
    if prize:
        print(f"You will get discount and {candy_box} candies as little prize")
    else:
        print("This is ordinary order. No discount, no prize")
# some_practice()

def pr_1():
    """
    Напишите инструкцию if, которая присваивает значение 20 переменной у и значение 40
переменной z, если переменная х больше 100.
    :return: none
    """
    x = float(input(" Enter digit for x : "))
    value_digit = 100
    if x > value_digit:
        y = 20
        z = 40
        print(f"Y = {y}, Z = {z} ")
    print("END")
# pr_1()

def pr_2():
    """
    Напишите инструкцию if, которая присваивает значение 0 переменной b и значение 1
переменной с, если переменная а меньше 10.
    :return: none
    """
    a = float(input(" Text digit for 'a' = "))
    reg_digit = 10
    if a < reg_digit:
        b = 0
        c = 1
        print(f"B = {b}, C={c}")
    print("END")
# pr_2()

def pr_3():
    """
    Напишите инструкцию if-else, которая присваивает значение 0 переменной b, если
переменная а меньше 10. В противном случае она должна присвоить переменной b значение
99.
    :return:None
    """
    val_digit = 10
    a = float(input(' text digit for "a" = '))
    if a < val_digit:
        b = 0
        print(f"'B' = {b}")
    else:
        b = 99
        print(f"'B' = {b}")
    print("END")
# pr_3()

def pr_4():
    """
    Приведенный ниже фрагмент кода содержит несколько вложенных инструкций if-else.
К сожалению, они были написаны без надлежащего выравнивания и выделения отступом.
Перепишите этот фрагмент и примените соответствующие правила выравнивания и выделения
отступом.
    :return: None
    """
    А_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    score = int(input("What is your score? "))
    if score >= А_score:
        print('Ваш уровень - А.')
    else:
        if score >= B_score:
            print('Ваш уровень - В. ')
        else:
            if score >= C_score:
                print('Ваш уровень - С. ')
            else:
                if score >= D_score:
                    print('Baш уровень - D.')
                else:
                    print('Ваш уровень - F. ')
# pr_4()

def pr_5():
    """
    Напишите вложенные структуры принятия решения, которые выполняют следующее:
если amountl больше 10 и amount2 меньше 100, то показать большее значение из двух переменных
amountl и amount2.
    :return:None
    """
    min_digit = 10
    max_digit = 100
    amount_1 = float(input("Put digit for amount_1: "))
    amount_2 = float(input("Put digit for amount_2: "))
    if amount_1>10 and amount_2<100:
        if amount_1>amount_2:
            print(f"Большим является amount_1 : {amount_1}")
        else:
            print(f"Большим является amount_2 : {amount_2}")
    else:
        print("Условие программы не выполняется. До свидания!")
#pr_5()

def pr_6():
    """
    Напишите инструкцию if-else, которая выводит сообщение 'Скорость нормальная',
если переменная speed находится в диапазоне от 24 до 56. Если значение переменной
speed лежит вне этого диапазона, то показать 'Скорость аварийная'.
    :return: None
    """
    min_speed=24
    max_speed=56
    speed=float(input("What is your speed ? "))
    if speed>min_speed and speed<max_speed:
        print("Speed is normal!")
    else:
        print("Speed is dangerous!")
#pr_6()

def pr_7():
    """
    Напишите инструкцию if-else, которая определяет, находится ли переменная points вне
диапазона от 9 до 51. Если значение переменной лежит вне этого диапазона, то она должна
вывести сообщение ' Недопустимые точки' . В противном случае она должна показать
сообщение 'Допустимые точки' .
    :return: None
    """
    min_diapazon=9
    max_diapazon=51
    points=float(input("What is points? "))
    if points<min_diapazon or points>max_diapazon:
        print("Недопустимые точки")
    else:
        print('Допустимые точки')
#pr_7()

def pr_8():
    """День недели. Напишите программу, которая запрашивает у пользователя число в диапазоне
от 1 до 7. Эта программа должна показать соответствующий день недели, где
l - понедельник, 2 - вторник, 3 - среда, 4 - четверг, 5 - пятница, 6 - суббота и
7 - воскресенье. Программа должна вывести сообщение об ошибке, если пользователь
вводит номер, который находится вне диапазона от 1 до 7.

    :return: None
    """
    nomer_dnya=int(input(" Enter number of the day :"))
    if nomer_dnya==1:
        print("Monday")
    elif nomer_dnya==2:
        print("Thuesday")
    elif nomer_dnya==3:
        print("Wednesday")
    elif nomer_dnya==4:
        print("Thursday")
    elif nomer_dnya == 5:
        print("Friday")
    elif nomer_dnya==6:
        print("Saturday")
    elif nomer_dnya==7:
        print("Sunday")
    else:
        print("Error!!!")
#pr_8()

def pr_9():
    """
    Площади прямоугольников. Площадь прямоугольника- это произведение его длины
на его ширину. Напишите программу, которая запрашивает длину и ширину двух прямоугольников.
Программа должна выводить пользователю сообщение о том, площадь какого
прямоугольника больше, либо сообщать, что они одинаковы.
    :return: None
    """
    dlina_1=int(input(" Введи длину первого прямоугольника : "))
    shirina_1 = int(input(" Введи ширину первого прямоугольника : "))
    dlina_2 = int(input(" Введи длину второго прямоугольника : "))
    shirina_2 = int(input(" Введи ширину второго прямоугольника : "))

    area_1=dlina_1*shirina_1
    area_2=dlina_2*shirina_2

    if area_1>area_2:
        print("Площадь первого прямоугольника больше.")
    elif area_2>area_1:
        print("Площадь второго треугольника больше.")
    else:
        print("Площадь прямоугольников равна.")
#pr_9()

def pr_10():
    """Классификатор возраста. Напишите программу, которая просит пользователя ввести
возраст человека. Программа должна определить, к какой категории этот человек принадлежит:
младенец, ребенок, подросток или взрослый, и вывести соответствующее сообщение.
Ниже приведены возрастные рекомендации:
• если возраст 1 год или меньше, то он или она - младенец;
• если возраст старше l года, но моложе 13 лет, то он или она- ребенок;
• если возраст не менее 13 лет, но моложе 20 лет, то он или она - подросток;
• если возраст более 20 лет, то он или она- взрослый.

    :return: None
    """
    humans_age=int(input("How old is human ? "))
    if humans_age<=1:
        print("Это младенец")
    elif humans_age>1 and humans_age<13:
        print("Это ребенок")
    elif humans_age>13 and humans_age<20:
        print("Это подросток")
    else:
        print("Это взрослый")
#pr_10()

def pr_11():
    """
    Римские цифры. Напишите программу, которая предлагает пользователю ввести число
в диапазоне от 1 до 10. Программа должна показать для этого числа римскую цифру.
Если число находится вне диапазона 1--1 О, то программа должна вывести сообщение об
ошибке. В табл. 3.8 приведены римские цифры для чисел от 1до10.
    :return: None
    """
    chislo=int(input(" Введи цифру : "))
    if chislo==1:
        print("I")
    elif chislo==2:
        print("II")
    elif chislo==3:
        print("III")
    elif chislo==4:
        print("IV")
    elif chislo==5:
        print("V")
    elif chislo==6:
        print("VI")
    elif chislo==7:
        print("VII")
    elif chislo==8:
        print("VIII")
    elif chislo==9:
        print("IX")
    elif chislo==10:
        print("X")
    else:
        print("Error!")
#pr_11()

def pr_12():
    """Масса и вес. Ученые измеряют массу физического тела в килограммах и вес в ньютонах.
Если известна величина массы тела в килограммах, то при помощи приведенной ниже
формулы можно рассчитать вес в ньютонах:
вес= массах *9,8.
Напишите программу, которая просит пользователя ввести массу тела и затем вычисляет
его вес. Если вес тела больше 500 Н (ньютонов), то вывести сообщение, говорящее о том,
что тело слишком тяжелое. Если вес тела меньше 100 Н, то показать сообщение, что оно
слишком легкое.

    :return: None
    """
    max_weight=500
    min_weight=100
    koef=9.8

    your_weight=float(input("Enter you weight in kilograms: "))
    massa_v_newton=your_weight*koef
    print(f"Это твоя масса тела в Ньютонах - {massa_v_newton} H")
    if massa_v_newton>max_weight:
        print("Your weight is too much big!")
    elif massa_v_newton<min_weight:
        print("You weight is so light!")
    else:
        print("Normal weight!")
#pr_12()

def pr_13():
    """
    Волшебные даты. Дата 1 О июня 1960 года является особенной, потому что если ее записать
в приведенном ниже формате, то произведение дня и месяца равняется году:
10.06.60
Разработайте программу, которая просит пользователя ввести месяц (в числовой форме),
день и двузначный год. Затем программа должна определить, равняется ли произведение
дня и месяца году. Если это так, то она должна вывести сообщение, говорящее, что введенная
дата является волшебной. В противном случае она должна вывести сообщение,
что дата не является волшебной.
    :return:
    """
    day=int(input("Enter day : "))
    month=int(input("Enter month : "))
    year=int(input("Enter year : "))
    if day*month==year:
        print("Its wonder!")
    else:
        print("no wonder...")
#pr_13()

def pr_14():
    """
    Цветовой ми кш ер. Красный, синий и желтый называются основными цветами, потому
что их нельзя получить путем смешения других цветов. При смешивании двух основных
цветов получается вторичный цвет:
• если смешать красный и синий, то получится фиолетовый;
• если смешать красный и желтый, то получится оранжевый;
• если смешать синий и желтый, то получится зеленый.
Разработайте программу, которая предлагает пользователю ввести названия двух основных
цветов для смешивания. Если пользователь вводит что-нибудь помимо названий
"красный", "синий" или "желтый", то программа должна вывести сообщение об ошибке.
В противном случае программа должна вывести название вторичного цвета, который получится
в результате.
    :return: None
    """
    color_1=input("First color for mix : ")
    color_2 = input("Second color for mix : ")

    if color_1=="red" and color_2=="blue":
        print("Fiolet")
    elif color_1=="blue" and color_2=="red":
        print("Fiolet")
    elif color_1=="red" and color_2=="yellow":
        print("Orange")
    elif color_1=="yellow" and color_2=="red":
        print("Orange")
    elif color_1=="blue" and color_2=="yellow":
        print("Green")
    elif color_1=="yellow" and color_2=="blue":
        print("Green")
    else:
        print("ERROR!")
#pr_14()

def pr_15():
    """
    Калькулятор сосисок для пикника. Допустим, что сосиски упакованы в пакеты по
10 штук, а булочки - в пакеты по 8 штук. Напишите программу, которая вычисляет
количество упаковок с сосисками и количество упаковок с булочками, необходимых для
пикника с минимальными остатками. Программа должна запросить у пользователя количество
участников пикника и количество хот-догов, которые будут предложены каждому
участнику. Программа должна показать приведенные ниже подробности:
• минимально необходимое количество упаковок с сосисками;
• минимально необходимое количество упаковок с булочками;
• количество оставшихся сосисок;
• количество оставшихся булочек.
    :return: None
    """
    sosiski_v_pakete=10
    bulki_v_pakete=8

    uchastniki=int(input("Какое количество людей на пикнике? "))
    kol_hot_dogs=int(input("Сколько хот-догов на каждого? "))
    #считаем для сосисок:
    if uchastniki<=sosiski_v_pakete:
        ostatok_sosisok=sosiski_v_pakete-uchastniki*kol_hot_dogs
        print("Количество пачек сосисок - 1 пачка, остаток сосисок =",ostatok_sosisok)


#pr_15()

def raschet_marji():
    """ Посчитаем маржу для нескольких позиций товара в магазине

    :return: None
    """
    #Создаем переменную для управления циклом:
    keep_going="yes"

    while keep_going=="yes":
        sebestoimost=float(input("Введи цену закупки: "))
        sale=float(input("Введи за сколько продал: "))

        marja=sale-sebestoimost
        print("Маржа составляет: ",format(marja,'.2f'),"грн" )

        #Убедиться,что пользователь хочет еще посчитать:
        keep_going=input("Хочешь посчитать еще? Введи 'yes' !")
#raschet_marji()

def temperatura():
    """

    :return: None
    """
    danger_temperature=37.0
    your_temperature=float(input("Введи какая у тебя температура: "))

    while danger_temperature<your_temperature:
        print("Выпей жаропонижающее")
        print("Завари и выпей липовый чай")
        print("Ляг в кровать и поспи")
        print("Померяй температуру через час")
        your_temperature=float(input("Какая теперь температура?"))
    print("Температура в норме")
    print("Проверяй температуру каждый час")
#temperatura()

def kopilka():
    """
    Програмка для накопления денег
    :return:
    """
    hotim_sobrat=1000
    tekyshiy_schet=0

    vznos=float(input("Сколько ложишь в копилку? "))
    while tekyshiy_schet<hotim_sobrat:
        tekyshiy_schet+=vznos
        ostalos=hotim_sobrat-tekyshiy_schet
        print("Продолжаем копить...")
        print("Сейчас в копилке:",tekyshiy_schet,"usd")
        print("Осталось собрать: ",ostalos,"usd")
        vznos=float(input("Сколько ложим сегодня?"))
    print("Поздравляю, ты накопил 1000 долларов!")
#kopilka()

def alcoparty():
    """

    :return: none
    """
    box_beer=20
    ostatok=0
    vipil_piva = int(input("Сколько бутылок пива ты уже выпил? "))
    while box_beer>1:
        ostatok = box_beer - vipil_piva
        box_beer -=vipil_piva
        print("Остаток в ящике:",ostatok,"бутылок")
        vipil_piva=int(input("Сколько еще выпил?"))
    print("Вы выпили ящик пива")
#alcoparty()

def speed():
    """
    Ваша подруга Аманда только что получила в наследство европейский спортивный автомобиль
от своего дяди. Аманда живет в США и боится, что будет оштрафована за превышение
скорости, потому что спидометр автомобиля показывает скорость в километрах в час. Она
попросила вас написать программу, которая выводит таблицу скоростей, где эти значения
преобразованы в мили в час. Формула для преобразования КРН (kilometers per hour) в МРН
(miles per hour):
МРН = КРН х 0.6214.
В данной формуле МРН - это скорость в милях в час, КРН - скорость в километрах в час.
Таблица, которую ваша программа выводит, должна показать скорости от 60 до 130 км/ч
с приращением l О км вместе с их значениями, преобразованными в мили в час.
    :return:none
    """
    start_speed=60
    end_speed=140
    step=10
    koef=0.6214
    print("KPH\tMPH")
    for kph in range (start_speed,end_speed,step):
        mph=kph*koef
        print(kph,'km\h','\t',format(mph,'.1f'), 'm\h')
#speed()

def kvadrat_chisel():
    """

    :return: none
    """
    start=int(input("С какого числа начинать? "))
    predel=int(input("До какого числа будем считать квадраты? "))
    print("Число\tКвадрат числа")
    print("---------------------")
    for number in range(start,predel+1):
        kvadrat=number**2
        print(number,'\t',kvadrat)
#kvadrat_chisel()

def pr_16():
    """Перепишите приведенный ниже фрагмент кода, чтобы вместо использования списка
он вызывал функцию range:
[О, 1, 2, 3, 4, 5]:
for х in [О, 1, 2, 3, 4, 5] :
print ('Обожаю эту программу!')

    :return: None
    """
    for x in range(6):
        print('Обожаю эту программу!')
#pr_16()

def pr_17():
    """

    :return: None
    """
    max_chislo=3
    summa=0

    for num in range(max_chislo):
        chislo=int(input("Введи число : "))
        summa+=chislo
        print("Текущая сумма :",summa)
    print("Сумма всех введенных чисел = ",summa)
#pr_17()

def pivo():
    """ Программка будет считать за сколько подходов сколько бутылок пива выпил Чаус (всего)

    :return:None
    """
    podhod=int(input("Сколько подходов сделает Чаус? "))
    total_vipil=0
    orientir_piva=8
    for i in range(1,podhod+1):
        vipil_za_podhod=int(input("Сколько бутылок Чаус выпил за этот подход? "))
        total_vipil+=vipil_za_podhod
        if total_vipil>=orientir_piva:
            print("Все плохо.Будет бадун...")
        elif total_vipil<orientir_piva:
            print("Все норм. Похмелья не будет...")
        else:
            print("Чаус даже без перегара:)")
    print("Сегодня Чаус выжрал: ",total_vipil,"бутылок пива")
#pivo()

def konechnaya_cena():
    """ Посчитаем в гривнах накрутку на кажду позицию в магазине

    :return: None
    """
    total=0
    procent_nakrutki=0.25
    nomer_poz=int(input("0 для выхода из программы или другое число для продолжения: "))
    while nomer_poz!=0:
        cena_zakup=float(input("Введи цену закупки: "))
        nakrutka=cena_zakup*procent_nakrutki
        total+=nakrutka
        print(nomer_poz, "Накрутка равняется:",nakrutka,"грн")
        nomer_poz=int(input("0 или 1?"))
    print("Программа завершена!")
    print("Всего заработали: ", total, "грн")
#konechnaya_cena()

def valid_1():
    """

    :return: None
    """
    temp=int(input("Введи свой темп бега: "))
    while temp<0:
        print("Темп не может быть отриццательным!")
        temp=int(input("Введи корректный темп: "))
    print("Твой темп в норме",temp)
#valid_1()

def valid_2():
    """

    :return: None
    """
    n=int(input("Какое количество учеников?"))
    ocenka=int(input("Введите оценку ученика: "))
    while ocenka<=0 or ocenka>5:
        print("Ошибка! Оценка не может быть 0, отрицательной или выше 5!")
        ocenka=int(input("Введите корректную оценку: "))
        for i in range(1,n+1):
            if ocenka==5:
                print("Perfect!")
            elif ocenka==4:
                print("well!")
            else:
                print("bad...!")
#valid_2()

def valid_3():
    """

    :return: None
    """
    proc=2.5
    one_more="y"

    while one_more=="y" or one_more=="Y":
        wholesale=float(input("Введи оптовую цену: "))

        while wholesale<=0:
            print("Некорректная оптовая цена!")
            wholesale=float(input("Введи корректную отповую цену: "))

        retail=wholesale*proc
        print(retail,"- это конечная цена в магазине.")
        #нужно ли еще посчитать?:
        one_more=input("Введи 'y' или 'Y', если хочешь продолжать считать: ")
#valid_3()

def valid_4():
    """

    :return: None
    """
    for hours in range(24):
        for minutes in range(60):
            for seconds in range(60):
                print(hours,':',minutes,":",seconds)
#valid_4()

def valid_5():
    """

    :return:
    """
    total=0
    next="y"

    while next=="y" or next=="Y":
        dengi=float(input("Сколько ложишь на счет? "))

        while dengi<=0 or dengi>1000:
            print("Нет таких купюр")
            dengi=float(input("Попробуй внести корректные купюры: "))

        total+=dengi
        print("Уже накоплено: ",total,"грн")

        next=input("Нажми 'y', если хочешь продолжить: ")
    print("всего накоплено: ",total,"грн")
#valid_5()

def student():
    row=int(input("row: "))
    com=int(input("com: "))

    for i in range(row):
        for j in range(com):
            print("*", end=" ")
        print()
#student()

def elka():
    """

    :return:
    """
    base_size=8
    for i in range(base_size):
        for j in range(i+1):
            print("*", end=" ")
        print()
#elka()

def karti():
    """

    :return:
    """
    size=6
    for i in range(size):
        for j in range(i):
            print(" ","#",end=" ")
        print()
#karti()

def cikl_v_cikle_1():
    """

    :return:
    """
    #строчек у нас 5,поэтому:
    stroka=int(input("Введи количество строк: "))
    #создаем строку:
    for num_str in range(stroka+1):
        for num_stolb in range(num_str):
            print(" ", end=" ")
        print("#")
        print()
#cikl_v_cikle_1()

def cikl_v_cikle_2():
    """

    :return:
    """
    for i in range(1,5):
        for j in range(1,7):
            print(f"i={i},j={j}",end=" ")
        print()
#cikl_v_cikle_2()

def priminenie():
    """
    Рассмотрим приминение вложенных циклов
    :return: None
    """
    a=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    b=[[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    c=[]
    for i,row in enumerate(a):
        r=[]
        for j,x in enumerate(row):
            r.append(x+b[i][j])
        c.append(r)
    print(c)
#priminenie()
def spisok_v_spiske():
    a=[[1,1,1],[2,2,2],[3,3,3]]
    b=[[4,4,4],[5,5,5],[6,6,6]]
    c=[]
    for index,smal_box in enumerate(a):
        new_box=[]
        for index_2,cifra in enumerate(smal_box):
            new_box.append(cifra+b[index][index_2])
        print(new_box)
#spisok_v_spiske()

def spisok():
    a=[[1,1,1],[2,2,2],[3,3,3]]
    b=[[1,1,1],[1,1,1],[1,1,1]]
    noviy_spisok=[]
    for index,cifra in enumerate(a):
        noviy_spisok.append(cifra+b[index])
    print(noviy_spisok)
#spisok()

def stih():
    """

    :return:
    """
    t=["- Скажи-ка,  дядя, ведь не даром ",
       "Я Python выучил с  каналом",
       "Балакирев что  раздавал?",
       "Ведь были ж задания боевые",
       "Да говорят еще какие!",
       "Не даром помнит  вся Россия",
       "Как мы рубили  их тогда!"
    ]
    for i, line in enumerate(t):
        while line.count("  "):
            line=line.replace("  ", ' ')
        t[i]=line
    print(t,end=" ")
    print()
#stih()

def risuem():
    """

    :return:
    """
    import turtle
    turtle.showturtle()
    num_circles=20
    start_radius=20
    offset=10
    radius=start_radius
    for x in range(num_circles):
        turtle.circle(radius)

        x=turtle.xcor()
        y=turtle.ycor()

        radius+=offset

        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
    turtle.done()
#risuem()

def risuem_1():
    """Нарисовать 36 кругов, наклоняя черепаху на
        10 градусов после того, как каждый круг был нарисован.

    :return:
    """
    num_krug=40
    ugol=10
    radius=100
    turtle.speed(9)
    for x in range(num_krug):
        turtle.circle(radius)
        turtle.left(ugol)
    turtle.done()
#risuem_1()

def risuem_2():
    """

    :return:
    """
#Именованные константы:
    start_x=-200      # стартовая координата х
    start_y=0         # стартовая координата у
    kol_liniy=36      # количество рисуемых линий
    dlina_linii=400   # длина каждой линии
    ugol=170          # угол поворота
    animation_speed=9 # скорость анимации

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(start_x,start_y)
    turtle.pendown()

    turtle.speed(animation_speed)

    for x in range(kol_liniy):
        turtle.forward(dlina_linii)
        turtle.right(ugol)
    turtle.done()
#risuem_2()

def risuem_3():
    """

    :return:
    """
    # Попросим от пользователя добавить значения для именованных констант:
    start_x=50
    start_y=50
    kol_uzor=20
    dlina_linii=50
    ugol=30
    turtle.speed(1)
    # Перемещаем черепашку в заданную точку:
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(start_x,start_y)
    turtle.pendown()
    # Рисуем квадрат:

    # Задаем красный цвет:
    turtle.pencolor("red")
    # Задаем размер кисти:
    turtle.pensize(3)
    # Создаем цикл for для прорисовки квадрата:
    for i in range(kol_uzor):
        for x in range(4):
            turtle.forward(dlina_linii)
            turtle.left(90)
            turtle.showturtle()
        turtle.right(ugol)
    turtle.done()
#risuem_3()

def boolev():
    """

    :return:
    """
    sales=int(input("Сколько продал: "))
    if sales>=5000:
        sales_quota=True
    else:
        sales_quota=False

    if sales_quota:
        print("Вы выполнили свой план!")
#boolev()

def bolnica():
    """

    :return:
    """
    max_temper=38
    temperatura=float(input("Vvedi temperaturu: "))
    if temperatura>max_temper:
        zabolel=True
    else:
        zabolel=False
    if zabolel:
        print("Не переживай,сейчас мы тебя вылечим!")
        while temperatura>=max_temper:
            print("Выпей жаропонижающее")
            temperatura=float(input("Ну что,какая теперь температура? "))
        print("Ну все, тебе уже легче.")
    else:
        print("Иди работай!")
#bolnica()

def pr_18():
    """Напишите цикл while, который позволяет пользователю ввести число. Число должно
быть умножено на 1 О, и результат присвоен переменной с именем product. Цикл должен
повторяться до тех пор, пока product меньше 100.

    :return:
    """
    product=0
    while product<100:
        chislo = int(input("Введи число: "))
        product = chislo * 10
        print(product)
    print("product - больше 100")
#pr_18()

def pr_19():
    """Напишите цикл while, который просит пользователя ввести два числа. Числа должны
быть сложены, и показана сумма. Цикл должен запрашивать у пользователя, желает ли он
выполнить операцию еще раз. Если да, то цикл должен повториться, в противном случае
он должен завершиться .
    :return: None
    """
    going_on="y"
    while going_on=="y" or going_on=="Y":
        chislo_1=float(input("Введи первое число: "))
        chislo_2=float(input("Введи второе число: "))
        total=chislo_1+chislo_2
        print("Сумма чисел =",total)
        #хотим продолжать?
        going_on=input("Нажми 'Y', если хочешь продолжать")
    print("Программа завершена.")
#pr_19()

def pr_20():
    """Напишите цикл for, который выводит приведенный ниже ряд чисел:
О, 10, 20, 30, 40, 50, ... , 1000
    :return:
    """
    for i in range(0,1001,10):
        print(i)
#pr_20()

def pr_21():
    """Напишите цикл, который просит пользователя ввести число. Цикл должен выполнить
1 О итераций и вести учет нарастающего итога введенных чисел.
    :return:
    """
    count=0
    skolko=0
    for num in range(10):
        chislo = int(input("Введи число: "))
        count+=chislo
        skolko+=1
        print("№",skolko,"Текущая сумма: ",count)
    print("Общая сумма= ",count)
#pr_21()

def pr_22():
    """Напишите цикл, который вычисляет сумму приведенного ниже числового ряда:
1 2 3 30
-+-+-+."+-.
30 29 28 1

    :return:
    """
    total=0
    summa=0
    for chislitel in range(1,30):
        for delitel in range(30,1,-1):
            total=chislitel/delitel
            summa+=total
    print("Сумма всех делений в цикле = ",format(summa,'.2f'))
#pr_22()

def pr_23():
    """Напишите серию вложенных циклов, которые выводят 10 строк символов #. В каждой
строке должно быть 15 символов #.
    :return:
    """
    for stroka in range(10):
        for stolb in range(15):
            print("#",end=" ")
        print()
#pr_23()

def pr_24():
    """Напишите программный код, который предлагает пользователю ввести положительное
ненулевое число и выполняет проверку допустимости входного значения.
    :return:
    """
    chislo=float(input("Введи число: "))
    while chislo>0:
        print(chislo)
        chislo=float(input("Введи число: "))
    print("Число меньше 0 или равно 0")
#pr_24()

def pr_25():
    """Напишите программный код, который предлагает пользователю ввести число в диапазоне
от 1 до 100 и проверяет допустимость введенного значения.
    :return:
    """
    chislo=float(input('Введи число: '))

    #  Проверяем это число на допустимость по условию задачи:
    while 1<=chislo<=100:
        chislo = float(input('Введи число: '))
    print("Число меньше 1 или больше 100")
#pr_25()

def errors_collector():
    """Сборщик ошибок. Сборщик ошибок собирает ошибки каждый день в течение пяти дней .
Напишите программу, которая ведет учет нарастающего итога ошибок, собранных в течение
пяти дней. Цикл должен запрашивать количество ошибок, собираемых в течение
каждого дня, и когда цикл завершается, программа должна вывести общее количество
собранных ошибок.
    :return: None
    """
    total_errors=0
    day=0
    for i in range(5):
        errors_1day=int(input("Сколько ошибок сегодня совершили? "))
        day+=1
        total_errors+=errors_1day
        print("В",day,"-й день", "количество ошибок =",errors_1day)
    print("Всего ошибок за 5 дней: ", total_errors)
#errors_collector()

def faired_kall():
    """Сожженные калории. Бег на беговой дорожке позволяет сжигать 4,2 калорий в минуту.
Напишите программу, которая применяет цикл для вывода количества калорий, сожженных
после 10, 15, 20, 25 и 30 минут бега.
    :return: None
    """
    koef=4.2
    for call in range(10,31,5):
        fired=call*koef
        print("После",call,"минут бега сожжено: ",fired,"каллорий")
#faired_kall()

def budjet():
    """Анализ бюджета. Напишите программу, которая просит пользователя ввести сумму,
выделенную им на один месяц . Затем цикл должен предложить пользователю ввести
суммы отдельных статей его расходов за месяц и подсчитать их нарастающим итогом. По
завершению цикла программа должна вывести сэкономленную или перерасходованную
сумму.
    :return:
    """
    kopilka_schetov = 0
    next="y"
    tvoy_budjet=float(input("Введи сумму, выделенную тобой на месяц: "))
    while next=="y" or next=="Y":
        schet=float(input("Введи сумму расходов: "))
        kopilka_schetov+=schet
        next=input("Для продолжения нажми 'Y'")
    print("Твои платежи по счетам в этом месяце составляют:",kopilka_schetov,"грн")
    ekonom=tvoy_budjet-kopilka_schetov
    if ekonom<0:
        print("Ты перерасходовал",ekonom,"грн в этом месяце")
    elif ekonom==0:
        print("Ты вышел в 'ноль'")
    else:
        print("Ты сэкономил",ekonom,"грн в этом месяце")
#budjet()

def proydi_rasst():
    """Пройденное расстояние. Пройденное транспортным средством расстояние можно вычислить
следующим образом:
расстояние = скорость х время.
Например, если поезд движется со скоростью 90 км/ч в течение трех часов, то пройденное
расстояние составит 270 км. Напишите программу, которая запрашивает у пользователя
скорость транспортного средства (в км/ч) и количество часов, которое оно двигалось.
Затем она должна применить цикл для вывода расстояния, пройденного транспортным
средством для каждого часа этого периода времени.
    :return: None
    """
    count=0
    distance=0
    print("ЧАС\tПРОЙДЕННОЕ РАССТОЯНИЕ")
    print("-------------------------")
    speed=int(input("С какой скоростью двигалось ТС? "))
    hours=int(input("Сколько часов ехало ТС? "))
    for i in range(hours):
        count+=1
        distance+=speed
        print(count,"час",        distance,"км пройдено")
#proydi_rasst()

def osadki():
    """Средняя толщина дождевых осадков. Напишите программу, которая применяет вложенные
циклы для сбора данных и вычисления средней толщины дождевых осадков за
ряд лет. Программа должна сначала запросить количество лет. Внешний цикл будет выполнять
одну итерацию для каждого года. Внутренний цикл будет делать двенадцать
итераций, одну для каждого месяца. Каждая итерация внутреннего цикла запрашивает
у пользователя миллиметры дождевых осадков в течение этого месяца. После всех итераций
программа должна вывести количество месяцев, общее количество миллиметров дождевых
осадков и среднюю толщину дождевых осадков в месяц в течение всего периода.
    :return: None
    """
    count_month=0
    total_osad=0
    years=int(input("За сколько лет? "))
    for i in range(years):
        for j in range(12):
            millim_osadkov=int(input("Сколько миллиметров дождевых осадков в этом месяце?"))
            count_month+=1
            total_osad+=millim_osadkov
            sr_osad = total_osad / count_month
        print(count_month, total_osad,sr_osad)
#osadki()

def cel_far():
    """Таблица соответствия между градусами Цельсия и градусами Фаренгейта. Напишите
программу, которая выводит таблицу температур по шкале Цельсия от О до 20 и их
эквиваленты по Фаренгейту. Формула преобразования температуры из шкалы Цельсия
в шкалу Фаренгейта:
9
F=-C+32,
5
где F - это температура по шкале Фаренгейта; С - температура по шкале Цельсия. Для
вывода этой таблицы ваша программа должна применить цикл.
    :return: None
    """
    print("ЦЕЛЬСИЙ\tФАРЕНТГЕЙТ")
    print("-------------------")
    for celciy in range(1,21):
        farent=(9/5)*celciy+32
        print(celciy,"градус","=",format(farent,'.1f'),"градусов")
#cel_far()

def zarplata():
    """Мелкая монета для зарплаты. Напишите программу, которая вычисляет сумму денег,
которую человек заработает в течение периода времени, если в первый день его зарплата
составит одну копейку, во второй день две копейки и каждый последующий день будет
удваиваться. Программа должна запросить у пользователя количество дней, вывести
таблицу, показывающую зарплату за каждый день, и затем показать заработную плату до
налоговых и прочих удержаний в конце периода. Итоговый результат должен быть выведен
в рублях, а не в количестве копеек.

    :return: None
    """
    total_sallary=0
    count_sallary=0
    start_zp=1
    zp=0
    total_dney=int(input("Сколько дней? "))
    for days in range(1,total_dney+1):
        zp=(zp+days)
        print(days,zp)

        #пока не знаю как решить #не решил!
#zarplata()

def zarplata_2():
    dni=int(input("Введи дни: "))
    zarplata=1
    print(1,zarplata,sep='\t')
    if dni>1:
        for i in range(2,dni+1):
            zarplata*=2
            print(i,zarplata, sep='\t')
#zarplata_2()

def summa_chisel():
    """Сумма чисел. Напишите программу с циклом, которая просит пользователя ввести ряд
положительных чисел. Пользователь должен ввести отрицательное число в качестве
сигнала конца числового ряда. После того как все положительные числа будут введены,
программа должна вывести их сумму.
    :return: None
    """
    total_sum=0
    chislo = int(input("Введи число: "))
    while chislo>0:
        total_sum+=chislo
        chislo=int(input("Введи еще одно число: "))
    print(total_sum)
#summa_chisel()

def ocean():
    """Уровень океана. Допустим, что уровень океана в настоящее время повышается примерно
на 1,6 мм в год. С учетом этого создайте приложение, которое выводит количество
миллиметров, на которые океан будет подниматься каждый год в течение следующих
25 лет.
    :return:None
    """
    years=25
    level_up=1.6
    ocean_level=0
    print("YEAR\tOCEAN LEVEL")
    print("------------------")
    for each_year in range(1,years+1):
        ocean_level+=level_up
        print(each_year,format(ocean_level,'.1f'),sep="        ")
#ocean()

def plata_za_obuchenie():
    """Рост платы за обучение. В заданном университете обучение студента-очника составляет
45 ООО рублей в семестр. Было объявлено, что плата за обучение будет повышаться на
3% каждый год в течение следующих 5 лет. Напишите программу с циклом, который
выводит плановую сумму за обучение в семестр в течение следующих 5 лет.
    :return: None
    """
    oplata_semestr=45000
    oplata_procent=0.03
    srok=5    
    some_koef=1.00
    print("YEAR\tPRICE")
    print("------------")
    print(1,oplata_semestr*some_koef,sep="     ")
    for year in range(2,srok+1):
        oplata_semestr+=oplata_semestr*oplata_procent
        print(year,format(oplata_semestr,'.2f'),sep='     ')
#plata_za_obuchenie()

def weight_lost():
    """Потеря массы. Если умеренно активный человек будет сокращать свое потребление
в калориях на 500 калорий в день, то, как правило, он может похудеть примерно на
1,5 кг в месяц. Напишите программу, которая позволяет пользователю ввести его исходную
массу и затем создает и выводит таблицу, показывающую, каким будет его ожидаемая
масса в конце каждого месяца в течение следующих 6 месяцев, если он останется на
этой диете.
    :return:None
    """
    print("МЕСЯЦ\tТВОЙ ВЕС")
    print("----------------")
    weight_now=float(input("Введи свою нынешний вес: "))
    hydeesh=1.5
    period=6
    for month in range(1,period+1):
        weight_now-=hydeesh
        print(month, weight_now,sep='       ')
#weight_lost()

def factorial():
    """Вычисление факториала числа. В математике запись в форме п! обозначает факториал
неотрицательного целого числа п. Факториал п - это произведение всех неотрицательных
целых чисел от 1 доп. Например,
7! = 1 х 2 х 3 х 4 х 5 х 6 х 7 = 5040
Напишите программу, которая позволяет пользователю ввести неотрицательное целое
число и затем применяет цикл для вычисления факториала этого числа и показывает
факториал.
    :return:
    """
    factorial=1
    chislo=int(input("Введи число: "))
    for num in range(1,chislo+1):
        factorial*=num
    print(factorial)
#factorial()

def population():
    """Популяция. Напишите программу, которая предсказывает приблизительный размер популяции
организмов. Приложение должно использовать текстовые поля, чтобы дать
пользователю ввести стартовое количество организмов, среднесуточное увеличение
популяции (как процент) и количество дней, которые организмам будет дано на размножение.
Например, допустим, что пользователь вводит приведенные ниже значения:
• стартовое количество: 2;
• среднесуточное увеличение: 30%;
• количество дней для размножения: 1 О.
    :return: None
    """
    start_kolichestvo=int(input("Введи стартовое количество организмов: "))
    boost=int(input("Введи среднесуточное увеличение популяции в %: "))
    days_all=int(input("Введи количество дней для размножения: "))
    #преобразуем проценты boost:
    boost_procent=boost/100
    print("ДЕНЬ\tПОПУЛЯЦИЯ")
    print(1,start_kolichestvo)
    for day in range(2,days_all+1):
        new_col=start_kolichestvo*boost_procent
        start_kolichestvo+=new_col
        print(day,         format(start_kolichestvo,'.3f'))
#population()

def snejinki():
    """
    Напишите программу, которая применяет вложенные циклы для рисования этого узора:
*******
******
*****
****
***
**
*
    :return:
    """
    n=7
    for i in range(n):
        for j in range(i+1):
            n+=1
            print("*",end=" ")
        print()
#snejinki()

def reshetki():
    """
    Напишите программу, которая применяет вложенные циклы для рисования этого узора:
н
# #
# #
# #
# #
# #
    :return:
    """
    size=6
    for i in range(size):
        print("#")
        for j in range(i+1):
            print(" ", end=" ")
        print("#")
#reshetki()

def kvadrat():
    """
    Черепашья графика: повторение квадратов. В этой главе вы увидели пример цикла,
который рисует квадрат. Напишите программу черепашьей графики, которая применяет
вложенные циклы для рисования 100 квадратов, чтобы создать узор, показанный на
рис. 4.13.
    :return:
    """
    import turtle
    kolichestvo_kvadratov=100
    #координаты начальной крайней правой нижней точки квадрата:
    coord_x=200
    coord_y=-200
    #параметры квадрата:
    dlina_storoni_kvadrata=5
    ugol_kvadrata=90
    #Рисуем квадрат:
    turtle.speed(0) #скорость анимации
    turtle.showturtle()
    turtle.left(180)
    turtle.penup()
    turtle.goto(coord_x,coord_y)
    turtle.pendown()
    for i in range(kolichestvo_kvadratov):
        dlina_storoni_kvadrata+=4
        for j in range(4):
            turtle.forward(dlina_storoni_kvadrata)
            turtle.right(ugol_kvadrata)
    turtle.done()
#kvadrat()

def treygolnik():
    """Черепашья графика: звезд очный узор. Примените цикл с библиотекой черепашьей
графики, чтобы нарисовать узор, показанный на рис. 4.14.
    :return:
    """
    import turtle
    turtle.speed(1)
    turtle.showturtle()
    # пропишем именованные константы:
    kolichestvo_treygolnikov=8
    koordinata_x=-100
    koordinata_y=100
    pyamoy_ugol=90
    katet=100
    ugol_katet=45
    gipotenuza=142
    ugol_povorota=45
    distance=60
    #отправляем курсор в заданную точку:
    turtle.penup()
    turtle.goto(koordinata_x,koordinata_y)
    turtle.right(90)
    turtle.pendown()
    #рисуем треугольник:
    for i in range(kolichestvo_treygolnikov):
        turtle.forward(katet)
        turtle.left(pyamoy_ugol)
        turtle.forward(katet)
        turtle.left(135)
        turtle.forward(gipotenuza)
        turtle.left(ugol_povorota)
        turtle.penup()
        turtle.forward(distance)
        turtle.pendown()
    turtle.done()
#treygolnik()

def labirint():
    """

    :return:
    """
    import turtle
    X=0
    Y=0
    dlina=50
    boost=50
    kol=100
    turtle.showturtle()
    turtle.penup()
    turtle.goto(X,Y)
    turtle.pendown()
    #
    for dlina in range(kol):
        turtle.left(90)
        turtle.forward(dlina)
        dlina+=boost
    turtle.done()
#labirint()

def znak_stop():
    """

    :return:
    """
    import turtle
    kol=8
    dlina=100
    ugol=45
    turtle.screensize(500,500)
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-15,-15)
    turtle.pendown()
    turtle.write("STOP")
    turtle.penup()
    turtle.goto(-50,100)
    turtle.pendown()
    #
    for i in range(kol):
        turtle.forward(dlina)
        turtle.right(ugol)
    turtle.done()
#znak_stop()

#   КОНЕЦ ЦИКЛОВ!






















