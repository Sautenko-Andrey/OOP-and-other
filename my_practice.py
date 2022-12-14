from collections import deque


class Algoritms:
    __slots__ = ('__algoritm_name',)

    __MY_ALGORITMS = ('binary_search', 'fast_sort', 'merge_sort', 'bubble_sort', 'BFS')

    @classmethod
    def __check_algoritm(cls, algoritm):
        if not algoritm in cls.__MY_ALGORITMS:
            raise AttributeError(f'We don\'t know this kind of algoritm! <{algoritm}>')

    def __new__(cls, *args, **kwargs):
        print('Welcome to algoritms hub!')
        return super().__new__(cls)

    def __init__(self, algoritm_name):
        self.__check_algoritm(algoritm_name)
        self.__algoritm_name = algoritm_name

    @property
    def algoritm_name(self):
        return self.__algoritm_name

    def __str__(self):
        return f'Algoritm: {self.__algoritm_name}'


class BinarySearch(Algoritms):

    @classmethod
    def __check_attribute(cls, some_list, some_digit):
        if type(some_list) != list and type(some_digit) != int:
            raise TypeError('first argument must be list and second - int')

    def execute(self, my_list, digit):
        self.__check_attribute(my_list, digit)
        my_list = sorted(my_list)
        first_index = 0
        last_index = len(my_list) - 1

        while first_index <= last_index:
            search_index = (first_index + last_index) // 2
            guess = my_list[search_index]

            if guess == digit:
                return f'We have found this number! It\'s index = {search_index}'
            elif guess > digit:
                last_index = search_index - 1
            else:
                first_index = search_index + 1

        return f'Sorry, we didn\'t find this number...'


class FastSort(Algoritms):

    @classmethod
    def __check_attribue(cls, attribute):
        if type(attribute) != list:
            raise TypeError('Attribute must be list')

    def execute(self, some_list):
        self.__check_attribue(some_list)
        if len(some_list) < 2:
            return some_list

        base_index = len(some_list) // 2
        base_item = some_list[base_index]

        low_list = [x for x in some_list[:base_index] if x < base_item] + [x for x in some_list[base_index + 1:] if
                                                                           x < base_item]
        high_list = [x for x in some_list[:base_index] if x > base_item] + [x for x in some_list[base_index + 1:] if
                                                                            x > base_item]
        return self.execute(low_list) + [base_item] + self.execute(high_list)


class BFS(Algoritms):

    def __search_name(self, name):
        if type(name) != str:
            raise TypeError('Atribute must be string!')
        if len(name) == 6 and name[0] == 'S' and name[-1] == 'r':
            return name

    def execute(self, dictionary, key):
        self.__search_name(key)
        turn = deque()
        turn += dictionary[key]
        checked = []

        while turn:
            person = turn.popleft()
            if not person in checked:
                if self.__search_name(person):
                    return f'we have found fucking {person}'
                else:
                    turn += dictionary[person]
                    checked.append(person)

        return 'no person here...'


class BubbleSort(Algoritms):

    def execute(self, some_list):
        count_items = len(some_list)
        count_iters = count_items - 1

        for iteration in range(0, count_iters):
            for dig in range(0, count_iters - iteration):
                if some_list[dig] > some_list[dig + 1]:
                    some_list[dig], some_list[dig + 1] = some_list[dig + 1], some_list[dig]
        return some_list


class MergeSort(Algoritms):

    @classmethod
    def __check_attributes(cls, x, y):
        if type(x) != list and type(x) != type(y):
            raise TypeError('Both attributes have to be lists!')

    def execut(self, list1, list2):
        self.__check_attributes(list1, list2)
        mutual_list = []

        length_first = len(list1)
        length_sec = len(list2)

        count_1 = 0
        count_2 = 0

        while length_first > count_1 and length_sec > count_2:
            if list1[count_1] > list2[count_2]:
                mutual_list.append(list2[count_2])
                count_2 += 1
            else:
                mutual_list.append(list1[count_1])
                count_1 += 1

        mutual_list += list1[count_1:] + list2[count_2:]

        return mutual_list


class Films:
    __FORBIDDEN_LT = '????????????????????????????????????????????????????????????????'
    __FORBIDDEN_LT_BIG = __FORBIDDEN_LT.upper()

    @classmethod
    def __check_name(cls, name):
        for lt in name:
            if lt in cls.__FORBIDDEN_LT or lt in cls.__FORBIDDEN_LT_BIG:
                raise AttributeError('fuck off russian films!')

    __slots__ = ('film_name',)

    def __new__(cls, *args, **kwargs):
        print(f'creating new instance of a class {cls}')
        return super().__new__(cls)

    def __init__(self, film_name):
        self.__check_name(film_name)
        self.film_name = film_name

    def show_film(self):
        return self.film_name

    def __str__(self):
        return self.film_name


class MyFavouriteFilms(Films):
    __slots__ = ('film_name', '__genre', 'year')
    __AVAILABLE_GENRES = ('comedy', 'action', 'adventures')
    __YEARS = (1980, 2022)

    @classmethod
    def __verify_genre(cls, genre):
        if not genre in cls.__AVAILABLE_GENRES:
            raise AttributeError('Invalid genre...sorry!')

    @classmethod
    def __verify_year(cls, year):
        if not isinstance(year, int):
            raise TypeError('year must be integer!')
        if cls.__YEARS[0] > year > cls.__YEARS[1]:
            raise AttributeError(f'{year} - incorrect year!')

    def __init__(self, film_name, genre, year):
        self.__verify_genre(genre)
        self.__verify_year(year)
        super().__init__(film_name)
        self.__genre = genre
        self.year = year

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def get_info(self):
        print(f'INFO ABOUT FILM:\n--------------\n'
              f'Film: {self.film_name}\nGenre: {self.__genre}\n'
              f'Year: {self.year}')

    @staticmethod
    def my_name():
        print('My name : Andrey')


class Descriptors:
    def __set_name__(self, owner, name):
        self.name='_'+name

    def __set__(self, instance, value):
        setattr(instance,self.name,value)

    def __get__(self, instance, owner):
        return getattr(instance,self.name)
class MyStuffs:

    clothes=Descriptors()
    shoes = Descriptors()
    meal = Descriptors()
    toys = Descriptors()
    def __init__(self,clothes,shoes,meal,toys):
        self.clothes=clothes
        self.shoes=shoes
        self.meal=meal
        self.toys=toys



#functor
class NameChanger:
    def __init__(self,symbols):
        self.__symbols=symbols

    def __call__(self, *args, **kwargs):
        if type(args[0])!=str:
            raise TypeError('Argument must be string!')
        return f'{self.__symbols}{args[0]}{self.__symbols}'

class Decorator:
    def __init__(self,some_func):
        self.__some_func=some_func

    def __call__(self,x,koef=0.85,*args, **kwargs):
        return self.__some_func(x*koef)

@Decorator
def value(price):
    return price



class Savings:
    def __init__(self,my_savings):
        self.my_savings=my_savings

    def __add__(self, other):
        if not isinstance(other,(int,Savings)):
            raise('Fucking error')

        sc =other
        if isinstance(other,Savings):
            sc=other.my_savings
        return Savings(self.my_savings+sc)

    def __radd__(self, other):
        return self.my_savings+other

    def __eq__(self, other):
        if not isinstance(other,(int,Savings)):
            raise TypeError('stupid error...')
        sc =other if type(other)==int else other.my_savings
        return self.my_savings==sc

    def show_sum(self):
        return self.my_savings



me=Savings(1000)
you=Savings(500)
res=me+you
print(res.show_sum())
print(you==me)



