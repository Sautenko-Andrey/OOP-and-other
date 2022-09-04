# В данном модуле функция производит различные
# финансовые операции для магазина спортивных товаров
import nacenka
import pribil_ili_ubitok_magazina
import zatrati_magazina
import viplati_manageram

# Создадим глобальные константы для меню программы:


RASSCHET_RETAIL_PRICE = 1
RASSCHET_VSEH_ZATRAT = 2
RASSCHET_VIPLAT = 3
RASSCHET_PRIBIL = 4
EXIT = 5


def main():
    vibor_stroki = 0
    while vibor_stroki != EXIT:
        menu()
        vibor_stroki = int(input("ВЫБЕРИ ПУНКТ ИЗ МЕНЮ: "))
        if vibor_stroki == RASSCHET_RETAIL_PRICE:
            whole_sale = float(input("Какая оптовая цена товара?"))
            nakrutka = float(input("Какой коэфициент накрутки?"))
            print("РОЗНИЧНАЯ ЦЕНА ТОВАРА =", nacenka.plus_price(whole_sale, nakrutka), "грн")
        elif vibor_stroki == RASSCHET_VSEH_ZATRAT:
            print("РАСХОДЫ МАГАЗИНА ЗА ТЕКУЩИЙ МЕСЯЦ СОСТАВЛЯЮТ:", zatrati_magazina.main_zatrati(), "грн")
        elif vibor_stroki == RASSCHET_VIPLAT:
            viplati_manageram.main()
        elif vibor_stroki == RASSCHET_PRIBIL:
            valovaya = float(input("Введи валовую прибыль магазина: "))
            vse_rash_magaz = zatrati_magazina.main_zatrati()
            pribil_ili_ubitok_magazina.main_rentabilnost(valovaya, vse_rash_magaz)
        elif vibor_stroki == EXIT:
            print("ВЫХОД ИЗ ПРОГРАММЫ")
        else:
            print("НЕКОРРЕКТНЫЙ ВЫБОР!")


def menu():
    print("МЕНЮ ПРОГРАММЫ")
    print("1) РАССЧЕТ РОЗНИЧНОЙ ЦЕНЫ ТОВАРА")
    print("2) РАССЧЕТ ВСЕХ ЗАТРАТ МАГАЗИНА")
    print("3) РАССЧЕТ ВЫПЛАТ СОТРУДНИКАМ")
    print("4) РАССЧЕТ ПРИБЫЛЬНОСТИ МАГАЗИНА")
    print("5) ВЫХОД ИЗ ПРОГРАММЫ")


main()
