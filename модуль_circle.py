# Cоздадим один из модулей программы для вычисления геометрических задач.

# Модуль circle содержит функции,которые выполняют вычисления,
# связанные с кругами.

import math


# Вычислим площадь круга:
def area(radius):
    return math.pi * radius ** 2


# Вычислим длину окружности:
def dlina_okruj(radius):
    return 2 * math.pi * radius
