import random

import phones_retail
import sportive_items


class Coin:
    #инициализируем первональное значение монеты:
    def __init__(self):
        self.__sideup='Орел'

    #генерируем случайное число от 0 до 1 для подбрасывания монеты:
    def toss(self):
        if random.randint(0,1)==0:
            self.__sideup='Орел'
        else:
            self.__sideup='Решка'

    # вернем значение монеты,на какую сторону она упала:
    def get_sideup(self):
        return self.__sideup

#Главная функция:
def main_1():
    #создадим объект на основе класса Coin:
    my_coin=Coin()

    #покажем обращенную вверх сторону монеты:
    print('Эта сторона обращена вверх:',my_coin.get_sideup())

    #подбросим монету:
    print('Подбрасываю монету:')
    my_coin.toss()

    #меняем намеренно результат падения монетки:
    my_coin.sideup='Орел'

    #покажу обращенную вверх сторону монеты:
    print('Эта сторона обращена вверх:',my_coin.get_sideup())

#main_1()

                                            #Сокрытие атрибутов


class Phones:
    #инициализируем атрибут:
    def __init__(self):
        self.__my_dict={'Andrey':'0950180611','Danil':'0994567893'}

    def show(self):
        for name,phones in self.__my_dict.items():
            print(name,'--',phones)

    def add_number(self):
        name=input('Введи имя:')
        number=input('Введи номер телефона:')
        if name not in self.__my_dict:
            self.__my_dict[name]=number
        print(self.__my_dict)


def main_3():
    #создаем объект:
    phonebook=Phones()
    #вызовем метод show:
    phonebook.show()
    #добавим ключ и значение в словарь:
    phonebook.add_number()
#main_3()

class Shop:
    def __init__(self):
        self.__my_list=[1,2,3,4,5]

    def perebor(self):
        for num in self.__my_list:
            print(num,end=' ')
        print()

    def total(self):
        total=0
        for num in self.__my_list:
            total+=num
        print(total)

def main_5():
    my_shop=Shop()
    my_shop.perebor()
    my_shop.total()
    print('Я пробую всему научиться сам!')
#main_5()

                                       # Хранение классов в модулях

# Программисты обычно упорядочивают свои определения классов, размещая их в модулях.
# Затем модули можно импортировать в любые программы, которым требуется использовать
# содержащиеся в них классы.
import chaus
def my_evening():
    #эта программа имопртирует модуль chaus и создает экзмепляр класса Buhlo:
    party=chaus.Buhlo()
    #посмотрим,что за пиво нам предлагают:
    party.show()
    #теперь позволим программе решить что мы будем пить и в каком количестве:
    party.choice()

#my_evening()

import bank
# получим начальный остаток на карточке:
def main_6():
    start_balance=float(input('Введите свой начальный остаток:'))

    #создадим объек Bankaccount:
    savings=bank.Bankaccount(start_balance)

    #внесем на счет зарплату пользователя:
    summa=float(input('Сколько вносим на счет?'))
    print(f'Вношу эту сумму {summa} на счет')
    savings.deposit(summa)

    #покажем баланс на карте:
    print('Покажем баланс по карте:')
    print(savings.get_balance())

    #получим сумму для снятия с банковского счета:
    take_money=float(input('Какую сумму снимем?'))
    savings.withdraw(take_money)

    #еще раз посмотрим остаток на карте:
    print('На твоей карточке осталось:',savings.get_balance())

#main_6()

import shopCalk
def main_7():
    #инициализируем нашу банковскую карту:
    my_card=0
    my_finance=shopCalk.Finance(my_card)

    #совершим некоторые операции с помощью методов:
    put_money=float(input('Сколько денег ложим на счет?'))
    my_finance.grove_balance(put_money)

    # покажем баланс по карте в данный момент:
    print('На твоей карте в данный момент:',my_finance.show_money(),'грн')

    #посчитаем твой заработок:
    rent=float(input('Сколько ты заплатил за аренду?'))
    comun = float(input('Сколько ты заплатил за коммуналку?'))
    sequrity = float(input('Сколько ты заплатил за охрану?'))
    taxes = float(input('Сколько ты заплатил налогов?'))
    my_finance.marja(rent,comun,sequrity,taxes)

    # посмотрим баланс по карте после вычета расходов:
    print('На твоей карточке осталось:',my_finance.show_money())


#main_7()

import volley
def main_8():
    print('Эта программа для регистрации участников Кубка Донбасса и их жеребьевки!')
    # инициализуирем:
    spisok_komand={}
    dbv=volley.BeachVolley(spisok_komand)
    # заведем список команд:
    print('Получим заявки от команд.')
    print("------------------------")
    count=int(input('Введи количество команд-участниц: '))
    for team in range(count):
        name=input('Введи название команды: ')
        rank=float(input('Введи рейтинг команды: '))
        dbv.get_teams(name,rank)

    # проведем жеребьевку среди команд:
    print('Проведем жеребьевку среди команд и расставим по сетке!')
    spisok_komand=dbv.jrebiy()
    print(spisok_komand)



#main_8()


#                                          Метод _str_()

# Довольно часто возникает необходимость вывести сообщение, которое показывает состояние
# объекта. Состояние объекта - это просто значения атрибутов объекта в тот или иной
# конкретный момент.
import alcocount
def main_9():
    phone_list={}
    my_phonebook=alcocount.PhonesFriends(phone_list)

    #добавим контакты друзей в справочник:
    count=int(input('Сколько друзей внесем в телефонный справочник?'))
    for friend in range(count):
        name=input('Введи имя друга:')
        phone_number=input('Введи номер телефона друга:')
        my_phonebook.add_phones(name,phone_number,phone_list)

    #посмотрим на список контактво в нашем телефонном справочнике:
    #print(my_phonebook)

    #покажем список контактов:
    print('Список твоих контактов выглядит вот так:')
    my_phonebook.show_book()

    #удалим контакт:
    search = input('Введи имя для удаления контакта:')
    my_phonebook.delete_number(phone_list,search)

    # покажем список контактов:
    print('Список твоих контактов выглядит вот так:')
    my_phonebook.show_book()

#main_9()

import bank
def main_10():
    card=0
    my_account=bank.Bankaccount(card)

    #положим денежку на карточку:
    money_to_put=float(input('сколько будешь ложить денег на карту?'))
    my_account.deposit(money_to_put)

    # посмотрим что у нас на карте в данный момент:
    print(my_account)


#main_10()

#                                    РАБОТА С ЭКЗЕМПЛЯРАМИ

#Эта программа импортирует имитационный модуль и создает три экземпляра класса Coin:
import coin
def main_11():
    #создадим три объекта класса Coin
    coin1=coin.Coin()
    coin2=coin.Coin()
    coin3=coin.Coin()

    # показать повернутую вверх сторону монеты:
    print('Вот три монеты,у которых стороны обращены вверх:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    #подбросим все три монеты:
    print('Подбрасываем все три монеты...')
    coin1.toss()
    coin2.toss()
    coin3.toss()

    #теперь показываем,какая сторона выпала у каждой монеты:
    print('Выпали такие стороны монеты:')
    print('Первая монета---',coin1.get_sideup())
    print('Вторая монета---',coin2.get_sideup())
    print('Третья монета---',coin3.get_sideup())
    print()

#main_11()

import lotery
def main_12():
    #создаем три объекта:
    kubik_1=lotery.Bet()
    kubik_2=lotery.Bet()
    kubik_3=lotery.Bet()
    #задаем начальное положение каждого кубика:
    print(kubik_1.show())
    print(kubik_2.show())
    print(kubik_3.show())

    #бросим кубики:
    print('Бросаем все кубики...')
    kubik_1.brosaem()
    kubik_2.brosaem()
    kubik_3.brosaem()

    #показываем стороны всех кубиков:
    print(kubik_1.show())
    print(kubik_2.show())
    print(kubik_3.show())

#main_12()

import cellphone
def cell_phone_test():
    # протестируем класс CellPhone
    # получим данные о телефоне:
    proizvoditel=input('Введи производителя телефона:')
    phone_model=input('Введи номер модели телефона:')
    price=float(input('Введи розничную цену телефона:'))
    #создадим объект (мобильный телефон)
    mobile_phone=cellphone.CellPhone(proizvoditel,phone_model,price)
    # выведем полученные данные на экран:
    print('Производитель телефона--',mobile_phone.get_manufact())
    print('Номер модели телефона--',mobile_phone.get_model())
    print('Розничная цена телефона--',format(mobile_phone.get_retail_price(),'.2f'))


#cell_phone_test()

import cellshoes
def main_13():
    #создадим объект:
    articul=input("Введи артикул:")
    name=input('Введи название модели:')
    price=float(input('Введи цену закупки:'))
    sneakers=cellshoes.Sneakers(articul,name,price)
    # с помощью геттеров извлечем инфу о кроссовках:
    print('Название модели:',sneakers.get_name())
    print('Артикул:',sneakers.get_art())
    print('Оптовая цена:',sneakers.get_price())
    #
#main_13()

#посчитаем зарплату работника завода
import zarplata
def main_14():
    #внесем данные по сотруднику:
    personal_name=input('Введи имя сотрудника:')
    doljnost=input('Введи должность сотрудника:')
    oklad=float(input('Введи оклад сотрудника:'))
    koef_premiya=float(input('Введи коэфициент премии:'))
    doplata_za_staj=float(input('Введи доплату за стаж:'))

    #создадим объект "сотрудник":
    rabotnik=zarplata.Zarplata(personal_name,doljnost,oklad)

    #начнем производить операции над данными,используя методы класса zarplata
    #выведем данные на экран:
    print('Имя сотрудника:',rabotnik.show_name())
    print('Должность сотрудника:',rabotnik.show_position())
    print('Оклад сотрудника:',rabotnik.show_sallary())

    #посчитаем зарплату,которая прийдет сотруднику в этом месяце:
    print(f'За прошедший месяй сотрудник {personal_name} заработал(а):'
          ,format(rabotnik.calc_zp(oklad,koef_premiya,doplata_za_staj), '.2f'),"грн")

#main_14()
import koordinats
def main_15():
    print(koordinats.Point.color)
    print(koordinats.Point.circle)
    print(koordinats.Point.__dict__)

    # создадим экземпляр (объект) класса:
    object=koordinats.Point()
    object_2=koordinats.Point()
    print(type(object))
    koordinats.Point.circle=1
    print(object.circle)
    print(object_2.circle)
    print(object.__dict__)
    print(object.color,object_2.color)
    object.color='green'
    print(object.color,object_2.color)
    print(object.__dict__)
    setattr(koordinats.Point,'prop',99)
    print(object.__dict__)
    print(hasattr(object,'color'))


#main_15()

import koordinats
def main_16():
    ob1=koordinats.Point()
    ob2=koordinats.Point()

    ob1.x=1
    ob1.y=2

    ob2.x=10
    ob2.y=20
    print(koordinats.Point.__doc__)
    print(ob1.__dict__)
    print(ob2.__dict__)
    print('---------------')

    pt=koordinats.Point()
    pt.set_coords(99,999)
    print(pt.__dict__)
    print('---------')
    pt2=koordinats.Point()
    pt2.set_coords(55,55)
    print(pt2.__dict__)
    print('----------------')
    print(pt.get_coords())
    print(pt2.get_coords())
    print('-------------')
    func=getattr(pt,'get_coords')
    print(func())

#main_16()
import pivo
def main_17():
    Chaus=pivo.Buhlo()
    Chaus.count_beer('Carslberg',25.99,8)
    print(Chaus.count_beer('Carslberg',25.99,8))
    print(Chaus.__dict__)
    print('----------')
    print(Chaus.get_beer())
    print('___________')
    bottles=int(input('Сколько бутылок пива собирается выпить Саша?'))
    Chaus.beer_control(bottles)
#main_17()


#                                 ИНИЦИАЛИЗАТОР И ФИНАЛИЗАТОР
import volley_modul
def main_18():
    team=volley_modul.Shurovo('Arsenal','London',98)
    print(team.__dict__)


#main_18()
import articles
def main_19():
    name=input('Enter item name:')
    article=input('Enter item article:')
    my_shop=articles.Magazin(name,article)
    print(my_shop.__dict__)
    print('-----------------------')
    sklad={}
    my_shop.save_items(sklad,name,article)
    print(my_shop.__dict__)
#main_19()


import koordinats
def main_20():
    pt=koordinats.Point(1,2)
#main_20()

import igra_palci
def main_21():
    # создаем экземпляр класса Chet_nechet (объект):
    igrok=igra_palci.Chet_nechet()
    #посмотрим,что показывают пальцы игрока в данный момент:
    print(igrok.get_palec())
    #вызовем функцию выбрасывания пальцев:
    print('Выбрасываю пальцы...')
    print('Выбросим 10 раз!')
    for i in range(10):
        igrok.bros_palec()
    #посмотрим результат выброса пальцев(это чет или нечет):
        print(igrok.get_palec())


#main_21()

import bank_card
def main_22():
    #зададим начальный баланс карточке:
    balance=0
    #создаем объект класса:
    my_card=bank_card.Money_card(balance)
    # проверим баланс по карте:
    print('Баланс на карточке:',my_card.check_balance(),'грн')

    # пополним карточку:
    summa_popolneniya=float(input('Введи сумму пополнения карточки:'))
    my_card.put_money(summa_popolneniya)

    # еще раз проверим баланс на карте:
    print('Баланс карточки:',my_card.check_balance(),'грн')

    # снимем некоторую сумму с карты:
    snimem_dengi=float(input('Сколько снимем с карты?'))
    my_card.took_money(snimem_dengi)

    # снова проверим баланс:
    print('Теперь баланс вот такой:',my_card.check_balance(),'грн')

    print('----------')
    print('Проверим состояние обекта,используя метод __str__')
    print(my_card)

#main_22()



#                                        РАБОТА С ЭКЗЕМПЛЯРАМИ
import igra_palci
def main_23():
    # создадим три объекта класса:
    player_1=igra_palci.Chet_nechet()
    player_2 = igra_palci.Chet_nechet()
    print(player_1)
    print(player_2)

    #два игрока выбрасывают пальцы:
    print('Оба игрока выбрасывают пальцы...')
    player_1.bros_palec()
    player_2.bros_palec()

    # посмотрим результат:
    print('Игрок №1 выбросил: ',player_1.get_palec())
    print('Игрок №2 выбросил: ',player_2.get_palec())


#main_23()

def main_24():
    # тестируем класс по телефонам:
    # получим данныео телефоне:
    made=input('Введи название производителя: ')
    model=input('Введи номер модели: ')
    price=float(input('Введи розничную цену: '))

    # создаем экзмепляр класса:
    phone=phones_retail.Mobile(made,model,price)

    # покажем введенные данные:
    print('Производитель: ',phone.get_proizvoditel())
    print('Номер модели: ',phone.get_nomer_modeli())
    print('Розничная цена: ',phone.get_retail_price())

    print('Посмотрим состояние объекта:')
    print(phone.__dict__)


#main_24()

#                                     ХРАНЕНИЕ ОБЪЕКТОВ В СПИСКЕ
import phones_retail
def main_25():
    'Эта программа создает пять объектов(телефонов) и сохраняет их в списке'
    # получим список объектов (телефонов):
    phone_list=make_list()
    # покажем данные в списке:
    print('Введенные вами данные по телефонам:')
    show_display(phone_list)

# создадим функцию make_list,
# которая получает данные по пяти телефонам и создает список из них:
def make_list():
    #создаем пустой список:
    phone_list=[]
    count_phones=5
    for item in range(count_phones):
        made_by=input('Введи производителя: ')
        model=input('Введи номер модели: ')
        price=float(input('Введи цену: '))
        print()

        #создаем новый объект класса и присваиваем ему эти значения:
        phone=phones_retail.Mobile(made_by,model,price)

        #добавляем этот объект (телефон) в наш пустой список:
        phone_list.append(phone)

    return phone_list

def show_display(phone_list):
    for item in phone_list:
        print(item.get_proizvoditel())
        print(item.get_nomer_modeli())
        print(item.get_retail_price())

#main_25()

import sportive_items

def main_26():
    'Протестируем работу класса Sport'
    # напишем программу,которая получает данные
    # о трех спортивных вещах и заносит их в список и распечатывает
    shop_list=make_list()


def making_list():
    #создадим пустой список:
    sport_list=[]
    count_item=3
    for item in range(count_item):
        nazvanie=input('Введи название вещи: ')
        articul=input('Введи артикул вещи: ')
        kol=int(input('Введи количество на остатке: '))
        cena=float(input('Введи цену товара: '))

        #создадим объект:
        tovar=sportive_items.Sport1(nazvanie,articul,kol,cena)
        #добавим товар в список:
        sport_list.append(tovar)
    return sport_list

#main_26()

import sklad
def main_27():
    my_list=make_sklad_list()
    show_tmc(my_list)


def make_sklad_list():
    # создадим список для 5 ТМЦ:
    sklad_list=[]
    repite=5
    for item in range(repite):
        # получим данные о ТМЦ от пользователя:
        name=input('Название ТМЦ: ')
        kod=input('Артикул ТМЦ: ')
        kolich=int(input('Количество штук на остатке: '))
        # создадим объект класса sklad с вышеуказанными атрибутами:
        tmc=sklad.Save(name,kod,kolich)
        # добавим объект в список:
        sklad_list.append(tmc)
        print()
    return sklad_list

def show_tmc(some_list):
    for item in some_list:
        print(item.get_name())
        print(item.get_art())
        print(item.get_count())


#main_27()



#                                ПЕРЕДАЧА ОБЪЕКТОВ В КАЧЕСТВЕ АРГУМЕНТОВ

# эта программа передает объект Coin в качестве аргумента в функцию:
import coin
def main_28():
    #создадть объект Coin:
    my_coin=coin.Coin()
    # эта инструкция покажет орел:
    print(my_coin.get_sideup())
    #передадим объект в функцию flip(подброс):
    print('Подбрасываем монету!')
    flip(my_coin)

    #эта инструкция покажет либо орел,либо решку:
    print('Получаем: ')
    print(my_coin.get_sideup())

def flip(obj):
    #данная функция подбрасывает монету:
    obj.toss()

#main_28()

#поиграем игру в чет и нечет:
import igra_palci
def main_29():
    # создадим объект:
    player_1=igra_palci.Chet_nechet()

    # покажем стартовое значение пальцев:
    print('Сначала загадал:')
    print(player_1.get_palec())

    # брсаем палец:
    za_spinoy(player_1)

    # показываем результат:
    print('Ииии....')
    print(player_1.get_palec())

def za_spinoy(object):
    object.bros_palec()

#main_29()


#                           КОНСЕРВАЦИЯ СОБСТВЕННЫХ ОБЪЕКТОВ

import pickle
import phones_retail
#заведем константу для имени файла:
FILE_NAME='cellphones.dat'
def main_30():
    # эта программа консервирует объекты Mobile.

    # инициализируем переменную для работы с циклом:
    answer='y'

    # открываем файл:
    file=open('D:\Фильмы\cellphones.dat', 'wb')

    # получим данные от пользователя:
    while answer.upper()=='Y':
        proizvoditel=input('Введи производителя модели: ')
        nomer=input('Введи номер модели: ')
        price=float(input('Введи центу модели: '))

        # создаем объект (тедефон)
        phone=phones_retail.Mobile(proizvoditel,nomer,price)

        #закончервируем объект и запишем его в файл
        pickle.dump(phone,file)

        # управляем циклом
        answer=input('press Y or y to continue: ')

    # закрываем файл
    file.close()
    print('Данные по телефонам записаны в "D:\Фильмы\cellphones.dat"')


#main_30()
import pickle
import phones_retail
# константа для имени файла

def main_31():
    # эта программа расконсервирует данные по телефонам:

    #для обозначения конца файла:
    end_of_file=False

    #откроем файл
    file=open('D:\Фильмы\cellphones.dat', 'rb')

    #прочитать до конца файла:
    while not end_of_file:
        try:
            # расконсервировать следующий объект
            phone=pickle.load(file)

            #показать данные по телефону:
            show_phone(phone)
        except EOFError:
            # установим флаг,чтобы обозначаить,что былдостигнут конец файла
            end_of_file=True

    file.close()

def show_phone(object):
    # показывает характеристики телефона
    print('Производитель: ',object.get_proizvoditel())
    print('Номер модели: ',object.get_nomer_modeli())
    print('Розничная цена: ',object.get_retail_price())

#main_31()

import pickle
import sklad
def main_32():
    # получим и законсервируем данные по тмц склада
    # создадим файл:
    file=open('D:\Фильмы\sklad.dat', 'wb')

    #заведем переменную,управляющую циклом
    answer='y'

    # получим от пользователя данные по ТМЦ
    while answer.upper()=='Y':
        nazvanie=input('Введи название ТМЦ: ')
        kod=input('Введи артикул ТМЦ: ')
        kol=int(input('Введи остаток ТМЦ на складе: '))

        # создаем объект класса Save
        tmc=sklad.Save(nazvanie,kod,kol)

        #записываем объект в файл
        pickle.dump(tmc,file)

        # управляем циклом
        answer=input('press y or Y to continue...')

    file.close()
    print('Данные по складу можно найти по адрессу: "D:\Фильмы\sklad.dat"')

#main_32()

import pickle
import sklad
def main_33():
    # расконсервируем данные по складу и выведем их на экран
    end_of_file=False
    file=open('D:\Фильмы\sklad.dat', 'rb')
    # прочитать до конца файла:
    while not end_of_file:
        try:
            # расконсервировать следующий объект
            tmc = pickle.load(file)

            # показать данные по телефону:
            show_info(tmc)
        except EOFError:
            # установим флаг,чтобы обозначаить,что былдостигнут конец файла
            end_of_file = True

    file.close()

def show_info(tmc):
    print('Покажем данные тмц,хранящихся на складе.')
    print('Название тмц: ',tmc.get_name())
    print('Артикул ТМЦ: ',tmc.get_art())
    print('Конечный остаток: ',tmc.get_count())
    print()

#main_33()

import phones_retail
import pickle
def main_34():
    user_answer='y'
    file=open('D:\Фильмы\cellphones.dat', 'wb')
    while user_answer.upper()=='Y':
        name=input('производитель:')
        nomer=input('номер модели:')
        cena=float(input('цена:'))

        mobile=phones_retail.Mobile(name,nomer,cena)
        pickle.dump(mobile,file)

        user_answer=input('press y or Y to continue...')

    file.close()

#main_34()

import pickle
import phones_retail
def main_35():
    end_of_file=False
    file=open('D:\Фильмы\cellphones.dat', 'rb')
    while not end_of_file:
        try:
            mobile=pickle.load(file)
            display_info(mobile)
        except EOFError:
            end_of_file=True

    file.close()

def display_info(object):
    print(object.get_proizvoditel())
    print(object.get_nomer_modeli())
    print(object.get_retail_price())
    print()


#main_35()


#                               ХРАНЕНИЕ ОБЪЕКТОВ В СЛОВАРЕ

def main_36():
    my_dict={}
    name='Andrey'
    phone='0950180611'
    pos='developer'
    my_dict['name']=name
    my_dict['phone']=phone
    my_dict['pos']=pos
    print(my_dict)
#main_36()

import pickle
import my_contacts
# глобальные константы для пунктов меню:
FIND_CONTACT=1
ADD_CONTACT=2
CHANGE_CONTACT=3
DELETE_CONTACT=4
QUIT=5
def main_37():
    #загрузим существующий словарь контактов и присвоим его переменной
    contacts=load_contacts()

    # инициализируем переменную для выбора пользователя
    user_choice=0

    # обрабатывать запросы пользователя из меню,
    # пока он не нажмет выход
    while user_choice!=QUIT:
        # получить выбранный пункт меню
        user_choice=get_menu_choice()

        #обработать выбранный вариант действий
        if user_choice==FIND_CONTACT:
            find(contacts)
        elif user_choice==ADD_CONTACT:
            add(contacts)
        elif user_choice==CHANGE_CONTACT:
            change_info(contacts)
        elif user_choice==DELETE_CONTACT:
            delete_contact(contacts)

    # когда будем выходить из программы,
    # сохраним словарь my_contacts в файл
    save_contacts(contacts)

def load_contacts():
    try:
        # попытаемся открыть файл contacts_friends.dat
        file=open('D:\Фильмы\contacts_friends.dat', 'rb')

        # расконсервируем словарь
        contact_dict=pickle.load(file)

        file.close()
    except IOError:
        # если не получится открыть файл,будет создан новый словарь
        contact_dict={}

    return contact_dict
def get_menu_choice():
    # функция выводит меню и проверяет на допустимость выбранный пользователем пункт
    print('МЕНЮ')
    print('-----------')
    print('1.Найти контакт')
    print('2.Добавить контакт')
    print('3.Изменить контакт')
    print('4.Удалить контакт')
    print('5.Выход')

    # получить выбранный полльзователем пункт
    user_choice=int(input('Выбери пункт из меню!'))

    # проверим выбранный пункт на допустимость
    if user_choice>QUIT or user_choice<ADD_CONTACT:
        user_choice=int(input('Выбери корректно!'))

    return user_choice

def find(contacts):
    # получить искомое имя
    name=input('Введи имя человека: ')
    print(contacts.get(name,'no name...'))

def add(contacts):
    # получить всю инфу о человеке:
    name=input('Name: ')
    phone=input('Phone: ')
    email=input('Mail: ')

    # создадим объект класса,куда добавим эту инфу
    new_person=my_contacts.Phones(name,phone,email)

    # если имя не существует,то добавить его
    # в качестве ключа со связанным с ним значением в виде объекта
    if name not in contacts:
        contacts[name]=new_person
        print('added')
    else:
        print('Wrrrrrrooong! this name is already here...')

def change_info(contacts):
    # введем имя
    name=input('Введи имя: ')
    if name in contacts:
        # получить новый телефон и почту
        new_phone=input('enter new phone number: ')
        new_mail=input('enter new mail adress: ')

        # создать новый объект класса с новыми данными
        changed_contact=my_contacts.Phones(name,new_phone,new_mail)

        # обновить запись
        contacts[name]=changed_contact
        print('info is upgreate!')
    else:
        print('Wrrrrrong! name out of your contacts!')

def delete_contact(contacts):
    # получим имя
    name=input('text name: ')
    if name in contacts:
        del contacts[name]
        print('name has been deleted!')
    else:
        print('wrrrrong! name out of list!')

def save_contacts(contacts):
    # Функция save_contacts консервирует указанный
    # объект и сохраняет его в файле контактов.

    # Открыть файл для записи.
    file=open('D:\Фильмы\contacts_friends.dat', 'wb')

    # Законсервировать словарь и сохранить его.
    pickle.dump(contacts,file)

    file.close()

#main_37()


import vegas
def main_55():
    # создадим объект на основе класса Вегас
    cube=vegas.Cube()

    # покажем текущую сторону куба
    print('В данный момент кубик лежит стороной:',cube.get_side())

    # подбросим кубик в воздух
    print('Бросаем кубик...')
    cube.mix_cube()

    # покажем,что выпало
    print('Кубик выпал стороной  с числом:',cube.get_side())


#main_55()


def main



















