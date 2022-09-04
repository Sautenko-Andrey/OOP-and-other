# binary search
#
# def binary_search(massive, num):
#     low = 0
#     high = len(massive) - 1
#
#     while low <= high:
#
#         middle_index = (low + high) // 2
#         programm_guess = massive[middle_index]
#
#         if programm_guess == num:
#             return f'Index for your digit {num} is <{middle_index}>.'
#
#         if programm_guess > num:
#             high = middle_index - 1
#
#         elif programm_guess < num:
#             low = middle_index + 1
#
#     return f'There is no digit <{num}> in your massive {massive}'
#
#
# mass = [1, 4, 7, 11, 56, 89, 100]
#
#
# # quick sort
#
# def quick_sort(massive):
#     if len(massive) < 2:
#         return massive
#
#     basic_index = len(massive) // 2
#     basic_element = massive[basic_index]
#
#     less = [x for x in massive[:basic_index] if x < basic_element] + [x for x in massive[basic_index + 1:] if
#                                                                       x < basic_element]
#
#     high = [x for x in massive[:basic_index] if x > basic_element] + [x for x in massive[basic_index + 1:] if
#                                                                       x > basic_element]
#
#     return quick_sort(less) + [basic_element] + quick_sort(high)
#
#
# our_list = [5, 3, 7, 8, 0, 13, -11, 4, 77, 90, 1000, 55]
#
# # breadth-first search
#
# friends = {}
#
# friends['Andrey'] = ['Danil', 'Radik', 'Alex', 'Chaus']
# friends['Danil'] = ['Andrey', 'Ivan', 'Shoker', 'Anna']
# friends['Radik'] = ['Nastya']
# friends['Nastya'] = ['Radik']
# friends['Alex'] = []
# friends['Chaus'] = []
# friends['Ivan'] = []
# friends['Shoker'] = []
# friends['Anna'] = []
# from collections import deque
#
#
# def check_name(name):
#     return len(name) == 6 and name[-2:] == 'ya'
#
#
# def breadth_first_search(collection, name):
#     ochered = deque()
#     ochered += collection[name]
#     proshli_proverky = []
#     while ochered:
#         first_in_ochered = ochered.popleft()
#         if not first_in_ochered in proshli_proverky:
#             if check_name(first_in_ochered):
#                 return f"We have found him! This is <{first_in_ochered}>!"
#             else:
#                 proshli_proverky.append(first_in_ochered)
#                 ochered += collection[first_in_ochered]
#
#     return 'There is no name for your parameters!'
#
#
# res = breadth_first_search(friends, 'Andrey')
#
# lst = [5, -3, 10, 7, 13, 0]
#
#
# def sort_puzir(massive):
#     # определяем количество элементов в массиве
#     col_elements = len(massive)
#
#     # определяем число итераций. мы должны сделать col_elements-1 итераций,чтобы полностью отсортировать массив
#     for iteration in range(0, col_elements - 1):
#         # на каждой итерации мы проходим по парам , которые еще не отсортировали
#         for j in range(0,
#                        col_elements - 1 - iteration):  # когда i=0,мы переберем все пары, а когда i увеличится на 1, мы переберем все пары кроме последнего эл-та,потому что он уже максимален
#             # и накаждом проходе мы для каждой пары проверяемтакое условие
#             if massive[j] > massive[j + 1]:
#                 # если послежующий эл-т j+1 меньше предыдущего j,то мы их меняем местами
#                 massive[j], massive[j + 1] = massive[j + 1], massive[j]
#     print(massive)
#
#
# def vpliv_puzirka(spisok):
#     # определеяем количество элементов в списке
#     count_elements = len(spisok)
#
#     # определеям сколько нам нужно пройти итераций,чтобы отсортировать список
#     col_iteration = count_elements - 1
#
#     # для каждой итерации
#     for iteration in range(0, count_elements):
#         # мы будем для каждой пары чисел,кроме последнего
#         for dig in range(0, col_iteration - iteration):
#             # делать сравнение
#             if spisok[dig] > spisok[dig + 1]:
#                 # тогда мы меняем их местами
#                 spisok[dig], spisok[dig + 1] = spisok[dig + 1], spisok[dig]
#
#     print(spisok)
#
#
# def my_binary_algorithm(massive, dig):
#     low = 0
#     high = len(massive) - 1
#
#     while low <= high:
#         middle_index = (low + high) // 2
#         guess_dig = massive[middle_index]
#
#         if dig == guess_dig:
#             return f'We\'ve found this digit, it\'s index=<{middle_index}>'
#         if guess_dig > dig:
#             high = middle_index - 1
#         elif guess_dig < dig:
#             low = middle_index + 1
#     return f'There is not digit which you are looking for!'
#
#
# def my_quick_sort_algorithm(spisok):
#     if len(spisok) < 2:
#         return spisok
#
#     basic_index = len(spisok) // 2
#     base = spisok[basic_index]
#
#     low_digs = [x for x in spisok[:basic_index] if x < base] + [x for x in spisok[basic_index + 1:] if x < base]
#     high_digs = [x for x in spisok[:basic_index] if x > base] + [x for x in spisok[basic_index + 1:] if x > base]
#
#     return my_quick_sort_algorithm(low_digs) + [base] + my_quick_sort_algorithm(high_digs)
#
#
# # spisok=[4,-1,100,34,6,-45,0,77,1017]
# # result=my_quick_sort_algorithm(spisok)
# # print(spisok)
# # print(result)
#
#
# employers = {}
# employers['CEO'] = ['CTO', 'CFO']
# employers['CTO'] = ['TEAM_LEAD', 'PRODUCT_MANAGER']
# employers['CFO'] = ['HEAD_ACCOUNTANT']
# employers['TEAM_LEAD'] = ['developers']
# employers['PRODUCT_MANAGER'] = ['sallers']
# employers['developers'] = []
# employers['sallers'] = []
#
#
# def search_sallers(position):
#     return position == 'sallers'
#
#
# from _collections import deque
#
#
# def breadth_first_search(dic, position):
#     ochered = deque()
#
#     ochered += dic[position]
#     proverennie = []
#
#     while ochered:
#
#         dude = ochered.popleft()
#         if not dude in proverennie:
#             if search_sallers(dude):
#                 return 'We have found sallers!'
#             else:
#                 proverennie.append(dude)
#                 ochered += dic[dude]
#
#     return 'No sallers here!'
#
#
# def puzir(spisok):
#     # определяем кл=оличество элементов в списке
#     colichestvo_elementov = len(spisok)
#
#     # определяем количество итераций для этого списка
#     col_iter = colichestvo_elementov - 1
#
#     # для каждой итерации
#     for iteration in range(0, col_iter):
#         # для каждого числа,кроме последнего
#         for dig in range(0, col_iter - iteration):
#             # проверяем
#             if spisok[dig] > spisok[dig + 1]:
#                 spisok[dig], spisok[dig + 1] = spisok[dig + 1], spisok[dig]
#
#     print(spisok)
#
#
# # binary search
# def b_s(some_list, number):
#     first_index = 0
#     last_index = len(some_list) - 1
#
#     while first_index <= last_index:
#         middle_index = (first_index + last_index) // 2
#         programm_guess = some_list[middle_index]
#
#         if programm_guess == number:
#             return f'Index for {number} in this list is {middle_index}'
#
#         elif programm_guess > number:
#             last_index = middle_index - 1
#
#         elif programm_guess < number:
#             first_index = middle_index + 1
#
#     return f'There is no number <{number}> in list.'
#
#
# ls = [1, 5, 7, 9, 10, 15]
#
#
# # quick sort
# def q_s(array):
#     if len(array) < 2:
#         return array
#
#     base_index = len(array) // 2
#     base_item = array[base_index]
#
#     low = [x for x in array[:base_index] if x < base_item] + [x for x in array[base_index + 1:] if x < base_item]
#     high = [x for x in array[:base_index] if x > base_item] + [x for x in array[base_index + 1:] if x > base_item]
#
#     return q_s(low) + [base_item] + q_s(high)
#
#
# l1 = [1, 78, 12, 4, 5, 100, -77, 34, -9]
#
# friends = {}
#
# friends['Andrey'] = ['Danil', 'Radik', 'Alex', 'Chaus']
# friends['Danil'] = ['Andrey', 'Ivan', 'Shoker', 'Anna']
# friends['Radik'] = ['Nastya']
# friends['Nastya'] = ['Radik']
# friends['Alex'] = []
# friends['Chaus'] = []
# friends['Ivan'] = []
# friends['Shoker'] = []
# friends['Anna'] = []
# from collections import deque
#
#
# def find_reverse_name(name):
#     name = name.lower()
#     if name[:2] == name[-2:]:
#         return name
#
#
# def BFS(dic, friend):
#     if find_reverse_name(friend):
#         return f'Here we are! its {friend}!'
#
#     ochered = deque()
#     ochered += dic[friend]
#     verifyed = []
#
#     while ochered:
#         individual = ochered.popleft()
#         if not individual in verifyed:
#             if find_reverse_name(individual):
#                 return f'Thats it! its a {individual}!'
#             else:
#                 verifyed.append(individual)
#                 ochered += dic[individual]
#
#     return f'sorry, there is no person with that name.'
#
#
# def puzzir(masssiv):
#     col_elements = len(masssiv)
#     col_iteration = col_elements - 1
#
#     for iteration in range(0, col_iteration):
#         for element in range(0, col_iteration - iteration):
#             if masssiv[element] > masssiv[element + 1]:
#                 masssiv[element], masssiv[element + 1] = masssiv[element + 1], masssiv[element]
#
#     print(masssiv)
#
#
# def shampaine(spisok):
#     count_elements_in_spisok = len(spisok)
#     count_iterations = count_elements_in_spisok - 1
#
#     for itetation in range(0, count_iterations):
#         for digit in range(0, count_iterations - iteration):
#             if spisok[digit] > spisok[digit + 1]:
#                 spisok[digit], spisok[digit + 1] = spisok[digit + 1], spisok[digit]
#
#     print(spisok)
#
#
# # метод слияния списков
#
#
# def merge_sort(first_list, second_list):
#     if not isinstance(first_list, list) and not isinstance(second_list, list):
#         raise TypeError('Attributes must be lists!')
#
#     final_list = []
#
#     length_first_list = len(first_list)
#     length_second_list = len(second_list)
#
#     counter_1_list = 0
#     counter_2_list = 0
#
#     # делаем цикл пока мы не дойдем до конца первого и второго списка
#     while length_first_list > counter_1_list and length_second_list > counter_2_list:
#         # далее делаем проверку
#         if first_list[counter_1_list] <= second_list[counter_2_list]:
#             final_list.append(first_list[counter_1_list])
#             counter_1_list += 1
#
#         else:
#             final_list.append(second_list[counter_2_list])
#             counter_2_list += 1
#
#     final_list += first_list[counter_1_list:] + second_list[counter_2_list:]
#
#     print(final_list)
#
#
# def bubble_sort(massive):
#     if type(massive) != list:
#         raise TypeError('Attribut has to be list!')
#     elements_in_massive = len(massive)
#     need_iterations = elements_in_massive - 1
#
#     for every_iteration in range(0, need_iterations):
#         for digit in range(0, need_iterations - every_iteration):
#             if massive[digit] > massive[digit + 1]:
#                 massive[digit], massive[digit + 1] = massive[digit + 1], massive[digit]
#
#     print(massive)
#
#
# mas = [4, 5, 6, 2, 44, 0, -1, 56]
#
#
# def mY_merge_sort(list1, list2):
#     total_list = []
#
#     arrow_1 = 0
#     arrow_2 = 0
#
#     len_1 = len(list1)
#     len_2 = len(list2)
#
#     while len_1 > arrow_1 and len_2 > arrow_2:
#         if list1[arrow_1] < list2[arrow_2]:
#             total_list.append(list1[arrow_1])
#             arrow_1 += 1
#
#         else:
#             total_list.append(list2[arrow_2])
#             arrow_2 += 1
#
#     print(total_list)
#
#
# class Sneaker:
#
#     def __new__(cls, *args, **kwargs):
#         print(f'Creating new instance of a class {cls}')
#         return super().__new__(cls)
#
#     def __str__(self):
#         return f'{self.__brand} {self.__model} of a class {self.__class__}'
#
#     def __getattribute__(self, item):
#         if item=='provider':
#             raise AttributeError('you cant read it')
#         else:
#             return object.__getattribute__(self,item)
#
#     def __setattr__(self, key, value):
#         if key=='IBAN':
#             raise AttributeError('forbidden attribute')
#         else:
#             object.__setattr__(self,key,value)
#
#     def __getattr__(self, item):
#         print(f'There is not attribute with name {item}')
#
#     def __delattr__(self, item):
#         print(f'Attribute {item} is delited!')
#         object.__delattr__(self,item)
#
#
#
#     ALLOWED_BRANDS = ('Nike', 'Under Armour', 'Puma', 'Asics')
#
#     @classmethod
#     def __verify_brand(cls, brand):
#         if not brand in cls.ALLOWED_BRANDS:
#             raise AttributeError('Unknown brand, sorry!')
#
#     @classmethod
#     def __check_model(cls, model):
#         if type(model) != str:
#             raise TypeError('Name of model has to be string!')
#
#     def __init__(self, brand, model):
#         self.__verify_brand(brand)
#         self.__check_model(model)
#         self.__brand = brand
#         self.__model = model
#
#     @property
#     def brand(self):
#         return self.__brand
#
#     @brand.setter
#     def brand(self, brand):
#         self.__brand = brand
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         self.__model = model
#
#     @staticmethod
#     def show_all_our_brands():
#         print('We are working with four brands:\n\tNike\nUnder Armour\nPuma\nAsics')
#
# class RunningShoes(Sneaker):
#
#     ROAD_TYPES=('asphalt','ground')
#
#     @classmethod
#     def __check_road(cls,road):
#         if not road in cls.ROAD_TYPES:
#             raise AttributeError('You can choose \\asphalt\\ or \\ground\\')
#
#     def __init__(self,brand,model,road):
#         self.__check_road(road)
#         super().__init__(brand,model)
#         self.road=road
#
#     def get_info_road(self):
#         print(f'Sneacker\'s config information:\n\troad type----{self.road}')
#
# class ShoesRetailPrice(Sneaker):
#     def __init__(self,brand,model,price):
#         super().__init__(brand,model)
#         self.price=price
#
#
#     def get_info_road(self):
#         print(f'Price of model is {self.price}')
#
#
#
# def slyanie_spiskov(spisok_1,spisok_2):
#
#     dlina_spiska_1=len(spisok_1)
#     dlina_spiska_2=len(spisok_2)
#
#     mutual_list=[]
#
#     ukazatel_1=0
#     ukazatel_2=0
#
#     while dlina_spiska_1>ukazatel_1 and dlina_spiska_2>ukazatel_2:
#         if spisok_1[ukazatel_1]< spisok_2[ukazatel_2]:
#             mutual_list.append(spisok_1[ukazatel_1])
#             ukazatel_1+=1
#
#         else:
#             mutual_list.append(spisok_2[ukazatel_2])
#             ukazatel_2+=1
#
#     mutual_list+=spisok_1[ukazatel_1:]+spisok_2[ukazatel_2:]
#
# # lst=[1,2,3,4,5]
# # res=list(map(lambda x:x+1,lst))
# #
# # print(abs(-2))
# # print(min(4,5))
# # print(max(8,10))
# # print(pow(2,5))
# # print(round(99.99))
#
# from math import ceil,floor,log,factorial,sqrt,cos,sin,trunc,pi,e

# print('My name is Andrey.','I am goung to live in Germany',sep=' | ',end=' ')
# print('Coz i am exhausted of war.')
#
# # x,y=map(int, input('choose numbers: ').split())
#
# print(bool(0),bool(1))
#
# text='I am Python-developer'
# # print(text+'.')
# # print('Py' in text)
# # print(text*2)
# # print(str(123))
# # print(ord('8'))
#
# print(text[text.index('P'):text.index('-')])
#
# #1 upper
# print(text.upper())
#
# #2lower
# print(text.lower())
#
# #3 index
# print(text.index('P'))
#
# #4 find
# print(text.find('n'))
#
# #5 rfind
# print(text.rfind('o'))
#
# #6 rjust
# print(text.rjust(30,'*'))
#
# #7 ljust
# print(text.ljust(30,'*'))
#
# #8 strip
# print(text.strip())
#
# #9 rstrip
# print(text.rstrip())
#
# #10 lstrip
# print(text.lstrip())
#
# #11 count
# print(text.count('s'))
#
# #12 isdigit
# print(text.isdigit())
#
# #13 isalpha
# print(text.isalpha())
#
# #14 replace
# print(text.replace('n','N'))
#
# #15 join
# print('+'.join(text))
#
# #16 split
# print(text.split())

# array=[1,2,3,4,5,6,7]
# print(len(array))
# print(max(array))
# # print(min(array))
# # print(sorted(array))
# # print(sum(array))
# print(array+[8,9])
# print(3 in array)
# print(array*2)
#
# #1 append
# array.append(0)
# print(array)
#
# #2 insert
# array.insert(3,90)
# print(array)
#
# #3 pop
# array.pop()
# print(array)
#
# #4 remove
# array.remove(90)
# print(array)
#
# #5 copy
# a=array.copy()
# print(a)
#
# #6 clear
# a.clear()
# print(a)
#
# #7 index
# print(array.index(4))
#
# #8 reverse
# array.reverse()
# print(array)
#
# #9sort
# array.sort()
# print(array)
#
# #10 count
# print(array.count(5))
#
# print('yes' if True else 'no')
#
# #break
# lst=set()
# i=0
# while True:
#     lst.add(i)
#     i+=1
#     print(lst)
#     if len(lst)>=10:
#         break
# #continue
# lst=set()
# i=0
# while True:
#
#     i+=1
#     if i%2!=0:
#         continue
#     lst.add(i)
#     print(lst)
#     if len(lst)>=10:
#         break
#
# x=0
# i=0
# while x<10:
#     x+=i
#     i+=1
#     print(x)
#
# else:
#     print('loop while is over')

# factorial
# def get_factorial(dig):
#     base=1
#     for i in range(1,dig+1):
#         base*=i
# #     print(base)
# #
# #
# # res=get_factorial(5)
#
# #elka
#
# # def elochka(layer):
# #     for i in range(layer+1):
# #         print('*'*i)
# #
# # res=elochka(5)
#
# array=[1,4,55,6,8,90,13,1,2,66,-66,-9]
# # def change_2dig(massive):
# #     for i in range(len(massive)):
# #         if abs(massive[i])>=10 or abs(massive[i])>99:
# # #             massive[i]=0
# # #
# # #     print(massive)
# # #
# # # res=change_2dig(array)
# # #
# # # def list_changer(array):
# # #     for index,value in enumerate(array):
# # #         if abs(value)>=10 or abs(value)>99:
# # #             array[index]=0
# # #     print(array)
# # #
# # # res=list_changer(array)
# #
# # array=[[1,4,55,6,8],[90,13,1,2,66],[-66,-9]]
# # for box in array:
# #     for dig in box:
# #         print(dig, end=' ')
# #     print()
# #
# # generator=[x for x in range(11) if x%2==0]
# # print(generator)
# #
# # array=[[1,4,55,6,8],[90,13,1,2,66],[-66,-9]]
# # print([[x**2 for x in row]for row in array])
# # print(
# #     [
# #         x**2
# #         for box in array
# #         for x in box
# #     ]
# # )
# #
# # #dicts
# # dic={'name':'Andrey','secondname':'Sautenko'}
# # #1 fromkeys
# # l=[1,2,3,4,5]
# # res=dict.fromkeys(l,'***')
# # print(res)
# #
# # #2 copy
# # cop=dic.copy()
# # print(cop)
# #
# # #3clear
# # cop.clear()
# # print(cop)
# #
# # #4 get
# # print(dic.get('name'))
# #
# # #5 setdefault
# # dic.setdefault('job','Python developer')
# # print(dic)
# #
# # #6 keys
# # print(dic.keys())
# #
# # #7 values
# # print(dic.values())
# #
# # #8 items
# # print(dic.items())
# #
# # #9 pop
# # dic.pop('job')
# # print(dic)
# #
# # #10 popitem
# # dic.popitem()
# # print(dic)
# #
# #
# # #11 update
# # a={'a':100,'b':200}
# # b={'a':199,'ccc':1000}
# # a.update(b)
# # print(a)
# #
# # #12 unpacking
# # res={**a,**b}
# # print(res)
#
#
# # my_set=set([1,2,3,4,5])
# # print(my_set)
# # my_set={1,2,3,4,5,6,7}
# # print(my_set)
# #
# # #1 add
# # my_set.add(999)
# # print(my_set)
# #
# # #2 update
# # my_set.update([9,44,77])
# # print(my_set)
# #
# # #3 discard
# # my_set.discard(44)
# # print(my_set)
# #
# # #4 remove
# # my_set.remove(999)
# # print(my_set)
# #
# # #5 pop
# # my_set.pop()
# # print(my_set)
# #
# # #6 clear
# # my_set.clear()
# # print(my_set)
# #
# # #1 &
# # a={1,2,3,4,5}
# # b={4,5,6,7,8}
# # res=(a&b)
# # print(res)
# #
# # #2 ^
# # print(a^b)
# #
# # #3 |
# # print(a|b)
# #
# # #4 -
# # print(a-b)
# #
# # l=[1,2,3,'4',5,'6',7,8,9,10]
# # res={int(x) for x in l}
# # print(res)
# #
# # dic={'name':'Andrey','secondname':'Sautenko'}
# # result={values.lower():keys.upper() for keys, values in dic.items()}
# # print(result)
# #
# # #замыкания
# # def get_name(name):
# #     def name_changer():
# #         print(name.upper())
# #     return name_changer
# #
# # res=get_name('Andrey')
# # res()
#
# # decorators
# # def decorator(some_func):
# #     def wrapper(*args,**kwargs):
# #         print('We do something before main function...')
# #         res=some_func(*args,**kwargs)
# #         print('We do something after main function...!')
# #         return res
# #     return wrapper
# # @decorator
# # def print_name(name):
# #     print(name)
# #
# #
# # res=print_name('Andrey')
#
# # def bills_calculator(gaz=1000,svet=500,voda=150):
# #     def decorator(some_func):
# #         def wrapper(x,*args,**kwargs):
# #             res=some_func(x+gaz+svet+voda)
# #             return res
# #         return wrapper
# #     return decorator
# #
# # @bills_calculator()
# # def get_arenda(money):
# #     return money
# #
# # res=get_arenda(1000)
# # print(res)
#
# class Film:
#     GENRE = ('comedy', 'scary', 'drama', 'action', 'fantasy')
#
#     @classmethod
#     def __check_genre(cls, genre):
#         if not genre in cls.GENRE:
#             raise AttributeError('We can\'t identify folm\'s genre!Try again!')
#
#     def __getattribute__(self, item):
#         if item == 'destributor':
#             raise ValueError('You can\'t reaf this attriburte')
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if str(key[0]) == 'A':
#             raise AttributeError('You can\'t set up this attribute!')
#         else:
#             object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         print('There is not attribute you wanna get!')
#
#     def __delattr__(self, item):
#         print(f'Attribute {item} is deleted!')
#         object.__delattr__(self, item)
#
#     def __new__(cls, *args, **kwargs):
#         print('Creating new film!')
#         return super().__new__(cls)
#
#     def __init__(self, film_name, genre, duration):
#         self.__check_genre(genre)
#         self.__film_name = film_name
#         self.__genre = genre
#         self.__duration = duration
#
#     @property
#     def film_name(self):
#         return self.__film_name
#
#     @film_name.setter
#     def film_name(self, name):
#         self.__name = name
#
#     @property
#     def genre(self):
#         return self.__genre
#
#     @genre.setter
#     def genre(self, genre):
#         self.__genre = genre
#
#     @property
#     def duration(self):
#         return self.__duration
#
#     @duration.setter
#     def duration(self, duration):
#         self.__duration = duration
#
#     @staticmethod
#     def show_info():
#         print('This is some info about film')
#
#     def __str__(self):
#         return f'{self.__film_name} of a {self.__class__}'
#
#     def __len__(self):
#         return len(self.__film_name)
#
#
# # my_movie=Film('Rain Main','drama',195)
# # print(len(my_movie))
# # print(my_movie)
#
# # descriptors
# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
#
# class Gear:
#     hat = Descriptor()
#     shirt = Descriptor()
#     pants = Descriptor()
#     socks = Descriptor()
#     shoes = Descriptor()
#     underwear = Descriptor()
#
#     def __init__(self, hat, shirt, pants, socks, shoes, underwear):
#         self.hat = hat
#         self.shirt = shirt
#         self.pants = pants
#         self.socks = socks
#         self.shoes = shoes
#         self.underwear = underwear
#
#
# my_equipment = Gear('nike cap 78', 'nice basic t-shirt', 'nike swwosh grey pants',
#                     'white socks', 'Nike Air', 'trouthers')
#
#
# # functors
#
# class NameChanger:
#     def __init__(self, change_symbols):
#         self.change_symbols = change_symbols
#
#     def __call__(self, *args, **kwargs):
#         if type(args[0]) != str:
#             raise TypeError('Argument has to be string!')
#         return f'{self.change_symbols}{args[0]}{self.change_symbols}'
#
#
# # functor=NameChanger('***')
# # result=functor('Andrey')
# # print(result)
#
#
# # class-decorator
#
# class BeearBottleCalculator:
#     def __init__(self, function):
#         self.function = function
#
#     def __call__(self, x, chest=20, *args, **kwargs):
#         return self.function(x // chest, *args, **kwargs)
#
#
# @BeearBottleCalculator
# def get_beer(bottles):
#     return int(bottles)
#
#
# # res=get_beer(323420)
# # print(res)
#
#
# # __add__
#
# class RetailPrice:
#     def __init__(self, price):
#         self.price = price
#
#     @classmethod
#     def check_type(cls, item):
#         if not isinstance(item, (float, int, RetailPrice)):
#             raise TypeError('Argument must be float,int or instance of a class RetailPrice.')
#
#     def __add__(self, other):
#         self.check_type(other)
#         sc = other
#         if isinstance(other, RetailPrice):
#             sc = other.price
#
#         return RetailPrice(self.price + sc)
#
#     def __radd__(self, other):
#         return self + other
#
#     def __str__(self):
#         return f'Object of a class {self.__class__}'
#
#     def get_price(self):
#         return self.price
#
#     def __eq__(self, other):
#         self.check_type(other)
#         sc = other if isinstance(other, (float, int)) else other.price
#         return self.price == sc
#
#
# # shoes=RetailPrice(100)
# # pants=RetailPrice(50)
# # total=shoes+pants
# # print(total.get_price())
# # print(total)
# # print(shoes==pants)
#
# class DartGame:
#     def __init__(self, player, points):
#         self.player = player
#         self.points = list(points)
#
#     def __getitem__(self, item):
#         return self.points[item]
#
#     def __setitem__(self, key, value):
#         self.points[key] = value
#
#     def __delitem__(self, key):
#         del self.points[key]
#
#
# # Richard=DartGame('Richard',[190,345,111,99,300])
# # print(Richard[2])
# # Richard.points[4]=0
# # print(Richard.points)
#
#
# class Footballer:
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         print(f'This is class for set up new footballer.'
#               f'\nPlayer\'s name: {self.name}\nPlayer\'s position: {self.position}')
#
#     def name_changer(self, symbol='***'):
#         print(f'{symbol}{self.name}{symbol}')
#
#     def __str__(self):
#         return f'{self.name} ---{self.__class__}'
#
#
# class Defenders(Footballer):
#     MARK_RANGE = (0, 100)
#
#     @classmethod
#     def verify(cls, mark):
#         if cls.MARK_RANGE[0] > mark or cls.MARK_RANGE[1] < mark:
#             raise AttributeError('Mark should be between 0 to 100.')
#
#     def __init__(self, name, position, mark_level):
#         self.verify(mark_level)
#         super().__init__(name, position)
#         self.mark_level = mark_level
#
#     def get_info(self):
#         print(f'Info about defensive player:\nNAME: {self.name}'
#               f'\nPosition: {self.position}\nMark: {self.mark_level}%')
#
#
# class WingBack(Defenders):
#     __FLANGS = ('right', 'left')
#
#     @classmethod
#     def __check_flang(cls, flang):
#         if not flang in cls.__FLANGS:
#             raise AttributeError('There are only two kinds of flangs: left and right!')
#
#     def __init__(self, name, position, mark_level, flang):
#         self.__check_flang(flang)
#         super().__init__(name, position, mark_level)
#         self.flag = flang
#
#
# class Referee:
#     __slots__ = ('name','runk')
#
#     def __init__(self,name,runk):
#         self.name=name
#         self.runk=runk

# binary search
# def binary_search(massive,digit):
#     first_index=0
#     last_index=len(massive)-1
#
#     while first_index<=last_index:
#         middle_index=(first_index+last_index)//2
#         program_guess=massive[middle_index]
#
#         if program_guess==digit:
#             return f'Index of digit {digit} is {middle_index}'
#
#         elif program_guess>digit:
#             last_index=middle_index-1
#
#         elif program_guess<digit:
#             first_index=middle_index+1
#
#     return 'There is not digit you want.'
#
# array=[4,7,8,10,11,45,78]
#
# #quick sort
# def quick_sort(massive):
#     if len(massive)<2:
#         return massive
#
#     base_index=len(massive)//2
#     base_item=massive[base_index]
#
#     low=[x for x in massive[:base_index] if x<base_item]+[x for x in massive[base_index+1:]if x < base_item]
#     high=[x for x in massive[:base_index] if x>base_item]+[x for x in massive[base_index+1:]if x > base_item]
#
#     return quick_sort(low)+[base_item]+quick_sort(high)
#
# array=[6,3,8,90,-13,0,4]
#
# friends = {}
#
# friends['Andrey'] = ['Danil', 'Radik', 'Alex', 'Chaus']
# friends['Danil'] = ['Andrey', 'Ivan', 'Shoker', 'Anna']
# friends['Radik'] = ['Nastya']
# friends['Nastya'] = ['Radik']
# friends['Alex'] = []
# friends['Chaus'] = []
# friends['Ivan'] = []
# friends['Shoker'] = []
# friends['Anna'] = []
#
# def find_name(name):
#     return name[-3:]=='dik'
#
# from collections import deque
# #breadth first search
# def BFS(dic,key):
#     ochered=deque()
#     ochered+=dic[key]
#     checked=[]
#
#     while ochered:
#         person=ochered.popleft()
#         if not person in checked:
#             if find_name(person):
#                 return f'We have found {person}!'
#             else:
#                 checked.append(person)
#                 ochered+=dic[person]
#
#     return 'sorry< no name!'
#
#
# # res=BFS(friends,'Andrey')
# # print(res)
#
#
# #bubble sort
# def bubble_sort(massive):
#     col_items=len(massive)
#     all_iterations=col_items-1
#
#     for iteration in range(0,all_iterations):
#         for dig in range(0,all_iterations-iteration):
#             if massive[dig]>massive[dig+1]:
#                 massive[dig],massive[dig+1]=massive[dig+1],massive[dig]
#     print(massive)
# # array=[6,3,8,90,-13,0,4]
# # res=bubble_sort(array)
#
# #merge sort
# def merge_sort(first_list,second_list):
#     mutual_list=[]
#
#     arrow_first_list=0
#     arrow_second_list = 0
#
#     length_1=len(first_list)
#     length_2=len(second_list)
#
#     while length_1>arrow_first_list and length_2>arrow_second_list:
#         if first_list[arrow_first_list]<second_list[arrow_second_list]:
#             mutual_list.append(first_list[arrow_first_list])
#             arrow_first_list+=1
#         else:
#             mutual_list.append(second_list[arrow_second_list])
#             arrow_second_list += 1
#
#     mutual_list+=first_list[arrow_first_list:]+second_list[arrow_second_list:]
#
#     print(mutual_list)
# sp1=[1,5,6,77,89,445]
# sp2=[66,88,890,1000]
# res=merge_sort(sp1,sp2)

# binary search
# def binary_search(spisok, chislo):
#     first_index = 0
#     last_index = len(spisok) - 1
#
#     while first_index <= last_index:
#         middle_index = (first_index + last_index) // 2
#         programm_guess = spisok[middle_index]
#         if programm_guess == chislo:
#             return f'index for your digit is <{middle_index}>'
#         elif programm_guess > chislo:
#             last_index = middle_index - 1
#
#         elif programm_guess < chislo:
#             first_index = middle_index + 1
#
#     return 'No digitin massive.'
#
#
# # quick sort
# def quick_sort(massive):
#     if len(massive) < 2:
#         return massive
#
#     base_index = len(massive) // 2
#     base_digit = massive[base_index]
#
#     low = [x for x in massive[:base_index] if x < base_digit] + [x for x in massive[base_index + 1:] if x < base_digit]
#     bigger = [x for x in massive[:base_index] if x > base_digit] + [x for x in massive[base_index + 1:] if
#                                                                     x > base_digit]
#
#     return quick_sort(low)+[base_digit]+quick_sort(bigger)
#
#
# friends = {}
#
# friends['Andrey'] = ['Danil', 'Radik', 'Alex', 'Chaus']
# friends['Danil'] = ['Andrey', 'Ivan', 'Shoker', 'Anna']
# friends['Radik'] = ['Nastya']
# friends['Nastya'] = ['Radik']
# friends['Alex'] = []
# friends['Chaus'] = []
# friends['Ivan'] = []
# friends['Shoker'] = []
# friends['Anna'] = []
#
# def find_shoker(name):
#     return name=='Shoker'
#
# from collections import deque
#
# def BFS(dictionary,key):
#     turn=deque()
#     turn+=dictionary[key]
#     checked=[]
#
#     while turn:
#         person=turn.popleft()
#         if not person in checked:
#             if find_shoker(person):
#                 return f'We find fucking {person}!'
#             else:
#                 checked.append(person)
#                 turn+=dictionary[person]
#
#     return 'No person you wanna find.'
#
#
# #bubble sort
# def bubble_sort(array):
#     count_elements=len(array)
#     count_iterations=count_elements-1
#
#     for iteration in range(0,count_iterations):
#         for dig in range(0,count_iterations-iteration):
#             if array[dig]>array[dig+1]:
#                 array[dig],array[dig+1]=array[dig+1],array[dig]
#
#     print(array)
#
#
# #merge sort
# def merge_sort(first_list,second_list):
#     final_list=[]
#
#     length_1=len(first_list)
#     length_2=len(second_list)
#
#     counter_1=0
#     counter_2=0
#
#     while length_1>counter_1 and length_2>counter_2:
#         if first_list[counter_1]<second_list[counter_2]:
#             final_list.append(first_list[counter_1])
#             counter_1+=1
#         else:
#             final_list.append(second_list[counter_2])
#             counter_2+=1
#
#
#     final_list+=first_list[counter_1:]+second_list[counter_2:]
#
#     print(final_list)
#
#
#
# binary search

def binary_search(massive, item):
    first_index = 0
    last_index = len(massive) - 1

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        program_guess = massive[middle_index]

        if program_guess == item:
            return f'We\'ve found it! index is {middle_index}'

        elif program_guess > item:
            last_index = middle_index - 1

        elif program_guess < item:
            first_index = middle_index + 1

    return 'There is no digit you have asked to.'


# fast sort
def fast_sort(massive):
    if len(massive) < 2:
        return massive

    base_index = len(massive) // 2
    base_item = massive[base_index]

    low = [dig for dig in massive[:base_index] if dig < base_item] + [dig for dig in massive[base_index + 1:] if
                                                                          dig < base_item]
    high = [dig for dig in massive[:base_index] if dig > base_item] + [dig for dig in massive[base_index + 1:] if
                                                                          dig > base_item]

    return fast_sort(low)+[base_item]+fast_sort(high)


#breadth first search

friends = {}

friends['Andrey'] = ['Danil', 'Radik', 'Alex', 'Chaus']
friends['Danil'] = ['Andrey', 'Ivan', 'Shoker', 'Anna']
friends['Radik'] = ['Nastya']
friends['Nastya'] = ['Radik']
friends['Alex'] = []
friends['Chaus'] = []
friends['Ivan'] = []
friends['Shoker'] = []
friends['Anna'] = []

def fimd_name(name):
    if 'hau' in name:
        return name

from collections import deque

def BFS(dic,key):
    turn=deque()
    turn+=dic[key]
    verifyed=[]

    while turn:
        person=turn.popleft()
        if not person in verifyed:
            if fimd_name(person):
                return f'We did it! Here he is {person}'
            else:
                verifyed.append(person)
                turn+=dic[person]

    return 'here is no man you are looking at.'

#bubble sort
def bubble_sort(massive):
    count_elements=len(massive)
    count_iterations=count_elements-1

    for iteration in range(0,count_iterations):
        for dig in range(0,count_iterations-iteration):
            if massive[dig]>massive[dig+1]:
                massive[dig],massive[dig+1]=massive[dig+1],massive[dig]
    print(massive)

#merge sort
def merge_sort(list_1,list_2):
    total_list=[]

    length_1=len(list_1)
    length_2=len(list_2)

    arrow_1=0
    arrow_2=0

    while length_1>arrow_1 and length_2>arrow_2:
        if list_1[arrow_1]<list_2[arrow_2]:
            total_list.append(list_1[arrow_1])
            arrow_1+=1
        else:
            total_list.append(list_2[arrow_2])
            arrow_2+=1

    total_list+=list_1[arrow_1:]+list_2[arrow_2:]

    print(total_list)





