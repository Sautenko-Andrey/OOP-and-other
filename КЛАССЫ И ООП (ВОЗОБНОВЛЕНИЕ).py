import for_bank


def main_1():
    # зададим первоначальный баланс карты
    balance = 0
    # создадим объект класса
    my_card = for_bank.Your_card(balance)

    # посмотрим остаток по карте в текущий момент
    print('Остаток на карте сейчас составляет:', my_card.show_money(), 'грн')

    # пополним карточку на сумму 1000 грн
    money_to_card = float(input('На сколько пополним карточку?'))
    print(f'Выполняется пополнение карты на {money_to_card} грн')
    my_card.put_money(money_to_card)

    # проверим еще раз остаток на карте
    print('Остаток на карте составляет:', my_card.show_money(), 'грн')

    # снимем 500 грн и снова проверим остаток на карте
    money_to_get = float(input('Сколько денег ты хочешь снять?'))
    print(f'Выдача наличных в размере {money_to_get} грн')
    my_card.get_money(money_to_get)
    print('Остаток по карте:', my_card.show_money(), 'грн')

    print(my_card)


# main_1()

import vegas


def main_2():
    # будем подбрасывать сразу 5 кубиков
    cube_1 = vegas.Cube()
    cube_2 = vegas.Cube()
    cube_3 = vegas.Cube()
    cube_4 = vegas.Cube()
    cube_5 = vegas.Cube()

    # посмотрим текущее состояние всех кубиков
    print('Кубик 1 лежит на стороне:' + cube_1.get_side())
    print('Кубик 2 лежит на стороне:' + cube_2.get_side())
    print('Кубик 3 лежит на стороне:' + cube_3.get_side())
    print('Кубик 4 лежит на стороне:' + cube_4.get_side())
    print('Кубик 5 лежит на стороне:' + cube_5.get_side())

    # подбросим сразу все кубики
    print('Бросаем все пять кубиков на стол...')
    cube_1.mix_cube()
    cube_2.mix_cube()
    cube_3.mix_cube()
    cube_4.mix_cube()
    cube_5.mix_cube()

    # посмотрим результат
    print('Кубики легли такими сторонами:')
    print(cube_1.get_side(), cube_2.get_side(), cube_3.get_side(), cube_4.get_side(), cube_5.get_side(), sep='|')


# main_2()

def main_3():
    # теперь будет 3 банковские карточки
    start_balance = 0
    my_card = for_bank.Your_card(start_balance)
    mothers_card = for_bank.Your_card(start_balance)
    fathers_card = for_bank.Your_card(start_balance)

    # проверим текущее состояние всех карточек
    print(my_card)
    print(mothers_card)
    print(fathers_card)

    # пополним каждую из карточек
    add_money = float(input('Введи сумму пополнения карточки:'))
    my_card.put_money(add_money)
    add_money = float(input('Введи сумму пополнения карточки:'))
    mothers_card.put_money(add_money)
    add_money = float(input('Введи сумму пополнения карточки:'))
    fathers_card.put_money(add_money)

    print('Карточки пополняются на указанные суммы...')

    # посмотрим баланс на всех карточках
    print(my_card)
    print(mothers_card)
    print(fathers_card)

    # снимеме некоторые суммы с каждой карточки
    money = float(input('Введи сумму, которую хочешь снять с карты:'))
    my_card.get_money(money)
    money = float(input('Введи сумму, которую хочешь снять с карты:'))
    mothers_card.get_money(money)
    money = float(input('Введи сумму, которую хочешь снять с карты:'))
    fathers_card.get_money(money)

    # проверим состояние карт
    print(my_card)
    print(mothers_card)
    print(fathers_card)


# main_3()
import producti


def main_4():
    # протестируем здесь класс Товар
    # получим данные о товаре
    name = input('Введи название товара:')
    kol = float(input('Введи вес продукта:'))
    cena = float(input('Введи цену за 1 кг:'))

    # создадим экземпляр класса
    tovar = producti.Tovar(name, kol, cena)

    # покажем данные по товару,которые мы ввели
    print('Наименование продукта:' + tovar.get_name())
    print('Вес:', tovar.get_count())
    print('Цена за 1 кг: ', tovar.get_price())
    print('Товара на складе на сумму:', tovar.get_count() * tovar.get_price(), 'грн')


# main_4()

#                                     ХРАНЕНИЕ ОБЪЕКТОВ В СПИСКЕ

# Создадим три товара с данными и заведем их в список, который потом покажем
def main_5():
    # получим список объектов
    object_list = spisok_tovarov()
    # посмотрим данные по каждому объектув списке
    print('Данные,которые ты ввел:')
    show_objects(object_list)


# создадим список
def spisok_tovarov():
    moy_spisok = []
    # добавим три объкта класса Товар в список
    for i in range(3):
        # получим данные о товарах
        nazvanie = input('Введи название товара:')
        ves = float(input('Введи вес продукта:'))
        stoimost = float(input('Введи цену товара за 1 кг:'))
        # создадим непосредственно объекты для записи этих данных
        moy_tovar = producti.Tovar(nazvanie, ves, stoimost)
        # добавим в список
        moy_spisok.append(moy_tovar)

    return moy_spisok


def show_objects(moy_spisok):
    # функция принимает в качестве аргумента список товаров
    # и показывает данные по каждому из них
    for tovar in moy_spisok:
        print('Название товара:' + tovar.get_name())
        print('Вес товара:', tovar.get_count(), 'кг')
        print('Цена за 1 кг:', tovar.get_price(), 'грн')
        print('---------------')


# main_5()
KOL_TOVAR = 2


def main_6():
    # создать объекты и засунуть их в список
    my_list = make_list()
    # показать данные по всем объектам в списке
    print('Данные по товару в магазине.')
    print('----------------------------')
    show_objects(my_list)


def make_list():
    # сначала создаем пустой список, в который будем вносить наши объекты
    list = []
    # внесем 2 товара в список

    for i in range(KOL_TOVAR):
        # получим данные по каждому товару
        name = input('Наименование:')
        massa = float(input('Вес на складе:'))
        price = float(input('Цена за 1 кг:'))

        # создадим непосредственно экземпляр класса
        product = producti.Tovar(name, massa, price)
        # занесем теперь его в пустой список
        list.append(product)

    # и вернем наполненный список
    return list


def show_list(list):
    # покажем все данные по товару
    for tovar in list:
        print('Наименование:' + tovar.get_name())
        print('Вес на складе:', tovar.get_count())
        print('Цена за 1 кг:', tovar.get_price())
        print()


# main_6()

def main_7():
    kubik = vegas.Cube()
    print('Изначально было вот так: ', kubik.get_side())

    podbrosit_kubik(kubik)

    print('Стало вот так: ', kubik.get_side())


def podbrosit_kubik(cube):
    cube.mix_cube()


# main_7()

def main_8():
    # создадим список,в которой положим несколько объектов класса
    # и потом выведем информацию на экран
    tovar_list = create_list()
    show_tovar(tovar_list)


def create_list():
    # создадим объекты класса и положим их в список при помощи цикла for
    my_list = []
    kol_obj = int(input('Какое количество товара добавим в список?'))
    for i in range(kol_obj):
        # получим все данные по товару:
        item_name = input('Введи наименование товара:')
        item_kol = float(input('Введи наличие товара в кг:'))
        item_price = float(input('Введи цену товара за 1 кг:'))

        # теперь создадим объект класса и в него положим эти данные
        prod = producti.Tovar(item_name, item_kol, item_price)

        # положим каждый созданный объект в пустой список
        my_list.append(prod)

    # вернем уже полностью наполненный товавром список
    return my_list


def show_tovar(my_list):
    for tovar in my_list:
        print('Здесь собрана вся актуальная информация по товару!')
        print('-------------------------------------------------')
        print('Наименование', tovar.get_name())
        print('Остаток в магазине:', tovar.get_count(), 'кг')
        print('Цена за 1 кг:', tovar.get_price(), 'кг')
        print('-------------------------------------------------')


# main_8()


#                                  КОНСЕРВАЦИЯ СОБСТВЕННЫХ ОБЪЕКТОВ


# эта программа консервирует объекты класса Товар
import pickle


def main_9():
    # инициализируем переменную для управления циклом
    answer = 'y'

    # откроем файл
    file = open('D:\Фильмы\c_tovar.dat', 'wb')

    # получим данные от пользователя,и запишем их в созданные объекты
    while answer.upper() == 'Y':
        # получим данные от пользователя
        tovar_name = input('Введи название товара:')
        tovar_kol = float(input('Введи остаток товара в кг:'))
        tovar_cena = float(input('Введи цену товара за 1 кг:'))

        # создадим объект класса Товар:
        tovar = producti.Tovar(tovar_name, tovar_kol, tovar_cena)

        # законсервируем объект
        pickle.dump(tovar, file)

        # спросим у пользователя,нужно ли законсервировать еще один объект
        answer = input('press Y or y to continue...')

    # закроем файл
    file.close()
    print('Данные по товару записаны в "D:\Фильмы\c_tovar.dat"')


# main_9()


# эта программа расконсервирует объекты класса Товар
def main_10():
    end = False  # для обозначения конца файла

    # откроем файл
    file = open('D:\Фильмы\c_tovar.dat', 'rb')

    # прочитаем файл до конца
    while not end:
        # пытаемся расконсервировать объект(мы не знаем существует он или нет
        try:
            tovar = pickle.load(file)

            # покажем данные о товаре
            show_info(tovar)

        except EOFError:
            # установим флаг,чтобы обозначить,что был достигнут конец файла
            end = True

    # закроем файл
    file.close()


def show_info(tovar):
    # функция показывает всю инфу по объектам
    print('Актуальная информация по товару на складе магазина!')
    print('----------------------------------------------------')
    print('Наименование:', tovar.get_name())
    print('Остаток в кг:', tovar.get_count(), 'кг')
    print('Цена за 1 кг:', tovar.get_price(), 'грн')
    print('----------------------------------------------------')


# main_10()

def main_11():
    # эта программа законсервирует объекты
    # инициализируем переменную для управления циклом
    user_answer = 'y'

    # создадим цикл,в котором будем получать данные по товару и записывать их в объект,
    # который в свою очередь будет консервироваться в файле

    # откроем файл
    file = open('D:\Фильмы\c_produkt.dat', 'wb')

    # запустим цикл
    while user_answer.upper() == 'Y':
        # получим данные от пользователя
        name = input('Введи наименование товара: ')
        kol = float(input('Введи остаток на складе в кг: '))
        price = float(input('Введи цену за 1 кг: '))

        # создаем объект класса Товар
        tovar = producti.Tovar(name, kol, price)

        # консервируем объект
        pickle.dump(tovar, file)

        # спрашиваем у пользователя про повтор операции
        user_answer = input('press y  or Y to continue...')

    # закрываем файл
    file.close()
    print('Вся информация по товару записана в D:\Фильмы\c_produkt.dat')


# main_11()


def main_12():
    # эта программа расконсервирует объекты и показывает инфу по товару
    end = False
    file = open('D:\Фильмы\c_produkt.dat', 'rb')
    while not end:
        try:
            tovar = pickle.load(file)

            # показать инфу из расконсрвированного объекта
            get_info(tovar)
        except EOFError:
            end = True


def get_info(tovar):
    print('Информация,которую ввел пользователь:')
    print('-------------------------------------')
    print('Наименование:', tovar.get_name())
    print('Остаток:', tovar.get_count(), 'кг')
    print('Цена за 1 кг:', tovar.get_price(), 'грн')
    print('-------------------------------------')


# main_12()


#                                     ХРАНЕНИЕ ОБЪЕКТОВ В СЛОВАРЕ
import personal_info

# эта программа управляет продуктами вмагазине
# глобальные константы для пунктов меню
LOOK_FOR_PERSON = 1
ADD_PERSON = 2
CHANGE_PERSON = 3
DELETE_PERSON = 4
EXIT = 5


def main_13():
    # загрузить сужествующий словарь с данными о работниках и присовить его переменной
    info = load_slovar()
    # инициализировать переменную для выбора пользователя из меню и присвоить ей ноль
    user_choice = 0

    # обрабатывать пункты меню до тех пор,пока пользователь не захочет выйти
    while user_choice != EXIT:
        # получим выбранный пользователем пункт меню
        user_choice = menu()
        # обработаем выбор
        if user_choice == 1:
            look_for_person(info)
        elif user_choice == 2:
            add_person(info)
        elif user_choice == 3:
            change_person(info)
        elif user_choice == 4:
            delete_person(info)

        # сохраняем и консервируем словарь
        save_info(info)


def load_slovar():
    # функция будет расконсервировать словарь
    # с данными о товаре или же создавать новый
    # пустой словарь,если не найдет его по адресу
    try:
        # пытаемся открыть файл
        file = open('D:\Фильмы\c__dannie.dat', 'rb')
        # расконсервируем его и закроем файл
        person = pickle.load(file)
        file.close()
    except EOFError:
        # если не получилось открыть файл,то создаем пустой словарь
        person = {}
    # и вернем этот словарь из функции
    return person


def menu():
    # функция показывает меню и проверят выбор пользователя на допустимость
    print('МЕНЮ ПРОГРАММЫ')
    print('--------------')
    print('1.Найти человека')
    print('2.Добавить человека')
    print('3.Изменить данные о человеке')
    print('4.Удалить данные о человеке')
    print('5.Выйти из программы')
    print('------------------------------')

    # получить выбранный пользователем пункт меню
    user_choice = int(input('Выбери пункт из меню: '))

    # проверим выбранный пункт на допустимость
    if user_choice < LOOK_FOR_PERSON or user_choice > EXIT:
        user_choice = int(input('Выбери допустимый пункт из меню!'))

    # вернем выбранный пункт из функции
    return user_choice


def look_for_person(person):
    # функция поиска человека по ключу словаря (по имени)
    # получим имя,которое нужно найти
    name = input('Введи имя человека, которого нужно найти: ')

    # отыщем его в словаре
    print(person.get(name, 'Нет такого человека!'))


def add_person(person):
    # функция добавления новой записи в словарь
    name = input('Введи имя для добавления:')
    pos = input('Введи должность:')
    id = input('Введи персональный код:')

    # создадим новый объект
    new_person = personal_info.Human(name, pos, id)

    # если этого человека нет в словаре,то добавить
    if name not in person:
        person[name] = new_person
        print('Запись добавлена')
    else:
        print('Это имя уже существует!')


def change_person(person):
    name = input('Введи имя человека,чью инфу ты хочешь изменить: ')

    # проверим,есть ли это имя в словаре
    if name in person:
        # получим от пользователя новые данные
        pos = input('Введи новую должность: ')
        id = input('Введи новый персональный код: ')

        # создадим измененный объект
        changed_person = personal_info.Human(name, pos, id)

        # обновим запись
        person[name] = changed_person
        print('Информация обновлена')
    else:
        print('Такое имя не найдено!')


def delete_person(person):
    name = input('Введи имя человека,чьи данные ты хочешь удалить: ')
    if name in person:
        del person[name]
        print('Заптсь удалена!')
    else:
        print('Нет такого человека!')


def save_info(person):
    # функция консервирует объект и сохраняет его в файле
    # откроем файл для записи
    file = open('D:\Фильмы\c__dannie.dat', 'wb')

    # консервируем объект
    pickle.dump(person, file)

    file.close()


#main_13()


#                              УНИФИЦИРОВАННЫЙ ЯЗЫК МОДЕЛИРОВАНИЯ

