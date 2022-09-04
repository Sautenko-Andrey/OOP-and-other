def pr1():
    phone_book = {'Andrey': '0950180611', 'Tanya': '0995045594', 'Jenya': '0502329017'}
    print(phone_book['Andrey'])
    print(phone_book['Tanya'])
    print(phone_book['Jenya'])


# pr1()


#                            Применение операторов in и not in
#                          для проверки на наличие значения в словаре

def pr2():
    try:
        search = input("Введи название кроссовок: ")
        sportive_shop = {'Nike': '1600', 'Asics': '1990', 'Puma': '2500'}
        if search in sportive_shop:
            print(sportive_shop[search])

    except KeyError as err:
        print(err)


# pr2()


def pr3():
    try:
        search = input("Что ищем?")
        vocabulary = {'car': 'машина', 'book': 'книга', 'sales': 'продажи'}
        if search not in vocabulary:
            print("Нет такого слова в словаре!")
        else:
            print(vocabulary[search])

    except KeyError as err:
        print(err)


# pr3()


#                              Добавление элементов в существующий словарь

def pr4():
    try:
        articules = {'bv4320-001': 'Nike Revolution 5', 'ci4330-100': 'Nike Swift Run 2',
                     '4900-400': 'UA Pahntom 3'}
        print(articules)

        articules['bv5510-200'] = 'Nike Downshifter 12'
        print(articules)
    except KeyError as err:
        print(err)


# pr4()


#                                            Удаление элементов

def pr5():
    try:
        spisok_del = {'1': 'Забрать кроссовки', '2': 'Снять контент для кроссовок',
                      '3': 'Сделать уборку',
                      '4': 'Смонтировать видео для инсты', '5': 'Пожрать?'}
        print(spisok_del)

        del spisok_del['5']
        print(spisok_del)

    except KeyError as err:
        print(err)
    except ValueError as err2:
        print(err2)


# pr5()

def pr6():
    try:
        search_for_delete = input("Напиши,что будем удалять: ")
        vocabulary = {'1': 'Денщик/Седых', '2': 'Чаусов/Саутенко', '3': 'Коструб/Терещук'}
        if search_for_delete in vocabulary:
            del vocabulary[search_for_delete]
        else:
            print(f'{search_for_delete} - нет такого в списке!')
        print(vocabulary)
    except ValueError as err:
        print(err)


# pr6()


#                         Получение количества элементов в словаре

def pr7():
    my_films = {'1': 'Все без ума от Мэри', '2': 'Идентификация Борна', '3': '5-й элемент'}
    kolichestvo_filmov = len(my_films)
    print(f'Количество фильмов в списке равно: {kolichestvo_filmov}')


# pr7()


#                                Смешивание типов данных в словаре

def pr8():
    try:
        ocenki = {'Andrey': [100, 87, 75],
                  'Danil': [88, 75, 97],
                  'Alex': [100, 55, 80]}

        score_Andrey = ocenki['Andrey']
        print("Оценки Андрея: ", score_Andrey)
        score_Danil = ocenki['Danil']
        print("Оценки Данила: ", score_Danil)
        score_Alex = ocenki['Alex']
        print("Оценки Саши: ", score_Alex)

    except KeyError as err:
        print(err)
    except ValueError as err2:
        print(err2)


# pr8()

def pr9():
    store = {1: 100, 2: 200, 3: 300}
    print(store)


# pr9()

def pr10():
    dela = {'утро': ("позавтракать", "забрать кроссовки", "прогуляться"),
            "обед": ("пообедать", "смонтировать видео", "посмотреть кино"),
            "вечер": ("попрограммировать", "поужинать", "лечь спать")}
    day_time = input("Введи время суток: ")
    if day_time in dela:
        print(dela[day_time])
    else:
        print("Неверно указано время дня!")


# pr10()


def pr11():
    my_mix = {1: 100, 2: 'abc', '3': [1, 2, 3, 4, 5], (4, 5): (6, 7, 8, 'salo')}
    print(my_mix)
    print(my_mix[1])
    print(my_mix[2])
    print(my_mix['3'])
    print(my_mix[(4, 5)])


# pr11()

def pr12():
    try:
        personal_info = {'name': 'Sautenko Andrey', 'id': 84320, 'office rooms': (5, 29)}
        print(personal_info['name'], end=" ")
        print(personal_info['id'], end=' ')
        print(personal_info['office rooms'])
    except KeyError as err:
        print(err)


# pr12()


#                                     Создание пустого словаря

def pr13():
    phonebook = {}
    phonebook['Andrey'] = '0950180611'
    phonebook['Chaus'] = '0994646547'
    phonebook['Danil'] = '0508894612'
    phonebook['Rodik'] = '0663301258'
    phonebook['Alex'] = '0995087946'
    print(phonebook)
    del phonebook['Rodik']
    del phonebook['Danil']
    print(phonebook)


# pr13()


#                                        Применение цикла for
#                                для последовательного обхода словаря

def pr14():
    try:
        my_slovar = {'one': 'один', 'digit': 'цифра', 'carrot': 'морковка'}
        for key in my_slovar:
            print(key)
        print()
        for key in my_slovar:
            print(my_slovar[key])
    except KeyError as err:
        print(err)
    except ValueError as err2:
        print(err2)


# pr14()


def pr15():
    player_ranks = {'Denshik': 97.88, 'Tereshyk': 88.70, 'Sautenko': 75.11}
    for key in player_ranks:
        print(key)
    print()
    for key in player_ranks:
        print(player_ranks[key])


# pr15()


#                                   Несколько словарных методов

#                                           Метод clear()
#                 Метод clear () удаляет все элементы в словаре, оставляя словарь пустым.
def pr16():
    my_dict = {1: 'salo', 2: 'bread', 3: 'potato'}
    my_dict.clear()
    print(my_dict)


# pr16()


#                                           Метод get()
# Для получения значения из словаря в качестве альтернативы оператору [] можно воспользоваться
# методом get() • Он не вызывает исключение, если заданный ключ не найден.

def pr17():
    phonebook = {'Andrey': '0950180611', 'Tanya': '0995045594'}
    get_phone = phonebook.get('Andrey', 'нет такого имени в книге')
    print(get_phone)
    get_phone = phonebook.get('Alex', 'Нет такого имени в телефонной книге!')
    print(get_phone)


# pr17()

#                                       Метод items()

# Метод items () возвращает все ключи словаря и связанные с ними значения. Они возвращаются
# в виде последовательности особого типа, которая называется словарным представлением.
# Каждый элемент в словарном представлении является кортежем, и каждый кортеж
# содержит ключ и связанное с ним значение.
def pr18():
    shop_price = {'nike downshifter 9': '1400.00', 'nike revolution 5': '1500.00', 'asics trail scout 2': '1550.00'}
    for key, value in shop_price.items():
        print(key, value)


# pr18()

#                                          Метод keys()
# Метод keys () возвращает все ключи словаря в виде словарного представления, т. е. особого
# типа последовательности. Каждый элемент в словарном представлении является ключом
# словаря.

def pr19():
    articles = {'bv4320-001': 1500, '654658-100': 1950, 'fv4002-002': 950}
    for keys in articles.keys():
        print(keys)


# pr19()

def pr20():
    my_dict = {'salo': 15, 'kartoshka': 12, 'pivo': 50}
    print(my_dict)
    my_dict.clear()
    print(my_dict)


# pr20()

def pr21():
    beer_price = {'chernigov': 15.00, 'carslberg': 19.75,
                  'stella arthois': 23.90, 'corona extra': 30.23}
    search_beer = beer_price.get('corona extra')
    print(search_beer)


# pr21()

def pr22():
    my_clothes = {'nike tee': 2, 'nike shorts': 2, 'ua cap': 1, 'puma jacket': 1, 'nike hoody': 1}
    print(my_clothes)
    new_file = my_clothes.items()
    print(new_file)


# pr22()

def pr23():
    need_to_pay = {'for Viktor': 5600, 'for bank': 7000}
    print(need_to_pay)
    get_keys = need_to_pay.keys()
    print(get_keys)


# pr23()

def pr24():
    cooking_soup = {'potato': 4, 'carrot': 0.5, 'onion': 1, 'chiken': 0.3, 'water': 2.5, 'spagetti': 0.25}
    print(cooking_soup)
    new_list = cooking_soup.pop('spagetti')
    print(cooking_soup)


# pr24()

def pr25():
    need_to_by = {'tea': 1, 'beer': 10, 'meat': 2.5, 'cheese': 0.4, 'vegetebles': 5}
    print(need_to_by)
    delete_random = need_to_by.popitem()
    print()
    print(delete_random)
    print(need_to_by)


# pr25()


def pr26():
    films = {1: 'Terminator 2', 2: 'Die hard', 3: 'Die hard 3', 4: 'Commandos', 5: 'Mortal Combat 2'}
    print(films)
    get_films = films.values()
    print()
    print(get_films)
    for every_film in get_films:
        print(every_film)


# pr26()

def pr27():
    plans_for_evening = {1: 'study Python', 2: 'have dinner', 3: 'watch football', 4: 'take a rest'}
    search_task = plans_for_evening.get(3, 'there is no task!')
    print(search_task)
    print()
    search_task = plans_for_evening.get(5, 'no task here!')
    print(search_task)


# pr27()


def pr28():
    phones = {'Alex': '0502354789', 'Danil': '0997894563', 'Chaus': '0667894125'}
    for keys, values in phones.items():
        print(keys, values)


# pr28()


def pr29():
    should_buy = {'socks': 6, 'jeans': 1, 'trousers': 5}
    for keys in should_buy.keys():
        print(keys)


# pr29()


def pr30():
    champioship = {'kramatorsk': 1, 'bahmut': 2, 'kharkov': 3}
    result_team = champioship.pop('kramatorsk', 'thereis no team with texted name!')
    result_team2 = champioship.pop('slavyansk', 'thereis no team with texted name!')
    print(result_team)
    print(result_team2)


# pr30()


def pr31():
    animator_team = {'nastya': 'rus', 'vlada': 'ukr', 'ibo': 'tur', 'andrey': 'ukr'}
    print(animator_team)
    print()
    key, value = animator_team.popitem()
    print(key, value)
    print(animator_team)


# pr31()


def pr32():
    player_runks = {1: 'Denshik', 2: 'Tereshyk', 3: 'Sautenko', 4: 'Veselov', 5: 'Kostrub'}
    count = 0
    for values in player_runks.values():
        count += 1
        print('#', count, values)


# pr32()


#                        Применение словаря для имитации карточной колоды
# GAME BLACK JACK

def main_game():
    # создадим колоду кард
    koloda_kart = make_cards()

    # получить количество карт для раздачи
    kolichestvo_cart = int(input("Сколько хочешь получить карт на руки?"))

    # раздадим карты на руки
    razday_karti = give_cards(koloda_kart, kolichestvo_cart)


def make_cards():
    # создадим словарь для карт и их значений
    koloda = {'tuz cherv': 1, '2 cherv': 2, '3 cherv': 3,
              '4 cherv': 4, '5 cherv': 5, '6 cherv': 6,
              '7 cherv': 7, '8 cherv': 8, '9 cherv': 9,
              '10 cherv': 10, 'valet cherv': 10, 'dama cherv': 10,
              'korol cherv': 10}
    return koloda


def give_cards(koloda, kolich_cart):
    # созадим накопитель для количества карт на руках
    cards_on_hands = 0
    # убедиться ,что количество карт на руках не больше количества карт в колоде.
    if kolich_cart > len(koloda):
        kolich_cart = len(koloda)

    # раздать карты и накопить их значения
    for count in range(kolich_cart):
        card, value = koloda.popitem()
        print(card)
        cards_on_hands += value
    # показать величину карт на руках:
    print('Величина карт на руках: ', cards_on_hands)


# main_game()


def game_21():
    try:
        user_name = input('Введите свое имя: ')
        print(f'{user_name},мы начинаем игру!')
        kolichestvo = int(input('Сколько раздать карт?'))
        get_coloda = koloda_card()
        cards_in_hand = karti_na_rukah(get_coloda, kolichestvo)

    except ValueError as err:
        print(err)
    except KeyError as err2:
        print(err2)


def koloda_card():
    koloda = {'dvoika': 2, 'troika': 3, 'chetverka': 4,
              'pyaterka': 5, 'shesterka': 6, 'semerka': 7,
              'vosmerka': 8, 'devyatka': 9, 'desyatka': 10,
              'valet': 10, 'dama': 10, 'korol': 10, 'tuz': 11}
    return koloda


def karti_na_rukah(koloda, kolichestvo_card):
    count_value = 0
    if count_value > len(koloda):
        count_value = len(koloda)

    for count in range(kolichestvo_card):
        card_name, card_value = koloda.popitem()
        print(card_name)
        count_value += card_value
    print('У тебя на руках:', count_value)


# game_21()


#                                Хранение имен и дней рождения в словаре


# Эта программа применяет словарь для хранения имен и дней рождения друзей

# заведем глобальные константы для меню программы:
POISK_DR = 1
DOBAVIT_DR = 2
IZMENIT_DR = 3
YDALIT_DR = 4
VIHOD = 5


def main_friends_birthdays():
    try:
        # создадим пустой словарь:
        birthdays = {}

        # создадь перменную для выбора пользователя из меню:
        user_choice = 0
        while user_choice != VIHOD:
            user_choice = get_menu_choice()

            # обработать варианты выбора:
            if user_choice == POISK_DR:
                find_birthday(birthdays)
            elif user_choice == DOBAVIT_DR:
                add_birthday(birthdays)
            elif user_choice == IZMENIT_DR:
                change_birthday(birthdays)
            elif user_choice == YDALIT_DR:
                delete_birthday(birthdays)
    except Exception:
        print(Exception)


def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('-------------------------')
    print('1.Найти день рождения')
    print('2.Добавить новый день рождения')
    print('3.Изменить день рождения')
    print('4.Удалить день рождения')
    print('5.Выход из программы')
    print()

    # получить выбранный пользователем пункт:
    choice = int(input("Выбери пункт из меню: "))
    while choice < POISK_DR or choice > VIHOD:
        choice = int(input('Введите выбранный пункт: '))

    return choice


def find_birthday(birthdays):
    # получить искомое имя:
    name = input('Введи имя: ')
    # отыщем его в словаре:
    print(birthdays.get(name, 'Нет такого человека в списке друзей!'))


def add_birthday(birthdays):
    # получим имя и день рождения друга:
    name = input("Введи имя друга для добавления в список: ")
    birthday = input('Введи день рождения друга для добавления в список: ')

    if name not in birthdays:
        birthdays[name] = birthday
    else:
        print('Эта запись уже существует!')


def change_birthday(birthdays):
    name = input('Получить имя,которое хотите изменить: ')
    if name in birthdays:
        # введем измененный день рождения:
        bday = input('Введи измененный день рождения: ')

        # обновить запись:
        birthdays[name] = bday
    else:
        print('Имя не найдено!')


def delete_birthday(birthdays):
    name = input('Введи имя друга,чей др ты хочешь удалить: ')
    if name in birthdays:
        del birthdays[name]
    else:
        print('Нет такого имени в списке!')


# main_friends_birthdays()


# напишем собственную подобную программу для закрепления материала:
# создадим глобальные константы для меню:
DOBAVIT_TOVAR = 1
POISK_TOVARA = 2
IZMENIT_TOVAR = 3
UDALIT_TOVAR = 4
VIHOD_IZ_PROGRAMMI = 5


def main_shop():
    shop_items = {}
    choice = 0
    my_choice = choice_from_menu()
    while choice != VIHOD_IZ_PROGRAMMI:
        choice = choice_from_menu()

        if choice == DOBAVIT_TOVAR:
            add_item(shop_items)
        elif choice == POISK_TOVARA:
            search_item(shop_items)
        elif choice == IZMENIT_TOVAR:
            change_item(shop_items)
        elif choice == UDALIT_TOVAR:
            delete_item(shop_items)


def choice_from_menu():
    print()
    print('Программа для работы с товаром в магазине.')
    print('-------------------------------------------')
    print('1.ДОБАВИТЬ ТОВАР')
    print('2.ПОИСК ТОВАРА')
    print('3.ИЗМЕНИТЬ АРТИКУЛ ТОВАРА')
    print('4.УДАЛИТЬ ТОВАР')
    print('5.ВЫХОД')
    user_choice = int(input('Выбери пункт из меню: '))
    while user_choice < DOBAVIT_TOVAR or user_choice > VIHOD_IZ_PROGRAMMI:
        user_choice = input("Выбери из меню: ")
    return user_choice


def add_item(some_dict):
    name_for_add = input('Введи название товара для добавления: ')
    article_for_add = input('Введи артикул для добавления: ')
    if name_for_add not in some_dict:
        some_dict[name_for_add] = article_for_add
    else:
        print('Такое товар уже записан!')


def search_item(some_dict):
    search_name = input('Введи название товара для поиска: ')
    if search_name in some_dict:
        print('Артикул товара:', some_dict.get(search_name))
    else:
        print('Такого товара нет в магазине!')


def change_item(some_dict):
    name_for_change = input('Введи название товара,который хочешь изменить: ')
    if name_for_change in some_dict:
        some_dict[name_for_change] = input('Введи другой артикул: ')
    else:
        print('Нет такого товара в магазине!')


def delete_item(some_dict):
    name_for_delete = input('Введи название товара,который хочешь удалить: ')
    if name_for_delete in some_dict:
        del some_dict[name_for_delete]
    else:
        print('Нет такого товара')


# main_shop()


def pr243():
    empl = {'andy': 12345, 'mary': 4567}
    print(empl)
    print()
    empl['id'] = 54321
    print(empl)
    print(empl['mary'])
    for el in empl:
        print(el)


# pr243()


#                                           МНОЖЕСТВА

# Множество - это объект-контейнер уникальных значений, который работает как математическое
# множество .
def set1():
    my_set = set()
    my_set2 = set(['one', 'two', 'three'])
    print(my_set2)


# set1()
def some9872():
    myset = set('Andrey')
    print(myset)


# some9872()


def some284():
    myset = set('aaabbvv')
    print(myset)


# some284()

#                    Получение количества элементов в множестве
def some343():
    myset = set([1, 2, 3, 4, 5])
    print(len(myset))


# some343()

def some98():
    my_set = set('123456')
    print(len(my_set))


# some98()


#                                Добавление и удаление элементов
def some872():
    my_set = set()
    print(my_set)
    my_set.add('hello')
    my_set.add('sally')
    my_set.add('matrix')
    my_set.add(99)
    print(my_set)


# some872()

def some54():
    my_set = set([1, 2, 3])
    print(my_set)
    my_set.update([4, 5, 6])
    my_set.update((7, 8, 9))
    print(my_set)


# some54()


def some724():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([6, 7, 8, 9, 10])
    set1.update(set2)
    print(set1)
    print(set2)


# some724()


def some1343():
    my_set1 = set([1, 2, 3])
    my_set2 = set('abcdef')
    my_set1.update(my_set2)
    print(my_set1)


# some1343()

def pr4234():
    my_set1 = set([1, 2, 3, 4, 5])
    print(my_set1)
    my_set1.remove(5)
    print(my_set1)
    my_set1.add('hello')
    print(my_set1)
    my_set1.discard(4)
    print(my_set1)


# pr4234()


def som11():
    my_set = set(['matrix', 'sally', 'bennet'])
    print(my_set)
    my_set.clear()
    print(my_set)
    my_set.add('commando')
    print(my_set)
    for i in my_set:
        print(i)


# som11()


#                                       Применение цикла for
#                               для последовательного обхода множества


def mypract1():
    my_set = set(['I', 'want', 'to', 'get', 'a', 'good', 'job', '!'])
    for element in my_set:
        print(element)
    my_set2 = set([10, 20, 30])
    for element in my_set2:
        print(element)


# mypract1()


#                               Применение операторов in и not in
#                        для проверки на принадлежность значения множеству

def mypr1():
    my_set = set([10, 20, 30, 40])
    if 10 in my_set:
        print('10 is in my_set!')
    else:
        print('no!')


# mypr1()


def mypr2():
    my_set = set('abcdef')
    if 'b' not in my_set:
        print("w is not in my_set!")
    else:
        print('w is here...')


# mypr2()


#                                      Объединение множеств

def somepr3():
    my_set1 = set([1, 2, 3, 4, 5])
    my_set2 = set([6, 7, 8, 9, 10])
    set3 = my_set1.union(my_set2)
    print(set3)


# somepr3()


#                                    Пересечение множеств

def somepr234():
    my_set1 = set([1, 2, 3, 4, 5])
    my_set2 = set([3, 4, 5, 6, 7])
    total_set = my_set1.intersection(my_set2)
    print(total_set)


# somepr234()

def pr234():
    set1 = set('andrey')
    set2 = set('danil')
    total = set1.intersection(set2)
    print(total)


# pr234()

def pr6567():
    set1 = set('12345')
    set2 = set('34567')
    total = set1 & set2
    print(total)


# pr6567()

def pr111():
    set1 = set([10, 20, 30])
    set2 = set([10, 40, 50])
    total = set1 & set2
    print(total)


# pr111()


#                                      Разность множеств

def pr28374():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([3, 4, 5, 6, 7])
    dif = set1.difference(set2)
    print(dif)


# pr28374()


def some123():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([3, 4, 5, 6, 7])
    dif = set1 - set2
    print(dif)


# some123()


#                                    Симметрическая разность множеств

def some19():
    set1 = set('abcdef')
    set2 = set('defghi')
    dif = set1.symmetric_difference(set2)
    print(dif)


# some19()

def some202():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([3, 4, 5, 6, 7])
    dif = set1.symmetric_difference(set2)
    print(dif)


# some202()

def some303():
    set1 = set([100, 200, 300, 400])
    set2 = set([300, 400, 500, 600])
    dif = set1 ^ set2
    print(dif)


# some303()


#                                     Подмножества и надмножества

def some404():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([4, 5])
    if set2.issubset(set1):
        print('True')
    if set1.issuperset(set2):
        print('True')


# some404()

def some44():
    set1 = set('abcdef')
    set2 = set('cdef')
    if set1 >= set2:
        print("True")
    if set2 <= set1:
        print('True')


# some404()

#                                    Операции над множествами

# заведем глобальные константы:
def main_univer():
    # заведем два множества с командами:
    basketball_team = set(['Bond', 'Danil', 'Oleg', 'Tereh', 'Chaus'])
    volley_team = set(['Andrey', 'Danil', 'Chaus', 'Tereh', 'Roman'])

    # найдем пересечние множеств:
    total_1 = basketball_team.intersection(volley_team)
    print('Пацаны, которые играют в обеих командах: ')
    for name in total_1:
        print(name)

    # найжем объединение множеств:
    total_2 = basketball_team.union(volley_team)
    print('Все ребята,играющие в обеих командах:')
    for name in total_2:
        print(name)

    # разность для баскета:
    dif_basket = basketball_team.difference(volley_team)
    print('Ребята,играющие только в баскетбол: ')
    for name in dif_basket:
        print(name)

    # разность для волея:
    dif_volley = volley_team - basketball_team
    print('Ребята,играющие только в волейбол: ')
    for name in dif_volley:
        print(name)

    # симметрическая разность:
    dif_simm = basketball_team.symmetric_difference(volley_team)
    print('Играющие только в один вид спорта:')
    for name in dif_simm:
        print(name)


# main_univer()


def some76():
    my_set = set([1, 2, 3])
    my_set.update([4, 5, 6])
    print(my_set)


# some76()


#                                    СЕРИАЛИЗАЦИЯ ОБЪЕКТОВ
# Сериализация объекта - это процесс преобразования объекта в поток байтов, которые
# могут быть сохранены в файле для последующего извлечения. В Python сериализация
# объекта называется консервацией.

import pickle


def some_pr_1():
    phone_book = {'andrey': '0950180611',
                  'Mama': '0995045594',
                  'Papa': '0502329017'}
    file = open('D:\Фильмы\phone_book.dat', 'wb')
    pickle.dump(phone_book, file)
    file.close()


# some_pr_1()

import pickle


def some_unpack():
    file = open('D:\Фильмы\phone_book.dat', 'rb')
    get_file = pickle.load(file)
    print(get_file)
    file.close()


# some_unpack()

import pickle


def personal_data():
    answer = 'Y'  # для управления повторением цикла

    file = open('D:\Фильмы\data.dat', 'wb')

    while answer.upper() == 'Y':
        save_data(file)

        # выход из цикла:
        answer = input('press y or Y to continue...')


def save_data(file):
    # создаем пустой словарь:
    my_dict = {}

    # получить данные о человеке и сохранить их в словаре:
    my_dict['name'] = input("Введи имя:")
    my_dict['age'] = int(input('Введи возраст:'))
    my_dict['position'] = input('Введи должность:')

    # законсервировать словарь:
    pickle.dump(my_dict, file)


# personal_data()
import pickle


def data_open():
    end_of_file = False  # для обозначения конца файла

    # открыть файл для двоичного чтения:
    file = open('D:\Фильмы\data.dat', 'rb')

    # прочитаем содержимое файла:
    while not end_of_file:
        try:
            # расконсервировать объект:
            my_dict = pickle.load(file)

            # показать данные:
            show(my_dict)

        except ValueError as err:
            print(err)
            # установим флаг ,чтобы обозначить,что был достигнут конец файла:
            end_of_file = True

    file.close()


def show(some_data):
    # функция,показывающая данные
    print()
    print('Name', some_data['name'])
    print('Age', some_data['age'])
    print('Position', some_data['position'])
    print()


# data_open()

import pickle


def player_ranks():
    try:
        answer = 'Y'
        file = open('D:\Фильмы\players.dat', 'wb')
        while answer.upper() == 'Y':
            save_info(file)

            answer = input('press y or Y to continue: ')

    except Exception:
        print(Exception)


def save_info(some_file):
    ranks = {}
    ranks['name'] = input('Введи фамилию игрока: ')
    ranks['points'] = float(input('Введи его рейтинг: '))
    ranks['city'] = input('Введи город игрока: ')

    pickle.dump(ranks, some_file)


# player_ranks()

import pickle


def open_player_ranks():
    try:
        end_of_file = False

        file = open('D:\Фильмы\players.dat', 'rb')
        while not end_of_file:
            players_dict = pickle.load(file)

            show_on_display(players_dict)
        end_of_file = True
        file.close()
    except ValueError as err:
        print(err)


def show_on_display(some_dict):
    print('Эта программа прочитает рейтинги игроков!')
    print()
    print('Name:', some_dict['name'])
    print('Rank:', some_dict['points'])
    print('City:', some_dict['city'])


# open_player_ranks()

import pickle


def conserv_magazin():
    # заведем переменную,управляющую циклом:
    user_answer = 'Y'
    file = open('D:\Фильмы\my_shop.dat', 'wb')

    while user_answer.upper() == 'Y':
        save_shop_info(file)
        user_answer = input('Press y or Y to continue...')
    file.close()


def save_shop_info(some_file):
    items_dict = {}
    # получим название товара:
    items_dict['name'] = input('Введи название товара: ')
    items_dict['art'] = input('Введи артикул товара: ')

    pickle.dump(items_dict, some_file)


# conserv_magazin()

def unlock_magazin():
    file = open('D:\Фильмы\my_shop.dat', 'rb')
    end_of_file = False
    while not end_of_file:
        items_dict = pickle.load(file)
        show_items(items_dict)
    end_of_file = True


def show_items(some_dict):
    print('Эта пргграмма покажет товары с артикулами!')
    print()
    print('Название товара:', some_dict['name'])
    print('Артикул:', some_dict['art'])


# unlock_magazin()

import pickle


def phones():
    file = open('D:\Фильмы\phones.dat', 'wb')
    answer = 'y'
    while answer.upper() == 'Y':
        write_info(file)
        answer = input('press y or Y to continue: ')
    file.close()


def write_info(some_file):
    phones_dict = {}
    phones_dict['name'] = input('Enter friends name: ')
    phones_dict['number'] = input('Enter number: ')
    pickle.dump(phones_dict, some_file)


# phones()

def unlock_phones():
    file = open('D:\Фильмы\phones.dat', 'rb')
    end_of_file = False
    while not end_of_file:
        try:
            phones = pickle.load(file)
            print_info(phones)
        except EOFError:
            end_of_file = True
    file.close()


def print_info(some_dict):
    print("Welcome!")
    print()
    print('Friend:', some_dict['name'])
    print("Phone number:", some_dict['number'])


# unlock_phones()


def pr1112():
    my_set = set('aa bbbb ccccccc')
    print(my_set)


# pr1112()

def pr91():
    m1 = set([1, 2, 3, 4, 5])
    m2 = set([3, 4, 5, 6, 7])
    m3 = m1.union(m2)
    print(m3)


# pr91()

def pr772():
    s1 = set('abcdef')
    s2 = set('defghi')
    s3 = s1.intersection(s2)
    print(s3)


# pr772()

def at1():
    my_dict = {}
    my_dict['a'] = 1
    my_dict['b'] = 2
    my_dict['c'] = 3
    print(my_dict)


# at1()

# Предположим, что переменная dct ссылается на словарь. Напишите инструкцию if, которая
# определяет, существует ли в словаре ключ 'Джеймс'. Если да, то покажите значение,
# которое связано с этим ключом. Если ключа в словаре нет, то покажите соответствующее
# сообщение.
def at2():
    try:
        dct = {'Nik': 'sales manager', 'Jake': 'economist', 'James': 'developer'}
        if 'James' in dct:
            print(dct['James'])
        else:
            print('No key "James"')
    except KeyError as err:
        print(err)


# at2()

# Предположим, что переменная dct ссылается на словарь. Напишите инструкцию if,
# которая определяет, существует ли в словаре ключ 'Джим'. Если да, то удалите ключ
# 'Джим' и связанное с ним значение.

def at3():
    try:
        dct = {'Jim': 100, 'Gareth': 200, 'Mike': 300}
        print(dct)
        if 'Jim' in dct:
            del dct['Jim']
        else:
            print('no key!')
        print(dct)
    except KeyError as err:
        print(err)


# at3()

# Напишите фрагмент кода, который создает множество с приведенными далее целыми
# числами в качестве его членов: 1 О, 20, 30 и 40
def at4():
    try:
        my_set = set()
        item = 10
        for count in range(4):
            my_set.add(item)
            item += 10
        print(my_set)
    except ValueError as err:
        print(err)


# at4()

# Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фрагмент
# кода, который создает еще одно множество, содержащее все элементы из setl и
# set2, и присваивает получившееся множество переменной setЗ.

def at5():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([6, 7, 8, 9, 10])
    set3 = set1.union(set2)
    print(set3)


# at5()

# Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фрагмент
# кода, который создает еще одно множество, содержащее только те элементы, которые
# одновременно находятся в setl и в set2, и присвойте получившееся множество переменной
# setЗ.

def at6():
    s1 = set([1, 2, 3, 4, 5])
    s2 = set([4, 5, 6, 7, 8])
    s3 = s1.intersection(s2)
    print(s3)


# at6()

# Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фрагмент
# кода, который создает еще одно множество, содержащее все элементы setl, не
# входящие в set2, и присвойте получившееся множество переменной setЗ.
def at7():
    s1 = set([1, 2, 3, 4, 5])
    s2 = set([3, 4, 5, 6, 7])
    s3 = s1.difference(s2)
    print(s3)


# at7()

# Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фрагмент
# кода, который создает еще одно множество, содержащее все элементы set2, не
# входящие в setl, и присвойте получившееся множество переменной setЗ.

def at8():
    s1 = set([1, 2, 3, 4, 5])
    s2 = set([3, 4, 5, 6, 7])
    s3 = s2.difference(s1)
    print(s3)


# at8()

# Допустим, что обе переменные setl и set2 ссылаются на множество. Напишите фрагмент
# кода, который создает еще одно множество с элементами, не принадлежащими
# одновременно setl и set2, и присвойте получившееся множество переменной setЗ.
def at9():
    s1 = set([1, 2, 3, 4, 5])
    s2 = set([3, 4, 5, 6, 7])
    s3 = s1.symmetric_difference(s2)
    print(s3)


# at9()

# Предположим, что переменная dct ссылается на словарь. Напишите фрагмент кода, который
# консервирует словарь и сохраняет его в файле mydata.dat.
import pickle


def at10():
    try:
        dct = {'Ann': 10, 'Mary': 20}
        file = open('D:\Фильмы\ph.dat', 'wb')
        pickle.dump(dct, file)
        file.close()
    except ValueError as err:
        print(err)


# at10()

# Напишите фрагмент кода, который извлекает и расконсервирует словарь, законсервированный
# в задании 11.
import pickle


def at11():
    file = open('D:\Фильмы\ph.dat', 'rb')
    my_dict = pickle.load(file)
    file.close()
    print(my_dict)


# at11()

# Информация об учебных курсах. Напишите программу, которая создает словарь,
# содержащий номера курсов и номера аудиторий, где проводятся курсы. Словарь должен
# иметь приведенные в табл. 9 .2 пары ключ/значение.
def pr_task1():
    try:
        # создаю словари с данными для каждого курса:
        CS101 = {'Room number': '3004', 'Teacher': 'Haynz', 'Time': '08:00'}
        CS102 = {'Room number': '4501', 'Teacher': 'Alvarado', 'Time': '09:00'}
        CS103 = {'Room number': '6755', 'Teacher': 'Rich', 'Time': '10:00'}
        CS104 = {'Room number': '1244', 'Teacher': 'Berck', 'Time': '11:00'}
        CS105 = {'Room number': '1411', 'Teacher': 'Lee', 'Time': '13:00'}
        # получаю от пользователя искомый курс:
        user_search = input('Введи номер искомого курса: ')
        # перебираем все курсы и печатаем нужные данные:
        if user_search == 'CS101':
            print('Номер аудитории:', CS101.get('Room number'))
            print('Преподаватель:', CS101.get('Teacher'))
            print('Время начала занятия:', CS101.get('Time'))

        elif user_search == 'CS102':
            print('Номер аудитории:', CS102.get('Room number'))
            print('Преподаватель:', CS102.get('Teacher'))
            print('Время начала занятия:', CS102.get('Time'))

        elif user_search == 'CS103':
            print('Номер аудитории:', CS103.get('Room number'))
            print('Преподаватель:', CS103.get('Teacher'))
            print('Время начала занятия:', CS103.get('Time'))

        elif user_search == 'CS104':
            print('Номер аудитории:', CS104.get('Room number'))
            print('Преподаватель:', CS104.get('Teacher'))
            print('Время начала занятия:', CS104.get('Time'))

        elif user_search == 'CS105':
            print('Номер аудитории:', CS105.get('Room number'))
            print('Преподаватель:', CS105.get('Teacher'))
            print('Время начала занятия:', CS105.get('Time'))

    except KeyError as err:
        print(err)
    except ValueError as err2:
        print(err2)


# pr_task1()

# Викторина со столицами. Напишите программу, которая создает словарь, содержащий
# в качестве ключей названия американских штатов и в качестве значений их столицы.
# (Список штатов и соответствующих им столиц можно найти в Интернете.) Затем программа
# должна провести викторину, случайным образом выводя название штата и предлагая
# ввести его столицу. Программа должна провести подсчет количества правильных
# и неправильных ответов. (Как вариант, вместо американских штатов программа может
# использовать названия стран и их столиц.)
import random


def pr_task_2():
    # создадим словарь,в котором в качестве ключей
    # будут названия стран,а в качестве значений
    # столицы этих стран.
    viktorina = {'England': 'London', 'France': 'Paris', 'Italy': 'Rome'}

    for i in range(len(viktorina)):
        country, capital = viktorina.popitem()
        print(country)
        get_answer = input('Назови столицу: ')
        count = 0
        total1 = 0
        if get_answer == capital:
            print('Верно!')
        else:
            print('Ошибка!')


# pr_task_2()

# Шифрование и дешифрование файлов. Напишите программу, которая применяет словарь
# для присвоения "кодов" каждой букве алфавита. Например:
# codes = { , А, : , % , , , а, : , 9 ,, , Б, : , @,, , 6 , : , #, ... }
# Здесь букве А присвоен символ %, букве а - число 9, букве Б - символ @ и т. д. Программа
# должна открыть заданный текстовый файл, прочитать его содержимое и применить
# словарь для записи зашифрованной версии содержимого файла во второй файл.
# Каждый символ во втором файле должен содержать код для соответствующего символа
# из первого файла.
# Напишите вторую программу, которая открывает зашифрованный файл и показывает его
# дешифрованное содержимое на экране.

def task_3():
    # заведем словарь с шифром:
    spy = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*',
           'I': '(', 'J': ')', 'K': '-', 'L': '_', 'M': '=', 'N': '+', 'O': '/', 'P': '-__',
           'Q': '__-', 'R': '<<', 'S': '>>', 'T': '??', 'U': '::', 'V': '<"', 'W': '}|',
           'X': '{', 'Y': ']', 'Z': '0|', ' ': ' ', '.': '.', ',': ','}

    file = open(r'D:\Фильмы\текст для шифра.txt', 'r')
    text = file.readline()

    file.close()
    print(text)

    file_2 = open(r'D:\Фильмы\зашифрованный текст.txt', 'w')

    index = 0
    while index < len(text):
        translate = spy.get(text[index])
        file_2.write(translate)
        print(translate, end=' ')
        index += 1
    file_2.close()


# task_3()

def deshifrator():
    # кодировка символов:
    spy = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*',
           'I': '(', 'J': ')', 'K': '-', 'L': '_', 'M': '=', 'N': '+', 'O': '/', 'P': '-__',
           'Q': '__-', 'R': '<<', 'S': '>>', 'T': '??', 'U': '::', 'V': '<"', 'W': '}|',
           'X': '{', 'Y': ']', 'Z': '0|', ' ': ' ', '.': '.', ',': ','}
    # откроем файл с шифром и прочтем его:
    file = open(r'D:\Фильмы\зашифрованный текст.txt', 'r')
    text = file.readline()
    file.close()
    print(text)

    index = 0
    for i in range(len(text)):
        for key, value in spy.items():
            if text[index] == value:
                print(key, end=' ')
        index += 1


# deshifrator()


# Уникальные слова. Напишите программу, которая открывает заданный текстовый файл
# и затем показывает список всех уникальных слов в файле. (Подсказка: храните слова
# в качестве элементов множества.)
def task_4():
    file = open(r'D:\Фильмы\уникальные слова.txt', 'r')
    text = file.readline()
    print(text)
    text = text.split(' ')
    print(text)

    my_set = set()
    index = 0
    for i in range(len(text)):
        my_set.add(text[index])
        index += 1
    print(my_set)


# task_4()

# Частотность слов. Напишите программу, которая считывает содержимое текстового
# файла. Она должна создать словарь, в котором ключами являются отдельные слова
# в файле, и значениями - количество появлений каждого слова. Например, если слово
# 'это' появляется 128 раз, то словарь должен содержать элемент с ключом 'это' и значением
# 128. Программа должна либо показать частотность каждого слова, либо создать
# второй файл, содержащий список слов и их частотностей.
import collections


def task_5():
    file = open(r'D:\Фильмы\уникальные слова.txt', 'r')
    text = file.readline()
    text = text.split(' ')

    dict_count = collections.Counter()
    for word in text:
        dict_count[word] += 1
    print(dict_count)


# task_5()

# Анализ файла. Напишите программу, которая читает содержимое двух текстовых файлов
# и сравнивает их следующим образом:
# • показывает список всех уникальных слов, содержащихся в обоих файлах;
# • показывает список слов, входящих в оба файла;
# • показывает список слов из первого файла, не входящих во второй;
# • показывает список слов из второго файла, не входящих в первый;
# • показывает список слов, входящих либо в первый, либо во второй файл, но не входящих
# в оба файла одновременно.
# Подсказка: для выполнения этого анализа используйте операции над множествами.
def task_6():
    # прочитаем два текстовых файла:
    file_1 = open(r'D:\Фильмы\файл_1.txt', 'r')
    text_1 = file_1.readline()
    text_1 = text_1.split(' ')
    set1 = set()
    index = 0
    for i in range(len(text_1)):
        set1.add(text_1[index])
        index += 1

    file_2 = open(r'D:\Фильмы\файл_2.txt', 'r')
    text_2 = file_2.readline()
    text_2 = text_2.split(' ')
    set2 = set()
    index = 0
    for i in range(len(text_2)):
        set2.add(text_2[index])
        index += 1

    print(set1.symmetric_difference(set2))
    print(set1.intersection(set2))
    print(set1.difference(set2))
    print(set2.difference(set1))


# task_6()

# Победители Мировой серии. Среди исходного кода главы 9, а также в подпапке data
# "Решений задач по программированию" соответствующей главы вы найдете файл
# WorldSeriesWiпners.txt. Этот файл содержит хронологический список командпобедителей
# Мировой серии по бейсболу с 1903 по 2009 годы. (Первая строка в файле
# является названием команды, которая победила в 1903 году, последняя строка - названием
# команды, которая победила в 2009 году. Обратите внимание, что Мировая серия не
# проводилась в 1904 и 1994 годах. В файле имеются указывающие на это пометки.)
# Напишите программу, которая читает этот файл и создает словарь, в котором ключиэто
# названия команд, а связанные с ними значения - количество побед команды в Мировой
# серии. Программа должна также создать словарь, в котором ключи - это годы, а связанные
# с ними значения - названия команд, которые побеждали в том году.
# Программа должна предложить пользователю ввести год в диапазоне между 1903 и
# 2009 годами и должна вывести название команды, которая выиграла Мировую серию
# в том году и количество побед команды в Мировой серии.
import collections


def task7():
    file = open(r'D:\Фильмы\АПЛ.txt', 'r')
    teams_list = []
    text = file.readline()
    text = text.rstrip('\n')
    teams_list.append(text)
    while text != '':
        text = file.readline()
        text = text.rstrip('\n')
        teams_list.append(text)
    file.close()
    print(teams_list)
    # вызываем функцию подсчета количества побед для каждой команды:
    print('Кто сколько раз побеждал: ', counter(teams_list))
    hronolog = years(teams_list)
    print(hronolog)
    # пользователь спрашивает:
    get_year = int(input('Введи искомый год от 2000 до 2020: '))
    if get_year >= 2000 and get_year <= 2020:
        if get_year in hronolog:
            print('В', get_year, 'победила команда:', hronolog[get_year])


def years(some_list):
    years_dict = {}
    index = 0
    key = 2000
    for i in range(21):
        years_dict[key] = some_list[index]
        key += 1
        index += 1
    return years_dict


def counter(some_list):
    slovar = collections.Counter()
    for count in some_list:
        slovar[count] += 1
    return slovar


#task7()

# Имена и адреса электронной почты. Напишите программу, которая сохраняет имена и
# адреса электронной почты в словаре в виде пар ключ/значение. Программа должна вывести
# меню, которое позволяет пользователю отыскать адрес электронной почты человека,
# добавить новое имя и адрес электронной почты, изменить существующий адрес электронной
# почты и удалить существующее имя и адрес электронной почты. Программа
# должна законсервировать словарь и сохранить его в файле при выходе пользователя из
# программы. При каждом запуске программы она должна извлечь словарь из файла и его
# расконсервировать.
FIND=1
ADD_NAME_AND_MAIL=2
CHANGE_MAIL=3
DELETE_NAME_AND_MAIL=4
EXIT=5
def task8_main():
    information_dict = {}
    get_info(information_dict)
    choice = 0
    # регулятор выбора:
    while choice!=EXIT:
        choice = show_menu()
        if choice==FIND:
            find_mail(information_dict)
        elif choice==ADD_NAME_AND_MAIL:
            add_info(information_dict)
        elif choice==CHANGE_MAIL:
            change_mail(information_dict)
        elif choice==DELETE_NAME_AND_MAIL:
            delete_info(information_dict)

def find_mail(information_dict):
    search=input('Введи имя для поиска эмейла:')
    if search in information_dict:
        print('Искомое имя:',search)


def add_info(some_dict):
    some_dict={}
    key=input('Введи имя для добавления:')
    value=input('Введи эмейл для добавления:')
    if key not in some_dict:
        some_dict[key]=value
    print(some_dict)

def change_mail(information_dict):
    search=input('Введи имя человека,чей эмейл нужно изменить:')
    new_mail=input('Введи новый эмейл:')
    if search in information_dict:
        information_dict[search]=new_mail
    else:
        print('Нет такого человека в словаре!')

def delete_info(information_dict):
    search=input('Введи имя человека,чьи данные ты хочешь стереть: ')
    if search in information_dict:
        del information_dict[search]
    else:
        print('Нет такого имени в словаре!')

def show_menu():
    print('МЕНЮ ПРОГРАММЫ')
    print('---------------')
    print('1.Найти эмейл человека')
    print('2.Добавить новое имя и эмейл')
    print('3.Изменить эмейл')
    print('4.Удалить имя и эмейл')
    print('5.Выход из программы')
    choice=int(input('Выбери нужное действие из меню программы:'))
    return choice

def get_info(email_box):
    email_box={}
    for count in range(3):
        name = input('Введи имя человека: ')
        mail = input('Введи адрес электронной почты человека: ')
        email_box[name]=mail
    print(email_box)


task8_main()

