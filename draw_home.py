import tkinter
class Facility:
    def __init__(self):
        #создадим главное окно интерфейса
        self.__main_window=tkinter.Tk()

        #создадим холст
        self.__holst=tkinter.Canvas(self.__main_window,
                                    width=500,
                                    height=500)

        #нарисуем стены дома при помощи прямоугольника
        self.__holst.create_rectangle(50,250,450,450)

        #нарисуем крышу при помощи многоугольника
        self.__holst.create_polygon(25,250,475,250,250,100)

        #наприсуем двери при помощи прямоугольника
        self.__holst.create_rectangle(200,300,300,450)

        #нарисуем 2 окна
        i = 0
        for window in range(2):
            self.__holst.create_rectangle(100+i,300,145+i,350)
            i+=250

        #нарисуем солнышко
        self.__holst.create_oval(400,50,500,150)

        #упакуем холст
        self.__holst.pack()

        #запустим главный цикл
        tkinter.mainloop()

