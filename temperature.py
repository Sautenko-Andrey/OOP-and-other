import tkinter
import tkinter.messagebox
class Farentgate:
    def __init__(self):
        #создадим главное окно
        self.__main_window=tkinter.Tk()

        #создадим 3 рамки
        # рамка для получения информации от пользователя
        self.__take_info_frame=tkinter.Frame(self.__main_window)
        #рамка для вывода результата
        self.__get_info_frame = tkinter.Frame(self.__main_window)
        #рамка для кнопок "Перевести" и "Выйти"
        self.__buttons_frame = tkinter.Frame(self.__main_window)

        #пропишем элементы для первой рамки
        self.__question_text=tkinter.Label(self.__take_info_frame,
                                           text='Введите температуру в градусах Цельсия: ')

        self.__entry=tkinter.Entry(self.__take_info_frame,width=15)

        #упакуем элементы
        self.__question_text.pack(side='left')
        self.__entry.pack(side='left')

        #пропишем элементы для второй рамки
        #текст вывода
        self.__show_text=tkinter.Label(self.__get_info_frame,
                                       text='Температура по шкале Фаренгейта: ')

        #создадим объект StringVar
        self.__object=tkinter.StringVar()

        #создадим надпись и привяжем ее к объекту
        self.__result=tkinter.Label(self.__get_info_frame,
                                    textvariable=self.__object)

        #упакуем эти элементы
        self.__show_text.pack(side='left')
        self.__result.pack(side='left')

        #создадим кнопки для нижней рамки
        self.__change=tkinter.Button(self.__buttons_frame,
                                     text='Преобразовать',
                                     command=self.__execute)

        self.__exit=tkinter.Button(self.__buttons_frame,
                                     text='Выйти',
                                     command=self.__main_window.destroy)

        #упакуем кнопки
        self.__change.pack(side='left')
        self.__exit.pack(side='left')

        #упакуем все рамки
        self.__take_info_frame.pack()
        self.__get_info_frame.pack()
        self.__buttons_frame.pack()

        #запустим главный цикл
        tkinter.mainloop()

    # функция=ответ
    def __execute(self):
        #получим данные от пользователя
        celciy=float(self.__entry.get())

        #преобразуем в фарентгейты
        result=((9/5)*celciy)+32

        #вывести результат
        self.__object.set(result)
