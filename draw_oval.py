import tkinter
COORDINATS=(0,0,500,500)
class Oval:
    def __init__(self):
        #напишем гл.окно
        self.__window=tkinter.Tk()

        #напишем холст
        self.__holst=tkinter.Canvas(self.__window,
                                    width=500,
                                    height=500)

        #нарисуем овалы
        i=0
        for oval in range(25):
            self.__holst.create_oval(0+i,0,500,500,fill='red')
            i+=10

        #упакуем холст
        self.__holst.pack()

        #цикл
        tkinter.mainloop()