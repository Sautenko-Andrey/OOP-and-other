# В этой программе будет считаться статистика футбольных игроков.

#Вызовем нужные нам модули:
import attempts_accuracy

#Создадим именованные константы для "МЕНЮ" программы:
import player_speed

PASS_ACCURACY=1
WIN_TAKLES=2
KIKS_ACCURACY=3
MIDDLE_SPEED=4
EXIT=5

#Создадим главную функцию:
def main():
    #Создадим перменную 'vibor' , которая будет управлять циклом в "МЕНЮ":
    vibor=0
    while vibor!=EXIT:
        #Далее показываем пользователю меню:
        user_meny()

        #Получить от пользователя выбор из меню:
        vibor=int(input("Какие данные Вы хотите подсчитать?"))

        #Задаем условия:
        if vibor==PASS_ACCURACY:
            total_passes=int(input("Сколько всего было совершено передач?"))
            lucky_passes=int(input("Сколько из них достигли цели?"))
            print("Точность передач равна",attempts_accuracy.attempts_accuracy(total_passes,lucky_passes),"%")
        elif vibor==WIN_TAKLES:
            total_takles = int(input("Сколько всего было совершено попыток отбора?"))
            win_takles = int(input("Сколько из них было удачных?"))
            print("Процент успешных отборов равен",attempts_accuracy.attempts_accuracy(total_takles,win_takles),"%")
        elif vibor==KIKS_ACCURACY:
            all_kiks=int(input("Сколько всего было сделано ударов?"))
            on_target_kiks=int(input("Сколько из них в створ ворот?"))
            print("Точность ударов по воротам равна",attempts_accuracy.attempts_accuracy(all_kiks,on_target_kiks),"%")
        elif vibor==MIDDLE_SPEED:
            distance=float(input("Сколько км игрок пробежал за матч?"))
            time=int(input("Сколько минут игрок находился на поле? "))
            print("Средняя скорость игрока равна",player_speed.middle_speed(distance,time),"metr\min")
        elif vibor==EXIT:
            print("Программа завершена.")
        else:
            print("Некорректный выбор!")


#Создадим функцию для "МЕНЮ":
def user_meny():
    print("МЕНЮ")
    print("1. ТОЧНОСТЬ ПЕРЕДАЧ")
    print("2. УДАЧНЫЙ ОТБОР")
    print("3. ТОЧНОСТЬ УДАРОВ ПО ВОРОТАМ")
    print("4. СРЕДНЯЯ СКОРОСТЬ ИГРОКА")
    print("5. ВЫХОД ИЗ ПРОГРАММЫ")


main()


