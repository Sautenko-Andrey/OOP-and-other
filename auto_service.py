import tkinter
import tkinter.messagebox


class AutoRepair:
    def __init__(self):
        # создадим гл.окно интерфейса
        self.__main_window = tkinter.Tk()

        # создадим 2 рамки
        self.__top_frame = tkinter.Frame(self.__main_window)
        self.__bottom_frame = tkinter.Frame(self.__main_window)

        # создадим 7 объектов IntVar для использования
        # с эд-ми Checkbutton
        self.__object1 = tkinter.IntVar()
        self.__object2 = tkinter.IntVar()
        self.__object3 = tkinter.IntVar()
        self.__object4 = tkinter.IntVar()
        self.__object5 = tkinter.IntVar()
        self.__object6 = tkinter.IntVar()
        self.__object7 = tkinter.IntVar()

        # назначим им значение 0
        self.__object1.set(0)
        self.__object2.set(0)
        self.__object3.set(0)
        self.__object4.set(0)
        self.__object5.set(0)
        self.__object6.set(0)
        self.__object7.set(0)

        # создадим эл-ты Checkbutton в рамке top_frame
        self.__zamena_masla = tkinter.Checkbutton(self.__top_frame,
                                                  text='Замена масла-500 грн',
                                                  variable=self.__object1)

        self.__smazka = tkinter.Checkbutton(self.__top_frame,
                                            text='Смазочные работы-300 грн',
                                            variable=self.__object2)

        self.__promivka_radiatora = tkinter.Checkbutton(self.__top_frame,
                                                        text='Промывка радиатора-700 грн',
                                                        variable=self.__object3)

        self.__zamena_transmisii = tkinter.Checkbutton(self.__top_frame,
                                                       text='Замена жидкости в трансмиссии-1000 грн',
                                                       variable=self.__object4)

        self.__osmotr = tkinter.Checkbutton(self.__top_frame,
                                            text='Осмотр-800 грн',
                                            variable=self.__object5)

        self.__zamena_glushitela = tkinter.Checkbutton(self.__top_frame,
                                                       text='Замена глушителя выхлопа-1300 грн',
                                                       variable=self.__object6)

        self.__perestanovka_shin = tkinter.Checkbutton(self.__top_frame,
                                                       text='Перестановка шин-1300 грн',
                                                       variable=self.__object7)

        # упакуем все эти элементы
        self.__zamena_masla.pack()
        self.__smazka.pack()
        self.__promivka_radiatora.pack()
        self.__zamena_transmisii.pack()
        self.__osmotr.pack()
        self.__zamena_glushitela.pack()
        self.__perestanovka_shin.pack()

        # создадим 2 кнопки для нижней рамки
        self.__doit = tkinter.Button(self.__bottom_frame,
                                     text='Показать стоимость',
                                     command=self.__execute)

        self.__exit = tkinter.Button(self.__bottom_frame,
                                     text='Выйти',
                                     command=self.__main_window.destroy)

        # упакуем эл-ты
        self.__doit.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем рамки
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        # запустим главный цикл
        tkinter.mainloop()

    # пропишем программу-реакцию
    def __execute(self):
        # строковое сообщение
        self.__messege = 'Ваши затраты = '
        # зададим значения для каждой услуги
        zam_masla = 500.00
        smaz_raboti = 300.00
        promiv_radiator = 700.00
        zamena_trans = 1000.00
        osmotr = 800.00
        zamena_glushitela = 1300.00
        perestanovka_shin = 1300.00

        # посчитаем услуги
        total = 0
        if self.__object1.get() == 1:
            total += zam_masla
        if self.__object2.get() == 1:
            total += smaz_raboti
        if self.__object3.get() == 1:
            total += promiv_radiator
        if self.__object4.get() == 1:
            total += zamena_trans
        if self.__object5.get() == 1:
            total += osmotr
        if self.__object6.get() == 1:
            total += zamena_glushitela
        if self.__object7.get() == 1:
            total += perestanovka_shin

        tkinter.messagebox.showinfo('Общая стоимость', 'Ваши затраты = ' + str(total) + 'грн')
