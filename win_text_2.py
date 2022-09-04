# класс создает окно и дваэлемента интерфейса лэйбл
import tkinter
class MyGUI:
    def __init__(self):
        # создадим корневой элемент интерфейса
        self.__main_window=tkinter.Tk()

        # создадим элемент интерфейса лэйбл, который будет относиться
        # корневому элементу
        self.__text_1=tkinter.Label(self.__main_window,text='---This is GUI---')
        self.__text_2=tkinter.Label(self.__main_window,text='|by Andrey|')

        # вызовем методы,показывающие эти два элемента интерфейса
        self.__text_1.pack()
        self.__text_2.pack()

        # запускаем бесконечный главный цикл
        tkinter.mainloop()

