class Shurovo:
    'В этом классе собраны методы для обработки данных участников "Чемпионата Донбасса"'

    def __init__(self,name,city,points):
        self.name=name
        self.city=city
        self.points=points


    def __del__(self):
        print('Удаление объекта'+str(self))

    def set_teams(self,name,city,points):
        self.name=name
        self.city=city
        self.points=points

    def get_teams(self):
        return (self.name,self.city,self.points)

    