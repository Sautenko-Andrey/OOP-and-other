import tkinter


class DrawTreeAge:
    def __init__(self):
        # создадим главное окно
        self.__main_window = tkinter.Tk()

        # создадим холст
        self.__holst = tkinter.Canvas(self.__main_window,
                                      width=500,
                                      height=500)

        # нарисуем 5 овалов
        i = 0
        k = 0
        y = 0
        for oval in range(5):
            self.__holst.create_oval(20 + i, 100 + y, 480 - k, 350 - y, width=2)
            i += 10
            k += 50
            y += 10

        # подпишем каждый овал
        self.__holst.create_text(460, 230, text='5 лет')
        self.__holst.create_text(410, 230, text='4 года')
        self.__holst.create_text(360, 230, text='3 года')
        self.__holst.create_text(310, 230, text='2 года')
        self.__holst.create_text(260, 230, text='1 год')

        # упакуем их
        self.__holst.pack()

        # запустим главный цикл
        tkinter.mainloop()
