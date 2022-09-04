import tkinter
class DrawRectangle:
    def __init__(self):
        #создадим главное окно
        self.__main_window=tkinter.Tk()

        #создадим холст
        self.__holst=tkinter.Canvas(self.__main_window,
                                    width=500,
                                    height=500)

        #нарисуем прямоугольник
        boost=0
        for rec in range(25):
            self.__holst.create_rectangle(50+boost,50+boost,200+boost,200+boost,
                                          outline='blue',width=3)
            boost+=10

        #упакуем холст
        self.__holst.pack()

        #цикл
        tkinter.mainloop()