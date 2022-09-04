import tkinter
import tkinter.font


class Text:
    def __init__(self):
        self.__window = tkinter.Tk()

        self.__holst = tkinter.Canvas(self.__window,
                                      width=500, height=500)

        my_font=tkinter.font.Font(family='Helvetica',size=18,
                                  weight='bold',slant='italic',
                                  overstrike=1)
        i=0
        for text in range(75):
            self.__holst.create_text(0+i, 0+i, text='Hello,world!',font=my_font)
            i+=20

        self.__holst.pack()

        tkinter.mainloop()
