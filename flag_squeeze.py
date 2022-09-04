import tkinter
import tkinter.messagebox


class Choose:
    def __init__(self):
        self.__main_window = tkinter.Tk()

        # создадим две рамки: одну для элементов Checkbutton
        # и одну для эл-в Button
        self.__top_frame = tkinter.Frame(self.__main_window)
        self.__bottom_frame = tkinter.Frame(self.__main_window)

        # создадим 3 объекта IntVar для использования с эл-ми Checkbutton
        self.__object1 = tkinter.IntVar()
        self.__object2 = tkinter.IntVar()
        self.__object3 = tkinter.IntVar()

        # назначим этим объектам значение 0
        self.__object1.set(0)
        self.__object2.set(0)
        self.__object3.set(0)

        # создадим єл-ті Сheckbutton в рамке top_frame
        self.__checkbuttom1 = tkinter.Checkbutton(self.__top_frame,
                                                  text='A',
                                                  variable=self.__object1)

        self.__checkbuttom2 = tkinter.Checkbutton(self.__top_frame,
                                                  text='B',
                                                  variable=self.__object2)

        self.__checkbuttom3 = tkinter.Checkbutton(self.__top_frame,
                                                  text='C',
                                                  variable=self.__object3)

        # упакуем эти элементы
        self.__checkbuttom1.pack()
        self.__checkbuttom2.pack()
        self.__checkbuttom3.pack()

        # создадим две кнопки в нижней рамки: "Ок" и  "Отмена"
        self.__ok = tkinter.Button(self.__bottom_frame,
                                   text='Ok',
                                   command=self.__backlash)
        self.__no = tkinter.Button(self.__bottom_frame,
                                   text='Exit',
                                   command=self.__main_window.destroy)

        # упаковываем две кнопки в нижнюю рамку
        self.__ok.pack(side='left')
        self.__no.pack(side='left')

        # упаковываем наши две рамки
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        # запускаем главный цикл
        tkinter.mainloop()

    def __backlash(self):
        self.__messege = 'Ты выбрал:\n'

        # определить какой из объектов был выбран и
        # показать соответстующее значение
        if self.__object1.get() == 1:
            self.__messege = self.__messege + 'A\n'
        if self.__object2.get() == 1:
            self.__messege += 'B\n'
        if self.__object3.get() == 1:
            self.__messege += 'C\n'

        # выведем сообщение в инфо-диалог. окне
        tkinter.messagebox.showinfo('Выбор', self.__messege)
