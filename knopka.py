import tkinter
import tkinter.messagebox

class Knopa:
    def __init__(self):
        #создадим главное окно
        self.__main_window=tkinter.Tk()

        # создадим элемент Баттон для кнопки
        self.__button=tkinter.Button(self.__main_window,
                                     text='Любишь пиво?!',
                                     command=self.__reaction)

        # упакуем элемент интерфейса и определим его местоположение
        self.__button.pack(side='left')

        # запустим главный цикл
        tkinter.mainloop()

    # пропишем функцию-раекцию на нажатие кнопки
    def __reaction(self):
        tkinter.messagebox.showinfo('Реакция','ХАХАХА!')