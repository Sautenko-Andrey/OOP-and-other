from collections import deque


class People:
    '''Main class for working with people,including friends, coworkers and other.'''

    __slots__ = ('name', 'sex', 'age')

    __AVAILABLE_LETTERS = 'qwertyuiopasdfghjklzxcvbnm '
    __RELEVANT_AGE = (18, 100)
    __SEX = ('female', 'male')

    @classmethod
    def __check_name(cls, name):
        for letter in name:
            if not letter in cls.__AVAILABLE_LETTERS:
                raise AttributeError(f'Undefined symbol <{letter}> in prespn\'s name.')

    @classmethod
    def __check_age(cls, age):
        if cls.__RELEVANT_AGE[0] > age > cls.__RELEVANT_AGE[1]:
            raise AttributeError('Age must be over than 18 and lower than 100!')

    @classmethod
    def __check_sex(cls, sex):
        if not sex in cls.__SEX:
            raise ValueError('Person has to be female or male.')

    def __new__(cls, *args, **kwargs):
        print('New person is created.')
        return object.__new__(cls)

    def __init__(self, name, sex, age):
        self.__check_name(name)
        self.__check_sex(sex)
        self.__check_age(age)
        self.name = name
        self.sex = sex
        self.age = age

    def get_person_info(self):
        return f'INFO:\nName: {self.name}\nSex: {self.sex}\nAge: {self.age}'


class Friend(People):
    __PHONE_CODE = '+38'
    __NUMBER_LENGTH = 13
    __FRIENDSHIP_STATUSES = ('best', 'simple', 'familiar')

    @classmethod
    def __check_phone(cls, phone):
        if not isinstance(phone, str):
            raise TypeError('Phone number must be string!')
        if phone[:3] != cls.__PHONE_CODE:
            raise AttributeError(f'<{phone[:3]}> - Undefined phone code!')
        if len(phone) != cls.__NUMBER_LENGTH:
            raise ValueError('There are 13 digits in phone number.')

    @classmethod
    def __check_status(cls, status):
        if not status in cls.__FRIENDSHIP_STATUSES:
            raise AttributeError(f'Unknown status <{status}>')

    __slots__ = ('name', 'sex', 'age', '__phone', '__status')

    def __getattribute__(self, item):
        if item == '__status':
            raise AttributeError('Unread attribute!')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == '__status':
            raise AttributeError('You can\'t change status!')
        else:
            object.__setattr__(self, key, value)

    def __init__(self, name, sex, age, phone, status):
        self.__check_phone(phone)
        self.__check_status(status)
        super().__init__(name, sex, age)
        self.__phone = phone
        self.__status = status

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    def __str__(self):
        return f'{self.__class__}:{self.name}'


class Coworker(People):
    __slots__ = ('name', 'sex', 'age', 'position')

    def __init__(self, name, sex, age, position):
        super().__init__(name, sex, age)
        self.position = position

    def adding_words(self, start='Sallary is: ', end='grn'):
        def decorator(func):
            def wrapper(x, *args, **kwargs):
                res = func(x, )
                res2 = start + str(res) + end
                return res

            return wrapper

        return decorator

    def estimate_sallary(self, days, sallary=500.00):
        max_koef = 0.25
        middle_koef = 0.15
        low_koef = 0.10
        if days > 20:
            result = sallary * days + (sallary * days) * max_koef
        elif 15 < days <= 20:
            result = sallary * days + (sallary * days) * middle_koef
        else:
            result = sallary * days + (sallary * days) * low_koef

        return result

    @staticmethod
    def job():
        print('We love our super best job!')


class Algoritms:
    '''Here i practice my favourite algoritms,
    including binary search, fast sort, BFS, bubble sort
    and merge sort'''

    def __init__(self, choose):
        self.choice = choose

    def binary_search(self, array, digit):
        first_index = 0
        last_index = len(array) - 1

        while first_index <= last_index:
            middle_index = (first_index + last_index) // 2
            program_guess = array[middle_index]

            if program_guess == digit:
                return f'Here is index of <{digit}> --- {middle_index}!'
            elif program_guess > digit:
                last_index = middle_index - 1
            else:
                first_index = middle_index + 1

        return f'There is not {digit}...'

    def fast_sort(self, array):
        if len(array) < 2:
            return array
        base_index = len(array) // 2
        base_item = array[base_index]

        low = [x for x in array[:base_index] if x < base_item] + [x for x in array[base_index + 1:] if x < base_item]
        high = [x for x in array[:base_index] if x > base_item] + [x for x in array[base_index + 1:] if x > base_item]

        return self.fast_sort(low) + [base_item] + self.fast_sort(high)

    def __search_Shoker(self, name):
        if name == 'Shoker':
            return name

    def BFS(self, dictionary, key):
        self.__search_Shoker(dictionary[key])
        turn = deque()
        turn += dictionary[key]
        verifed = []

        while turn:
            person = turn.popleft()
            if not person in verifed:
                if self.__search_Shoker(person):
                    return f'We find fucking {person}!'
                else:
                    verifed.append(person)
                    turn += dictionary[person]

        return 'We didn\'t find Shoker....'

    def bubble_sort(self, array):
        count_items = len(array)
        count_iterations = count_items - 1

        for iteration in range(0, count_iterations):
            for dig in range(0, count_iterations - iteration):
                if array[dig] > array[dig + 1]:
                    array[dig], array[dig + 1] = array[dig + 1], array[dig]

        return array

    def merge_sort(self, array1, array2):
        mutual_array = []

        length_1 = len(array1)
        length_2 = len(array2)

        arrow1 = 0
        arrow2 = 0

        while length_1 > arrow1 and length_2 > arrow2:
            if array1[arrow1] < array2[arrow2]:
                mutual_array.append(array1[arrow1])
                arrow1 += 1
            else:
                mutual_array.append(array2[arrow2])
                arrow2 += 1

        mutual_array += array1[arrow1:] + array2[arrow2:]

        return mutual_array


class Contacts:
    __slots__ = ('name', 'phone')

    LETTERS = 'qwertyuiopasdfghjklzxcvbnm '

    SYMBOLS = '1234567890-'

    @classmethod
    def __check_name(cls, name):
        if not isinstance(name, str):
            raise TypeError('Argument must be string!')
        for every_letter in name:
            if not every_letter in cls.LETTERS:
                raise AttributeError(f'Sorry, but you have tried'
                                     f' to use unsupportable symbol in name <{every_letter}>')
        name = name.split()
        if len(name) != 2:
            raise AttributeError('Please fill name and last name.')

    def __new__(cls, *args, **kwargs):
        print(f'Creating new instance of a class {cls}')
        return super().__new__(cls)

    def __init__(self, name, phone):
        self.__check_name(name)
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.__class__} --- {self.name}'

    def get_info(self):
        return f'{self.name} {self.phone}'


class MyFriend(Contacts):

    @classmethod
    def __check_adres(cls, adres):
        if not isinstance(adres, str):
            raise TypeError('Adres must be string!')
        for letter in adres:
            if not letter in cls.LETTERS or not letter in cls.SYMBOLS:
                raise AttributeError(f'Unknown symbol ---<{letter}>')

    def __init__(self, name, phone, adres):
        self.__check_adres(adres)
        super().__init__(name, phone)
        self.__adres = adres

    def show_friend_info(self):
        print(f'Name:{self.name}\nPhone:{self.phone}\nAdres:{self.__adres}')

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, adres):
        self.__check_adres(adres)
        self.__adres = adres


class MyAlgoritms:
    def __init__(self, algoritm):
        self.algoritm = algoritm

    def binary_search(self, array, digit):
        first_index = 0
        last_index = len(array) - 1

        while first_index <= last_index:
            guess_index = (first_index + last_index) // 2
            guess = array[guess_index]

            if guess == digit:
                return f'Your digit\'s index is <{guess_index}>'

            elif guess > digit:
                last_index = guess_index - 1

            elif guess < digit:
                first_index = guess_index + 1

        return f'We didn\'t find your digit here!'

    def quick_sort(self, array):
        if len(array) < 2:
            return array

        base_index = len(array) // 2
        base_item = array[base_index]

        low = [x for x in array[:base_index] if x < base_item] \
              + [x for x in array[base_index + 1:] if x < base_item]
        high = [x for x in array[:base_index] if x > base_item] + [x for x in array[base_index + 1:] if x > base_item]

        return self.quick_sort(low) + [base_item] + self.quick_sort(high)

    def __find_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Argument must be string!')
        if name[0] == 'S' and name[-1] == 'r':
            return name

    def breadth_first_search(self, diction, key):
        turn = deque()
        turn += diction[key]
        checked = []

        while turn:
            dude = turn.popleft()
            if not dude in checked:
                if self.__find_name(dude):
                    return f'We found fucking dude! it\'s {dude}!!!'
                else:
                    checked.append(dude)
                    turn += diction[dude]

        return 'We didn\'t find dude!'

    def bubble_sort(self, array):
        count_items = len(array)
        count_iterations = count_items - 1

        for iteration in range(0, count_iterations):
            for dig in range(0, count_iterations - iteration):
                if array[dig] > array[dig + 1]:
                    array[dig], array[dig + 1] = array[dig + 1], array[dig]

        return array

    def merge_sort(self, list1, list2):
        mutual_list = []

        index_1 = 0
        index_2 = 0

        length_1 = len(list1)
        length_2 = len(list2)

        while length_1 > index_1 and length_2 > index_2:
            if list1[index_1] < list2[index_2]:
                mutual_list.append(list1[index_1])
                index_1 += 1
            else:
                mutual_list.append(list2[index_2])
                index_2 += 1

        mutual_list += list1[index_1:] + list2[index_2:]

        return mutual_list

    def string_methods_list(self, text='i love beach volley'):
        first = text.upper()
        second = text.lower()
        third = text.find('i')
        fourth = text.rfind('l')
        fifth = text.index('b')
        sixth = text.strip()
        seventh = text.rjust(25, '*')
        eigth = text.ljust(25, '*')
        nineth = text.rstrip()
        tenth = text.lstrip()
        eleventh = text.isalpha()
        twelvth = text.isdigit()
        thirtheenth = text.count('o')
        fourtheenth = text.replace('i', 'I')
        fifteenth = text.join('***')
        sixteenth = text.split()
        print(text)
    def list_methods(self):
        array=[1,2,3,4,5]
        first=array.append(67)
        second=array.insert(3,100)
        third=array.pop(4)
        fourth=array.remove(1)
        fifth=array.copy()
        sixth=array.clear()
        seventh=array.sort()
        eighth=array.count(100)
        nineth=array.reverse()
        # tenth=array.index(1)
        print(array)

    def dict_methods(self):
        my_dict={'person':'Chaus','phone':'0502365478'}
        first=dict.fromkeys([1,2,3,4,5],'digs')
        second=my_dict.copy()
        third=my_dict.clear()
        fourth=my_dict.pop('phone')
        fifth=my_dict.popitem()
        sixth=my_dict.setdefault('status','best')
        seventh=my_dict.keys()
        eigth=my_dict.values()
        nineth=my_dict.items()
        tenth=my_dict.get('person')


