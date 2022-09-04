import tkinter
import tkinter.messagebox
class Info:
    def __init__(self):
        #создадим главное окно интерфейса
        self.__window=tkinter.Tk()

        #создадим рамку
        self.__frame=tkinter.Frame(self.__window)

        #создадим две кнопки
        self.__show_info=tkinter.Button(self.__frame,
                                        text='Показать инфо',
                                        command=self.__execute)

        self.__exit=tkinter.Button(self.__frame,
                                   text='Выйти',
                                   command=self.__window.destroy)

        #упакуем кнопки
        self.__show_info.pack(side='left')
        self.__exit.pack(side='left')

        #упакуем рамку
        self.__frame.pack(side='bottom')

        #запустим главный цикл
        tkinter.mainloop()

    #создадим фуекцию-ответку
    def __execute(self):
        tkinter.messagebox.showinfo(' ','Турция\nг.Анталия,п.Гойнюк\nотель "Топ Капы"\n')
