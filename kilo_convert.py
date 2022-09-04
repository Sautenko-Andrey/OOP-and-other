import tkinter
import tkinter.messagebox

class Changer:
    # создадим главное окно интерфейса
    def __init__(self):
        self.__main_wind=tkinter.Tk()

        # создадим три рамки,чтобы сгруппировать эл-ты интерфейса
        self.__top_frame=tkinter.Frame(self.__main_wind)
        self.__mid_frame=tkinter.Frame(self.__main_wind)
        self.__bottom_frame=tkinter.Frame(self.__main_wind)

        # создадим эл-ты интерфейса для верхней рамки
        # текст
        self.__text=tkinter.Label(self.__top_frame,text='Введи расстояние в км:')
        # окно для ввода
        self.__get_km=tkinter.Entry(self.__top_frame,width=15)

        #упакуем эти два элемента
        self.__text.pack(side='left')
        self.__get_km.pack(side='left')

        # создадим эл-ты интерфейса для средней рамки
        self.__middle_text=tkinter.Label(self.__mid_frame,
                                         text='Преобразовано в мили:')
        # объект StringVar нужен для того,чтобы его связать с выходной записью
        self.__result=tkinter.StringVar()

        # создадим надпись Лейбл и свяжем ее с объектом СтрингВар
        self.__miles_value=tkinter.Label(self.__mid_frame,
                                         textvariable=self.__result)

        # упакуем эл-ты интерфейса средней рамки
        self.__middle_text.pack(side='left')
        self.__miles_value.pack(side='left')

        # создадим кнопки для нижней рамки
        # кнопка "Преобразовать"
        self.__execute=tkinter.Button(self.__bottom_frame,
                                      text='Преобразовать',
                                      command=self.__reaction)
        # кнопка "Выход"
        self.__exit=tkinter.Button(self.__bottom_frame,
                                   text='Выход',
                                   command=self.__main_wind.destroy)

        # упакуем эти элементы
        self.__execute.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем все рамки
        self.__top_frame.pack()
        self.__mid_frame.pack()
        self.__bottom_frame.pack()

        # заупстим главный цикл интерфейса
        tkinter.mainloop()

    # программа -преобразователь
    def __reaction(self):
        kilometers=float(self.__get_km.get())
        result=kilometers*0.6214

        self.__result.set(result)

