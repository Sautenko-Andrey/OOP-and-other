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
                res = func(x,)
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


chaus = Friend('alex chausov', 'male', 35, '+380950180611', 'best')
kubasov = Coworker('kubasov artem', 'male', 35, 'engineer')
print(kubasov.estimate_sallary(23))
