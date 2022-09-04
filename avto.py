class Avto:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    # метод для ускорения авто
    def accelerate(self):
        self.__speed += 5

    # метод для торможения авто
    def tormoz(self):
        self.__speed -= 5

    # метод, возвращающий текущую скорость авто
    def get_speed(self):
        return self.__speed

