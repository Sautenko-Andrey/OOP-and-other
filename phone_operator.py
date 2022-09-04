import tkinter
import tkinter.messagebox


class PhoneProvider:
    def __init__(self):
        # создадим главное окно
        self.__main_window = tkinter.Tk()

        # создадим три рамки
        self.__top_frame = tkinter.Frame(self.__main_window)
        self.__mid_frame = tkinter.Frame(self.__main_window)
        self.__bottom_frame = tkinter.Frame(self.__main_window)

        # создадим эл-ты для верхней рамки
        # создадим объект IntVar для использования с эл-ми радиокнопок
        self.__object = tkinter.IntVar()

        # присвоим ему значение 2 позиции
        self.__object.set(1)

        # создадим эл-ты radiobutton  для верхней рамки
        self.__daily_period = tkinter.Radiobutton(self.__top_frame,
                                                  text='Дневное время (6:00-17:59)',
                                                  variable=self.__object,
                                                  value=1)

        self.__evening_period = tkinter.Radiobutton(self.__top_frame,
                                                    text='Вечернее время (18:00-23:59)',
                                                    variable=self.__object,
                                                    value=2)

        self.__night_period = tkinter.Radiobutton(self.__top_frame,
                                                  text='Непиковый период (00:00-5:59)',
                                                  variable=self.__object,
                                                  value=3)

        # упакуем эл-ты
        self.__daily_period.pack()
        self.__evening_period.pack()
        self.__night_period.pack()

        # создадим эл-ты для среней рамки,куда булут вводиться минуты
        self.__text_for_entry = tkinter.Label(self.__mid_frame, text='Введите количество минут')

        self.__entry = tkinter.Entry(self.__mid_frame, width=15)

        # упакуем эл-ты
        self.__text_for_entry.pack(side='left')
        self.__entry.pack(side='left')

        # создадим кнопки для нижней рамки
        self.__show_price_button = tkinter.Button(self.__bottom_frame,
                                                  text='Показать стоимость',
                                                  command=self.__execute)

        self.__exit = tkinter.Button(self.__bottom_frame,
                                     text='Выйти',
                                     command=self.__main_window.destroy)

        # упакуем кнопки
        self.__show_price_button.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем рамки
        self.__top_frame.pack()
        self.__mid_frame.pack()
        self.__bottom_frame.pack()

        # заупстим главный цикл
        tkinter.mainloop()

    # создадим функцию-реакцию на нажатие кнопки
    def __execute(self):
        # получим данные от пользователя
        minutes = float(self.__entry.get())

        # зададим условие
        if self.__object.get() == 1:
            messege = minutes * 10
        if self.__object.get() == 2:
            messege = minutes * 12
        if self.__object.get() == 3:
            messege = minutes * 5

        # выведем результат
        tkinter.messagebox.showinfo('Общая стоимость', 'Ваши затраты =' + str(messege) + 'грн')
