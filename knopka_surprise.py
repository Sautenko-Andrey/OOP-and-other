import tkinter
import tkinter.messagebox


class Surprise:
    def __init__(self):
        # создадим главное окно интерфейса
        self.__main_wind = tkinter.Tk()

        # создадим кнопку для главного окна
        self.__button = tkinter.Button(self.__main_wind,
                                       text='Жми,чтобы получить подарок!',
                                       command=self.__get_prise)

        # упакуем и разместим кнопку
        self.__button.pack(side='top')

        # запустим главный цикл
        tkinter.mainloop()

    # напишем функцию-реакцию на нажатие кнопки
    def __get_prise(self):
        tkinter.messagebox.showinfo('Поздравляем! Вы выграли!', '2л "Черниговское светлое!"')
