import tkinter


class SetLines:
    def __init__(self):
        self.__main_window = tkinter.Tk()

        # создадим холст
        self.__holst = tkinter.Canvas(self.__main_window,
                                      width=500,
                                      height=500)

        # нарисуем рисунок с помощью многочисленных линий

        boost = 0
        for line in range(15):
            self.__holst.create_line(0 + boost, 0, 100, 50, 200, 300, 350, 400,smooth=True,width=2)
            boost += 25

        self.__holst.pack()

        tkinter.mainloop()
