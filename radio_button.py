import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # создадим главное окно интерфейса
        self.__main_window = tkinter.Tk()

        # создадим две рамки
        # рамка для элементов Радио
        self.__top_frame = tkinter.Frame(self.__main_window)
        # рамка для элементов Button
        self.__bottom_frame = tkinter.Frame(self.__main_window)

        # создадим объект IntVar для использования с эл-ми Radiobutton
        self.__radio = tkinter.IntVar()
        # назначить объекту IntVar значение 2
        self.__radio.set(2)

        # создадим эл-ты Radiobutton  в рамке top_frame
        self.__el1 = tkinter.Radiobutton(self.__top_frame,
                                         text='Вариант 1',
                                         variable=self.__radio,
                                         value=1)
        # создадим эл-ты Radiobutton  в рамке top_frame
        self.__el2 = tkinter.Radiobutton(self.__top_frame,
                                         text='Вариант 2',
                                         variable=self.__radio,
                                         value=2)

        # упакуем эти 2 элемента
        self.__el1.pack()
        self.__el2.pack()

        # создадим кнопки "ОК" и "Выйти" для нижней рамки
        self.__ok = tkinter.Button(self.__bottom_frame,
                                   text='OK',
                                   command=self.__show_choice)

        self.__exit = tkinter.Button(self.__bottom_frame,
                                     text='Exit',
                                     command=self.__main_window.destroy)

        # упакуем эти два элемента
        self.__ok.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем 2 рамки
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        # запускаем главный цикл
        tkinter.mainloop()

    def __show_choice(self):
        tkinter.messagebox.showinfo('Выбор ', 'Выбран вариант' + str(self.__radio.get()))
