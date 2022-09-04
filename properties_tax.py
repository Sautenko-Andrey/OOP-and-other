import tkinter
import tkinter.messagebox


class Tax:
    def __init__(self):
        # создаем главное окно
        self.__main_window = tkinter.Tk()

        # моздаем 4 рамки
        # рамка для ввода данных
        self.__info_frame = tkinter.Frame(self.__main_window)
        # рамка для оценочной стоимости
        self.__price_frame = tkinter.Frame(self.__main_window)
        # рамка для налога на имущество
        self.__tax_frame = tkinter.Frame(self.__main_window)
        # рамка для кнопок
        self.__button_frame = tkinter.Frame(self.__main_window)

        # создадим эл-ты для первой рамки
        self.__quest_text = tkinter.Label(self.__info_frame,
                                          text='Введите стоимость имущества:$')

        self.__entry = tkinter.Entry(self.__info_frame, width=15)

        # упакуем эти два элемента
        self.__quest_text.pack(side='left')
        self.__entry.pack(side='left')

        # создадим элементы для второй рамки
        # пропишем текст
        self.__show_first_text = tkinter.Label(self.__price_frame,
                                               text='Оценочная стоимость:$')
        # создадим объект #1
        self.__object_1 = tkinter.StringVar()
        # создадим элемент текста и привяжем к объекту
        self.__give_info_1 = tkinter.Label(self.__price_frame,
                                           textvariable=self.__object_1)

        # упакуем эти 2 эл-та
        self.__show_first_text.pack(side='left')
        self.__give_info_1.pack(side='left')

        # пропишем эл-ты для 3 рамки
        # пропишем текст
        self.__show_sec_text = tkinter.Label(self.__tax_frame,
                                             text='Налог на имущество:$')
        # создадим объект #1
        self.__object_2 = tkinter.StringVar()
        # создадим элемент текста и привяжем к объекту
        self.__give_info_2 = tkinter.Label(self.__tax_frame,
                                           textvariable=self.__object_2)

        # упакуем эти 2 эл-та
        self.__show_sec_text.pack(side='left')
        self.__give_info_2.pack(side='left')

        # создадим две кнопки
        self.__calc = tkinter.Button(self.__button_frame,
                                     text='Вычислить',
                                     command=self.__execute)

        self.__exit = tkinter.Button(self.__button_frame,
                                     text='Выход',
                                     command=self.__main_window.destroy)

        # упакуем кнопки
        self.__calc.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем рамки
        self.__info_frame.pack()
        self.__price_frame.pack()
        self.__tax_frame.pack()
        self.__button_frame.pack()

        # запустим главный цикл
        tkinter.mainloop()

    # функция возврата при нажатии кнопки
    def __execute(self):
        # получим данные от пользователя
        properties_price = float(self.__entry.get())

        # Выведем оценочную стоимость
        probably_price = properties_price * 0.6
        self.__object_1.set(probably_price)

        # Выведем налог на имущество
        properties_tax = probably_price * 0.0075
        self.__object_2.set(properties_tax)
