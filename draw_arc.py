import tkinter
COORDINATS=(100,100,350,350)
class DrawArc:
    def __init__(self):
        #создадим главное окно
        self.__main_window=tkinter.Tk()

        #создадим холст
        self.__holst=tkinter.Canvas(self.__main_window,
                                    width=500,
                                    height=500)

        #нарисуем дугу
        self.__holst.create_arc(COORDINATS,start=90,extent=75,
                                fill='orange',outline='blue',
                                width=3)

        self.__holst.create_arc(COORDINATS,start=165,extent=25,
                                fill='red',outline='green',
                                width=3)

        self.__holst.create_arc(COORDINATS, start=190, extent=60,
                                fill='brown', outline='yellow',
                                width=3)

        self.__holst.create_arc(COORDINATS, start=250, extent=200,
                                fill='violet', outline='black',
                                width=3)



        #упакуем холст
        self.__holst.pack()

        #вызовем главный цикл
        tkinter.mainloop()
