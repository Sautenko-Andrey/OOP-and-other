import tkinter
import tkinter.messagebox


class Test:
    def __init__(self):
        # создадим главное окно интерфейса
        self.__main_window = tkinter.Tk()

        # создадим две рамки
        self.__top_frame = tkinter.Frame(self.__main_window)
        self.__bottom_frame = tkinter.Frame(self.__main_window)

        # создадим объект IntVar для использования с эл-ми Radiobutton
        self.__object = tkinter.IntVar()

        # зададим значение этому объекту(стртовая позиция)
        self.__object.set(1)

        # создадим эл-ты Radiobutton для первой рамки(3 шт)
        self.__first = tkinter.Radiobutton(self.__top_frame,
                                           text='Пиво',
                                           variable=self.__object,
                                           value=1)

        self.__second = tkinter.Radiobutton(self.__top_frame,
                                            text='Водка',
                                            variable=self.__object,
                                            value=2)

        self.__third = tkinter.Radiobutton(self.__top_frame,
                                           text='Коньяк',
                                           variable=self.__object,
                                           value=3)

        # упакуем эти три элемента в рамку
        self.__first.pack()
        self.__second.pack()
        self.__third.pack()

        # создадим кнопки в нижней рамке
        self.__execute = tkinter.Button(self.__bottom_frame,
                                        text='ОК',
                                        command=self.__react)

        self.__exit = tkinter.Button(self.__bottom_frame,
                                     text='Выход',
                                     command=self.__main_window.destroy)

        # упакуем эти кнопки
        self.__execute.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем две рамки
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        # запустим главный цикл
        tkinter.mainloop()

    # пропишем программу-реакцию
    def __react(self):
        tkinter.messagebox.showinfo('Тебе нужно выбрать пиво: ', 'Выбор: ' + str(self.__object.get()))
