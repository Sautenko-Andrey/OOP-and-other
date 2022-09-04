import tkinter


class ExitButton:
    def __init__(self):
        self.__window = tkinter.Tk()

        # создадим рамку для кнопк
        self.__frame = tkinter.Frame(self.__window)

        # создадим кнопку выхода
        self.__exit_button = tkinter.Button(self.__frame,
                                            text='Выход',
                                            command=self.__window.destroy)

        # разместим кнопку
        self.__exit_button.pack()

        # упакуем рамку
        self.__frame.pack()

        # запустим гл.цикл
        tkinter.mainloop()
