import tkinter
import tkinter.messagebox
class Field:
    def __init__(self):
        # создадим главное окно
        self.__window=tkinter.Tk()

        # создадим две рамки
        self.__top_frame=tkinter.Frame(self.__window)
        self.__low_frame = tkinter.Frame(self.__window)

        #создадим два эл-та для верхней рамки
        self.__info_text=tkinter.Label(self.__top_frame,
                                       text='Введи данные: ')

        self.__entry=tkinter.Entry(self.__top_frame,
                                   width=15)

        #упакуем два эл-та
        self.__info_text.pack(side='left')
        self.__entry.pack(side='left')

        #создадим две кнопки для нижней рамки
        self.__execute=tkinter.Button(self.__low_frame,
                                      text='Посчитать',
                                      command=self.__calc)

        self.__exit=tkinter.Button(self.__low_frame,
                                   text='Выход',
                                   command=self.__window.destroy)


        #упакуем эти 2 кнопки
        self.__execute.pack(side='left')
        self.__exit.pack(side='left')

        #упакуем все рамки
        self.__top_frame.pack()
        self.__low_frame.pack()

        #запустим главный цикл
        tkinter.mainloop()

    #пропишем функцию -реакцию
    def __calc(self):
        result=int(self.__entry.get())

        final_result=result*0.75
        #показать результат
        tkinter.messagebox.showinfo('Результат:',str(final_result))