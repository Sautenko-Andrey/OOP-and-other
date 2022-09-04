#                            Обход строкового значения в цикле for

def some_24():
    name="Andrey"
    for each_word in name:
        print(each_word)
#some_24()

def some_7236():
    try:
        some_text='Andrey, please, lets have a rest!'
        count=0
        for word in some_text:
            if word=='a' or word=='A':
                count+=1
        print("Букв а или А в данном тексте: ",count)
    except Exception:
        print(Exception)
#some_7236()

def some367():
    try:
        text=input("Enter some text: ")
        search=input("Enter word,what you wanna find: ")
        count=0
        for word in text:
            if word==search:
                count+=1
        print(f'There are {count} word {word} in text: {text}')
    except Exception:
        print(Exception)
#some367()


def some_827():
    try:
        text=input('enter some text: ')
        search_simbol=input("what simbol we gonna find?")
        count=0
        for simbol in text:
            if search_simbol==simbol:
                count+=1
        print(f"There are {count} simbol {search_simbol} in text {text}")
    except ValueError as err:
        print(err)
#some_827()

#                                         ИНДЕКСАЦИЯ

def some224():
    try:
        city_name=input("what city?")
        index=0
        while index<len(city_name):
            print(city_name[index])
            index+=1
        search=input("what are you looking for?")
        count=0
        for symbol in city_name:
            if search==symbol:
                count+=1
        print(f"there are {count} symbol '{search}' in {city_name}")
    except IndexError as err:
        print(err)
    except ValueError as err2:
        print(err2)
#some224()

#                                   КОНКАТЕНАЦИЯ

def konk():
    try:
        name=input("enter your name: ")
        secondname=input('enter your second name: ')
        message=name+' '+secondname
        print(message)
    except Exception:
        print(Exception)
#konk()


def konk2():
    try:
        text_1=input("enter some text: ")
        main_text='he wrote this sms: '
        main_text+=text_1
        print(main_text)
    except Exception:
        print(Exception)
#konk2()


def konk3():
    try:
        name='Andrey'
        name+=' '
        name+='Sautenko'
        name+=' '
        name+=',32 years old.'
        print(name)
    except Exception:
        print(Exception)
#konk3()


def practice_1():
    try:
        name=input("text here some words: ")
        for symbol in name:
            print(symbol)
    except Exception:
        print(Exception)
#practice_1()

#                                 НАРЕЗКА СТРОКОВЫХ ЗНАЧЕНИЙ
def srez():
    try:
        name='Sautenko Andrey Evgenievich'
        mid_name=name[:15]
        print(mid_name)
    except IndexError as err:
        print(err)
#srez()

#                             ИЗВЛЕЧЕНИЕ СИМВОЛОВ ИЗ СТРОКОВОГО ЗНАЧЕНИЯ

def login_py():
    try:
        get_name=input("enter student's name: ")
        get_surname=input("enter student's surname")
        get_id=input("enter student's id: ")
        login=get_name[:3]+get_surname[:3]+get_id[:3]
        print(f"Student's login for campus is:{login}")
    except Exception:
        print(Exception)
#login_py()


#                    ПРОВЕРКА , ПОИСК И МАНИПУЛЯЦИЯ СТРОКОВЫМИ ЗНАЧЕНИЯМИ
#                     Проверка строковых значений при помощи in и not in

def pr_1442():
    text='some people say club music is dead'
    search=input('what are YOU LOOKING FOR?')
    if search in text:
        print(f"{search} is in {text}")
    else:
        print("no!")
#pr_1442()

def some98():
    name=input("enter name: ")
    search=input("enter what are you looking for: ")
    if search not in name:
        print("no")
    else:
        print("owh yeah!")
#some98()


#                         МЕТОДЫ ПРОВЕРКИ СТРОКОВЫХ ЗНАЧЕНИЙ

def some823():
    text='234124'
    if text.isdigit():
        print("Текст содержит только числовые значения!")
    else:
        print("Это обычный текст")
#some823()

def some92348():
    text='kjhrekjhkj'
    if text.isalnum():
        print("ok")
    else:
        print('no')
#some92348()


def alpha():
    text='kwjerhuhf'
    if text.isalpha():
        print('ok')
    else:
        print('no')
#alpha()


def lower():
    text='jfhwfiwhf'
    if text.islower():
        print('small symbols')
    else:
        print('something wrong!')
#lower()


def space():
    text='           '
    if text.isspace():
        print('ok')
    else:
        print('no')
#space()


def upper():
    text='JHFYDUYU'
    if text.isupper():
        print('big symbols')
    else:
        print('wrong!')
#upper()

#                                      МЕТОДЫ МОДИФИКА

def lower_():
    text='HELLO!'
    mod=text.lower()
    print(mod)
#lower_()


def lstrip():
    text='  ' \
         'lkdfjgskl'
    mod=text.lstrip()
    print(mod)
#lstrip()

def rstrip():
    text='i dont want to be sic'
    mod=text.rstrip('to be sic')
    print(mod)
#rstrip()




def strip():
    text='   flwjfwl   ' \
         ' kwfwjf  lkj  ;wfk131 3123' \
         '131313 131'
    mod=text.strip()
    print(mod)
#strip()


def strip_argument():
    text='11salo11'
    mod=text.strip('1')
    print(mod)
#strip_argument()

def upper_():
    text='kjhfkjafh'
    mod=text.upper()
    print(mod)
#upper_()

def som_1():
    answer='y'
    while answer.upper()=='Y':
        ask=input("what is your name?")
        answer=input('press y to continue...')
#som_1()

def som_2():
    answer='y'
    while answer.lower()=='y':
        ask=input("Salo or banana?")
        answer=input('press y to continue: ')
#som_2()


#                                         ПОИСК И ЗАМЕНА

def endswith():
    text='we love you Arsenal'
    if text.endswith('Arsenal'):
        print('YES')
    else:
        print('no!')
#endswith()

def find():
    text='Carlsberg'
    mod=text.find('berg')
    print(mod)
#find()

def replace():
    text='we love you Arsenal'
    mod=text.replace('Arsenal','Arteta')
    print(mod)
#replace()

def startswith():
    text='We live in Ktamatorsk'
    if text.startswith('We'):
        print("YEAH")
    else:
        print('no...')
#startswith()


#                                  АНАЛИЗ СИМВОЛОВ В ПАРОЛЕ

# В университете пароли для компьютерной системы кампуса должны удовлетворять приведенным
# ниже требованиям:
# + пароль должен иметь как минимум семь символов;
# + должен содержать как минимум одну букву в верхнем регистре;
# + должен содержать как минимум одну букву в нижнем регистре;
# + должен содержать как минимум одну цифру.
# Во время создания студентом своего пароля допустимость пароля должна быть проверена,
# чтобы он гарантированно удовлетворял этим требованиям. Вас попросили написать
# программный код, который выполняет эту проверку. Вы решаете написать функцию
# valid_password, которая принимает пароль в качестве аргумента и возвращает истину либо
# ложь, чтобы указать, является ли он допустимым. Вот алгоритм функции в псевдокоде:
# функция valid_password:
# Назначить переменной correct_length значение false.
# Назначить переменной has_uppercase значение false.
# Назначить переменной has lowercase значение false.
# Назначить переменной has_digit значение false.
# Если пароль имеет длину семь символов или больше:
# Назначить переменной correct_length значение true
# для кЮIЩого символа в пароле:
# если этот символ является буквой в верхнем регистре:
# Назначить переменной has_uppercase значение true.
# если этот символ является буквой в нижнем регистре:
# Назначить переменной has_lowercase значение true.
# если этот символ является цифрой:
# Назначить переменной has_digit значение true.
# Если correct_length и has_uppercase и has_lowercase и has digit:
# Назначить переменной is valid значение true.
# Иначе:
# Назначить переменной is valid значение false.

def main_password():

    get_password=input("Введи пароль: ")
    while not valid_password(get_password):
        print("password is not correct!")
        get_password = input("Введи пароль: ")
    print('password is correct!')


def valid_password(password):
    # назначить булевым перменным значение False
    correct_length=False
    has_uppercase=False
    has_lowercase=False
    has_digit=False

    # приступим к валидации:
    # проверим длину пароля:
    if len(password)>=7:
        correct_length=True
    # проанализировать каждый символ и установить соответсвующий флаг,
    # когда требуемый символ найден.
    for symbol in password:
        if symbol.isupper():
            has_uppercase=True
        if symbol.islower():
            has_lowercase=True
        if symbol.isdigit():
            has_digit=True

    # определить , удовлетворены ли все требования:
    #если это так,то назначить переменной is_valid значение True.
    # если нет,то назначить значение False.
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid=True
    else:
        is_valid=False

    return is_valid

#main_password()

#                                     ОПЕРАТОР ПОВТОРЕНИЯ

def povtor():
    text='x'
    for count in range(10):
        print(count*'x')
    for count in range(9,0,-1):
        print(count*'z')
#povtor()

def povtor_2():
    text="Andrey"
    index=0
    n=1
    while index<len(text):
        print(text[index]*n)
        index+=1
        n+=1
#povtor_2()

#                                   РАЗБИЕНИЕ СТРОКОВОГО ЗНАЧЕНИЯ

def some_75():
    text='one two three four five'
    my_list=text.split()
    print(my_list)
#some_75()

def some0255():
    text='1 2 3 4 5 6 7 8 9 10'
    my_list=text.split()
    print(my_list)
#some0255()

def some89375():
    text='28/06/1989'
    my_list=text.split('/')
    print(my_list)
#some89375()


def some234():
    text='28/06/1989'
    my_list=text.split('/')
    print("День:",my_list[0])
    print("Месяц:",my_list[1])
    print("Год:",my_list[2])
#some234()


# Напишите фрагмент кода с использованием оператора in, который определяет, является
# ли 'd' подстрокой переменной mystring.
def pr_74():
    mystring=input('enter some text: ')
    if 'д' in mystring:
        print(f"'д' являтся подстрокой {mystring}")
    else:
        print(f"'д' не являтся подстрокой {mystring}")
#pr_74()


# Допустим, что переменная Ьig ссылается на строковое значение. Напишите инструкцию,
# которая преобразует строковое значение, на которое она ссылается, в нижний
# регистр и присваивает преобразованный результат переменной little.

def obmen():
    big='I LOVE FOOTBALL'
    small=big.lower()
    print(small)
#obmen()

# Напишите инструкцию, которая выводит сообщение "Цифра", если строковое значение,
# на которое ссылается переменная ch, содержит цифру. В противном случае эта
# инструкция должна показать сообщение "Цифр нет".
def cifra():
    text=(input("enter some text: "))
    if text.isdigit():
        print("Цифра")
    else:
        print("Цифр нет!")
#cifra()


# Напишите цикл, который запрашивает у пользователя "Желаете повторить программу
# или выйти? (П/В)". Цикл должен повторяться до тех пор, пока пользователь не введет
# Пили В (в верхнем или нижнем регистре).
def some87():
    answer='y'
    while answer.upper()=='Y':
        answer=input("Do you wanna repeat?")
#some87()

# Напишите цикл, который подсчитывает количество символов в верхнем регистре,
# появляющихся в строковом значении, на которое ссылается переменная mystring.
def some():
    count=0
    text="AAaa"
    for symbol in text:
        if symbol.isupper():
            count+=1
    print(count)
#some()

def some_6264():
    result=False
    text='iuhfwh1'
    for symbol in text:
        if symbol.isdigit():
            result=True
    if result:
        print("has digit")
    else:
        print('no digit')

    #print(result)
#some_6264()

def some989():
    try:
        text='hfuhfuhweu62378'
        if text.isalnum():
            print(f"Текст ({text}) содержит только цифры и буквы")
        else:
            print(f"Текст ({text}) содержит и другие символы")
    except ValueError as err:
        print(err)
#some989()


def some769():
    try:
        get_text=input("Enter some text: ")
        if get_text.isalnum:
            print("Текст содержит только цифры и буквы")
        elif get_text.isdigit():
            print("Текст содержит только цифры")
        elif get_text.isupper():
            print("Весь текст в верхнем регистре")
        elif get_text.islower():
            print("Весь текст в нижнем регистре")
        elif get_text.isalpha():
            print("Весь текст состоит из букв")
        else:
            print("Текс состоит из пробелов")
    except Exception:
        print(Exception)
#some769()


def pr782():
    try:
        answer='y'
        while answer.upper()=='Y':
            print("Everything will be ok!")
            answer=input("press y or Y to continue: ")
    except ValueError as err:
        print(err)
#pr782()


# Допустим, что в программе имеется приведенная ниже инструкция:
# days = 'Понедельник Вторник Среда'
# Напишите инструкцию, которая разбивает строковое значение, создавая приведенный
# ниже список:
# ['Понедельник', 'Вторник', 'Среда']

def test8():
    try:
        days='Понедельник Вторник Среда'
        my_list=days.split()
        print(my_list)
    except Exception:
        print(Exception)
#test8()

# Допустим, что в программе имеется приведенная ниже инструкция:
# values = 'один$два$три$четыре'
# Напишите инструкцию, которая разбивает строковое значение, создавая приведенный
# ниже список:
# [ ' один ' , 'два ' , ' три' , 'четыре ' ]
def test9():
    try:
        values='один$два$три$четыре'
        new_list=values.split('$')
        print(new_list)
    except Exception:
        print(Exception)
#test9()

def test10():
    try:
        text='one||two||three'
        new_list=text.split("||")
        print(new_list)
    except Exception:
        print(Exception)
#test10()

# Напишите цикл, который подсчитывает количество пробельных символов в строковом
# значении, на которое ссылается mystring.
def test_11():
    try:
        answer="y"
        count=0
        while answer.upper()=='Y':
            get_text=input("text something here: ")
            for every_symbol in get_text:
                if every_symbol.isspace():
                    count+=1

            print(f"Количество пробельных символов в тексте равно: {count}")
            answer = input('press Y or y to continue: ')
    except ValueError as err:
        print(err)
#test_11()


# Напишите цикл, который подсчитывает количество цифр в строковом значении, на которое
# ссылается mystring.
def test12():
    try:
        count=0
        my_string=input("text something here: ")
        for symbol in my_string:
            if symbol.isdigit():
                count+=1
        print(f"Количество цифр в тексте ({my_string}) равно: {count}")
    except ValueError  as err:
        print(err)
#test12()


# Напишите цикл, который подсчитывает количество символов в нижнем регистре в строковом
# значении, на которое ссылается mystring.
def test13():
    try:
        count=0
        my_string=input("text something here: ")
        for symbol in my_string:
            if symbol.islower():
                count+=1
        print(f"Вданном тексте в нижнем регистре содержится такое количество символов: {count}")
    except ValueError as err:
        print(err)
#test13()


# Напишите функцию, которая принимает строковое значение в качестве аргумента и возвращает
# истину, если аргумент заканчивается подстрокой ' . сот'. В противном случае
# функция должна вернуть ложь.

def tesr14(some_string):
    if some_string.endswith(".com"):
        return print("True")
    else:
        return False

def test14_1():
    my_text=input('text something: ')
    tesr14(my_text)
#test14_1()


# Напишите фрагмент кода, делающий копию строкового значения, в котором все вхождения
# буквы 'т' в нижнем регистре преобразованы в верхний регистр.
def test15():
    try:
        text=input("text something: ")
        for every_symbol in text:
            if every_symbol=='t':
                new_text=text.replace('t','T')
        print(new_text)
    except ValueError as err:
        print(err)
#test15()


# Напишите функцию, которая принимает строковое значение в качестве аргумента и показывает
# строковое значение в обратном порядке.
def test16():
    try:
        text=input("text something here: ")
        new_text=text[-1:0:-1]
        print(new_text+text[0])
    except ValueError as err:
        print(err)
#test16()

# Допустим, что переменная mystring ссылается на строковое значение. Напишите инструкцию,
# которая применяет выражение среза и показывает первые 3 символа в строковом
# значении.
def test17():
    try:
        my_string=input("text something: ")
        print(my_string[0:3])
    except ValueError as err:
        print(err)
#test17()

# Допустим, что переменная mystring ссылается на строковое значение. Напишите инструкцию,
# которая применяет выражение среза и показывает последние 3 символа в строковом
# значении.
def test18():
    try:
        my_string=input("text something: ")
        print(my_string[-3:])
    except ValueError as err:
        print(err)
#test18()


# Взгляните на приведенную ниже инструкцию:
# mystring = 'пирожки>молоко>стряпня>яблочный пирог>мороженое'
# Напишите инструкцию, которая разбивает это строковое значение, создавая приведенный
# ниже список:
# ['пирожки', 'молоко', 'стряпня', 'яблочный: пирог', 'мороженое']

def test19():
    try:
        mystring = 'пирожки>молоко>стряпня>яблочный пирог>мороженое'
        new_list=mystring.split(">")
        print(new_list)
    except ValueError as err:
        print(err)
#test19()

# Инициалы. Напишите программу, которая получает строковое значение, содержащее
# имя, отчество и фамилию человека и показывает инициалы. Например, если пользователь
# вводит Михаил Иванович Кузнецов, то программа должна вывести М.И.К.
def task1():
    try:
        get_name=input("Введи фамилию,имя и отчество: ")
        name_list=get_name.split()
        print(name_list[0][0],'.',name_list[1][0],'.',name_list[2][0],'.',sep='')
    except ValueError as err:
        print(err)
    except IndexError as err2:
        print(err2)
#task1()


# Сумма цифр в строке. Напишите программу, которая просит пользователя ввести ряд
# однозначных чисел без разделителей. Программа должна вывести на экран сумму всех
# однозначных чисел в строковом значении. Например, если пользователь вводит 2514, то
# этот метод должен вернуть значение 12, которое является суммой 2, 5, 1 и 4.

def task2():
    try:
        get_digits=input("Введите ряд однозначных чисел: ")
        total=0
        for num in get_digits:
            num=int(num)
            total+=num
        total=str(total)
        print("Сумма всех чисел в числовой строке равна: ",total)
    except ValueError as err:
        print(err)
#task2()


# Принтер дат. Напишите программу, которая считывает от пользователя строковое значение,
# содержащее дату в формате дд/мм/гггг. Она должна напечатать дату в формате
# 12 марта 2018 г.

def task3():
    try:
        get_date=input("Введи дату в формате дд/мм/гггг : ")
        new_list=get_date.split('/')
        print(new_list[0],new_list[1],new_list[2],"г.")
    except ValueError as err:
        print(err)
#task3()


# Конвертер азбуки Морзе. Азбука Морзе представляет собой кодировку, где каждая
# буква алфавита, каждая цифра и различные знаки препинания представлены серией точек
# и тире. В табл. 8.4 и 8.5 показана часть этой азбуки.
# Напишите программу, которая просит пользователя ввести строковое значение и затем
# преобразует это строковое значение в кодировку азбукой Морзе.

def task4():
    try:
        get_string=input("Введи строку: ").upper()
        for symbol in get_string:
            if symbol==' ':
                print(' ',end=' ')
            elif symbol==',':
                print('--..--',end=' ')
            elif symbol=='.':
                print(".-.-.-",end=' ')
            elif symbol=='?':
                print('..--..',end=' ')
            elif symbol=="0":
                print('-----',end=' ')
            elif symbol=="1":
                print('.----',end=' ')
            elif symbol=="2":
                print('..---',end=' ')
            elif symbol=="3":
                print('...--',end=' ')
            elif symbol=="4":
                print('....-',end=' ')
            elif symbol=="5":
                print('.....',end=' ')
            elif symbol=="6":
                print('-....',end=' ')
            elif symbol=="7":
                print('--...',end=' ')
            elif symbol=="8":
                print('---..',end=' ')
            elif symbol=="9":
                print('----.',end=' ')
            elif symbol=="A":
                print('.-',end=' ')
            elif symbol=="B":
                print('-...',end=' ')
            elif symbol=="C":
                print('-.-.',end=' ')
            elif symbol=="D":
                print('-..',end=' ')
            elif symbol=="E":
                print('.',end=' ')
            elif symbol=="F":
                print('..-.',end=' ')
            elif symbol=="G":
                print('--.',end=' ')
            elif symbol=="H":
                print('....',end=' ')
            elif symbol=="I":
                print('..',end=' ')
            elif symbol=="J":
                print('.---',end=' ')
            elif symbol=="K":
                print('-.-',end=' ')
            elif symbol=="L":
                print('.-..',end=' ')
            elif symbol=="M":
                print('--',end=' ')
            elif symbol=="N":
                print('-.',end=' ')
            elif symbol=="O":
                print('---',end=' ')
            elif symbol=="P":
                print('.--.',end=' ')
            elif symbol=="Q":
                print('--.-',end=' ')
            elif symbol=="R":
                print('.-.',end=' ')
            elif symbol=="S":
                print('...',end=' ')
            elif symbol=="T":
                print('-',end=' ')
            elif symbol=="U":
                print('..-',end=' ')
            elif symbol=="V":
                print('...-',end=' ')
            elif symbol=="W":
                print('.--',end=' ')
            elif symbol=="X":
                print('-..-',end=' ')
            elif symbol=="Y":
                print('-.-',end=' ')
            elif symbol=="Z":
                print('--..',end=' ')
            else:
                print("Некорректный символ!")
    except ValueError as err:
        print(err)
#task4()


# Алфавитный переводчик номера телефона. Многие компании используют телефонные
# номера наподобие 555-GET-FOOD, чтобы клиентам было легче запоминать эти номера.
# На стандартном телефоне буквам алфавита поставлены в соответствие числа следующим
# образом:
# А,В иС=2
# D,ЕиF=З
# G, Ни 1=4
# 456 Глава 8. Подробнее о строковых данных
# J, К и L = 5
# М,Nи0=6
# P,Q, Rи S=7
# Т, UиV=8
# W,X, УиZ=9
# Напишите программу, которая просит пользователя ввести 10-символьный номер телефона
# в формате ХХХ-ХХХ-ХХХХ. Приложение должно показать номер телефона, в котором
# все буквенные символы в оригинале переведены в их числовой эквивалент.
# Например, если пользователь вводит 555-GET-FOOD, то приложение должно вывести
# 555-438-3663.
def task5():
    try:
        get_number=input("Введи номер телефона в формате ХХХ-ХХХ-ХХХХ: ").upper()
        for num in get_number:
            if num=='A' or num=='B' or num=='C' or num=='2':
                print('2',sep='',end=' ')
            elif num=='D' or num=='E' or num=='F' or num=='3':
                print('3',sep='',end=' ')
            elif num == 'G' or num == 'H' or num == 'I' or num=='4':
                print('4',sep='', end=' ')
            elif num == 'J' or num == 'K' or num == 'L' or num=='5':
                print('5',sep='', end=' ')
            elif num == 'M' or num == 'N' or num == 'O' or num=='6':
                print('6',sep='', end=' ')
            elif num == 'P' or num == 'Q' or num == 'R' or num == 'S' or num=='7':
                print('7',sep='', end=' ')
            elif num == 'T' or num == 'U' or num == 'V' or num=='8':
                print('8',sep='', end=' ')
            elif num == 'W' or num == 'X' or num == 'Y' or num == 'Z' or num=='9':
                print('9',sep='', end=' ')
            elif num=="-":
                print('-',sep='',end=' ')
            else:
                print("Нет такой цифры!")
    except ValueError as err:
        print(err)
#task5()


# Среднее количество слов. Среди исходного кода главы 8, а также в подпапке data
# "Решений задач по программированию" соответствующей главы вы найдете файл
# text.txt. В нем в каждой строке хранится одно предложение. Напишите программу, которая
# читает содержимое файла и вычисляет среднее количество слов в расчете на предложение.

def task6():
    try:
        file=open(r'D:\Фильмы\text.txt','w')
        for stroka in range(5):
            text=input('Введи предложение для строки: ')
            file.write(str(text)+'\n')
        file.close()
    except ValueError as err:
        print(err)
#task6()


def task6_1():
    try:
        file=open(r'D:\Фильмы\text.txt','r')
        my_list=file.readlines()
        file.close()

        index=0
        while index<len(my_list):
            my_list[index]=my_list[index].rstrip('\n')
            index+=1

        index=0
        count=0
        while index<len(my_list):
            for bukva in my_list[index]:
                count+=1
            index += 1
        mid_in_string=count/len(my_list)
        print("Среднее количество символов в предложении: ",mid_in_string)

    except ValueError as err:
        print(err)
#task6_1()

# Анализ символов. Среди исходного кода главы 8, а также в подпапке data "Решений задач
# по программированию" соответствующей главы вы найдете файл text.txt. Напишите
# программу, которая читает содержимое файла и определяет:
# • количество букв в файле в верхнем регистре;
# • количество букв в файле в нижнем регистре;
# • количество цифр в файле;
# • количество пробельных символов в файле.
def task7():
    try:
        file=open(r'D:\Фильмы\task7.txt','w')
        for stroka in range(3):
            text=input("Введи строку: ")
            file.write(str(text)+'\n')
        file.close()
    except ValueError as err:
        print(err)
#task7()

def task7_1():
    try:
        file=open(r'D:\Фильмы\task7.txt','r')
        text=file.readlines()
        file.close()

        index=0
        while index<len(text):
            text[index]=text[index].rstrip('\n')
            index+=1

        index=0
        count_upper=0
        count_lower=0
        count_digit=0
        count_space=0
        while index<len(text):
            for bukva in text[index]:
                if bukva.isupper():
                    count_upper+=1
                elif bukva.islower():
                    count_lower+=1
                elif bukva.isdigit():
                    count_digit+=1
                else:
                    count_space+=1
            index+=1
        print('Количество букв в верхнем регистре: ',count_upper)
        print('Количество букв в нижнем регистре: ',count_lower)
        print('Количество букв\цифр регистре: ',count_digit)
        print('Количество пробелов: ',count_space)

    except ValueError as err:
        print(err)
#task7_1()

# Корректор предложений. Напишите программу с функцией, принимающей в качестве
# аргумента строковое значение и возвращающей его копию, в котором первый символ
# каждого предложения написан в верхнем регистре. Например, если аргументом является
# "привет! меня зовут джо. а как твое имя?", то эта функция должна вернуть строковое
# значение 'Привет! Меня зовут Джо. А как твое имя?'. Программа должна предоставить
# пользователю возможность ввести строковое значение и затем передать его в функцию.
# Модифицированное строковое значение должно быть выведено на экран.
def main_task8():
    try:
        get_string=input("Напиши предложения: ")
        new_string=change_symbol(get_string)

    except ValueError as err:
        print(err)

def change_symbol(some_text):
    some_list=some_text.split('.')
    for predlojenie in some_list:
        zaglavnaya_bukva = predlojenie[0].upper()
        print(zaglavnaya_bukva, predlojenie[1:],sep='')


#main_task8()


# Гласные и согласные. Напишите программу с функцией, которая в качестве аргумента
# принимает строковое значение и возвращает количество содержащихся в нем гласных.
# Приложение должно иметь еще одну функцию, которая в качестве аргумента принимает
# строковое значение и возвращает количество содержащихся в нем согласных. Приложение
# должно предоставить пользователю возможность ввести строковое значение и показать
# содержащееся в нем количество гласных и согласных.
def task9():
    try:
        get_text=input("Введи текст: ").upper()
        check_glasnie=glasnie(get_text)
        check_soglasnie=soglasnie(get_text)

    except ValueError as err:
        print(err)

def glasnie(some_text):
    count=0
    for bukva in some_text:
        if bukva=='A' or bukva=='E' or bukva=='I' or bukva=='O' or bukva=='Q'or bukva=='U' or bukva=='Y':
            count+=1
    return print('В тексте содержится ',count,"гласных букв")


def soglasnie(some_text):
    count=0
    for bukva in some_text:
        if bukva=='B' or bukva=='C' or bukva=='D'\
                or bukva=='F' or bukva=='G'or bukva=='H'\
                or bukva=='G' or bukva=='K' or bukva=='L'\
                or bukva=='M' or bukva=='N' or bukva=='P'\
                or bukva=='R' or bukva=='S' or bukva=='T'\
                or bukva=='V' or bukva=='W' or bukva=='X' or bukva=='Z':
            count+=1
    return print('В тексте содержится ',count,"согласных букв")

#task9()


# Самый частотный символ. Напишите программу, которая предоставляет пользователю
# возможность ввести строковое значение и выводит на экран символ, который появляется
# в нем наиболее часто.
def task10():
    try:
        get_text=input("Введи строку: ").lower()
        index=0
        count_q=0
        while index<len(get_text):
            if 'q' in get_text:
                count_q+=1
                index+=1
        print(count_q)

    except ValueError as err:
        print(err)
#task10()                                    ЕСТЬ ОЧЕНЬ ДЛИННОЕ РЕШЕНИЕ!

# Разделитель слов. Напишите программу, которая на входе принимает предложение,
# в котором все слова написаны без пробелов, но первая буква каждого слова находится
# в верхнем регистре. Преобразуйте предложение в строковое значение, в котором слова
# отделены пробелами, и только первое слово начинается с буквы в верхнем регистре. Например,
# строковое значение "ОстановисьИПочувствуйЗапахРоз" будет преобразовано
# в "Остановись и почувствуй запах роз".
def task11():
    try:
        text='ОстановисьИПочувствуйЗапахРоз'
        new_text=text.replace("ОстановисьИПочувствуйЗапахРоз","Остановись и почувствуй запах роз")
        print(new_text)
    except ValueError as err:
        print(err)
#task11()
import re
def task11_1():
    try:
        text = input("Введи любой текс без пробелов с заглавными буквами слов: ")
        new_text=re.findall(r'[А-Я]?[^А-Я]*',text)

        index=1
        while index<len(new_text):
            new_text[index]=new_text[index].lower()
            index+=1

        for word in new_text:
            print(word,end=" ")

    except ValueError as err:
        print(err)
#task11_1()



# Самый частотный символ. Напишите программу, которая предоставляет пользователю
# возможность ввести строковое значение и выводит на экран символ, который появляется
# в нем наиболее часто.

from collections import Counter
def task10_3():
    text=input("Введи текст: ")
    print(Counter(text).most_common(1).pop(0)[0])
#task10_3()


# Молодежный жаргон. Напишите программу, которая на входе принимает предложение
# и преобразует каждое его слово в "молодежный жаргон" . В одной из его версий во время
# преобразования слова в молодежный жаргон первая буква удаляется и ставится в конец
# слова. Затем в конец слова добавляется слог "ки". Вот пример.
# Русский язык: ПРОСПАЛ ПОЧТИ ВСЮ НОЧЬ
# Молодежный жаргон: РОСПАЛПКИ ОЧТИПКИ СЮВКИ ОЧЬНКИ

def task12():
    try:
        get_text=input("Введи любове предложение: ")
        new_list=get_text.split()

        index=0
        copy_list=[]
        while index<len(new_list):
            pervaja_bukva=new_list[index][:1]
            copy_list.append(new_list[index][1:]+pervaja_bukva+'ки')
            index+=1
        print(copy_list)

    except ValueError as err:
        print(err)

#task12()


# создадим файл с лотерейными номерами
import random
def make_lotery():
    try:
        file=open(r'D:\Фильмы\лотерея.txt','w')
        for ticket in range(655):

            for chisla in range(5):
                stroka_chisel=random.randint(10,69)
                file.write(str(stroka_chisel)+' ')
            power_ball = random.randint(1, 26)
            file.write(str(power_ball)+'\n')

        file.close()
    except ValueError as err:
        print(err)

#make_lotery()

# Напишите одну или несколько программ, которые работают с этим файлом и показывают:
# • 1О наиболее распространенных чисел , упорядоченных по частоте;
# • 1О наименее распространенных чисел, упорядоченных по частоте;
# • частоту каждого числа от 1 до 69 и частоту каждого PowerBall числа от 1 до 26.
from collections import Counter
def task13():
    try:
        file=open(r'D:\Фильмы\лотерея.txt','r')
        lotery_list=file.readlines()
        file.close()

        index=0
        while index<len(lotery_list):
            lotery_list[index]=lotery_list[index].rstrip('\n')
            index+=1
        print(lotery_list)

        my_string=' '.join(lotery_list)
        print(my_string)

        print(Counter(my_string).most_common(10))





    except IndexError as err2:
        print(err2)
    except IOError as err3:
        print(err3)

#task13()

def some74187():
    my_list=['11 20 30','11 40 50','11 60 70','11 20 90']
    print(my_list)
    my_string=' '.join(my_list)
    print(my_string)
    print(Counter(my_string).most_common(3))
#some74187()



