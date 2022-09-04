import tkinter
import tkinter.messagebox
class Change:
    def __init__(self):
        # создадим главное окно интерфейса
        self.__main_window=tkinter.Tk()

        # создадим две рамки для группирования элементов интерфейса
        self.__top_frame=tkinter.Frame(self.__main_window)
        self.__bottom_frame=tkinter.Frame(self.__main_window)

        # создадим элементы интерфейса для верхней рамки
        self.__request_text=tkinter.Label(self.__top_frame,
                                          text='Введи расстояние в километрах:')
        self.__data_pitch=tkinter.Entry(self.__top_frame,width=10)

        #упакуем элементы верхней рамки
        self.__request_text.pack(side='left')
        self.__data_pitch.pack(side='left')

        # создадим две кнопки в области нижней рамки
        self.__change=tkinter.Button(self.__bottom_frame,
                                     text='Execute',command=self.__reaction)
        self.__exit=tkinter.Button(self.__bottom_frame,
                                   text='Exit',command=self.__main_window.destroy)

        # упакуем эти две кнопки
        self.__change.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем рамки
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        # запускаем главный цикл интерфейса
        tkinter.mainloop()

    # пропишем функцию-реакцию на нажатие кнопки
    def __reaction(self):
        # получим значение, введенное пользователем с клавиатуры
        result=float(self.__data_pitch.get())

        # конвертировать километры в мили
        miles=result*0.6214

        # покажем результаты в информационном диалоговом окне
        tkinter.messagebox.showinfo('Результат: ',str(miles)+'миль')

