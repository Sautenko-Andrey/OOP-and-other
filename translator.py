import tkinter
import tkinter.messagebox


class WordsTranslator:
    def __init__(self):
        # создадим главное окно
        self.__window = tkinter.Tk()

        # создадим две рамки
        self.__top_frame = tkinter.Frame(self.__window)
        self.__bottom_frame = tkinter.Frame(self.__window)

        # создадим объект StringVar
        self.__result = tkinter.StringVar()

        # создадим надпись Лейбл и свяжем ее с объектом СтрингВар
        self.__text = tkinter.Label(self.__top_frame,
                                    textvariable=self.__result)

        # упакуем элемент
        self.__text.pack(side='top')

        # создадим эл-ты интерфейса для нижней рамки
        self.__word1 = tkinter.Button(self.__bottom_frame,
                                      text='One',
                                      command=self.__first_word)

        self.__word2 = tkinter.Button(self.__bottom_frame,
                                      text='Two',
                                      command=self.__sec_word)

        self.__word3 = tkinter.Button(self.__bottom_frame,
                                      text='Three',
                                      command=self.__third_word)

        # упакуем эти элементы
        self.__word1.pack(side='left')
        self.__word2.pack(side='left')
        self.__word3.pack(side='left')

        # упакуем рамки
        self.__top_frame.pack()
        self.__bottom_frame.pack()

        # запустим цикл
        tkinter.mainloop()

    def __first_word(self):
        self.__result.set('Один')

    def __sec_word(self):
        self.__result.set('Два')

    def __third_word(self):
        self.__result.set('Три')
