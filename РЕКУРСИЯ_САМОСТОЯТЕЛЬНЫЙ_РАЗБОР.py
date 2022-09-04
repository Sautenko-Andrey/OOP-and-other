def main_1():
    chislo=int(input('Введи число: '))
    rec_1(chislo)

def rec_1(num):
    if num>0:
        rec_1(num-1)
        print(num)
#main_1()


def main_2():
    # чтобы от заданного числа печаталось заданное количество чисел
    digit=int(input('Введи число "от": '))
    max_digit=int(input('введи число "до": '))

    rec_2(digit,max_digit)

def rec_2(num,roof):
    if num<=roof:
        print(num)
        rec_2(num+1,roof)

#main_2()

def main_3():
    'Чтобы считало сумму чисел в списке'
    my_list=[1,2,3,4]
    print('Сумма чисел в списке равна: ',rec_3(my_list))

def rec_3(some_list):
    if len(some_list)==1:
        return some_list[0]
    else:
        return some_list[0]+rec_3(some_list[1:])

#main_3()

def main_4():
    text='aa(bb(((ccc((((dddd(((((popa'
    new_text=rec_4(text)
    change_text=new_text.replace('(',')')
    print(text+change_text)


def rec_4(some_text):
    if len(some_text)==1:
        return some_text[0]
    else:
        return some_text[-1]+rec_4(some_text[0:-1])

#main_4()


def main_5():
    num1=7
    num2=4

    print(rec_5(num1,num2))

def rec_5(x,y):
    if y==x*y:
        return y
    else:
        return y+rec_5(x-1,y)


#main_5()


def main_6():
    stars=int(input('Введи максимальное количество звездочек для основания: '))
    rec_6(stars)

def rec_6(symbols):
    if symbols!=0:
        rec_6(symbols-1)
        print('*' * symbols)

#main_6()

def main_7():
    my_list=[1,3,55,6,7]
    print(rec_7(my_list))

def rec_7(some_list):
    if len(some_list)>1:
        # получим максимум из следующих рекурсивных вызовов
        max_digit=rec_7(some_list[1:])

        # сравним максимум с первым элементом списка
        if some_list[0]<max_digit:
            print('-----------')
            print('первый элемент',some_list[0])
            print("макс",max_digit)
            print('-----------')
            return max_digit
        else:
            return some_list[0]

    if len(some_list)==1:
        return some_list[0]

#main_7()

def main_8():
    my_list=[1,2,3,4,22,3424,34543]
    print('Сумма всех чисел в списке равна: ',rec_8(my_list))

def rec_8(some_list):
    if len(some_list)==1:
        return some_list[0]
    else:
        return some_list[0]+rec_8(some_list[1:])

#main_8()

def main_9():
    chislo=int(input('Введи любое число: '))
    while chislo<=0:
        chislo = int(input('Введи положительное число: '))
    print(f'Сумма чисел от 1 до {chislo} равна:',sum_chisel(chislo))

def sum_chisel(num):
    if num==1:
        return 1
    else:
        return num+sum_chisel(num-1)

#main_9()

def main_10():
    chislo=3
    stepen=3
    print(vozved_stepen(chislo,stepen))

def vozved_stepen(digit,degree):
    if degree==0:
        return 1
    elif degree%2==0:
        return vozved_stepen(digit,degree//2)*vozved_stepen(digit,degree//2)
    else:
        return vozved_stepen(digit,degree-1)*digit

#main_10()

