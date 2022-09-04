import tkinter
class Text:
    def __init__(self):
        #создадим главное окно
        self.__window=tkinter.Tk()

        #создадим рамку
        self.__frame=tkinter.Frame(self.__window)

        #создадим два эл-иа Лейбл
        self.__label1=tkinter.Label(self.__frame,
                                    text='Hello,')

        self.__label2=tkinter.Label(self.__frame,
                                    text='world!')

        # упакуем эти эл-ты
        self.__label1.pack(side='left')
        self.__label2.pack(side='left')

        #упакуем рамку
        self.__frame.pack()

        #запустим главный цикл
        tkinter.mainloop()
