class Magazin:
    'Класс для работы с вещами в магазине.'
    def __init__(self,name,article):
        self.name=name
        self.article=article

    def save_items(self,sklad,name,article):
        print('Создаем склад товаров с артикулами')
        self.sklad={}
        self.sklad[name]=article
        return self.sklad
