import tkinter
class MyGUI:
    def __init__(self):
        # создадим корневой элемент интерфейса
        self.__main_window=tkinter.Tk()

        # добавим текст в корневой элемент интерфейса
        self.__text_1=tkinter.Label(self.__main_window,text='WEST')
        self.__text_2=tkinter.Label(self.__main_window,text='NORTH')
        self.__text_3=tkinter.Label(self.__main_window,text='EAST')
        self.__text_4=tkinter.Label(self.__main_window,text='SOUTH')

        # покажем и определим месторасположения текстов
        self.__text_1.pack(side='left')
        self.__text_2.pack(side='top')
        self.__text_3.pack(side='right')
        self.__text_4.pack(side='bottom')

        # запустим главный цикл интерфейса
        tkinter.mainloop()

