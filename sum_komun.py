import tkinter
import tkinter.messagebox


class Komunal:
    'Класс подсчитывает все расходы по коммуналке за месяц и выводит общую сумму платежа'

    def __init__(self):
        # создадим главное окно интерфейса
        self.__main_window = tkinter.Tk()

        # создадим 9 рамок для нашей программы
        self.__frame1 = tkinter.Frame(self.__main_window)
        self.__frame2 = tkinter.Frame(self.__main_window)
        self.__frame3 = tkinter.Frame(self.__main_window)
        self.__frame4 = tkinter.Frame(self.__main_window)
        self.__frame5 = tkinter.Frame(self.__main_window)
        self.__frame6 = tkinter.Frame(self.__main_window)
        self.__frame7 = tkinter.Frame(self.__main_window)
        self.__frame8 = tkinter.Frame(self.__main_window)
        self.__frame9 = tkinter.Frame(self.__main_window)

        # создадим элемент-приветсвие ЛЕйбл для первой рамки
        self.__hello_text = tkinter.Label(self.__frame1,
                                          text='Здравствуйте,Андрей!')

        # упакуем этот элемент в первую рамку
        self.__hello_text.pack(side='top')

        # создадим текст+поле для ввода для второй рамки
        # текст
        self.__text2 = tkinter.Label(self.__frame2,
                                     text='Плата за электричество: ')

        # поле для ввода
        self.__field2 = tkinter.Entry(self.__frame2, width=15)

        # упакуем элементы в рамку
        self.__text2.pack(side='left')
        self.__field2.pack(side='left')

        # создадим текст+поле для ввода для 3 рамки
        # текст
        self.__text3 = tkinter.Label(self.__frame3,
                                     text='Плата за воду: ')

        # поле для ввода
        self.__field3 = tkinter.Entry(self.__frame3, width=15)

        # упакуем элементы в рамку
        self.__text3.pack(side='left')
        self.__field3.pack(side='left')

        # создадим текст+поле для ввода для 4 рамки
        # текст
        self.__text4 = tkinter.Label(self.__frame4,
                                     text='Плата за газ: ')

        # поле для ввода
        self.__field4 = tkinter.Entry(self.__frame4, width=15)

        # упакуем элементы в рамку
        self.__text4.pack(side='left')
        self.__field4.pack(side='left')

        # создадим текст+поле для ввода для 5 рамки
        # текст
        self.__text5 = tkinter.Label(self.__frame5,
                                     text='Плата за отопление: ')

        # поле для ввода
        self.__field5 = tkinter.Entry(self.__frame5, width=15)

        # упакуем элементы в рамку
        self.__text5.pack(side='left')
        self.__field5.pack(side='left')

        # создадим текст+поле для ввода для 6 рамки
        # текст
        self.__text6 = tkinter.Label(self.__frame6,
                                     text='Плата за услуги ЖЭКа: ')

        # поле для ввода
        self.__field6 = tkinter.Entry(self.__frame6, width=15)

        # упакуем элементы в рамку
        self.__text6.pack(side='left')
        self.__field6.pack(side='left')

        # создадим текст+поле для ввода для 7 рамки
        # текст
        self.__text7 = tkinter.Label(self.__frame7,
                                     text='Плата за услуги интернета: ')

        # поле для ввода
        self.__field7 = tkinter.Entry(self.__frame7, width=15)

        # упакуем элементы в рамку
        self.__text7.pack(side='left')
        self.__field7.pack(side='left')

        # для рамки 8 создадим элемент подсчета тотала
        # текст
        self.__text_mid = tkinter.Label(self.__frame8,
                                        text='Общая сумма: ')

        # создадим объект StringVar
        self.__object = tkinter.StringVar()

        # создадим надпись и привяжем ее к объекту
        self.__total = tkinter.Label(self.__frame8,
                                     textvariable=self.__object)

        # упакуем эл-ты в 8 рамку
        self.__text_mid.pack(side='left')
        self.__total.pack(side='left')

        # создадим кнопки для нижней рамки
        # кнопка "Считать!"
        self.__calc = tkinter.Button(self.__frame9,
                                     text='Считать!',
                                     command=self.__execute)
        # кнопка "Выйти"
        self.__exit = tkinter.Button(self.__frame9,
                                     text='Выйти',
                                     command=self.__main_window.destroy)

        # упакуем эти две кнопки в 9 рамку
        self.__calc.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем все рамки
        self.__frame1.pack()
        self.__frame2.pack()
        self.__frame3.pack()
        self.__frame4.pack()
        self.__frame5.pack()
        self.__frame6.pack()
        self.__frame7.pack()
        self.__frame8.pack()
        self.__frame9.pack()

        # запустим главный цикл
        tkinter.mainloop()

    def __execute(self):
        # получим данные от пользователя
        svet = float(self.__field2.get())
        voda = float(self.__field3.get())
        gaz = float(self.__field4.get())
        teplo = float(self.__field5.get())
        jek = float(self.__field6.get())
        inet = float(self.__field7.get())

        total = svet + voda + gaz + teplo + jek + inet

        # вызовем обратную функцию
        self.__object.set(total)
