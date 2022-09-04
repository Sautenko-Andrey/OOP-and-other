class Buhlo:
    'Класс для работы с бухлом'
    def count_beer(self,name,price,kolichestvo):
        self.name=name
        self.price=price
        self.kolichestvo=kolichestvo
        return self.kolichestvo*self.price

    def get_beer(self):
        return(self.name,self.price,self.kolichestvo)

    def beer_control(self,kolichestvo):
        gran=8
        minimum=5
        if kolichestvo>gran:
            return print('Ты будешь пьян в жопу')
        elif kolichestvo<gran and kolichestvo>minimum:
            return print('Ты будешь в норме!')
        else:
            return print('Ты будешь трезв!')

