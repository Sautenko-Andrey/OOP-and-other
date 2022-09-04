import tkinter


class DrawLine:
    def __init__(self):
        # создаем главное окно
        self.__main_window = tkinter.Tk()

        # создаем холст
        self.__holst = tkinter.Canvas(self.__main_window,
                                      width=200,
                                      height=200)

        # нарисуем линии с помощью цикла
        i = 0
        for line in range(10):
            self.__holst.create_line(0 + i, 0, 199, 199)
            i += 25

        i = 0
        for line in range(10):
            self.__holst.create_line(0, 0 + i, 199, 199)
            i += 25

        # упакуем холст
        self.__holst.pack()

        # вызовем главный цикл интерфейса
        tkinter.mainloop()
