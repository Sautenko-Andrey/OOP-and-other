import tkinter
import tkinter.messagebox


class OilCalculator:
    def __init__(self):
        # создадим главное окно интерфейса
        self.__window = tkinter.Tk()

        # создадим 4 рамки
        # первая рамка для ввода количества галлонов
        self.__gallons_frame = tkinter.Frame(self.__window)
        # вторая рамка для ввода количества миль
        self.__miles_frame = tkinter.Frame(self.__window)
        # третья рамка для вывода результата
        self.__result_frame = tkinter.Frame(self.__window)
        # четвертая колонка для кнопок "Посчитать" и "Выйти"
        self.__buttons_frame = tkinter.Frame(self.__window)

        # пропишем жлементы интерфейса для первой рамки
        self.__gallons_text = tkinter.Label(self.__gallons_frame,
                                            text='Введите количество галонов: ')

        self.__gallons_entry = tkinter.Entry(self.__gallons_frame, width=15)

        # упакуем эти жлементы в рамку
        self.__gallons_text.pack(side='left')
        self.__gallons_entry.pack(side='left')

        # создадим эл-ты для второй рамки
        self.__miles_text = tkinter.Label(self.__miles_frame,
                                          text='Введите количество миль: ')

        self.__miles_entry = tkinter.Entry(self.__miles_frame, width=15)

        # упакуем эти элементы
        self.__miles_text.pack(side='left')
        self.__miles_entry.pack(side='left')

        # создадим элемент для вывода подсчитаных данных
        self.__text_for_info = tkinter.Label(self.__result_frame,
                                             text='Милли на галлон (MPG): ')

        # создадим объект StringVar
        self.__object = tkinter.StringVar()

        # создадим надпись и привяжем ее к объекту
        self.__total = tkinter.Label(self.__result_frame,
                                     textvariable=self.__object)

        # упакуем эл-ты в рамку
        self.__text_for_info.pack(side='left')
        self.__total.pack(side='left')

        # создадим кнопки "Посчитать" и "Выйти" для самой нижней рамки
        self.__calculate = tkinter.Button(self.__buttons_frame,
                                          text='Посчитать',
                                          command=self.__execute)

        self.__exit = tkinter.Button(self.__buttons_frame,
                                     text='Выйти',
                                     command=self.__window.destroy)

        #упакуем кнопки в рамку
        self.__calculate.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем все рамки
        self.__gallons_frame.pack()
        self.__miles_frame.pack()
        self.__result_frame.pack()
        self.__buttons_frame.pack()

        # запустим главный цикл интерфейса
        tkinter.mainloop()

    # функция-реакия на кнопку "Посчитать"
    def __execute(self):
        # получим данные от пользователя
        gallons = int(self.__gallons_entry.get())
        miles = float(self.__miles_entry.get())

        result = miles / gallons

        # вызовем обратную функцию
        self.__object.set(result)
