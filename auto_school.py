import tkinter
import tkinter.messagebox


class Test:
    def __init__(self):
        # главное окно интерфейса
        self.__window = tkinter.Tk()

        # создадим 3 рамки
        self.__quest_frame = tkinter.Frame(self.__window)
        self.__top_frame = tkinter.Frame(self.__window)
        self.__bottom_frame = tkinter.Frame(self.__window)

        # пропишем вопрос для первой рамки
        self.__question = tkinter.Label(self.__quest_frame,
                                        text='Какой знак изображен?')

        # упакуем элемент в рамку
        self.__question.pack(side='left')

        # пропишем эл-ты для верхней рамки
        # создадим объект
        self.__object = tkinter.IntVar()

        # назначим объекту значение
        self.__object.set(1)

        # пропишем три варианта выбора
        self.__first = tkinter.Radiobutton(self.__top_frame,
                                           text='Уступить дорогу',
                                           variable=self.__object,
                                           value=1,
                                           command=self.__first_choice)

        self.__sec = tkinter.Radiobutton(self.__top_frame,
                                         text='Стоп',
                                         variable=self.__object,
                                         value=2)

        self.__third = tkinter.Radiobutton(self.__top_frame,
                                           text='Главная дорога',
                                           variable=self.__object,
                                           value=3)

        # упакуем эти три эл-та в рамку
        self.__first.pack(side='top')
        self.__sec.pack(side='top')
        self.__third.pack(side='top')

        # пропишем кнопки "ОК" и "ОТМЕНА"
        self.__ok = tkinter.Button(self.__bottom_frame,
                                   text='OK',
                                   command=self.__backlash)

        self.__no = tkinter.Button(self.__bottom_frame,
                                   text='Отмена',
                                   command=self.__window.destroy)

        # упакуем эти два эл-та в рамки
        self.__ok.pack(side='left')
        self.__no.pack(side='left')

        # упакуем эти рамки
        self.__quest_frame.pack()
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        # запустим гл.цикл
        tkinter.mainloop()

    # функция обратка
    def __backlash(self):
        tkinter.messagebox.showinfo('Выбор',
                                    'Твой выбор: ' + str(self.__object.get()))

    def __first_choice(self):
        tkinter.messagebox.showinfo('Результат: ', 'Правильно!')
