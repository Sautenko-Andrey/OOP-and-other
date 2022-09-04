#Потреним по применению модулей:
# Эта программа будет вызывать модули для круга,треугольника и прямоугольника,котрые мы сами написали.
# импортируем их:
import модуль_circle
import модуль_rectangle

#Эта программа позволяет производить различные операции над геометрическими фигурами.
#Создадим именованные константы:
AREA_CIRCLE_CHOICE=1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE=3
PERIMETR_RECTANGLE_CHOICE=4
QUIT_CHOICE=5

#Создадим главную функцию.

def main():
    # переменная choice управляет циклом и содержит вариант выбора пользователя.
    choice=0
    while choice!=QUIT_CHOICE:
        #показать меню
        display_menu()

        #получить вариант выбора пользователя
        choice=int(input("Выберите вариант из меню: "))

        #выполнить выбранное действие
        if choice==AREA_CIRCLE_CHOICE:
            radius=float(input("Выберите радиус круга: "))
            print("Площадь равна",модуль_circle.area(radius))
        elif choice==CIRCUMFERENCE_CHOICE:
            radius=float(input("Введи радиус круга: "))
            print("Длина окружности равна",модуль_circle.dlina_okruj(radius))
        elif choice==AREA_RECTANGLE_CHOICE:
            width=float(input("Введи ширину прямоугольника: "))
            length = float(input("Введи длину прямоугольника: "))
            print("Площадь прямоугольника равна",модуль_rectangle.area(width,length))
        elif choice==PERIMETR_RECTANGLE_CHOICE:
            width = float(input("Введи ширину прямоугольника: "))
            length = float(input("Введи длину прямоугольника: "))
            print("Периметр прямоугольника равен",модуль_rectangle.perimetr(width,length))
        elif choice==QUIT_CHOICE:
            print("ВЫХОД ИЗ ПРОГРАММЫ")
        else:
            print("ОШИБКА! НЕТ ТАКОГО ВЫБОРА!")
#функция display_menu() показывает пользователю меню программы. Создадим ее:
def display_menu():
    print("МЕНЮ")
    print("1. ПЛОЩАДЬ КРУГА")
    print("2. ДЛИНА ОКРУЖНОСТИ")
    print("3. ПЛОЩАДЬ ПРЯМОУГОЛЬНИКА")
    print("4. ПЕРИМЕТР ПРЯМОУГОЛЬНИКА")
    print("5. ВЫХОД")


main()


