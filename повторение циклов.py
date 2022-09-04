def perebor_stroki():
    """ Создаем функцию перебора любой строки,
    которая будет определять каждый сивол введенной строки
    и выводить информацию о нем.
    """
    stroka = input('Enter any string: ')
    while len(stroka) > 0:
        simbol = stroka[0]
        stroka = stroka[1:]
        if simbol >= 'a' and simbol <= 'z':
            print(simbol, '- small word')
        elif simbol >= 'A' and simbol <= 'Z':
            print(simbol, '- big word')
        elif simbol.isdigit():
            print(simbol, '- is digit')
        elif simbol == ' ':
            print(simbol, "- probel")
        else:
            print(simbol, '- another symbol')


# perebor_stroki()

def al_evklid_1():
    """ Создадим функцию нахождения наибольшего общего делителя
    двух чисел (Алгоритм Евклида).

    :return: None
    """
    chislo_1 = int(input('Enter digit #1: '))
    chislo_2 = int(input('Enter digit #2: '))
    while chislo_1 != chislo_2:
        if chislo_1 > chislo_2:
            chislo_1 = chislo_1 - chislo_2
        else:
            chislo_2 = chislo_2 - chislo_1
    print(f'NOD =', chislo_1)


# al_evklid_1()

def al_evklid_2():
    """
    Реализуем более совершенную функцию нахождения
    НОД двух чисел (Алоритм Евклида версии №2)
    :return: None
    """
    num_1 = int(input('Enter 1st digit: '))
    num_2 = int(input('Enter 2nd digit: '))
    assert num_1 > num_2
    while num_2 > 0:
        ostatok = num_1 % num_2
        num_1, num_2 = num_2, ostatok
    print(num_1)


# al_evklid_2()

def funcrange():
    """
    Повторим функицю range перед циклом for
    :return: None
    """
    a = range(1, 10)
    print(list(a), max(a))


# funcrange()

def forrange():
    """
    Повторение цикла for
    :return:
    """
    count = 0
    summa = 0
    from random import randint
    n = int(input("How many digits do you want to print? "))
    for num in range(n):
        count += 1
        chislo = randint(100, 1000)
        summa += chislo
        print(count, "-", chislo)
        print()
    print(summa)


# forrange()

def list_for():
    """
    Вспомню цикл фор для списков и строк
    :return:
    """
    a = [1, 1, 2, 3, 3, 4, 55, 5, 66, 66, 7, 8, 99, 99, 11, 12, 12, 12, 13]
    chet = []
    nechet = []
    n = len(a)
    for i in range(n):
        if a[i] % 2 == 0:
            chet.append(a[i])
        else:
            nechet.append(a[i])
    print(chet)
    print(nechet)


# list_for()

def str_for():
    """
    remembering cycle for str
    :return:
    """
    glasnie = 'aeiou'
    spisok = 'meoocewceekmmiiwcqrcqce'
    n = len(spisok)
    for bukva in range(n - 1):
        if spisok[bukva] in glasnie and spisok[bukva + 1] in glasnie:
            print(spisok[bukva], spisok[bukva + 1])
    print("FINISHED")


# str_for()

def vloj_cycle():
    """
    повторяем вложенные циклы
    :return:
    """
    slovo = 'smart'
    while len(slovo) > 0:
        s = slovo[0]
        slovo = slovo[1:]
        print(s, slovo)


# vloj_cycle()

def nested_list():
    """
    Вложенные списки(матрицы)
    :return:
    """


a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
#for i in a:
 #   for j in i:
  #      print(j,end='  ')
   # print()
#print(a)

#обход по индексам!!!
for j in range(4):
    sum=0
    for i in range(3):
        sum+=a[i][j]
    #print(sum)


#nested_list()

def zapolni_spisok():
    """
    Как заполнять вложенный список каким-то одним числом
    :return:
    """
    a=[]
    n=int(input('введи количество строк')) #кол-во строк
    m=int(input("введи количество столбцов")) #кол-во столбцов
    for i in range(n):
        a.append([0]*m)
    for i in a:
        print(i)
#zapolni_spisok()

def zapolni_matrix():
    """
    Как заполнить список с клавиатуры
    :return:
    """
    a=[]
    n=int(input("КОличество строк: "))
    m=int(input("Количество столбцов: "))
    for i in range(n):
        b=[]
        for i in range(m):
            b.append(int(input()))
        a.append(b)
    for i in a:
        print(i)
#zapolni_matrix()

def kvadrat_tabl():
    """
    Квадратные таблицы
    :return:
    """
    a=[]
    n=int(input('ВВеди значение квадратной таблицы'))
    for i in range(n):
        a.append([0]*n)

    for i in range(n):
        for j in range(n):
            if i==j:
                a[i][j]=10
            elif i>j:
                a[i][j]=5
            else:
                a[i][j]=3
    for i in a:
        print(i)



kvadrat_tabl()