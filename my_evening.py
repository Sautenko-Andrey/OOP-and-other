import tkinter
import tkinter.messagebox

class MyEvent:
    def __init__(self):
        self.__main_wind=tkinter.Tk()

        # создадим 2 рамки
        self.__fr1=tkinter.Frame(self.__main_wind)
        self.__fr2 = tkinter.Frame(self.__main_wind)

        # создадим эл-ты для первой рамки
        # создадим объект IntVar
        self.__object=tkinter.IntVar()

        # зададим ему начальное значение
        self.__object.set(1)

        # создадим эл-ты Радио
        self.__first=tkinter.Radiobutton(self.__fr1,
                                         text='Волейбол',
                                         variable=self.__object,
                                         value=1)

        self.__sec = tkinter.Radiobutton(self.__fr1,
                                           text='Пиво+рыба',
                                           variable=self.__object,
                                           value=2)

        self.__third = tkinter.Radiobutton(self.__fr1,
                                           text='Кино надиване',
                                           variable=self.__object,
                                           value=3)

        # упакуем элементы
        self.__first.pack()
        self.__sec.pack()
        self.__third.pack()

        # создадим кнопки
        self.__knopka=tkinter.Button(self.__fr2,
                                     text='OKEY',
                                     command=self.__choose)
        self.__vihod=tkinter.Button(self.__fr2,
                                    text='Выходим',
                                    command=self.__main_wind.destroy)

        # пакуем эти элементы
        self.__knopka.pack(side='left')
        self.__vihod.pack(side='left')

        # пакуем рамки
        self.__fr1.pack()
        self.__fr2.pack()

        # вызываем главный цикл
        tkinter.mainloop()

    def __choose(self):
        tkinter.messagebox.showinfo('Планы на вечер?','Твой выбор: '+str(self.__object.get()))

