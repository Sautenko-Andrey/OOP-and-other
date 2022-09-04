# этот класс создает окно и надпись с текстом
import tkinter

class MyGUI:
    def __init__(self):
        # создадим коневой элемент интерфейса
        self.__main_window=tkinter.Tk()

        #создадим элемент интерфейса,содержащий надпись
        self.__text=tkinter.Label(self.__main_window,text='Привет, Андрей!')

        # вызовем метод pack для элемента интерфейса Label
        self.__text.pack()

        # запустим главный цикл
        tkinter.mainloop()
