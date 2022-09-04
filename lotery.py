import random
class Bet:
    # инициируем первое значение кубика:
    def __init__(self):
        self.__kubik=0

    def brosaem(self):
        if random.randint(1,6)==1:
            self.__kubik='1'
        elif random.randint(1,6)==2:
            self.__kubik='2'
        elif random.randint(1,6)==3:
            self.__kubik='3'
        elif random.randint(1,6)==4:
            self.__kubik = '4'
        elif random.randint(1,6)==5:
            self.__kubik = '5'
        elif random.randint(1,6)==6:
            self.__kubik = '6'


    def show(self):
        return self.__kubik
