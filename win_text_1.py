# класс который создает главное окно и пишет текст
import tkinter
class MyGUI:
    def __init__(self):
        # создадим корневой элемент интерфейса
        self.__main_window=tkinter.Tk()

        # создадим элемент текста
        self.__text=tkinter.Label(self.__main_window,text='=\ARSENAL=/')

        # создадим пак
        self.__text.pack()

        # запустим главный цикл
        tkinter.mainloop()

