import tkinter
import tkinter.messagebox

class Start:
    def __init__(self):
        # создаем главное окно интерфейса
        self.__main_wind=tkinter.Tk()

        # создаем кнопку
        self.__knopka=tkinter.Button(self.__main_wind,text='START!',command=self.__reaction)

        # создаем кнопку-выход
        self.__exit=tkinter.Button(self.__main_wind,text='Exit',command=self.__main_wind.destroy)

        # пропишем текст слева
        self.__text=tkinter.Label(self.__main_wind,text='Good luck!')

        # укомплектуем кнопки
        self.__knopka.pack(side='top')
        self.__exit.pack(side='bottom')
        # укомплекуем надпись
        self.__text.pack(side='left')

        # заупсктим главный цикл
        tkinter.mainloop()
    # пропишем функцию-реакцию на кнопку
    def __reaction(self):
        tkinter.messagebox.showinfo('Championshp is begin!','GO-GO!')

