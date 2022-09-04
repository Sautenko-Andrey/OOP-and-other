import tkinter

class MyGUI:
    def __init__(self):
        #создадим главное окно
        self.__main_window=tkinter.Tk()

        # создадим 2 рамки
        self.__frame1=tkinter.Frame(self.__main_window)
        self.__frame2=tkinter.Frame(self.__main_window)

        # создадим 2 эл-та Label для первой рамки
        self.__text1=tkinter.Label(self.__frame1,text='Север')
        self.__text11=tkinter.Label(self.__frame1,text='холодно здесь...')

        # упакуем эти 2 элемента и определим их положение
        self.__text1.pack(side='top')
        self.__text11.pack(side='top')

        # создадим 2 эл-та для второй рамки
        self.__text2=tkinter.Label(self.__frame2,text='Юг')
        self.__text22=tkinter.Label(self.__frame2,text='здесь жарко...')

        # упакуем эти 2 элемента и определим их положение
        self.__text2.pack(side='top')
        self.__text22.pack(side='top')

        # упакуем сами рамки и определим их положение
        self.__frame1.pack(side='top')
        self.__frame2.pack(side='bottom')

        # запустим главный цикл
        tkinter.mainloop()






