class Human:
    def __init__(self,name,position,id):
        self.__name=name
        self.__position=position
        self.__id=id

    def set_name(self,name):
        self.__name=name

    def set_position(self,position):
        self.__position=position

    def set_id(self,id):
        self.__id=id

    def get_name(self):
        return self.__name
    def get_position(self):
        return self.__position
    def get_id(self):
        return self.__id

    def __str__(self):
        return 'Имя: '+str(self.__name)+\
            '\nДолжность: '+str(self.__position)+\
            '\nПерсональный код: '+str(self.__id)