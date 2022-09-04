import tkinter
import tkinter.messagebox

class Bar:
    def __init__(self):
        # создаем главное окно интерфейса
        self.__main_wind=tkinter.Tk()

        # создаем виджет (кнопку "Заходим в бар")
        self.__go_bar=tkinter.Button(self.__main_wind,
                                     text='Заходим в БАР!',
                                     command=self.__inside_bar)


        # создаем еще один виджет (кнопку "Уходим")
        self.__exit_bar=tkinter.Button(self.__main_wind,
                                       text='Уходим...',
                                       command=self.__main_wind.destroy)

        # упаковываем кнопки
        self.__go_bar.pack(side='top')
        self.__exit_bar.pack(side='top')

        # запускаем главный цикл интерфейса
        tkinter.mainloop()

    # напишем функцию-реакцию на нажатие кнопки
    def __inside_bar(self):
        tkinter.messagebox.showinfo('Бармен:','Правильный выбор! А теперь давай нажремся:)')