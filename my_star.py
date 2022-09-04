import tkinter
class DrawMyStar:
    def __init__(self):
        # пропишем главное окно
        self.__main_window=tkinter.Tk()

        #пропишем холст
        self.__holst=tkinter.Canvas(self.__main_window,
                                    width=500,
                                    height=500)

        #нарисуем звезду с помощью многоугольника
        self.__holst.create_polygon(230,250,250,200,275,250,325,250,275,300,300,350,)

        #упакуем холст
        self.__holst.pack()

        #запустим главный цикл
        tkinter.mainloop()