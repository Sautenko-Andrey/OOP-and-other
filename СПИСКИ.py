# Отличие списков от кортежей
# простое: список является мутирующей последовательностью (т. е. программа может
# изменять его содержимое), а кортеж- немутирующей последовательностью (т. е. после его
# создания его содержимое изменить невозможно).

#                                 СПИСКИ
import fileinput


def some_1():
    try:
        numbers = list(range(10))
        print(numbers)
    except ValueError as err:
        print(err)


# some_1()

def some_2():
    try:
        numbers = list(range(0, 11, 2))
        print(numbers)
    except ValueError as err:
        print(err)
# some_2()


def some_3():
    try:
        numbers=["Andrey "]*3
        print(numbers)
    except ValueError as err:
        print(err)
#some_3()


def some_4():
    try:
        numbers=[0,1,2,3,]*5
        print(numbers)
    except ValueError as err:
        print(err)
#some_4()

def some_5():
    try:
        numbers=[1,2,3]
        for digit in numbers:
            print(digit)
    except ValueError as err:
        print(err)
#some_5()

def some_6():
    try:
        my_list=[10,20,30,40]
        print(my_list[0],my_list[1],my_list[2],my_list[3])
    except ValueError as err:
        print(err)
#some_6()

def some_7():
    try:
        my_list=[10,20,30,40,50]
        index=0
        while index<4:
            print(my_list[index])
            index+=1
    except ValueError as err:
        print(err)
#some_7()

def some_8():
    try:
        some_list=['name',123,3.14]
        print(some_list[-1])
        print(some_list[-2])
        print(some_list[-3])
    except ValueError as err:
        print(err)
#some_8()

def some_9():
    try:
       my_list=[1,3,5,'hello',3.14,'name']
       list_size=len(my_list)
       print("количество элементов в списке равно: ",list_size)
    except ValueError as err:
        print(err)
#some_9()

def some_10():
    try:
        my_list=[10,20,30,40,50]
        index=0
        while index<len(my_list):
            print(my_list[index])
            index+=1
    except ValueError as err:
        print(err)
#some_10()


def some_11():
    try:
        my_list=[10,20,30,40,50]
        print(my_list)
        my_list[0]="Digits: "
        print(my_list)
    except ValueError as err:
        print(err)
#some_11()

def some_12():
    try:
        my_list=[10,20,30,40,50]
        my_list[-1]='end'
        for elements in my_list:
            print(elements)
    except ValueError as err:
        print(err)
#some_12()


def some_13():
    try:
        my_list=[0]*5
        index=0
        while index<len(my_list):
            my_list[index]=1
            index+=1
        print(my_list)
    except ValueError as err:
        print(err)
#some_13()

# В программе 7 .1 приведен пример присвоения элементам списка вводимых пользователем
# значений. Пользователю нужно ввести суммы продаж, которые будут присвоены списку.


# КОНСТАНТА DAYS СОДЕРЖИТ КОЛИЧЕСТВО ДНЕЙ ЗА КОТОРОЫЕ МЫ СОБЕРЕМ ДАННЫЕ ПРОДАЖ:
DAYS=5
def main_1():
    try:
        # создать список, который будет содержать продажи за каждый день:
        sales_list=[0]*DAYS

        # создать перменную,которая будет содержать индекс:
        index=0

        print("Введите продажи за каждый день!")

        # получаем продажи за каждый день:
        while index<DAYS:
            sales_list[index]=float(input("Сколько продали?"))
            index+=1
        # покажем введенные значения:
        print("Вот значения, которые были введены: ")
        for every_sale in sales_list:
            print(every_sale)

    except ValueError as err:
        print(err)

#main_1()


def donbass_cup():
    try:
        count_players=int(input("Какое количество участников турнира?"))
         # создадим список для будущего наполнения:
        players_list=[0]*count_players
        # создадим переменную индекса и присвоим ей значение 0:
        index=0
        print("Введи данные по игрокам! ")
        # создаем цикл, где каждому из индексов будет присвоено значение,введенное с клавиатуры:
        while index<count_players:
            players_list[index]=input("Введи Фамилию и имя игрока: ")
            index+=1

        # выведем на экран то,что ввели в список:
        for elements in players_list:
            print(elements)
    except ValueError as err:
        print(err)
#donbass_cup()

def my_room():
    try:
        # зададаим чсило предметов в комнате:
        count_staff=int(input("Какое количество предметов будем вносить в список?"))
        # создадим переменную для индексации и присвоем ей значение 0:
        index=0
        # создадим список со значением 0, в который будем добавлять элементы:
        room_list=[0]*count_staff # чтобы задать сразу количество элементов в списке

        print("Добавим предметы в комнате!")

        #создадим цикл, внутри которого будем добавлять жоементы в список:
        while index<count_staff:
            room_list[index]=input("Введи название вещи")
            index+=1

        # выведем полученные данные списка на экран:
        for elements in room_list:
            print(elements)
    except ValueError as err:
        print(err)
#my_room()

def some_242():
    try:
        count_questions=int(input("сколько вопросов будем задавать?"))
        question_list=[0]*count_questions
        index=0

        print("Впросы к кандидату: ")
        while index<count_questions:
            question_list[index]=input("Напиши здесь вопрос.")
            index+=1

        for each_qestion in question_list:
            print(each_qestion)
    except ValueError as err:
        print(err)
#some_242()

def some_2424():
    try:
        list_1=[24,52,734,3]
        list_2=[2447,734,855,347]
        list_3=list_1+list_2
        print(list_3)
    except ValueError as err:
        print(err)
#some_2424()


def boys_girls():
    try:
        boys_list=["Phil","Mario","Johnny"]
        girls_list=["Eva","Nicole","Emma"]
        mix_list=boys_list+girls_list
        print(mix_list)
        for every_name in mix_list:
            print(every_name)
    except ValueError as err:
        print(err)
#boys_girls()


#                                               НАРЕЗКА СПИСКА
def week_days():
    try:
        week_list=['monday','thuesday',
                   'wednesday','thursday','friday',
                   'saturday','sunday']
        work_days=week_list[0:5]
        weekend=week_list[5:]
        print(week_list)
        print(work_days)
        print(weekend)
    except ValueError as err:
        print(err)
#week_days(


#                          поиск значения в списках при помощи оператора in
# эта программа демонстрирует работу оператора in применительно к списку:
def some_87284():
    try:
        # создать список артикулов товара:
        articul_list=['bv4320-001','ar1001-003','134700-005','443098-001']
        # получим искомый номер изделия:
        search_articul=input("Введи искомый артикул: ")
        # определить,является ли искомый номе элементом списка:
        if search_articul in articul_list:
            print(search_articul,"Товар с этим артикулом найден!")
        else:
            print("Такого артикула в этом списке нет!")
    except ValueError as err:
        print(err)

#some_87284()


def some_898():
    try:
        name_list=['Jim','Kelly','Eva','Alan','Bill']
        search=input("enter the search name: ")

        if search not in name_list:
            print("no this name")
        else:
            print("name in list")
    except ValueError as err:
        print(err)
#some_898()


#                       СПИСКОВЫЕ МЕТОДЫ И ПОЛЕЗНЫЕ ВСТРОЕННЫЕ ФУНКЦИИ

#                                          APPEND
def some284():
    try:
        #этапрограмма демонстрирует применение метода append:
        # создадим пустой список:
        new_list=[]
        # создадим перменную для управления циклом:
        answer='y'

        #добавим в список несколько имен:
        while answer=='y' or answer=="Y":
            # получаем имя с клавиатуры:
            name=input("Enter the name: ")
            # добавляем в конец списка каждое введенное имя:
            new_list.append(name)

            answer=input(" press y or Y to contunue: ")
        for each_name in new_list:
            print(each_name)
    except ValueError as err:
        print(err)
#some284()

def some24237():
    try:
        new_list=[]
        digit_list=[52,362,433,4642564,45,2664,2354,4568,567,347,26,73434,5634,34425]
        for elements in digit_list:
            if elements%2==0:
                new_list.append(elements)
        print(new_list)
        total=0
        count=0
        for digits in new_list:
            count+=1
            total+=digits
            print(count,' ',digits)
        print("Сумма всех четных элементов в списке равна: ",total)
    except ValueError as err:
        print(err)
#some24237()

def some76583():
    try:
        some_list=['Ann','John','Richard']
        print(some_list)
        some_list.append('- they are good friends')
        print(some_list)
    except ValueError as err:
        print(err)
#some76583()


#                                               INDEX

def some83783():
    try:
        some_list=['Ann',"Terry","Kieran",'Connor','Drake']
        search=some_list.index('Connor')
        print(search)
    except ValueError as err:
        print(err)
#some83783()


# эта программа демонстрирует как получить индексную позицию элемента в списке
# и затем заменить его значение новым
def some7346583():
    try:
        # создаем список с несколькими значениями:
        some_list=['car','job','sallary','cinema','volleyball']

        # показываем список:
        print(some_list)

        # получить значение,которо хотим заменить:
        change_item=input("Какое значение в списке ты хочешь заменить?")

        #получим индексную позицию элемента в списке:
        index_change_item=some_list.index(change_item)

        # получить значение, на которое стоит заменить:
        new_item=input("Введите новое значение: ")

        # заменить старое значение новым:
        some_list[index_change_item]=new_item

        # показать результат:
        print(some_list)
    except ValueError as err:
        print(err)

#some7346583()

def pract141():
    try:
        calc=int(input("Введи количество команд в списке: "))
        players_list=[0]*calc

        index=0

        while index<calc:
            players_list[index]=input("Введи название команды: ")
            index+=1

        for team in players_list:
            print(team)

        # введем команду,которую нужно заменить:
        search_team=input("Введи команду,которую будем менять: ")

        # найдем ее индекс в списке:
        search_index=players_list.index(search_team)

        # получим новую команду с клавиатуры:
        new_team=input("Введи новую команду: ")

        #заменим старое значение на новое:
        players_list[search_index]=new_team

        # выведем на экран:
        for new_teams in players_list:
            print(new_teams)

    except ValueError as err:
        print(err)
    finally:
        print("Thank you!")

#pract141()


def practice_1():
    try:
        #введем количество вещей для похода:
        count_item=int(input("Введи количество вещей,нужных для поездки: "))

        # создадим список,который будет наполняться:
        travel_list=[0]*count_item

        index=0

        while index<count_item:
            travel_list[index]=input("Введи название вещи: ")
            index+=1
        print(travel_list)

        # добавим значение в список:

        # введем значение,которое будем добавлять:
        add_item=input("Введи значение,которое хочешь добавить в конец списка: ")

        # добавим это значение в текущий список:
        travel_list.append(add_item)

        # выведем обновленный список на экран:
        print(travel_list)

        # заменим одну позицию в списке на другую:

        # введем с клавы значение,которое хотим заменить:
        search_item=input("Введи позицию,которую хочешь заменить: ")

        # найдем индекс этой позиции в списке:
        index_search_item=travel_list.index(search_item)

        # введем новую позицию с клавиатуры:
        new_item=input("введи новую позицию: ")

        # поменяем старую позицию на новую:
        travel_list[index_search_item]=new_item

        # распечатаем обновленный список:
        print(travel_list)

        for every_item in travel_list:
            print(every_item)

    except ValueError as err:
        print(err)
#practice_1()
import random



#                                         метод INSERT


# Метод insert () позволяет вставлять значение в список в заданной позиции. В метод
# insert () передается два аргумента: индекс, задающий место вставки значения, и значение,
# которое требуется вставить.

def some_7246():
    try:
        # эта программа демонстирирует применение insert()
        my_daily_plan_list=["1) почистить зубы",
                            "2)позавтракать",
                            "3)позаниматься учебой",
                            "4)сделать пост"]
        # получим элемент,который хотим добавить:
        new_item=input("Введи,что хочешь добавить в план: ")
        new_index=int(input("Введи индекс места добавления нового элемента списка: "))

        # добавляемэлемент в нужном месте:
        my_daily_plan_list.insert(new_index,new_item)

        for each_plan in my_daily_plan_list:
            print(each_plan)
    except ValueError as err:
        print(err)
#some_7246()


def prac8():
    try:
        name_list=['Andrey','Kate','Junel']
        print(name_list)

        name_list.insert(1,'Kyle')
        print(name_list)
    except ValueError as err:
        print(err)
#prac8()


def donbass_ranking():
    try:
        players_rank=[]
        calc=int(input("сколько игроков хотим добавить в список?"))

        for each_player in range(1,calc+1):
            name=input("Введи фамилию и рейтинг игрока: ")
            players_rank.append(name)

        print("Исходный список: ",players_rank)

        new_name=input("Введи фамилию и рейтинг игрока,которого хочешь добавить в список для коррекции: ")
        new_index=int(input("Введи индекс для нового добавления: "))
        players_rank.insert(new_index,new_name)

        print("Отформатированный список:",players_rank)

        for names in players_rank:
            print(names)

    except ValueError as err:
        print(err)
    except Exception as err_2:
        print(err_2)
    finally:
        print("Have a nice day!")
#donbass_ranking()


#                                        МЕТОД SORT()
# Метод sort () перестраивает элементы списка таким образом, что их значения появляются
# в возрастающем порядке (от самого малого значения до самого большого).

def some_827():
    try:
        calc=int(input("Сколько элементов добавить в список?"))
        my_list=[0]*calc
        index=0
        while index<calc:
            my_list[index]=int(input("Вводи элемент списка: "))
            index+=1
        print(my_list)

        #отсортируем список:
        my_list.sort()

        print(my_list)
    except Exception as err:
        print(err)
#some_827()

def some_89():
    try:
        first_list=['Ira','Max','Jane','Oleg']
        print(first_list)

        first_list.sort()
        print(first_list)
    except ValueError as err:
        print(err)
#some_89()

#                                             МЕТОД REMOVE

# Метод remove () удаляет значение из списка. Методу в качестве аргумента передается значение,
# и первый элемент, который содержит это значение, удаляется


def some_989725():
    try:
        some_list=['hello','world','python','facebook','love']
        print(some_list)

        some_list.remove('facebook')
        print(some_list)
    except ValueError as err:
        print(err)
#some_989725()

def some_4827():
    try:
        sales_list=[1000,2000,3000,4000,5000]
        print(sales_list)

        for_delete=int(input("Что будем удалять?"))

        sales_list.remove(for_delete)
        print(sales_list)
    except ValueError as err:
        print(err)
#some_4827()

def some8275():
    try:
        my_list=[]
        max_size=int(input("Сколько элементов будем добавлять в список?"))
        while len(my_list)<max_size:
            for_add=input("Введи имя для добавления в список: ")
            my_list.append(for_add)
        print(my_list)

        for_change=input("Какое имя ты хочешь заменить?")
        get_index_for_change=my_list.index(for_change)

        get_new_name=input("Введи имя, на которое будем менять: ")
        my_list[get_index_for_change]=get_new_name

        print(my_list)

        for names in range(3):
            add_name=input("Напиши имя для добавления в список: ")
            index_add_name=int(input("Какой индекс у этого элемента: "))

            my_list.insert(index_add_name,add_name)

        print(my_list)

        my_list.sort()
        print(my_list)

        for_delete=input("Введи имя, которое хочешь удалить: ")
        my_list.remove(for_delete)
        print(my_list)
    except ValueError as err:
        print(err)
#some8275()


#                                         МЕТОД REVERCE()

# Метод reverse () просто инвертирует порядок следования значений в списке.

def my_1():
    try:
        my_list=[1,2,3,4,5]
        print(my_list)

        my_list.reverse()
        print(my_list)
    except Exception:
        print(Exception)
#my_1()

#                                       ИНСТРУКЦИЯ DEL()

# Некоторые ситуации могут потребовать удалить элемент из
# заданной индексной позиции, независимо от значения, которое хранится в этой индексной
# позиции.

def my_2():
    try:
        some_list=['Andrey','Junell',123,'Chaus','beach volley']
        print("Первоначальный список: ",some_list)

        del some_list[2]
        print("Измененный список: ",some_list)
    except Exception:
        print(Exception)
#my_2()

# ФУНКЦИИ MIN MAX
# Python имеет две встроенные функции, rnin и rnax, которые работают с последовательностями.
# Функция rnin принимает в качестве аргумента последовательность, в частности список, и
# возвращает элемент, который имеет минимальное значение в последовательности.

# Функция rnax принимает в качестве аргумента последовательность, в частности список,
# и возвращает элемент, который имеет максимальное значение в последовательности.

def my_3():
    try:
        some_list=[10,20,30,40,50]

        min_item=min(some_list)
        max_item=max(some_list)

        print("Минимальное значение в списке: ",min_item)
        print("Максимальное значение в списке: ", max_item)
    except Exception:
        print(Exception)
#my_3()

def some989():
    name=[]
    name.append('Wendy')
    print(name)
#some989()

#                                      КОПИРОВАНИЕ СПИСКОВ

def copy():
    try:
        list_1=[1,2,3,4,5]
        list_2=list_1
        print(list_1)
        print(list_2)

        list_1[-1]=10000
        print(list_1)
        print(list_2)
    except Exception:
        print(Exception)
#copy()

def copy2():
    try:
        list1=[1,2,3,4,5,6,7]
        list2=[]
        for item in list1:
            list2.append(item)
        print(list1)
        print(list2)
    except Exception:
        print(Exception)
#copy2()


def copy_3():
    try:
        spisok=[100,200,300,400]
        copy_spisok=[]+spisok
        print(spisok)
        print(copy_spisok)
    except Exception:
        print(Exception)
#copy_3()

def some72356():
    try:
        my_list=[131,2352,363,586679,7070,80]
        my_list_2=[]
        for each_digit in my_list:
            my_list_2.append(each_digit)
        print(my_list)
        print(my_list_2)
    except Exception:
        print(Exception)
#some72356()


#            ПРИМЕНЕНИЕ ЭЛЕМЕНТОВ СПИСКА В МАТЕМАТИЧЕСКИХ ВЫРАЖЕНИЯХ!!!

# Меган владеет небольшим кафе, и у нее работают шесть сотрудников в качестве барменов
# и официантов. У всех сотрудников одинаковая почасовая ставка оплаты труда. Меган
# попросила вас разработать программу, которая позволит ей вводить количество часов, отра-
# Глава 7. Списки и кортежи 383
# ботанных каждым сотрудником, и затем будет показывать суммы заработной платы всех
# сотрудников до удержаний. Вы решаете, что программа должна выполнять следующие
# шаги:
# + для каждого сотрудника получить количество отработанных часов и сохранить его в элементе
# списка;
# + для каждого элемента списка использовать сохраненное в элементе значение для вычисления
# общей заработной платы сотрудника до удержаний. Показать сумму заработной
# платы.

def cafe():
    try:
        #эта программа вычисляет заработную плату для каждого сотрудника кафе:
        NUM_BARMENS=6   #КОНСТАНТА ДЛЯ РАЗМЕРА СПИСКА

        # создадим список,который будет содержать отработанные часы:
        hours=[0]*NUM_BARMENS

        # получить часы,отработанные каждым сотрудником:
        for index in range(NUM_BARMENS):
            print("Введите количество отработанных часов сотрудником: ")
            hours[index]=float(input("Сколько отработал сотрудник?"))

        #получить почасовую ставку оплаты труда:
        money_per_hour=float(input("Сколько платят в час: "))

        # показать заработную плату каждого сотрудника:
        for index in range(NUM_BARMENS):
            zp=hours[index]*money_per_hour
            print("Зарпалата сотрудника составляет: ",zp)
    except ValueError as err:
        print(err)
    except IOError as err2:
        print(err2)
#cafe()


def practice_7632762():
    try:
        kol_vo_veshei=int(input("Введите количество вещей: "))

        # создадим список закупочных цен:
        wholesale_prices_list=[0]*kol_vo_veshei

        # получим коэфициент наценки:
        nacenka=float(input("Введи коэффициент наценки: "))

        #введем оптовые цены дляя каждого товара:
        for index in range(kol_vo_veshei):
            wholesale_prices_list[index]=float(input("Введи закупочную цену товара: "))


        for index in range(kol_vo_veshei):
            retail=wholesale_prices_list[index]*nacenka
            print(retail)
    except Exception:
        print(Exception)

#practice_7632762()

#                                 СУММИРОВАНИЕ ЗНАЧЕНИЙ В СПИСКЕ
def find_sum():
    try:
        # эта программа вычисляет сумму значений в списке:
        total_sum=0
        some_list=[10,20,30]
        for item in some_list:
            total_sum+=item

        print(total_sum)
    except ValueError as err:
        print(err)
#find_sum()

#                          УСРЕДНЕНИЕ ЗНАЧЕНИЙ В СПИСКЕ
def mid_list():
    try:
        my_list=[]
        answer='y'
        count=0
        while answer=="y" or answer=="Y":
            sale=float(input("Сколько заработал на продаже?"))
            my_list.append(sale)
            count+=1
            answer=input("Press Y or y to continue: ")
        print("Список всех продаж: ",my_list)

        total=0
        for each_sale in my_list:
            total+=each_sale
        print("Сумма всех продаж: ",total,"грн")

        mid_sale=total/count
        print("Среднее занчение продаж: ",mid_sale,"грн")
    except Exception:
        print(Exception)
#mid_list()

def some8745():
    try:
        results_list=[10.2,9.87,10.43,12.27,16.1]
        total=0
        for each_result in results_list:
            total+=each_result
        print(total)
        mid_result=total/len(results_list)
        print(mid_result)
    except Exception:
        print(Exception)
#some8745()

#                  ПЕРЕДАЧА СПИСКА В ФУНКЦИЮ В КАЧЕСТВЕ АРГУМЕНТА

def main_sum_items():
    try:
        my_list=[25,67.4,1,1001,345.76]
        summa=get_total(my_list)
        print(summa)
    except Exception:
        print(Exception)

# функия get_total принимает список в качестве аргумента и возвращает сумму значений в списке:
def get_total(some_list):
    total=0
    for item in some_list:
        total+=item
    return total

#main_sum_items()

def main_competitions():
    try:
        result_list=[]
        how_much=int(input("Сколько данных ты хочешь добавить? "))
        for every_result in range(how_much):
            result=float(input("Введи результат спортсмена: "))
            result_list.append(result)

        mid_result=middle_result(result_list)
        print("Средний показатель бега на 100 метров: ",mid_result)

    except ValueError as err:
        print(err)
def middle_result(some_list):
    total=0
    for item in some_list:
        total+=item
        return total/len(some_list)

#main_competitions()


#                         ВОЗВРАЩЕНИЕ СПИСКА ИЗ ФУНКЦИИ:
# Функция может возвращать ссылку на список. Это дает возможность написать функцию,
# которая создает список, добавляет в него элементы и затем возвращает ссылку на этот список,
# чтобы другие части программы могли с ним работать.

def main_some_1():
    try:
        get_list=give_list()
        print(get_list)

    except Exception:
        print(Exception)

def give_list():
    some_list=[]
    answer='y'
    while answer=='y' or answer=="Y":
        item=float(input("Добавь что-то в список: "))
        some_list.append(item)

        answer=input("press y or Y to continue: ")
    return some_list

#main_some_1()

#                                            ОБРАБОТКА СПИСКА
# Получить оценки студента.
# Вычислить сумму оценок.
# Найти минимальную оценку.
# Вычесть минимальную оценку из суммы оценок. Это дает скорректированную сумму.
# Разделить скорректированную сумму на количество оценок минус 1. Это средняя
# оценка.
# Показать среднюю оценку.

def main_univer():
    try:
        # создадим список оценок студента:
        # 1) сколько всего оценок?
        score_calc=int(input("Сколько всего оценок у студента?"))


        # создадим список из оценок:
        score_list=[]

        for item in range(score_calc):
            score=float(input("Введи оценку студента: "))
            score_list.append(score)
        print(score_list)

        # 2) вычисляем сумму всех оценок студента:
        total_sum_score=summa_ocenok(score_list)
        print("Сумма всех оценок: ",total_sum_score)

        # 3) находим минимальную оценку в списке:
        min_score=find_minimal_score(score_list)
        print("Минимальная оценка студента: ",min_score)

        # 4) вычитаем минимальную оценку из общей суммы в списке:
        new_sum=total_sum_score-min_score
        print("Сумма оценок за вычетом минимальной оценки равна: ",new_sum)

        # 5) получим среднюю оценку:
        middle_score=new_sum/(score_calc-1)
        print("Итоговая средняя оценка студента равна: ",middle_score)
    except ValueError as err:
        print(err)
    except Exception:
        print(Exception)
    finally:
        print("Have a good day,Andrey:)")

def summa_ocenok(some_list):
    total=0
    for item in some_list:
        total+=item
    return total


def find_minimal_score(some_list):
    minimum=min(some_list)
    return minimum


#main_univer()

def main_donbass_cup():
    try:
        # получаем список:
        players_points_list=get_list()
        print("Список очков,набранных игроками: ",players_points_list)

        #получаем сумму очков:
        total_sum=summa_ochkov(players_points_list)
        print("Сумма все очков: ",total_sum)

        #считаем  среднее количество очков:
        mid_point=total_sum/len(players_points_list)
        print("Среднее число очков равно: ",mid_point)

        # получаем максимальное значение очков в списке:
        maximum=max_point(players_points_list)
        print("Максимум очков в списке: ",maximum)

        # получаем манимальное значение очков в списке:
        minimum = min_point(players_points_list)
        print("Минимум очков в списке: ",minimum)

    except ValueError as err:
        print(err)
    except Exception:
        print(Exception)

def get_list():
    # создадим пустой список:
    some_list=[]
    calc=int(input("Введи количество игроков: "))
    for player in range(calc):
        points_player=float(input("Введи очки игрока: "))
        some_list.append(points_player)
    return some_list

def summa_ochkov(some_list):
    total=0
    for item in some_list:
        total+=item
    return total

def max_point(some_list):
    return max(some_list)

def min_point(some_list):
    return min(some_list)


#main_donbass_cup()




#                                РАБОТА СО СПИСКАМИ И ФАЙЛАМИ!!!
def prac():
    try:
        file=open(r'D:\Фильмы\list.txt','w')
        get_text=[1,2,3,4,5,6,7,8,9,10]
        file.write(str(get_text))

        file.close()
    except ValueError as err:
        print(err)
#prac()


def some41():
    try:
        city_list=['Paris','London','Viena','Rome','Madrid']
        file=open(r'D:\Фильмы\city.txt','w')

        for each_city in city_list:
            file.write(each_city+'\n')

        file.close()
    except ValueError as err:
        print(err)


#some41()


def main_read_file():
    try:
        file=open(r'D:\Фильмы\city.txt','r')
        city_list=file.readlines()
        file.close()

        index=0
        while index<len(city_list):
            city_list[index]=city_list[index].rstrip('\n')
            index+=1


        print(city_list)
    except ValueError as err:
        print(err)
#main_read_file()

def some_2685():
    try:
        file=open(r'D:\Фильмы\отложил.txt','w')
        answer='y'
        while answer=="y" or answer=="Y":
            collect=float(input("Сколько сегодня отложил денег?"))
            file.write(str(collect)+'\n')
            answer=input("press Y or y to continue: ")
        file.close()
    except Exception:
        print(Exception)
#some_2685()

def read_some_2685():
    try:
        file=open(r'D:\Фильмы\отложил.txt','r')
        some_list=file.readlines()
        file.close()

        index=0
        while index<len(some_list):
            some_list[index]=some_list[index].rstrip('\n')
            index+=1

        print(some_list)
    except Exception:
        print(Exception)
#read_some_2685()

def practice_762():
    try:
        my_list=[28.06,6.11,15.2]
        file=open(r'D:\Фильмы\birthdays.txt','w')

        for element in my_list:
            file.write(str(element)+'\n')
        file.close()
    except Exception:
        print(Exception)

#practice_762()

def read_practice_762():
    try:
        file=open(r'D:\Фильмы\birthdays.txt','r')
        birthdays_list=file.readlines()
        file.close()

        index=0
        while index<len(birthdays_list):
            birthdays_list[index]=float(birthdays_list[index])
            index+=1
        print(birthdays_list)
    except Exception:
        print(Exception)
#read_practice_762()


#                                        ДВУМЕРНЫЕ СПИСКИ
def practice_34568():
    scores=[[1,1,1],
            [2,2,2],
            [3,3,3]]
    print(scores[0][1])
#practice_34568()

def some23():
    try:
        # эта программа присваивает случайные числа двумерному списку:
        import random
        KOL_STROK=3
        KOL_STOLBCOV=4

        spisok=[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        for element_strok in range(KOL_STROK):
            for element_stolbcov in range(KOL_STOLBCOV):
                spisok[element_strok][element_stolbcov]=random.randint(1,100)
        print(spisok)
    except ValueError as err:
        print(err)
#some23()

def pract_44():
    try:
        import random
        file=open(r'D:\Фильмы\matrix.txt','w')

        KOL_STROK=4
        KOL_STOLB=4
        random_size_from=int(input("Введи размер случайного выбора от: "))
        random_size_to = int(input("Введи размер случайного выбора до: "))
        matrix=[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

        for el_strok in range(KOL_STROK):
            for el_stolb in range(KOL_STOLB):
                matrix[el_strok][el_stolb]=random.randint(random_size_from,random_size_to)
                file.write(str(matrix[el_strok][el_stolb])+'\n')
        file.close()
    except ValueError:
        print(ValueError)
#pract_44()

def read_pract():
    try:
        file=open(r'D:\Фильмы\matrix.txt','r')
        read_list=file.readlines()
        file.close()

        index=0
        while index<len(read_list):
            read_list[index]=read_list[index].rstrip('\n')
            index+=1
        print(read_list)
    except ValueError as err:
        print(err)
#read_pract()

def pr_178():
    import random
    STROKA=3
    STOLB=4
    some_list=[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    for el_str in range(STROKA):
        for el_stolb in range(STOLB):
            some_list[el_str][el_stolb]=random.randint(1,9)
    print(some_list)
#pr_178()

def parct_252():
    # numЬers = [ [1, 2], [10, 20], [100, 200], [1000, 2000]]
    STR=4
    STB=2

    numbers=[[0,0],
             [0,0],
             [0,0],
             [0,0]]
    for element_str in range(STR):
        for element_stb in range(STB):
            numbers[0][0]=1
            numbers[0][1] = 2
            numbers[1][0] = 10
            numbers[1][1] = 20
            numbers[2][0] = 100
            numbers[2][1] = 200
            numbers[3][0] = 1000
            numbers[3][1] = 2000

    print(numbers)
#parct_252()

#                                             КОРТЕЖИ

# Кортеж - это немутирующая последовательность; под этим подразумевается, что его
# содержимое невозможно изменить.
# Кортеж - это последовательность, которая очень напоминает список. Главная разница
# между кортежами и списками состоит в том, что кортежи являются немутирующими последовательностями.
# Это означает, что после того как кортеж создан, его невозможно изменить.

def some72():
    my_tuple=(1,2,3,4,5)
    print(my_tuple)
    for element in my_tuple:
        print(element)
    for index in range(len(my_tuple)):
        print(my_tuple[index])
#some72()

# Если необходимо создать кортеж всего с одним элементом, то после значения элемента следует
# написать замыкающую запятую :
def some72234():
    one_element_tuple=("Andrey",)
    print(one_element_tuple)
#some72234()

#                    ПРЕОБРАЗОВАНИЕ КОРТЕЖА В СПИСОК И НАОБОРОТ
def change_1():
    some_list=[1,2,4,5,6]
    print(some_list)
    some_list=tuple(some_list)
    print(some_list)
#change_1()

def change_2():
    some_tuple=(1,2,3,5,6)
    print(some_tuple)
    new=list(some_tuple)
    print(new)
#change_2()

def trenajer_1():
    """
    Напишите инструкцию, которая создает список с приведенными далее строковыми значениями:
'Эйнштейн', 'Ньютон', 'Коперник' и 'Кеплер'.
    :return:
    """
    try:
        spisok=['Эйнштейн', 'Ньютон', 'Коперник', 'Кеплер']
        print(spisok)
    except ValueError as err:
        print(err)
#trenajer_1()

def trenajer_2():
    """
    Допустим, что переменная names ссылается на список. Напишите цикл for, который выводит
каждый элемент списка.
    :return:
    """
    try:
        names=["Paris","london","Coventry",'Leeds']
        for each_city in names:
            print(each_city)
    except Exception:
        print(Exception)
#trenajer_2()

def trenajer_3():
    """
    Допустим, что список numЬersl имеет 100 элементов, а numЬers2 является пустым списком.
Напишите код, который копирует значения из списка numЬersl в список numЬers2.
    :return:
    """
    try:
        numbers_1=[]
        for num in range(100):
            numbers_1.append(num)
        print(numbers_1)

        numbers_2=[]+numbers_1
        print(numbers_2)
    except Exception:
        print(Exception)
#trenajer_3()

def trenajer_4():
    """Напишите функцию, которая принимает список в качестве аргумента (допустим, что список
содержит целые числа) и возвращает сумму значений в списке.

    :return:
    """
    try:
        spisok=[10,20,30]
        print(spisok)
        result=summa_znach(spisok)
        print("Сумма значений списка равна: ",result)
    except Exception:
        print(Exception)


def summa_znach(some_spisok):
    total=0
    for element in some_spisok:
        total+=element
    return total

#trenajer_4()

def tren_5():
    """
    Допустим, что переменная narnes ссылается на список строковых значений. Напишите
программный код, который определяет, находится ли имя 'Руби' в списке names. Если
это так, то выведите сообщение 'Привет, Руби! ' . В противном случае выведите сообщение
' Руби отсутствует ' .
    :return:
    """
    try:
        names=[]
        count_names=int(input("Сколько имен будет в списке?"))
        for name in range(count_names):
            add_name=input("введи новое имя: ")
            names.append(add_name)
        if "Rubi" not in names:
            print("Rubi is out!")
        else:
            print("hey,Rubi!")
    except ValueError as err:
        print(err)
#tren_5()

def tren_6():
    list1=[10,20,30]
    list2=[40,50,60]
    list3=list1+list2
    print(list3)
#tren_6()

def tren_7():
    """
    Напишите инструкцию, которая создает двумерный список с 5 строками и 3 столбцами.
Затем напишите вложенные циклы, которые получают от пользователя целочисленное
значение для каждого элемента в списке.
    :return:
    """
    try:
        STROKA=5
        STOLBEC=3

        some_list=[[0,0,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]]

        for el_str in range(STROKA):
            for el_stolb in range(STOLBEC):
                some_list[el_str][el_stolb]=int(input("Введи значение для списка: "))
        print(some_list)
    except Exception:
        print(Exception)
#tren_7()

def tren_8():
    """
    Общий объем продаж. Разработайте программу, которая просит пользователя ввести
продажи магазина за каждый день недели. Суммы должны быть сохранены в списке.
Примените цикл, чтобы вычислить общий объем продаж за неделю и показать результат.
    :return:
    """
    try:
        print("Эта программа вычисляет объем продаж за заданный промежуток времени.")
        my_spisok=get_list_for_tren_8()
        print("Вычислим сумму всех продаж!")
        all_sales=total_sales(my_spisok)
        print(all_sales,"грн")
    except ValueError as err:
        print(err)

def get_list_for_tren_8():
    days=int(input("За сколько дней будем суммировать продажи?"))
    sales_list=[0]*days
    index=0
    while index<days:
        sales_list[index]=float(input("Введите сумму продаж за день: "))
        index+=1
    return sales_list


def total_sales(some_list):
    total=0
    for item in some_list:
        total+=item
    return total

#tren_8()

def tren_9():
    """
    Генератор лотерейных чисел. Разработайте программу, которая генерирует семизначную
комбинацию лотерейных чисел. Программа должна сгенерировать семь случайных
чисел, каждое в диапазоне от О до 9, и присвоить каждое число элементу списка. (Случайные
числа рассматривались в главе 5.) Затем напишите еще один цикл, который показывает
содержимое списка.
    :return:
    """
    try:
        import random
        KOL_CHISEL=7
        lotery_list=[0]*KOL_CHISEL
        index=0
        while index<KOL_CHISEL:
            lotery_list[index]=random.randint(0,9)
            index=0
        for num in lotery_list:
            print(num)
    except Exception:
        print(Exception)

#tren_9()


def main_rain():
    """
    Статистика дождевых осадков. Разработайте программу, которая позволяет пользователю
занести в список общее количество дождевых осадков за каждый из 12 месяцев.
Программа должна вычислить и показать суммарное количество дождевых осадков за
год, среднее ежемесячное количество дождевых осадков и месяцы с самым высоким и
самым низким количеством дождевых осадков.
    :return:
    """
    print("Эта программа делает расчеты по осадкам.")
    rain=get_rain_list()
    print("Рассчитаем сумарное количество осадков:")
    allyear_rain=total_rain(rain)
    print(allyear_rain)
    print("Рассчитаем среднее ежемесячное количество осадков: ")
    middle_value=mid_rain(rain)
    print(middle_value)
    print("Самое малое количество осадков за год: ")
    minimal=min_rain(rain)
    print(minimal)
    print("Самое большое количество осадков за год: ")
    maximum = max_rain(rain)
    print(maximum)

def get_rain_list():
    month=12
    rain_list=[0]*month
    index=0
    while index<month:
        rain_list[index]=float(input("Введи количество осадков за месяц: "))
        index+=1
    return rain_list

def total_rain(some_list):
    total=0
    for item in some_list:
        total+=item
    return total

def mid_rain(some_list):
    total = 0
    for item in some_list:
        total += item
    result=total/len(some_list)
    return result

def min_rain(some_list):
    result=min(some_list)
    return result


def max_rain(some_list):
    result=max(some_list)
    return result


#main_rain()


# Проrрамма анализа чисел. Разработайте программу, которая просит пользователя ввести
# ряд из 20 чисел. Программа должна сохранить числа в списке и затем показать приведенные
# ниже данные:
# • наименьшее число в списке;
# • наибольшее число в списке;
# • сумму чисел в списке;
# • среднее арифметическое значение чисел в списке.
def main_analiz_digits():
    try:
        print("Эта программа анализирует числа!")
        main_list=get_digit_list()
        minimal=min_value(main_list)
        print("Минимальное число из списка: ",minimal)
        maximum=max_value(main_list)
        print("Максимально число из списка: ",maximum)
        total=summa_chisel(main_list)
        print("Сумма чисел в списке: ",total)
        middle=srednee(main_list,total)
        print("Среднее арифметическое: ",middle)
    except ValueError as err:
        print(err)
    finally:
        print("Have a nice day,bro:)")

def get_digit_list():
    LONG=20
    some_list=[]
    for num in range(LONG):
        digit=float(input("Введи число: "))
        some_list.append(digit)
    return some_list

def min_value(some_list):
    result=min(some_list)
    return result


def max_value(some_list):
    result=max(some_list)
    return result

def summa_chisel(some_list):
    total=0
    for item in some_list:
        total+=item
    return total

def srednee(some_list,total):
    result=total/len(some_list)
    return result


#main_analiz_digits()


# Проверка допустимости номера расходноrо счета. Среди исходного кода главы 7,
# а также в подпапке data "Решений задач по программированию" соответствующей главы
# вы найдете файл charge_accounts.txt. Этот файл содержит список допустимых номеров
# расходных счетов компании. Каждый номер счета представляет собой семизначное число,
# в частности 5658845.
# Напишите программу, которая считывает содержимое файла в список. Затем эта программа
# должна попросить пользователя ввести номер расходного счета. Программа
# должна определить, что номер является допустимым, путем его поиска в списке. Если
# число в списке имеется, то программа должна вывести сообщение, указывающее на то,
# что номер допустимый. Если числа в списке нет, то программа должна вывести сообщение,
# указывающее на то, что номер недопустимый.
import random
def main_schet():
    try:
        KOL=5
        file=open(r'D:\Фильмы\charge_accounts.txt','w')
        list_numbers=[0]*KOL
        index=0
        while index<KOL:
            list_numbers[index]=random.randint(1000000,9999999)
            index+=1
        file.writelines(str(list_numbers)+'\n')
        file.close()
    except ValueError as err:
        print(err)
#main_schet()


def read_main_schet():
    try:
        file=open(r'D:\Фильмы\charge_accounts.txt','r')

        our_list=file.read()
        file.close()

        search_number=input("Введи семизначный номер счета: ")
        if search_number in our_list:
            print(search_number,'-допустимый номер счета')
        else:
            print(search_number,'-недопустимый номер счета')
    except ValueError as err:
        print(err)
    finally:
        print('have a nice day,bro:)')
#read_main_schet()

# Больше числа п. В программе напишите функцию, которая принимает два аргумента:
# список и число п. Допустим, что список содержит числа. Функция должна показать все
# числа в списке, которые больше п.

def main_exerc_6():
    try:
        print("Эта программа решает задачу номер 6!")
        our_list=make_list()
        print("Наш список: ",our_list)
        digit_n=get_digit()
        print("Число n: ",digit_n)
        difference=sravnenie(digit_n,our_list)
        #for num in our_list:
            #if num>digit_n:
                #print(num,'>',digit_n)

    except ValueError as err:
        print(err)

def make_list():
    DLINNA=4
    some_list=[]
    for item in range(DLINNA):
        chislo=int(input("enter some digit: "))
        some_list.append(chislo)
    return some_list

def get_digit():
    result=int(input("enter digit 'n':"))
    return result

def sravnenie(chislo,spisok):
    for num in spisok:
        if num>chislo:
            return print(num,'>',chislo)

#main_exerc_6()

# Экзамен на получение водительских прав.
def main_autoschool():
    try:
        # создадим двумерный список с правильными ответами на тест:
        right_answers_list=['1.A','2.C','3.A','4.A','5.D',
                            '6.B','7.C','8.A','9.C','10.B',
                            '11.A','12.D','13.C','14.A','15.D',
                            '16.C','17.B','18.B','19.D','20.A']

        # прочитаем ответы студента из файла:
        file=open(r'D:\Фильмы\автошкола.txt','r')

        answers=file.readlines()
        file.close()

        index=0
        while index<len(answers):
            answers[index]=answers[index].rstrip('\n')
            index+=1

        wrong_list=[]
        count=0
        index=0

        for i in range(len(right_answers_list)):
            if right_answers_list[index]!=answers[index]:
                count+=1
                print(right_answers_list[index],'не верно',answers[index])
            else:
                print(right_answers_list[index],'верно',answers[index])

            index+=1
        print(count)
        if count>4:
            print("Экзамен не сдан!")
        else:
            print("Ты успешно сдал экзамен:)")

    except ValueError as err:
        print(err)
#main_autoschool()

# Поиск имени. Среди исходного кода главы 7, а также в подпапке data "Решений задач
# по программированию" соответствующей главы вы найдете приведенные ниже файлы:
# • GirlNames.txt - файл содержит список 200 самых популярных имен, данных девочкам,
# родившимся в США между 2000 и 2009 годами;
# • BoyNames.txt- файл содержит список 200 самых популярных имен, данных мальчи-
# кам, родившимся в США между 2000 и 2009 годами.
# Напишите программу, которая считывает содержимое этих двух файлов в два отдельных
# списка. Пользователь должен иметь возможность ввести имя мальчика, имя девочки или
# оба имени, и приложение должно вывести сообщения о том, что введенные имена находятся
# среди самых популярных имен.

def main_names():
    try:
        # считаем два файла с именами.
        # откроем и занесем в список файл с мужскими именами:
        file_man=open(r'D:\Фильмы\мужские_имена.txt','r')
        man_list=file_man.readlines()
        file_man.close()

        # откроем и занесем в список файл с женскими именами:
        file_woman=open(r'D:\Фильмы\женские_имена.txt','r')
        woman_list=file_woman.readlines()
        file_woman.close()

        #уберем переносы строк:
        index=0
        while index<len(man_list):
            man_list[index]=man_list[index].rstrip('\n')
            index+=1

        index = 0
        while index < len(woman_list):
            woman_list[index] = woman_list[index].rstrip('\n')
            index += 1

        # получим имя и проверим его по спискам:
        search_name=input("Введите имя: ")
        check_name(man_list,woman_list,search_name)

    except ValueError as err:
        print(err)

def check_name(man_names_list,woman_names_list,name):
    if name in man_names_list or name in woman_names_list:
        return print("Это имя среди самых популярных имен в мире!")
    else:
        return print("Это имя непопулярно!")


#main_names()

#  создадим файл с населением США с 1950-1 по 1990-1 год
def naselenie():
    try:
        file=open(r'D:\Фильмы\население.txt','w')
        for every_year in range(40):
            population=int(input("Введи население в этом году: "))
            file.write(str(population)+'\n')
        file.close()
    except ValueError as err:
        print(err)
#naselenie()

# Данные о населении. Среди исходного кода главы 7, а также в подпапке data "Решений
# задач по программированию" соответствующей главы вы найдете файл USPopulation.txt.
# Этот файл содержит данные о среднегодовой численности населения США в тысячах с
# 1950 по 1990 годы. Первая строка в файле содержит численность населения в 1950 году,
# вторая строка - численность населения в 1951 году и т. д.
# Напишите программу, которая считывает содержимое файла в список. Программа должна
# показать приведенные ниже данные:
# • среднегодовое изменение численности населения в течение указанного периода времени;
# • год с наибольшим увеличением численности населения в течение указанного периода
# времени;
# • год с наименьшим увеличением численности населения в течение указанного периода
# времени.

def work_population():
    try:
        file=open(r'D:\Фильмы\население.txt','r')
        population_list=file.readlines()
        file.close()

        # удалим переносы:
        index=0
        while index<len(population_list):
            population_list[index]=population_list[index].rstrip('\n')
            index+=1
        print(population_list)

        # переведем строки в числа:
        index=0
        while index<len(population_list):
            population_list[index]=int(population_list[index])
            index+=1


        middle=mid_population(population_list)
        print("Среднегодовое изменение числености населения:",middle )

        maximum=max_population(population_list)
        print("Максимум прирост населения: ",maximum)

        minimum=min_population(population_list)
        print("Минимальный прирост населения: ", minimum)

    except ValueError as err:
        print(err)


def mid_population(some_list):
    total=0
    for value in some_list:
        total+=value
    result=total/len(some_list)
    return result


def max_population(some_list):
    result=max(some_list)
    return result


def min_population(some_list):
    result=min(some_list)
    return result


#work_population()


def world_tour_list():
    try:
        file=open(r'D:\Фильмы\world_tour.txt','w')
        for team in range(30):
            team_name=input("Введи название команды-победителя серии: ")
            file.write(team_name+'\n')
        file.close()
    except ValueError as err:
        print(err)
#world_tour_list()


def find_cahmpion():
    try:
        file=open(r'D:\Фильмы\world_tour.txt','r')

        teams_list=file.readlines()
        file.close()

        index=0
        while index<len(teams_list):
            teams_list[index]=teams_list[index].rstrip('\n')
            index+=1
        print(teams_list)


        search=input("Введи название искомой команды: ")
        calc=0
        for team in teams_list:
            if search==team:
                calc+=1

        print(f'{search} выигрывал этот трофей : {calc} раз!')

    except ValueError as err:
        print(err)
#find_cahmpion()

# Магический квадрат Ло Шу. Магический квадрат Ло Шу представляет собой таблицу
# с 3 строками и 3 столбцами (рис. 7 .18). Магический квадрат Ло Шу имеет приведенные
# ниже свойства:
# • таблица содержит числа строго от 1 до 9;
# • сумма каждой строки, каждого столбца и каждой диагонали в итоге составляет одно
# и то же число (рис. 7 .19).
# Магический квадрат можно сымитировать в программе при помощи двумерного списка.
# Напишите функцию, которая принимает двумерный список в качестве аргумента и
# определяет, не является ли список магическим квадратом Ло Шу. Протестируйте функцию
# в программе.

def magic_square(some_list):
    if some_list[0][0]+some_list[0][1]+some_list[0][2]==some_list[1][0]+some_list[1][1]+some_list[1][2]:
        if some_list[1][0]+some_list[1][1]+some_list[1][2]==some_list[2][0]+some_list[2][1]+some_list[2][2]:
            return print("Это магический квадрат!!!!")
        else:
            return print("Это обычная хрень!")

def main_8282():
    magic_cube = [[4, 9, 2],
                  [3, 5, 7],
                  [8, 1, 6]]
    magic_square(magic_cube)
#main_8282()

# Генерация простого числа. Натуральное (целое положительное) число является простым,
# если оно не имеет делителей кроме 1 и самого себя. Натуральное (целое положительное)
# число является составным, если оно не является простым. Напишите программу,
# которая просит пользователя ввести целое число больше 1 и затем выводит все простые
# числа, которые меньше или равны введенному числу. Программа должна работать
# следующим образом:
# • после того как пользователь ввел число, программа должна заполнить список всеми
# целыми числами начиная с 2 и до введенного значения;
# • затем программа должна применить цикл, чтобы пройти по списку. Каждый элемент
# должен быть в цикле передан в функцию, которая определяет и сообщает, что элемент
# является простым числом.

def main_generation():
    spisok=[]
    get_digit=int(input("Введи число,большее 1: "))
    for num in range(2,get_digit+1):
       spisok.append(num)
    print(spisok)

    index=0
    while index<len(spisok):
        prostoe(spisok[index])
        index+=1



def prostoe(chislo):
    for delitel in (2, int(chislo ** 0.5) + 1):
        if chislo % delitel == 0:
            return False
    return print(chislo,'-это простое число!')


#main_generation()
import random
def magic_circle():
    try:
        file=open(r'D:\Фильмы\ответы.txt','r')

        answer_list=file.readlines()
        file.close()

        index=0
        while index<len(answer_list):
            answer_list[index]=answer_list[index].rstrip('\n')
            index+=1

        answer = 'y'
        while answer == 'y' or answer == 'Y':
            question = input("Напиши свой вопрос: ")
            print(random.choice(answer_list))
            answer=input("press Y or y to continue...")

    except Exception:
        print(Exception)


#magic_circle()

def krugovaya_diagramma():
    try:
        file =open(r'D:\Фильмы\расходы.txt','w')

        answer='y'
        while answer=='y' or answer=="Y":
            pay=float(input("Введи расход: "))
            file.write(str(pay)+'\n')
            answer=input("press y or Y to continue...")
        file.close()
    except Exception:
        print(Exception)

#krugovaya_diagramma()

import matplotlib.pyplot as plt

def read_krug():
    try:
        file=open(r'D:\Фильмы\расходы.txt','r')
        list_rashodi=file.readlines()
        file.close()

        index=0
        while index<len(list_rashodi):
            list_rashodi[index]=list_rashodi[index].rstrip('\n')
            index+=1
        print(list_rashodi)

        metki_doley=['Аренда','Квартплата','Обслуживание машины','Еда','Карманные расходы','Учеба']

        plt.pie(list_rashodi,labels=metki_doley)

        plt.title("Мои расходы")

        plt.show()

    except ValueError as err:
        print(err)
#read_krug()
import random
def make_benzin():
    try:
        file=open(r'D:\Фильмы\бензин.txt','w')
        for each_year in range(1,53):
            give_cost=random.randint(25,33)
            file.write(str(give_cost)+'\n')
        file.close()
    except ValueError as err:
        print(err)
#make_benzin()


def get_benzin():
    import matplotlib.pyplot as plt
    try:
        file=open(r'D:\Фильмы\бензин.txt','r')

        benzin_list=file.readlines()
        file.close()

        index=0
        while index<len(benzin_list):
            benzin_list[index]=benzin_list[index].rstrip('\n')
            index+=1

        index=0
        while index < len(benzin_list):
            benzin_list[index] = int(benzin_list[index])
            index += 1

        left_x=[1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26,27,28,29,30,
                31,32,33,34,35,36,37,38,39,40,
                41,42,43,44,45,46,47,48,49,50,
                51,52]

        height_stlb=benzin_list

        plt.title("Стоимость бензина")

        plt.bar(left_x,height_stlb)

        plt.show()


    except ValueError as err:
        print(err)
#get_benzin()















