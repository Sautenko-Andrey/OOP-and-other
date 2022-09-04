# этот класс создает надписи в двух разных рамках
import tkinter


class MyGUI:
    def __init__(self):
        # создадим элемент интерфейса главного окна
        self.__main_window = tkinter.Tk()

        # создадим две рамки: одну для верхней части окна,другую для нижней
        self.__top_frame = tkinter.Frame(self.__main_window)
        self.__bottom_frame = tkinter.Frame(self.__main_window)

        # создадим три элемента интерфейса Лэйбл для верхней рамки
        self.__text_1 = tkinter.Label(self.__top_frame, text='1.Для верхней рамки')
        self.__text_2 = tkinter.Label(self.__top_frame, text='2.Для верхней рамки')
        self.__text_3 = tkinter.Label(self.__top_frame, text='3.Для верхней рамки')

        # упакуем эти 3 эл-та и определим их положение сверху
        self.__text_1.pack(side='left')
        self.__text_2.pack(side='left')
        self.__text_3.pack(side='left')

        # теперь создадим два элемента Лэйбл для нижней рамки
        self.__text_down = tkinter.Label(self.__bottom_frame, text='1.для нижней рамки')
        self.__text_down_2 = tkinter.Label(self.__bottom_frame, text='2.для нижней рамки')

        # упакуем эти 2 эл-та и определим их положение снизу
        self.__text_down.pack(side='left')
        self.__text_down_2.pack(side='left')

        # также мы должны упаковать сами рамки!!!
        self.__top_frame.pack(side='top')
        self.__bottom_frame.pack(side='bottom')

        # запустим главный цикл
        tkinter.mainloop()
