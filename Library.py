class Books:
    def __init__(self,name):
        self.__name=name

    def show_name(self):
        print('Вид книг:',self.__name)

    def about_what(self):
        print('Здесь о чем-то рассказывают...')

class Travel_book(Books):
    def __init__(self):
        Books.__init__(self,'Книги про путешествия!')

    def about_what(self):
        print('Описываются путешествия отважных и интересных людей.')

class Education_book(Books):
    def __init__(self):
        Books.__init__(self,'Обучающие книги!')

    def about_what(self):
        print('Эти книги чему-то полезному обучают.')

class Romantic_book(Books):
    def __init__(self):
        Books.__init__(self,'Романтические книги!')

    def about_what(self):
        print('Книги про любовь и романтику.')

