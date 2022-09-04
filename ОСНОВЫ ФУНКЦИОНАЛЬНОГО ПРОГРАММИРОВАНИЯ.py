#                  ОПЕРАТОР LAMBDA, ФУНКЦИИ MAP,FILTER, REDUCE И ДР.
# Помимо стандартного определения функции, которое состоит из заголовка функции с ключевым
# словом def и блока инструкций, в Python имеется возможность создавать короткие
# однострочные функции с использованием оператора lamЬda, которые называются ля.нбдафункциями.
# Вот общий формат определения лямбда-функции:
# lamЬda список_аргументов; выражение
# В данном формате список_аргументов- это список аргументов, отделенных запятой,
# выражение - значение либо любая порция программного кода, которая в результате дает
# значение.

# Например, следующие два определения функций эквивалентны:
#def standart_function(x,y):
    #return x+y

lambda_function=lambda x,y:x+y
lambda_function(5,7)
func=lambda_function
func(3,4)

#                                   Функция MAP
seq=(1,2,3,4,5)
seq2=(6,7,8,9,10)
result=map(lambda_function,seq,seq2)
#print(list(result))

lambda_function_2=lambda x,y:x/y*100
list1=[10,10,10,10,10]
list2=[2,2,2,2,2]
result=map(lambda_function_2,list1,list2)
#print(list(result))

#посчитаем процент от числа
procent=lambda x,y:x/y*100
digit1=(16,77,456,785)
digit2=(34,120,500,999)
result=map(procent,digit1,digit2)
#print(list(result))


#                                   ФУНКЦИЯ FILTER

chetnost=lambda x:x%2==0
digits=(1,2,3,4,5,6,7,8,9,10)
filtered=filter(chetnost,digits)
#print(list(filtered))

polojitelno=lambda x:x>0
digits=[864,848,68,168,1,847,3,-5,-8,-659,-94,0]
filtered=filter(polojitelno,digits)
#print(list(filtered))

func=lambda x,y:x+y
text1='andrey'
text2='sautenko'
result=map(func,text1,text2)
#print(list(result))

func=lambda x:10<x<100
some_list=[325,23,535,457,457,457,35,25,36,68,858658,5865,46,7]
filtered=filter(func,some_list)
#print(list(filtered))

some_list=(1,2,3,4,5,6,7,8,10)
result=filter(lambda x:x%2!=0,some_list)
#print(next(result))

#                               ФУНКЦИЯ REDUCE

#           !!!!! посмотреть в другом источнике,т.к в книге совсем непонятно



#                                 ФУНКЦИЯ ZIP

x='abc'
y='def'
zipped=zip(x,y)
#print(list(zipped))

text1='ade'
text2='nry'
zipped=zip(text1,text2)
#print(list(zipped))
x2,y2=zip(*zip(text1,text2))
#print(list(x2))
#print(list(y2))


#                                   ФУНКЦИЯ ENUMERATE

list3='Andrey Sautenko'
lazy=enumerate(list3)
#print(list(lazy))



#                             ВКЛЮЧЕНИЕ В ПОСЛЕДОВАТЕЛЬНОСТЬ
# возведение в квадрат
spisok=[1,2,3,4,5,6,7,8,9]
kvadrat=[x*x for x in spisok]
#print(list(kvadrat))

text='Sautenko Andrey'
result=[x+x for x in text]
#print(str(result))

some=[1,2,3,4,5,6,7,8,9]
result=[x/2 for x in some]
#print(list(result))

dic={'Chaus':'1','Andrey':'2'}
result={x:x+'1' for x in dic}
#print(dict(result))

list_1=[1,2,3,4,5,6,7,8,9,10]
list_2=[11,12,13,14,15,16,17,18,19,20]
list_3=[999,111]
summa=[x+y+z for x,y,z in zip(list_1,list_2,list_3)]
#print(list(summa))

func=lambda x:x%2==0
my_list=[1,2,3,4,5,6,7,8,9,10]
result=[x for x in my_list if func(x)]
#print(list(result))


#                             ЗАМЫКАНИЕ
def func1(x):
    def func2(y):
        return x+y
    return func2

sum_three=func1(3)
#print(sum_three)
sum_three(1)

adder=lambda x:lambda y: x+y
sum_three=adder(3)
#print(sum_three)
#print(sum_three(1))

#степень
def vozv_stepen(stepen):
    return lambda chislo:pow(chislo,stepen)

result=vozv_stepen(2)
#print(result(7))

def main1():
    counter=0
    def calc_sum(i):
        nonlocal counter
        counter+=i
        return counter
    return calc_sum

my_counter=main1()
##print(my_counter(5))
#print(my_counter(7))
#print(my_counter(13))


#                ФУНКЦИОНАЛЬНОЕ ЯДРО ПРОГРАММЫ НА ОСНОВЕ КОНВЕЙЕРА

# конвеер обработки данных
# Функциональная реализация вычисления факториала числа

def conveer_func(digit,*func):
    for every_func in func:
        digit=every_func(digit)
    return digit

#print(conveer_func(5,
             #lambda x:x**2,
             #lambda x:100-x,
             #lambda x:x+25,
             #lambda x:str(x)))


def functional_conveer(digit,*function):
    for each_func in function:
        digit=each_func(digit)
    return digit

#print(functional_conveer(10,
                         #lambda i:i-1,
                         #lambda i:i-2,
                         #lambda i:i-3,
                         #lambda i:str(i)))










