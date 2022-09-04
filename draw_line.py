import tkinter
class Line:
    'Программа,рисующая линию'
    def __init__(self):
        # создадим главное окно интерфейса
        self.__main_window=tkinter.Tk()

        #создадим эл-т интерфейса Canvas (т.е. холст,на котором будем рисовать)
        self.__canvas=tkinter.Canvas(self.__main_window,
                                     width=200,
                                     height=200)
        #нарисуем 2 прямые линии
        self.__canvas.create_line(0,0,199,199)
        self.__canvas.create_line(199,0,0,199)

        #упакуем холст
        self.__canvas.pack()

        #запустим главный цикл интерфейса
        tkinter.mainloop()

