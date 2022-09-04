import home_animals


def main_1():
    pat = home_animals.Animals('Обычное млекопитающее')
    pat.show_vid()
    pat.make_sound()


# main_1()

def main_2():
    pat = home_animals.Dog()
    pat.show_vid()
    pat.make_sound()


# main_2()

def main_3():
    pat = home_animals.Cat()
    pat.show_vid()
    pat.make_sound()


# main_3()

def main_4():
    pat = home_animals.Spider()
    pat.show_vid()
    pat.make_sound()


# main_4()

def main_5():
    pat = home_animals.Homka()
    pat.show_vid()
    pat.make_sound()


# main_5()

import figures


def main_6():
    my_figure = figures.Geometrik('Некая фигура')
    my_figure.show_figure()
    my_figure.make_pic()


# main_6()

def main_7():
    kvadrat = figures.Kvadrat()
    kvadrat.show_figure()
    kvadrat.make_pic()


# main_7()

def main_8():
    krug = figures.Circle()
    krug.show_figure()
    krug.make_pic()


# main_8()
import football_players


def main_9():
    player = football_players.Footballer('unknown')
    player.show_position()
    player.get_tasks()


# main_9()

def main_10():
    player = football_players.Defender()
    player.show_position()
    player.get_tasks()


# main_10()

def main_11():
    player = football_players.Midfielder()
    player.show_position()
    player.get_tasks()


# main_11()


def main_12():
    # создадим объект неизвестного животного, кота и собачки
    some_pat = home_animals.Animals('Unknown')
    cat = home_animals.Cat()
    dog = home_animals.Dog()

    # покажем инфу о каждом животном
    print('Вот некоторые животные и звуки,которые они издают')
    print('-------------------------------------------------')
    show_pat_info(some_pat)
    print('-------------------------------------------------')
    show_pat_info(cat)
    print('-------------------------------------------------')
    show_pat_info(dog)
    print('-------------------------------------------------')


def show_pat_info(some_obj):
    some_obj.show_vid()
    some_obj.make_sound()


# main_12()

def main_13():
    # создадим трех футболистов
    unknown_player = football_players.Footballer('Unknown')
    defender = football_players.Defender()
    midfield = football_players.Midfielder()

    # вызовем функцию show info для вывода информации о футболистах
    print('Игроки:')
    show_info(unknown_player)
    print('-----------')
    show_info(defender)
    print('-----------')
    show_info(midfield)
    print('-----------')


def show_info(some_player):
    some_player.show_position()
    some_player.get_tasks()


# main_13()


def main_14():
    kvadrat = figures.Kvadrat()
    krug = figures.Circle()
    show_info_geom(kvadrat)
    show_info(krug)


def show_info_geom(object):
    object.show_figure()
    object.make_pic()


# main_14()

def main_15():
    midfielder = football_players.Midfielder()
    defender = football_players.Defender()
    unknown_player = football_players.Footballer('Unknown')
    # покажем инфу
    print('Инфа по игрокам:')
    show(midfielder)
    show(defender)
    show(unknown_player)


def show(player):
    player.show_position()
    player.get_tasks()


# main_15()

def main_16():
    # создадим котика и хомячка
    cat = home_animals.Cat()
    homka = home_animals.Homka()
    # а так-же какое-то животное
    pat = home_animals.Animals('Чудо-Юдо-Рыба-Кит')
    # и создадим объект,не являющийся животным
    human = 'Andrey'

    # выведем информацию на экран


def show_imfo(choose_pat):
    if isinstance(choose_pat, home_animals.Animals):
        choose_pat.show_vid()
        choose_pat.make_sound()
    else:
        print('Это не домашнее животное!')


# main_16()

import family


def main_17():
    # создадим некоего члена семьи
    family_guy = family.Family('Член семьи')
    show_family_info(family_guy)


def show_family_info(object):
    object.show_pos()
    object.make_events()


# main_17()

def main_18():
    # создадим мою семью
    mama = family.Mother()
    papa = family.Father()
    me = family.Son()
    neighbor = 'some pal'

    # вызовем функцию show_up
    show_up(mama)
    print('-----------')
    show_up(papa)
    print('-----------')
    show_up(me)
    print('-----------')
    show_up(neighbor)


def show_up(object):
    if isinstance(object, family.Family):
        object.show_pos()
        object.make_events()
    else:
        print('- Этот человек не является членом семьи.')


# main_18()

import Library


def main_19():
    some_book = Library.Books('Неизвестная книга')
    # вызываем функцию get_info_book
    get_info_book(some_book)


def get_info_book(book):
    book.show_name()
    book.about_what()


# main_19()


def main_20():
    # создадим три книги
    karl_may = Library.Travel_book()
    toni_geddis = Library.Education_book()
    pray_eat_love = Library.Romantic_book()
    # покажем инфу по книжкам
    show_book(karl_may)
    show_book(toni_geddis)
    show_book(pray_eat_love)


def show_book(book):
    book.show_name()
    book.about_what()


# main_20()

#                                            ПРАКТИКА!

# Задача №1
# Напишите программный код для класса с именем Cola (Кока-кола), который является
# подклассом класса Beverage (Напиток). Метод _ ini t _ () класса Cola должен вызывать
# метод ini t () класса Beverage, передавая строковое значение 'кока-кола' в качестве
# аргумента
def main_21():
    class Beverage:
        def __init__(self, bev_name):
            self.__bev_name = bev_name

    class Cola(Beverage):
        def __init__(self):
            Beverage.__init__(self, 'coca-cola')


# main_21()

# Задача №2
# Классы Employee и ProductionWorker. Напишите класс Ernployee (Сотрудник), который
# содержит атрибуты приведенных ниже данных:
# • имя сотрудника;
# • номер сотрудника.
# Затем напишите класс ProductionWorker (Рабочий), который является подклассом класса
# Ernployee. Класс ProductionWorker должен содержать атрибуты приведенных ниже данных:
# • номер смены (целое число, к примеру, 1, 2 или 3);
# • ставка почасовой оплаты труда.
# Рабочий день разделен на две смены: дневную и вечернюю. Атрибут смены будет содержать
# целочисленное значение, представляющее смену, в которую сотрудник работает.
# Дневная смена является сменой 1, вечерняя смена - сменой 2. Напишите соответствующие
# методы-получатели и методы-модификаторы для каждого класса.
# После того как эти классы будут написаны, напишите программу, которая создает объект
# класса ProductionWorker и предлагает пользователю ввести данные по каждому атрибуту
# данных этого объекта. Сохраните данные в объекте и примените в этом объекте методыполучатели,
# чтобы получить эти данные и вывести их на экран.

import job


def main_22():
    # предложим пользователю ввести данные по сотруднику
    name = input('Введите имя сотрудника: ')
    id_number = int(input('Введи АЙДИ сотрудника: '))
    smena_number = int(input('Введи номер смены сотрудника(1 или 2): '))
    sallary_hour = float(input('Введи зарплатную ставку в час: '))

    # создадим объект (сотрудник завода)
    worker = job.ProductionWorker(name, id_number, smena_number, sallary_hour)

    # выведем полученные данные на экран
    print('Данные по сотруднику.')
    print('---------------------')
    print('Имя: ', worker.get_name())
    print('ID: ', worker.get_id())
    print('Смена: ', worker.get_smena())
    print('Оклад в час:', worker.get_sallary())
    print('=====================')


# main_22()


# Задача №3
# Класс ShiftSupervisor. На некой фабрике начальник смены является штатным сотрудником,
# который руководит сменой. В дополнение к фиксированному окладу начальник
# смены получает годовую премию за выполнение его сменой производственного плана.
# Напишите класс ShiftSupervisor (Начальник смены), который является подклассом
# класса Ernployee, созданного в задаче по программированию 1. Класс ShiftSupervisor
# должен содержать атрибут данных для годового оклада и атрибут данных для годовой
# производственной премии, которую заработал начальник смены. Продемонстрируйте
# класс, написав программу, которая применяет объект ShiftSupervisor.

def main_23():
    # получим от пользователя данные по начальнику
    fio = input('Ф.И.О. начальника: ')
    manager_id = int(input('Введи ID начальника: '))
    year_sallary = float(input('Введи годовой оклад начальника: '))
    year_prime = float(input('Введи годовую производственную премию начальника: '))

    # создадим объект (начальника)
    supervisor = job.ShiftSupervisor(fio, manager_id, year_sallary, year_prime)

    # покажем полученные данные по начальнику
    print('========================')
    print('Данные начальника смены.')
    print('ФИО: ', supervisor.get_name())
    print('ID: ', supervisor.get_id())
    print('Годовой оклад: ', supervisor.get_year_sallary(), 'грн')
    print('Годовая премия: ', supervisor.get_year_prime(), 'грн')
    print('========================')


#main_23()


# Задача №4
# Классы Person и Custaaer.
# Напишите класс Person с атрибутами данных для имени, адреса и телефонного номера
# человека. Затем напишите класс Custorner (Клиент), который является подклассом класса
# Person. Класс Custorner должен иметь атрибут данных для номера клиента и атрибут
# булевых данных, указывающий, хочет ли клиент быть в списке рассылки или нет. Продемонстрируйте
# экземпляр класса Custorner в простой программе.

import chelovek
def main_24():
    # получим данные по клиенту
    name=input('Введи имя клиента: ')
    address=input('Введи адресс клиента: ')
    phone=int(input('Введи телефон клиента: '))
    cust_num=int(input('Введи номер клиента: '))
    quest_subscribe=input('Подписать клиента на рассылку?')
    if quest_subscribe=='yes':
        subscribe='customer is subscribed'
    else:
        subscribe = 'customer is not subscribed'

    # создадим объект (клиента)
    client=chelovek.Customer(name,address,phone,cust_num,subscribe)
    prodavec=chelovek.Saler()
    # покажем данные клиента
    print('---------------------------------------------')
    print('Ниже предоставленна вся информация о клиенте.')
    print('---------------------------------------------')
    print('Имя:',client.get_name())
    print('Адресс:',client.get_address())
    print('Телефон:',client.get_phone())
    print('Номер клиента в базе:',client.get_custtomer_number())
    print('Статус подписки:',client.get_subscribe())
    print('=============================================')
    show_saler(prodavec)
def show_saler(object):
    object.get_name()
    object.get_address()
    object.get_phone()
    object.what_doing()

#main_24()




