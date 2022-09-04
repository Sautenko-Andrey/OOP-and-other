# этот класс демонстрирует элемент интерфейса Button
import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # создадим главное окно
        self.__main_window = tkinter.Tk()

        # создадим эл-т интерфейса Button widget
        # на кнопке появится текст "Нажми меня!"
        # при нажатии кнопки должен быть исполнен
        # метод do_something
        self.__my_button = tkinter.Button(self.__main_window,
                                          text='Нажми меня!', command=self.do_something)

        # упакуем элемент интерфейса
        self.__my_button.pack()

        # запустим главный цикл
        tkinter.mainloop()

        # метод do_something является функцией обратного
        # вызова для эл-та интерфейса Button

    def do_something(self):
        # покажем информационное диалоговое окно
        tkinter.messagebox.showinfo('Реакция', 'Благодарю,что нажали кнопку!')
