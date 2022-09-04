# пример для класса Car
import avto_sredstva


def main_1():
    # создать объект на основе класса Car
    # Легковое авто : 2007 г Audi с 12500 миль пробега
    # цена 21000.00 и 4 дверьми
    legkovushka = avto_sredstva.Car('Audi', 2007, 12500, 21000.00, 4)

    # покажем данные этого автомобиля
    print('Фирма-производитель: ', legkovushka.get_firma())
    print('Модель: ', legkovushka.get_model())
    print('Пробег авто: ', legkovushka.get_probeg(), 'миль')
    print('Цена: ', legkovushka.get_cena(), 'usd')
    print('Количество дверей: ', legkovushka.get_dveri())


# main_1()

# пример с кроссовками
import delta_sport


def main_2():
    # введем следующие данные по кроссовкам
    name = 'Asics Gel-Sonoma 6'
    articul = '6848646-600'
    price = 122.50
    type_for = 'Trail'

    # создадим объект класса Кроссовок
    sneaker = delta_sport.Krossovki(name, articul, price, type_for)

    # выведем информацию на экран
    print('Название модели:', sneaker.get_name())
    print('Артикул:', sneaker.get_articul())
    print('Цена:', sneaker.get_price())
    print('Предназначение:', sneaker.get_type_for())


# main_2()

def main_3():
    name = 'Nike M Run Suit black ops'
    articul = '6846-200'
    price = 75.00
    gender = 'Male'

    # создадим объект класса Костюм
    my_suit = delta_sport.Suits(name, articul, price, gender)

    # выведем информацию по костюму на экран
    print('Модель:', my_suit.get_name())
    print('Артикул:', my_suit.get_articul())
    print('Цена:', my_suit.get_price(), 'usd')
    print('Для:', my_suit.get_gender())


# main_3()

def main_4():
    # получим данные по сумке
    name = 'Gym swoosh training bag'
    articul = '6868-785'
    price = 40.99
    size = 60

    # создадим объект подкласса Сумки
    my_bag = delta_sport.Bags(name, articul, price, size)

    # выведем инфу на экран
    print('Модель:', my_bag.get_name())
    print('Артикул:', my_bag.get_articul())
    print('Цена:', my_bag.get_price(), 'usd')
    print('Объем:', my_bag.get_size(), 'cm3')


# main_4()


def main_5():
    # программа использует все три подкласса Спортивные вещи
    # введем следующие данные по кроссовкам
    name = 'Asics Gel-Sonoma 6'
    articul = '6848646-600'
    price = 122.50
    type_for = 'Trail'

    krossovok = delta_sport.Krossovki(name, articul, price, type_for)

    # данные по костюму
    name = 'Nike M Run Suit black ops'
    articul = '6846-200'
    price = 75.00
    gender = 'Male'

    kostum = delta_sport.Suits(name, articul, price, gender)

    # данные по сумке
    name = 'Gym swoosh training bag'
    articul = '6868-785'
    price = 40.99
    size = 60

    sumka = delta_sport.Bags(name, articul, price, size)

    # выведем все на экран
    print('Вы заказали следующий товар на нашем сайте.')
    print('===========================================')
    print('Информация по кроссовкам')
    print('Название модели:', krossovok.get_name())
    print('Артикул:', krossovok.get_articul())
    print('Цена:', krossovok.get_price(), 'usd')
    print('Предназначение:', krossovok.get_type_for())
    print('-------------------------------------------')
    print('Тнформация по костюму')
    print('Модель:', kostum.get_name())
    print('Артикул:', kostum.get_articul())
    print('Цена:', kostum.get_price(), 'usd')
    print('Для:', kostum.get_gender())
    print('-------------------------------------------')
    print('Информация по сумке')
    print('Модель:', sumka.get_name())
    print('Артикул:', sumka.get_articul())
    print('Цена:', sumka.get_price(), 'usd')
    print('Объем:', sumka.get_size(), 'cm3')
    print('-------------------------------------------')
    print('Спасибо!')


# main_5()


#                                        применение наследования
# эта программа создаст экземпляр класса Сберегательный счет и Депозит
import credit_systems


def main_6():
    # получим данные по сберегательному счету
    nomer = 79787682
    pr_stavka = 5.5
    balance = 50000.00

    # создадим объект класса Сберигательный счет
    sber_account = credit_systems.Sberegatelniy_schet(nomer, pr_stavka, balance)

    # получим данные по депозитному счету
    nomer = 1344884
    pr_stavka = 7.2
    balance = 75000.00
    data = '24.25.2022'

    # создадим объект класса Депозитный счет
    dep_account = credit_systems.DepositSertificat(nomer, pr_stavka, balance, data)

    # выведем инфориацию на экран
    password = 3496
    enter_password = int(input('Введи ПИН-код: '))
    if enter_password == password:
        print('Здравствуйте,Андрей!')
        print('Предлагаем Вам выписку по вашему сберегательному счету:')
        print('Номер сберегательного счета | ', sber_account.get_nomer_scheta())
        print('Процентная ставка | ', sber_account.get_procent_stavka(), '%')
        print('Остаток на счете | ', sber_account.get_ostatok_scheta(), 'usd')
        print('=====================================================================')
        print('Предлагаем Вам выписку по вашему депозитному счету:')
        print('Номер сберегательного счета | ', dep_account.get_nomer_scheta())
        print('Процентная ставка | ', dep_account.get_procent_stavka(), '%')
        print('Остаток на счете | ', dep_account.get_ostatok_scheta(), 'usd')
        print('Дата выплаты | ', dep_account.get_data())
        print('=====================================================================')
        print('Спасибо,что используете услуги нашего банка. До свидания,Андрей!')

    else:
        print('Неверный пароль...')


#main_6()


