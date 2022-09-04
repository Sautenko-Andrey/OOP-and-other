# эта программа показывает пустое окно
import tkinter

class MyGUI:
    def __init__(self):
        # создадим элемент интерфейса главного окна
        self.__main_window=tkinter.Tk()

        # войти в главный цикл
        tkinter.mainloop()

# создадим экземпляр класса
main_window=MyGUI()