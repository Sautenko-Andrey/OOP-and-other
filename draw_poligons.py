import tkinter

COORDINATS = (150, 150, 200, 130, 300, 170, 300, 220)


class Polygon:
    def __init__(self):
        self.__window = tkinter.Tk()

        self.__holst = tkinter.Canvas(self.__window,
                                      width=500,
                                      height=500)

        self.__holst.create_polygon(COORDINATS,fill='blue')

        self.__holst.pack()

        tkinter.mainloop()
