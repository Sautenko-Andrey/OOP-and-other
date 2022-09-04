import tkinter
import tkinter.messagebox

class Beer:
    def __init__(self):
        # создадим главное окно интерфейса
        self.__main_window=tkinter.Tk()

        # создадим две рамки (нижнюю и верхнюю)
        # верхняя рамка
        self.__top_frame=tkinter.Frame(self.__main_window)
        #нижняя рамка
        self.__bottom_frame=tkinter.Frame(self.__main_window)

        # создадим элементы для верхней рамки (текст + кнопка)
        # текс с вопросом
        self.__require=tkinter.Label(self.__top_frame,
                                     text='Введи количество бутылок: ')
        #кнопка
        self.__knopka=tkinter.Entry(self.__top_frame,width=15)

        # упакуем эти элементы
        self.__require.pack(side='left')
        self.__knopka.pack(side='left')

        # создадим элементы для нижней рамки
        # кнопка "Выполнить операцию"
        self.__execute=tkinter.Button(self.__bottom_frame,
                                      text='Execute',
                                      command=self.__doit)
        # кнопка выхода
        self.__exit=tkinter.Button(self.__bottom_frame,
                                   text='Exit',
                                   command=self.__main_window.destroy)

        # упакуем эти две кнопки
        self.__execute.pack(side='left')
        self.__exit.pack(side='left')

        # упакуем рамки
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        #запустим главный цикл интерфейса
        tkinter.mainloop()

    # создадим программу подсчета
    def __doit(self):
        # получим данніе от пользователя
        bottles=int(self.__knopka.get())

        #преобразуем данные
        liters=bottles*0.5

        # выведем инфу
        tkinter.messagebox.showinfo('Результат',str(liters)+'л')