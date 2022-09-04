# в этой программе напишем три строки данных в файл "список":
def main_spisok():
    # откроем файл с именем "список":
    outfile = open(r'D:\Фильмы\Кино\список.txt', 'w')

    # запишем имена трех участников:
    outfile.write('Саутенко \ Чаусов \n')
    outfile.write('Трубиев \ Веселов \n')
    outfile.write('Терещук \ Коструб \n')
    outfile.write('Дыкань \ Горишний \n')

    # закроем файл:
    outfile.close()


# main_spisok()


# в этой программе создадим и откроем текстовый файл
# и внесем данные:
def main_spisok_1():
    # создаем и открываем список:
    outfile = open(r'D:\Фильмы\Кино\spisok_2.txt', 'a')
    # запишем какие-нибудь данные:
    outfile.write('ИМЯ        ФАМИЛИЯ           РОСТ\n')
    outfile.write('Андрей     Саутенко          191\n')
    outfile.write('Александр  Дыкань            191\n')
    outfile.write('Роман      Веселов           188\n')
    outfile.write('Дмитрий    Трубиев           190\n')
    # закроем файл:
    outfile.close()


# main_spisok_1()


def main_3():
    outfile = open(r'D:\Фильмы\Аннешечка.txt', 'w')

    outfile.write('Сатунеко Татьяна Павловна\n')
    outfile.write('Родилась 06.11.1955\n')
    outfile.write('Любит смотреть "Ориел и Решка"\n')

    outfile.close()


# main_3()


# ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА
def main_4():
    # открыть файл spisok_2
    infile = open(r'D:\Фильмы\Кино\spisok_2.txt', 'r')
    # прочитать содержимое:
    file_read = infile.read()
    # закрыть файл
    infile.close()
    # вывести данные,прочитанные в файле:
    print(file_read)


# main_4()


def main_5():
    # откроем файл док с рабочего стола компа:
    infile = open(r'D:\Фильмы\Аннешечка.txt', 'r')
    # прочитаем данные:
    read_content = infile.read()
    # закроем программу
    infile.close()
    # выведем прочитанное на экран:
    print(read_content)


# main_5()

def main_6():
    infile = open(r'D:\Фильмы\Аннешечка.txt', 'r')
    read_line1 = infile.readline()
    read_line2 = infile.readline()
    read_line3 = infile.readline()
    # закрываем:
    infile.close()
    # печатаем:
    print(read_line1)
    print(read_line2)
    print(read_line3)


# main_6()

def main_7():
    # создадим и откроем файл:
    outfile = open(r'D:\Фильмы\new_project_1.txt', 'w')
    # что-то там напишем:
    outfile.write("Проснуться в 7:00\n")
    outfile.write("Съездить на примерку\n")
    outfile.write("Позвонить Чаусу\n")
    outfile.write("Позаниматься дома программированием\n")

    # закрываем файл:
    outfile.close()


# main_7()

def read_main_7():
    infile = open(r'D:\Фильмы\new_project_1.txt', 'r')
    infile.read()
    read_content = infile.read()
    infile.close()
    print(read_content)


# read_main_7()

def read_line():
    infile = open(r'D:\Фильмы\new_project_1.txt', 'r')
    first_line = infile.readline()
    sec_line = infile.readline()
    third_line = infile.readline()
    fourth_line = infile.readline()
    infile.close()
    print(third_line)


# read_line()


def friends_name():
    print("Enter your 3 friend names!")
    name_1 = input("Enter first name: ")
    name_2 = input("Enter second name: ")
    name_3 = input("Enter third name: ")

    # creat and opening new file:
    output = open(r'D:\Фильмы\my_friends.txt', 'w')
    # writting names in file:
    output.write(name_1 + '\n')
    output.write(name_2 + '\n')
    output.write(name_3 + '\n')
    # closing file
    output.close()
    print("Имена были записаны в файл 'my_friends'")


# friends_name()

def print_friends():
    input = open(r'D:\Фильмы\my_friends.txt', 'r')
    read_text = input.read()
    input.close()
    print(read_text)


# print_friends()

def competition_list():
    name = input("Фамилия участника: ")
    rank = input("Рейтинг участника: ")
    city = input("Город, который представляет участник: ")
    # создаем и открываем файл:
    file = open(r'D:\Фильмы\competition_list.txt', 'w')
    # вписываем инфу в файл:
    str_1 = file.write(name + '\n')
    str_2 = file.write(rank + '\n')
    str_3 = file.write(city + '\n')
    # закрываем файл:
    file.close()
    print("Лист участника соревнования хранится на 'competition_list.txt'")


# competition_list()

def read_competition_list():
    file = open(r'D:\Фильмы\competition_list.txt', 'r')
    str_1 = file.readline()
    str_2 = file.readline()
    str_3 = file.readline()

    str_1 = str_1.rsplit('\n')
    str_2 = str_2.rsplit('\n')
    str_3 = str_3.rsplit('\n')

    file.close()
    print(str_1)
    print(str_2)
    print(str_3)


# read_competition_list()

# дозапись данных в файл:
def add_names():
    file_add = open(r'D:\Фильмы\my_friends.txt', 'a')
    file_add.write("Danil\n")
    file_add.write("Radik\n")
    file_add.close()


# add_names()


# преобразоание чисел в строки и добавление в файл

def chislo_v_str():
    new_file = open(r'D:\Фильмы\chisla_v_stroki.txt', 'w')

    first = float(input("enter first digit: "))
    sec = float(input("enter second digit: "))
    thirf = float(input("enter third digit: "))

    new_file.write(str(first) + '\n')
    new_file.write(str(sec) + '\n')
    new_file.write(str(thirf) + '\n')

    new_file.close()


# chislo_v_str()


def summa_schetov():
    gaz = float(input("Сколько за газ? "))
    voda = float(input("Сколько за воду? "))
    svet = float(input("Сколько за электричество? "))
    total_sum = gaz + voda + svet

    # создадим и откроем файл:
    file = open(r'D:\Фильмы\счета.txt', 'w')

    # пропишем полученные данные в файле:
    file.write("За газ: " + str(gaz) + "грн" + '\n')
    file.write("За воду:" + str(voda) + "грн" + '\n')
    file.write("За свет:" + str(svet) + "грн" + '\n')
    file.write("Всего за коммуналку: " + str(total_sum) + "грн" + '\n')

    # закроем файл:
    file.close()

    # выведем на экран:
    print("За газ:", gaz)
    print("За воду:", voda)
    print("За свет:", svet)
    print("Всего:", total_sum)


# summa_schetov()


def some_1():
    file = open(r'D:\Фильмы\chisla.txt', 'w')
    line_1 = file.write("100\n")
    line_2 = file.write("200\n")
    line_3 = file.write("300\n")

    file.close()


# some_1()


def some_3():
    file = open(r'D:\Фильмы\chisla.txt', 'r')
    stroka_1 = int(file.readline())
    stroka_2 = int(file.readline())
    stroka_3 = int(file.readline())
    file.close()

    total_sym = stroka_1 + stroka_2 + stroka_3

    print(total_sym)


# some_3()


def some_5():
    file = open(r'D:\Фильмы\zp.txt', 'w')
    file.write("10000\n")
    file.write("15000\n")
    file.write("18000\n")

    file.close()


# some_5()

def read_some_5():
    file = open(r'D:\Фильмы\zp.txt', 'r')
    zp_1 = int(file.readline())
    zp_2 = int(file.readline())
    zp_3 = int(file.readline())
    file.close()
    sr_zp = (zp_1 + zp_2 + zp_3) / 3
    print(format(sr_zp, '.2f'))


# read_some_5()

# ЦИКЛЫ В ФАЙЛАХ!!!

def main_99():
    # получить количество дней
    days = int(input(" За какое количество дней ввести продажи? "))

    # открыть новый файл,куда будут записываться данные:
    file = open(r'D:\Фильмы\sales.txt', 'w')

    # получить суммы продаж за каждый день
    # и записать их в файл:

    for day_number in range(1, days + 1):
        # получить продажи за день
        sales = float(input("Введи продажи за день: "))

        # записать сумму продаж в файл:

        file.write(str(sales) + "\n")

    file.close()
    print("Файлы записаны в D:\Фильмы\sales.txt")


# main_99()


def open_main_99():
    file = open(r'D:\Фильмы\sales.txt', 'r')
    day_1 = float(file.readline())
    day_2 = float(file.readline())
    day_3 = float(file.readline())

    file.close()
    summa = day_1 + day_2 + day_3
    print(summa)


# open_main_99()


def main100():
    days = int(input("За какое количество дней вводить заказы? "))
    file = open(r'D:\Фильмы\zakaz.txt', 'w')

    for every_day in range(1, days + 1):
        zakaz = float(input("Введи сумму заказов в день: "))

        file.write(str(zakaz) + '\n')
    file.close()
    print("Все данные хранятся в D:\Фильмы\zakaz.txt")


# main100()


def cikl_v_read():
    file = open(r'D:\Фильмы\zakaz.txt', 'r')
    day = file.readline()
    while day != "":
        convert = float(day)
        print(convert)
        day = file.readline()
    file.close()
    print(day)


# cikl_v_read()


def vvod_pokupok():
    file = open(r'D:\Фильмы\покупки.txt', 'w')
    kol_vo_pokupok = int(input("Сколько покупок сделано? "))
    for pokupka in range(1, kol_vo_pokupok + 1):
        summa = float(input("Сколько потратил за эту покупку? "))
        file.write(str(summa) + '\n')
    file.close()


# vvod_pokupok()

def chtenie_pokupok():
    file = open(r'D:\Фильмы\покупки.txt', 'r')
    read = file.readline()
    while read != "":
        change_type = float(read)
        print(read)
        read = file.readline()

    file.close()


# chtenie_pokupok()

def chtenie_pokupok_2():
    file = open(r'D:\Фильмы\покупки.txt', 'r')
    sum = 0
    for line in file:
        change_type = float(line)
        print(change_type)
        sum += change_type
    file.close()
    print(sum)


# chtenie_pokupok_2()


def commun():
    file = open(r'D:\Фильмы\коммуналка.txt', 'w')
    page = int(input("Введи количество статей коммуналки: "))
    for poz in range(1, page + 1):
        plata = float(input("Введи сумму оплаты: "))
        file.write(str(plata) + '\n')
    file.close()


# commun()


def read_commun():
    file = open(r'D:\Фильмы\коммуналка.txt', 'r')
    for line in file:
        change_type = float(line)
        print(change_type)
    file.close()


# read_commun()


def video_calc():
    """Задание сделать:
    Программу, которая позволяет ему вводить длительность каждого видеоклипа в проекте
(в секундах). Продолжительность клипа сохраняется в файле.
    Программу, которая читает содержимое файла, показывает длительность клипа и общую
длительность всех сегментов.
    :return:
    """
    # эта программа сохраняет последовательность , состоящую из видеоклипов
    # в файле video_times.txt

    # получаем количество видеоклипов в проекте:
    clips = int(input("Напиши количество видеоклипов в проекте: "))

    # создать и открыть файл для записи длительности видеоклипов:
    file = open(r'D:\Фильмы\video_times.txt', 'w')

    # получить длительность каждого видеоклипа и записать его в файл:
    for each_clip in range(1, clips + 1):
        video_time = float(input("Сколько времени в секундах занимает каждый клип: "))
        file.write(str(video_time) + '\n')
    file.close()
    print("Время каждого видео сохранено в D:\Фильмы\ video_times.txt")


# video_calc()

def video_calc_2():
    """
    Инициализировать накапливаЮilfу'Ю переменную total значением О.
Инициализировать переменную-счетчик count значением О.
Открыть файл ввода.
Для каждой строки в файле:
Конвертировать строку в число с плавающей точкой. (Это длительность
видеоклипа.)
Прибавить его в переменную-счетчик. (Она ведет учет количества видеоклипов.)
Показать длительность этого видеоклипа.
Прибавить длительность в накапливаЮilfу'Ю переменную.
Закрыть файл.
Показать содержимое накопителя с общей длительностью.
    :return:
    """
    total = 0
    count = 0
    file = open(r'D:\Фильмы\video_times.txt', 'r')

    for line in file:
        change_type = float(line)
        count += 1
        print(count, "-й клип: ", change_type, "секунд")
        total += change_type
    file.close()
    print("Общая длительность = ", total, "секунд")


# video_calc_2()

def kopilka():
    # напишем программу для участников соревнований,которая будет сохранять данные по взносам в файл:
    count = int(input("Сколько участнико сдало деньги? "))

    file = open(r'D:\Фильмы\volley_finance.txt', 'w')

    for player in range(1, count + 1):
        money = float(input("Сколько внес денег участник? "))
        file.write(str(money) + '\n')

    file.close()

    print("Данные по взносам можно посмотреть на D:\Фильмы\ volley_finance.txt")


# kopilka()


def kopilka_calc():
    # произведем финансовые подсчеты с данными файла:

    count = 0
    total = 0
    shoud_got = 12000
    file = open(r'D:\Фильмы\volley_finance.txt', 'r')

    for line in file:
        count += 1
        change_type = float(file.readline())
        total += change_type

    file.close()
    print(f"Всего собрали: {total}грн")
    if total == shoud_got:
        print("Собрали всю сумму!")
    elif total > shoud_got:
        print("Собрали больше,чем нужно было!")
    else:
        print(f"Недостача: {shoud_got - total} грн")


# kopilka_calc()


def home_work_1():
    """
    Напишите короткую программу, которая применяет цикл for для записи в файл чисел
от 1до10.
    :return:
    """
    file = open(r'D:\Фильмы\home_work_1.txt', 'w')

    for chislo in range(10):
        get_chislo = int(input("Enter digit: "))
        file.write(str(get_chislo) + '\n')
    file.close()


# home_work_1()


def home_work_2():
    """
    Допустим, что существует файл data.txt, который содержит несколько строк текста.
Напишите короткую программу с использованием цикла while, который показывает
все строки в файле.
    :return:
    """
    file = open(r'D:\Фильмы\data.txt', 'r')

    read = file.readline()
    while read != "":
        read = file.readline()

    file.close()


# home_work_2()

def home_work_3():
    """
    Пересмотрите программу, которую вы написали выше, применив вместо цикла while
цикл for.
    :return:
    """
    file = open(r'D:\Фильмы\data.txt', 'r')

    for line in file:
        print(line)
    file.close()


# home_work_3()


def practice_114():
    """
    создадим файл со списком игроков чемпионата Донбасса
    :return:
    """
    count_players = int(input("Сколько игроков заявлено?"))

    file = open(r'D:\Фильмы\donbass.txt', 'w')

    for player in range(1, count_players + 1):
        name = input("Пиши фамилию и имя игрока: ")
        file.write(name + '\n')

    file.close()


# print("Список участников находится вот здесь D:\Фильмы\donbass.txt")


# practice_114()

def donbass_show():
    file = open(r'D:\Фильмы\donbass.txt', 'r')

    for player in file:
        print(player)
    file.close()


# donbass_show()


def office():
    # Эта программа получает от пользователя данные о сотрудниках и сохраняет их
    # в виде записей в файл employee.txt.

    # получить количество записей о сотрудниках для создания:
    count_personal = int(input("Какое количество сотрудников? "))

    # открыть файл для записи:
    file = open(r'D:\Фильмы\employee.txt', 'w')

    # получить данные каждого сотрудника и записать их в файл:
    for person in range(1, count_personal + 1):
        print("Введите данные о сотруднике: ")
        name = input("Имя: ")
        id = input("Идентификационный номер: ")
        department = input("Отдел: ")

        # записать в файл данные как запись:
        file.write(name + '\n')
        file.write(id + '\n')
        file.write(department + '\n')

        print()

    file.close()

    print("Запись о сотрудниках сохранена в D:\Фильмы\employee.txt")


# office()

def read_office():
    # эта программа прочитает данные из файла,созданного выше:
    file = open(r'D:\Фильмы\employee.txt', 'r')

    # читаем файлы с циклом:
    name = file.readline()

    while name != "":
        id = file.readline()
        department = file.readline()

        # удаляем символы новой строки из полей:
        name = name.rstrip('\n')
        id = id.rstrip('\n')
        department = department.rstrip('\n')

        # показать запись:
        print("Имя: ", name)
        print("Идентификационный: ", id)
        print("Отдел: ", department)

        # прочитать поле с именем следующей записи:
        name = file.readline()

    file.close()


# read_office()


def pract_office():
    # получим количество людей:
    personal = int(input("Какое количество сотрудников запишем? "))
    # создаем и открываем новый файл:
    file = open(r'D:\Фильмы\my_office.txt', 'w')
    # создаем цикл для записи данных о сотрудниках:
    for emp in range(1, personal + 1):
        print("Получаем данные о сотруднике: ")
        name = input("Введите имя: ")
        id = input("Введите идентиф.номер: ")
        position = input("Введите должность: ")

        # запишем полученные данные в файл:
        file.write(name + '\n')
        file.write(id + '\n')
        file.write(position + '\n')

    # закрываем файл
    file.close()
    print("Данные записаны в файл D:\Фильмы\my_office.txt")


# pract_office()


def read_pract_office():
    # открываем файл:
    file = open(r'D:\Фильмы\my_office.txt', 'r')
    # прочитываем первую строку:
    name = file.readline()
    # создаем цикл:
    while name != "":
        id = file.readline()
        position = file.readline()
        # удаляем пробелы:
        name = name.rstrip('\n')
        id = id.rstrip('\n')
        position = position.rstrip('\n')

        # печатаем полученные данные:
        print("Имя: ", name)
        print("Идент.номер: ", id)
        print("Должность: ", position)

        # читаем первую строку еще раз:
        name = file.readline()

    # закрываем файл
    file.close()


# read_pract_office()


def cofee_shop():
    # эта программа добавляет записи о запасах кофе на складе
    # и сохраняет в файле coffee.txt

    # создадим переменную для управления циклом:
    another = "д"
    # открыть файл coffee.txt в режиме дозаписи:
    file = open(r'D:\Фильмы\coffee.txt', 'a')

    # ДОбавляем запись в файл:
    while another == "д" or another == "Д":
        # получить данные с записью о кофе:
        print("Введите следующие данные о кофе: ")
        sort_coffee = input("какой сорт: ")
        count_funt = int(input("количество в фунтах: "))

        # добавить данные в файл:
        file.write(sort_coffee + '\n')
        file.write(str(count_funt) + '\n')
        print("Желаете добавить еще одну запись?")
        another = input("Нажмите Д или д для продолжения!")
    file.close()
    print("Данные о сортах и количестве кофе на складах хранится в D:\Фильмы\coffee.txt")


#cofee_shop()


def sportive_store():
    #  напишем программу,которая помогает вести складские запасы магазина
    #создаем переменную для управления циклом:
    answer="д"

    # создаем файл в режиме дозаписи:
    file=open(r'D:\Фильмы\sport_store.txt', 'a')

    # создаем цикл:
    while answer=="д" or answer=="Д":
        #print("Получим необходимые данные о товаре: ")
        articul=input("Введите артикул товара: ")
        ostatok=int(input("Какое количество на остатке: "))

        # запишем полученные данные в файл:
        file.write(articul+'\n')
        file.write(str(ostatok)+'\n')

        print("Хотите добавить еще одну запись в файл?")
        answer=input("Если ДА, то напишите 'ДА' или 'да'")

        #закрываем файл
    file.close()
#sportive_store()


def trans_gaz_store():
    answer = "д"

    file = open(r'D:\Фильмы\gaz.txt', 'a')

    while answer=="д" or answer=="Д":
        print("Пропишите информацию по ТМЦ: ")
        nomer=input("Номенклатурный номер: ")
        count=int(input("Количество единиц: "))

        # добавляем данные в файл:
        file.write(nomer+'\n')
        file.write(str(count)+'\n')

        print("Хотите добавить еще одну позицию ТМЦ?")
        answer=input("Если хотите,то введите 'ДА'")

    file.close()
    print("Данные по складу хранятся в файле D:\Фильмы\gaz.txt")

#trans_gaz_store()


def show_file():
    #эта программа показывает записи из файла gaz.txt

    #ооткрываем файл gaz.txt:
    file=open(r'D:\Фильмы\gaz.txt', 'r')

    #прочиатть поле с описанием первой записи:
    nomer=str(file.readline())

    #прочитать остаток файла в цикле:
    while nomer!="":
        count=file.readline()

        # удалить перенос из описания:
        #nomer=nomer.rsplit('\n')


        #показать запись на экране:
        print("Номенклатурный номер: ",nomer)
        print("Количество: ",count,"ед.")

        # прочитать самую первую строку:
        nomer = int(file.readline())

    file.close()
#show_file()


def my_room():
    # создадим переменную,управляющую главным циклом:
    answer="y"

    # создадим файл с функцией добавления записей
    file=open(r'D:\Фильмы\my_room.txt','a')

    # создаем цикл с повторяющимся вопросом:
    while answer=='y' or answer=="Y":
        print("Напишите подробности по интвентарю вашей комнаты.")
        predmet_name=input("Название предмета: ")
        kolichestvo=float(input("Количество штук: "))

        # добавляем эти записи в наш файл:
        file.write(predmet_name+'\n')
        file.write(str(kolichestvo)+'\n')

        #задаем вопрос повторно:
        print("Хотите доавить еще одну запись в файл? ")
        answer=input("Если да,то нажмите'y'или'Y',если нет,то любую другую клавишу: ")

    #закрываем файл:
    file.close()

    #печатаем ифныу где искать файл на компе:
    print("Данные сохранены в файл D:\Фильмы\my_room.txt")


#my_room()


def read_my_room():
    # откроем нужный файл в режиме для чтения:
    file=open(r'D:\Фильмы\my_room.txt','r')

    # прочитаем первую строку на предмет проверки ее пустоты:
    predmet_name=file.readline()
    # создадим цикл с условием:
    while predmet_name!="":
        kolichestvo=float(file.readline())

        # уберем "\n" из строк:
        predmet_name=predmet_name.rstrip('\n')
        #kolichestvo=kolichestvo.rstrip('\n')

        #выводим данные на экран:
        print("Название предмета: ",predmet_name)
        print("Количество: ",kolichestvo,"штук")

        # прочитываем еще раз первую строку:
        predmet_name = file.readline()

    # закрываем файл:
    file.close()


#read_my_room()


#                ПОИСК ЗАПИСЕЙ В ФАЙЛЕ!!!!

def search_in_file():
    # эта программа позволяет пользовтелю производить поиск в файле записей,
    #которые соответствуют описанию.

    # создаем булевую переменную для использования ее в качестве флага:
    found=False
    # получим искомое значение:
    search=input("Введите искомое описание: ")

    # открыть файл,в котором будем искать:
    file=open(r'D:\Фильмы\my_room.txt','r')

    # прочитать первое поле:
    predmet_name = file.readline()

    # прочитать остаток файла:
    while predmet_name!="":
        kolichestvo = float(file.readline())

        # удаляем пропуск из описания:
        predmet_name=predmet_name.rstrip("\n")

        # определить, соответствует ли эта запись поисковому значению:
        if predmet_name==search:
            # выводим запись на экран:
            print("",predmet_name)
            print("",kolichestvo)
            print()
            # назначит флагу found значение True
            found=True

            # читаем следующее ( самое первое) описание:
        predmet_name = file.readline()

    file.close()
        # если поисковое значение не найдено, вывести на экран сообщение:
    if not found:
        print("Такого значения в файле нет!")


#search_in_file()


def my_bagaj():
    #создаем переменую,управляющую циклом:
    answer="Y"
    # создаем файл:
    file=open(r'D:\Фильмы\my_bag_for_travel.txt','a')
    # создаем цикл:
    while answer=="Y" or answer=="y":
        print("Опишите предметы багажа: ")
        staff=input("Наименование: ")
        calc=float(input("Количество: "))

        # прописыаем данные в файл:
        file.write(staff+'\n')
        #file.write(str(calc)+'\n')

        # задаем вопрос еще раз:
        print("Есди хотите добавить еще один предмет, ответьте 'y'")
        answer=input("y or n ?")
    file.close()
    print("Все записанные данные хранятся в файле D:\Фильмы\my_bag_for_travel.txt")
#my_bagaj()

def search_bagaj():
    # заводим булевую переменную:
    found=False

    # запросить что будем искать:
    search=input("Введи название того,что хочешь найти: ")

    #открываем файл:
    file=open(r'D:\Фильмы\my_bag_for_travel.txt','r')

    # читаем первую строку:
    staff=file.readline()

    # создаем цикл:
    while staff!="":
        calc=file.readline()

        #удаляем переносы:
        staff=staff.rstrip("\n")
        #calc=calc.rstrip("\n")

        # ищем нужный файл:
        if staff==search:
            print("",search)
            print("",calc,"шт")
            found=True
        # прочитываем первую строку еще раз:
        staff = file.readline()
    file.close()
    if not found:
        print("Такого предмета в багажнике нет!")

#search_bagaj()


#                           ИЗМЕНЕНИЯ ЗАПИСЕЙ

# Для того чтобы изменить запись в последовательном файле, необходимо создать второй
# временный файл. Все записи исходного файла копируются во временный файл, но, когда вы
# добираетесь до записи, которая должна быть изменена, старое содержимое записи во временный
# файл не сохраняется. Вместо этого во временный файл записываются новые измененные
# значения записи. Затем из исходного файла во временный файл копируются все
# остальные записи.
# Временный файл занимает место исходного файла. Исходный файл удаляется и временный
# файл переименовывается, получая имя, которое имел исходный файл на диске компьютера.
# Вот общий алгоритм вашей программы.
# Открыть исходный файл для ввода и создать временный файл для вывода.
# Получить описание изменяемой записи и новое значение количества.
# Прочитать из исходного файла первое поле с описанием.
# До тех пор, пока поле с описанием не пустое:
# Прочитать поле с количеством.
# Если поле с описанием этой записи соответствует введенному описанию:
# Записать во временный файл новые данные.
# Иначе:
# Записать во временный файл существуюшую запись.
# Прочитать следующее поле с описанием.
# Закрыть исходный файл и временный файл.
# Удалить исходный файл.
# Переименовать временный файл, дав ему имя исходного файла.

def changes_bagaje():
    # эта программа позволяет пользователю изменять количество в
    # записях файла

    # импортируем модуль os для применения функций удаления и переименования файлов
    import os

    # создаем будевую переменную для использования ее в качестве флага:
    found=False

    # получаем искомое значение и новое количество:
    search=input("Введи что ищем: ")
    new_calc=int(input("Введи обновленное количество: "))

    # открываем исходный файл:
    file=open(r'D:\Фильмы\my_bag_for_travel.txt','r')

    # открыть временный файл:
    temp_file=open(r'D:\Фильмы\temp_my_bag_for_travel.txt','w')

    # прочитать поле с описанием первой записи:
    staff=file.readline()

    # прочитать остаток файла:
    while staff!="":
        calc=file.readline()

        # удаляем пропуск из описания:
        staff=staff.rstrip('\n')

        # записать во временный файл дибо эту запись,
        # либо новую запись, если она подлежит изменению.
        if staff==search:
            # записать во временный файл измененную запись:
            temp_file.write(staff+'\n')
            temp_file.write(str(new_calc)+'\n')
            #назначит флагу новое значение:
            found=True
        else:
            #записать исходную запись во временный файл:
            temp_file.write(staff+'\n')
            temp_file.write(str(calc)+'\n')

        # прочитать первую строку еще раз:
        staff=file.readline()

    # закрыть файл с данными о багаже и временный файл
    file.close()
    temp_file.close()

    # удалить исходный файл:
    os.remove("my_bag_for_travel.txt")

    # переименовать временный файл:
    os.rename("temp_my_bag_for_travel.txt","my_bag_for_travel.txt")

    # если искомое значение в файле не найдено,то вывести на экран:
    if found:
        print("Файл обновлен!")
    else:
        print("Нет такого в багаже!")

#changes_bagaje()


a=5
if a<6:
    print('1')
elif print('2')










