import tkinter
import tkinter.messagebox

class Points:
    def __init__(self):
        # создадим главное окно
        self.__main_window=tkinter.Tk()

        # создадим 5 рамок
        self.__frame1=tkinter.Frame(self.__main_window)
        self.__frame2 = tkinter.Frame(self.__main_window)
        self.__frame3 = tkinter.Frame(self.__main_window)
        self.__frame4 = tkinter.Frame(self.__main_window)
        self.__frame5 = tkinter.Frame(self.__main_window)

        # создадим строку и поле для первой рамки
        # строка
        self.__text1=tkinter.Label(self.__frame1,
                                   text='Ввести экзаменационную оценку №1: ')
        #окно для ввода данных
        self.__field1=tkinter.Entry(self.__frame1,width=10)

        #упакуем эти данные в рамку
        self.__text1.pack(side='left')
        self.__field1.pack(side='left')



        # создадим строку и поле для второй рамки
        # строка
        self.__text2 = tkinter.Label(self.__frame2,
                                     text='Ввести экзаменационную оценку №2: ')
        # окно для ввода данных
        self.__field2 = tkinter.Entry(self.__frame2, width=10)

        # упакуем эти данные в рамку
        self.__text2.pack(side='left')
        self.__field2.pack(side='left')

        # создадим строку и поле для третей рамки
        # строка
        self.__text3 = tkinter.Label(self.__frame3,
                                     text='Ввести экзаменационную оценку №3: ')
        # окно для ввода данных
        self.__field3 = tkinter.Entry(self.__frame3, width=10)

        # упакуем эти данные в рамку
        self.__text3.pack(side='left')
        self.__field3.pack(side='left')


        # создадим инфо поле,гдебудет выводиться результат подсчета баллов
        self.__result_text=tkinter.Label(self.__frame4,
                                         text='Средний балл: ')

        # создадим объект StringVar
        self.__object=tkinter.StringVar()

        # создадим надпись лейбл и свяжем  ее с объектом
        self.__result_info=tkinter.Label(self.__frame4,
                                         textvariable=self.__object)

        # упакуем эти элементы в четвертую рамку
        self.__result_text.pack(side='left')
        self.__result_info.pack(side='left')

        # создадим эл-ты для самой нижней рамки
        # кнопка "ПОсчитать"
        self.__knopka=tkinter.Button(self.__frame5,
                                     text='Посчитать!',
                                     command=self.__calculate)
        # кнопка "Выйти"
        self.__exit=tkinter.Button(self.__frame5,
                                   text='Выйти',
                                   command=self.__main_window.destroy)

        # упакуем кнопки
        self.__knopka.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем все 5 рамок
        self.__frame1.pack()
        self.__frame2.pack()
        self.__frame3.pack()
        self.__frame4.pack()
        self.__frame5.pack()

        # запустим главный цикл
        tkinter.mainloop()

    def __calculate(self):
        # получим данные по трем оценкам
        point1=float(self.__field1.get())
        point2 = float(self.__field2.get())
        point3 = float(self.__field3.get())

        # посчитаем среднюю
        middle_point=(point1+point2+point3)/3

        self.__object.set(middle_point)


