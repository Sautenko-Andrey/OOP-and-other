import tkinter
class Task_1:
    def __init__(self):
        self.__window=tkinter.Tk()

        self.__text=tkinter.Label(self.__window,
                                  text='Программировать-это круто!')

        self.__text.pack()

        tkinter.mainloop()
