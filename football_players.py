class Footballer:
    def __init__(self,position):
        self.__position=position

    def show_position(self):
        print('Позиция',self.__position)

    def get_tasks(self):
        print('some tasks')

class Defender(Footballer):
    def __init__(self):
        Footballer.__init__(self,'Защитник')

    def get_tasks(self):
        print('Отбор мяча, начало атаки, офсайдная ловушка ')

class Midfielder(Footballer):
    def __init__(self):
        Footballer.__init__(self,'Полузащитник')

    def get_tasks(self):
        print('Контроль центра поля, развитие атак, защитные действия, поддержка атаки')