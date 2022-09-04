import tkinter
import tkinter.messagebox
class SchoolTest:
    def __init__(self):
        # создадим гл.окно
        self.__window=tkinter.Tk()

        #создадим две рамки для эл-в интерфейса
        self.__hello_frame=tkinter.Frame(self.__window)
        self.__top_frame=tkinter.Frame(self.__window)
        self.__bottom_frame = tkinter.Frame(self.__window)

        # создадим приветственнуюнадпись в начале программы
        self.__text=tkinter.Label(self.__hello_frame,
                           text='Выбери правильный вариант: ')

        #упакуем элемент в рамку
        self.__text.pack(side='top')

        #создадим два объекта IntVar
        self.__obj1=tkinter.IntVar()
        self.__obj2 = tkinter.IntVar()

        #зададим значение 0 для каждого объекта
        self.__obj1.set(0)
        self.__obj2.set(0)

        #создадим флаговые элементы для первой рамки
        #и привяжем их к объектам
        self.__first=tkinter.Checkbutton(self.__top_frame,
                                         text='1',
                                         variable=self.__obj1)

        self.__sec = tkinter.Checkbutton(self.__top_frame,
                                           text='2',
                                           variable=self.__obj2)

        #упакуем эти два элемента
        self.__first.pack()
        self.__sec.pack()

        #создадим эл-ты для второй рамки( 2 кнопки "ОК" и "ВЫХОД")
        self.__ok=tkinter.Button(self.__bottom_frame,
                                 text='ОК',
                                 command=self.__backlash)

        self.__exit=tkinter.Button(self.__bottom_frame,
                                   text='Выход',
                                   command=self.__window.destroy)

        #упаковываем эти элементы в нижнюю рамку
        self.__ok.pack(side='left')
        self.__exit.pack(side='left')

        #упаковываем рамки
        self.__hello_frame.pack()
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        #запускаем цикл
        tkinter.mainloop()

    #функция возврата
    def __backlash(self):

        text='Ты выбрал:\n'

        # покажем варианты
        if self.__obj1.get()==1:
            text+='1\n'
        if self.__obj2.get()==1:
            text+='2\n'

        # выведем результат
        tkinter.messagebox.showinfo('Результат',text)


