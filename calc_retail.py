import tkinter
import tkinter.messagebox
class RetailPrice:
    def __init__(self):
        #создадим главное окно интерфейса
        self.__main_window=tkinter.Tk()

        #создадим три рамки
        self.__top_fr=tkinter.Frame(self.__main_window)
        self.__mid_fr = tkinter.Frame(self.__main_window)
        self.__bott_fr = tkinter.Frame(self.__main_window)

        # создадим эл-ты для верхней рамки(текст+поле для ввода)
        # текс
        self.__request_text=tkinter.Label(self.__top_fr,
                                          text='Введи оптовую цену: ')
        # поле для ввода
        self.__info_field=tkinter.Entry(self.__top_fr,width=15)

        # упакуем эти данные в верхнюю рамку
        self.__request_text.pack(side='left')
        self.__info_field.pack(side='left')

        # создадим эл-ты интерфейса для средней рамки
        # текст
        self.__mid_text=tkinter.Label(self.__mid_fr,
                                      text='Преобразовано в ретейл: ')
        # создадим объект StringVar
        self.__object=tkinter.StringVar()

        # создадим надпись лейбл  свяжем с объектом
        self.__result=tkinter.Label(self.__mid_fr,
                                    textvariable=self.__object)

        # упакуем эл-ты в среднюю рамку
        self.__mid_text.pack(side='left')
        self.__result.pack(side='left')

        # создадим элементы для нижней рамки(две кнопки)
        # кнопка "Выполнить"
        self.__execute=tkinter.Button(self.__bott_fr,
                                      text='Рассчитать!',
                                      command=self.__doit)
        # кнопка "Выход"
        self.__exit=tkinter.Button(self.__bott_fr,
                                   text='Выйти',
                                   command=self.__main_window.destroy)

        # упакуем эл-ты в нижнюю рамку
        self.__execute.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем все три рамки
        self.__top_fr.pack()
        self.__mid_fr.pack()
        self.__bott_fr.pack()

        # запустим главный цикл
        tkinter.mainloop()

    def __doit(self):
        # получим инфу от пользователя
        opt=float(self.__info_field.get())

        # посчитаем
        result=opt+(opt*0.25)

        self.__object.set(result)

