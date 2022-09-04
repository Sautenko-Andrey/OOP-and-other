import tkinter
import tkinter.messagebox
class Knopka:
    def __init__(self):
        self.__main_window=tkinter.Tk()

        #создадим рамку для кнопки
        self.__button_frame=tkinter.Frame(self.__main_window)

        #создадим саму кнопку
        self.__knopka=tkinter.Button(self.__button_frame,
                                     text='Вычислить',
                                     command=self.__calculate)

        #упакуем кнопку
        self.__knopka.pack(side='top')

        #упакуем рамку
        self.__button_frame.pack()

        #заупстим главный цикл
        tkinter.mainloop()

    #пропишем функцию возврата
    def __calculate(self):
        tkinter.messagebox.showinfo('Итого:','Какой-то результат...')